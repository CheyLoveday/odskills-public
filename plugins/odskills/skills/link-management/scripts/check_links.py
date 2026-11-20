#!/usr/bin/env python3
"""Read-only Markdown file/anchor checks; never fetch URLs or rewrite sources."""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import unicodedata
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
from markdown_it.token import Token


@dataclass(frozen=True)
class Link:
    line: int
    target: str


@dataclass(frozen=True)
class Issue:
    file: str
    line: int
    target: str
    reason: str


@dataclass(frozen=True)
class Report:
    documents: int
    local_links: int
    external_links_skipped: int
    issues: tuple[Issue, ...]

    @property
    def ok(self) -> bool:
        return not self.issues


class HTMLLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[Link] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.anchors.add(str(values["id"]))
        if tag == "a" and values.get("name"):
            self.anchors.add(str(values["name"]))
        key = "href" if tag == "a" else "src" if tag == "img" else None
        if key is not None and values.get(key):
            self.links.append(Link(self.getpos()[0], str(values[key])))

    handle_startendtag = handle_starttag


class LinkParser(MarkdownIt):
    def validateLink(self, url: str) -> bool:
        # Inspect file: links too. This analysis never renders or follows a URL.
        return True


def heading_text(children: list[Token]) -> str:
    parts = []
    for child in children:
        if child.type == "image":
            parts.append(heading_text(child.children or []))
        elif child.type in {"text", "code_inline", "text_special"}:
            parts.append(child.content)
        elif child.type in {"softbreak", "hardbreak"}:
            parts.append(" ")
    return "".join(parts)


def slug(text: str) -> str:
    # GitHub-style heading IDs. Keep hyphens/underscores and Unicode letters,
    # marks and numbers; remove punctuation/formatting, then replace spaces.
    return "".join(
        char
        for char in text.strip().lower()
        if char in "-_ " or unicodedata.category(char)[0] in "LMN"
    ).replace(" ", "-")


def parse_markdown(raw: str) -> tuple[list[Link], set[str]]:
    parser = LinkParser("commonmark").enable(["table", "strikethrough"])
    tokens = parser.parse(raw)
    links: list[Link] = []
    automatic: set[str] = set()
    custom: set[str] = set()

    def visit(token: Token, line: int) -> None:
        if token.type in {"link_open", "image"}:
            key = "href" if token.type == "link_open" else "src"
            target = token.attrGet(key)
            if target is not None:
                links.append(Link(line, str(target)))
        if token.type in {"html_block", "html_inline"}:
            html = HTMLLinks()
            html.feed(token.content)
            custom.update(html.anchors)
            links.extend(Link(line + item.line - 1, item.target) for item in html.links)
        for child in token.children or []:
            visit(child, line)

    for index, token in enumerate(tokens):
        line = token.map[0] + 1 if token.map else 1
        if token.type == "heading_open":
            base = slug(heading_text(tokens[index + 1].children or []))
            candidate, suffix = base, 0
            while candidate in automatic:
                suffix += 1
                candidate = f"{base}-{suffix}"
            automatic.add(candidate)
        visit(token, line)
    return links, automatic | custom


def _read(path: Path) -> str:
    if not stat.S_ISREG(path.stat().st_mode):
        raise ValueError("not a regular document")
    return path.read_text(encoding="utf-8")


def _case_error(root: Path, path: Path) -> str | None:
    """Compare actual entry spelling even on a case-insensitive volume."""
    current = root
    for part in path.relative_to(root).parts:
        try:
            names = {entry.name for entry in current.iterdir()}
        except (FileNotFoundError, NotADirectoryError):
            return None
        if part not in names:
            if part.casefold() in {name.casefold() for name in names}:
                return "case-mismatch"
            return None
        current = current / part
    return None


def check(root: Path, inputs: list[Path]) -> Report:
    root = root.resolve()
    documents: set[Path] = set()
    issues: list[Issue] = []
    for supplied in inputs:
        path = supplied if supplied.is_absolute() else root / supplied
        lexical = Path(os.path.abspath(path))
        try:
            path = lexical.resolve()
        except (OSError, RuntimeError, ValueError):
            issues.append(Issue(str(supplied), 1, "", "unresolvable-input"))
            continue
        if not path.is_relative_to(root):
            issues.append(Issue(str(supplied), 1, "", "input-outside-root"))
            continue
        try:
            if lexical.is_relative_to(root) and _case_error(root, lexical):
                issues.append(Issue(str(supplied), 1, "", "input-case-mismatch"))
                continue
        except OSError as error:
            issues.append(Issue(str(supplied), 1, "", f"unreadable-input: {error}"))
            continue
        if path.is_dir():

            def scan_error(error: OSError) -> None:
                failed = Path(error.filename) if error.filename else path
                name = (
                    failed.relative_to(root).as_posix()
                    if failed.is_relative_to(root)
                    else str(failed)
                )
                issues.append(Issue(name, 1, "", "unreadable-directory"))

            for directory, _, files in os.walk(
                path, onerror=scan_error, followlinks=False
            ):
                documents.update(
                    Path(directory) / name
                    for name in files
                    if Path(name).suffix.lower() in {".md", ".markdown"}
                )
        elif path.is_file():
            documents.add(path)
        else:
            issues.append(Issue(str(supplied), 1, "", "missing-input"))
    if not documents and not issues:
        issues.append(Issue(".", 1, "", "no-markdown-documents"))
    cache: dict[Path, tuple[list[Link], set[str]]] = {}
    local = external = 0
    for selected in sorted(documents):
        try:
            source = selected.resolve()
        except (OSError, RuntimeError, ValueError):
            issues.append(Issue(str(selected), 1, "", "unresolvable-input"))
            continue
        if not source.is_relative_to(root):
            issues.append(Issue(str(source), 1, "", "input-outside-root"))
            continue
        name = source.relative_to(root).as_posix()
        try:
            if _case_error(root, source):
                issues.append(Issue(name, 1, "", "input-case-mismatch"))
                continue
            if source not in cache:
                cache[source] = parse_markdown(_read(source))
        except (OSError, UnicodeError, ValueError) as error:
            issues.append(Issue(name, 1, "", f"unreadable-document: {error}"))
            continue
        for link in cache[source][0]:
            try:
                url = urlsplit(link.target)
            except ValueError:
                issues.append(Issue(name, link.line, link.target, "invalid-url"))
                continue
            if url.scheme or url.netloc:
                if url.scheme.lower() == "file":
                    issues.append(
                        Issue(name, link.line, link.target, "nonportable-file-url")
                    )
                else:
                    external += 1
                continue
            local += 1
            relative = unquote(url.path)
            if "\\" in relative or "\x00" in relative:
                issues.append(Issue(name, link.line, link.target, "nonportable-path"))
                continue
            lexical = Path(
                os.path.abspath(
                    root / relative.lstrip("/")
                    if relative.startswith("/")
                    else source.parent / relative
                    if relative
                    else source
                )
            )
            try:
                target = lexical.resolve()
            except (OSError, RuntimeError, ValueError):
                issues.append(
                    Issue(name, link.line, link.target, "unresolvable-target")
                )
                continue
            reason = None
            if not target.is_relative_to(root):
                reason = "target-outside-root"
            else:
                try:
                    reason = _case_error(root, target)
                    if reason is None and lexical.is_relative_to(root):
                        reason = _case_error(root, lexical)
                except OSError as error:
                    reason = f"unreadable-target: {error}"
            if reason is None and not target.exists():
                reason = "missing-target"
            elif reason is None and url.fragment:
                fragment = unquote(url.fragment)
                try:
                    if target.suffix.lower() in {".md", ".markdown"}:
                        if target not in cache:
                            cache[target] = parse_markdown(_read(target))
                        if fragment not in cache[target][1]:
                            reason = "missing-anchor"
                    elif target.suffix.lower() in {".html", ".htm"}:
                        html = HTMLLinks()
                        html.feed(_read(target))
                        if fragment not in html.anchors:
                            reason = "missing-anchor"
                    elif match := re.fullmatch(
                        r"L([1-9][0-9]*)(?:-L([1-9][0-9]*))?", fragment
                    ):
                        start = int(match[1])
                        end = int(match[2]) if match[2] else start
                        if end < start or end > len(_read(target).splitlines()):
                            reason = "missing-line-anchor"
                    else:
                        reason = "unsupported-fragment"
                except (OSError, UnicodeError, ValueError) as error:
                    reason = f"unreadable-target: {error}"
            if reason:
                issues.append(Issue(name, link.line, link.target, reason))
    return Report(len(documents), local, external, tuple(issues))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "paths", nargs="+", type=Path, help="Markdown files or directories to check"
    )
    args = parser.parse_args(argv)
    report = check(args.root, args.paths)
    if args.json:
        print(
            json.dumps(
                {"ok": report.ok, **asdict(report)}, ensure_ascii=False, sort_keys=True
            )
        )
    else:
        for issue in report.issues:
            print(f"{issue.file}:{issue.line}: {issue.reason}: {issue.target}")
        print(
            f"{report.documents} documents; {report.local_links} local links; "
            f"{report.external_links_skipped} external links skipped; {len(report.issues)} issues"
        )
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
