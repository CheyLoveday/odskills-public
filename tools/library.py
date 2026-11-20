"""Library-wide canonical skill discovery and deterministic catalogue rendering."""

from __future__ import annotations

import json
import os
import re
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml

SLUG = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"\]\(([^)]+)\)")
SECTIONS = ("When to use", "Inputs", "Procedure", "Outputs", "Verification", "Stop")
METADATA_FIELDS = frozenset({"status", "tags", "examples", "related", "requirements"})
STATUSES = frozenset({"experimental", "stable", "deprecated"})


class LibraryError(ValueError):
    """Invalid canonical skill source, metadata, reference or collection."""


class _UniqueKeyLoader(yaml.SafeLoader):
    """Keep SafeLoader's tag restrictions and refuse ambiguous mappings."""

    def construct_mapping(
        self, node: yaml.MappingNode, deep: bool = False
    ) -> dict[str, Any]:
        if not isinstance(node, yaml.MappingNode):
            raise yaml.constructor.ConstructorError(
                None, None, "expected a mapping node", node.start_mark
            )
        self.flatten_mapping(node)
        mapping: dict[str, Any] = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if type(key) is not str:
                raise yaml.constructor.ConstructorError(
                    None, None, "expected a string key", key_node.start_mark
                )
            if key in mapping:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate key '{key}'", key_node.start_mark
                )
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


@dataclass(frozen=True, slots=True)
class Skill:
    name: str
    description: str
    domain: str
    path: str
    status: str
    tags: tuple[str, ...]
    example_requests: tuple[str, ...]
    related: tuple[str, ...]
    requirements: tuple[str, ...]


def _mapping(value: Any, path: Path) -> dict[str, Any]:
    if not isinstance(value, dict) or any(not isinstance(k, str) for k in value):
        raise LibraryError(f"{path}: expected YAML mapping with string keys")
    return value


def _load_mapping(text: str, path: Path) -> dict[str, Any]:
    try:
        return _mapping(yaml.load(text, Loader=_UniqueKeyLoader), path)
    except yaml.YAMLError as error:
        raise LibraryError(f"{path}: invalid YAML: {error}") from error


def _strings(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, list) or any(
        type(x) is not str or not x.strip() for x in value
    ):
        raise LibraryError(f"{label}: expected a list of nonempty strings")
    values = tuple(x.strip() for x in value)
    if len(values) != len(set(values)):
        raise LibraryError(f"{label}: duplicate entries")
    return values


def _safe_path(path: Path, root: Path) -> None:
    if not path.is_relative_to(root) or not path.resolve().is_relative_to(
        root.resolve()
    ):
        raise LibraryError(f"Unsafe path outside root: {path}")
    for member in (path, *path.parents):
        if member.is_symlink():
            raise LibraryError(f"Unsafe symlink: {member}")
        if member == root:
            break


def _safe_file(path: Path, root: Path) -> None:
    _safe_path(path, root)
    if not path.is_file():
        raise LibraryError(f"Unsafe or missing file: {path}")


def _instruction_headings(text: str) -> set[str]:
    """Only actual level-two headings count; fenced examples are not instructions."""
    headings: set[str] = set()
    fence_marker: str | None = None
    fence_length = 0
    for line in text.splitlines():
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            marker, suffix = fence.groups()
            if fence_marker is None:
                fence_marker, fence_length = marker[0], len(marker)
            elif (
                marker[0] == fence_marker
                and len(marker) >= fence_length
                and not suffix.strip()
            ):
                fence_marker, fence_length = None, 0
            continue
        if fence_marker is None and line.startswith("## "):
            headings.add(line[3:].strip())
    return headings


def parse_frontmatter(
    content: str, path: Path = Path("SKILL.md")
) -> tuple[dict[str, Any], str]:
    """Parse supplied text; path is diagnostic context, never a filesystem read."""
    lines = content.splitlines()
    if not lines or lines[0] != "---":
        raise LibraryError(f"{path}: missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise LibraryError(f"{path}: unclosed YAML frontmatter") from error
    front = _load_mapping("\n".join(lines[1:end]), path)
    text = "\n".join(lines[end + 1 :])
    if not text.strip():
        raise LibraryError(f"{path}: empty instructions")
    headings = _instruction_headings(text)
    for section in SECTIONS:
        if section not in headings:
            raise LibraryError(f"{path}: missing section '{section}'")
    return front, text


def _references(text: str, directory: Path, package: Path) -> None:
    for destination in LINK.findall(text):
        target = destination.split("#", 1)[0]
        if not target or target.startswith(("https://", "http://", "mailto:")):
            continue
        if target.startswith("/") or " " in target:
            raise LibraryError(f"{directory}: unsupported relative link {destination}")
        file = directory / target
        _safe_file(file, package)


def _read_skill(root: Path, path: Path) -> Skill:
    _safe_file(path, root)
    front, body = parse_frontmatter(path.read_text(encoding="utf-8"), path)
    name = front.get("name")
    description = front.get("description")
    if (
        type(name) is not str
        or not SLUG.fullmatch(name)
        or len(name) > 64
        or name != path.parent.name
        or type(description) is not str
        or not description.strip()
        or len(description.strip()) > 1024
        or description.splitlines() != [description]
    ):
        raise LibraryError(f"{path}: invalid name, path or description")
    domain = path.parent.parent.name
    if not SLUG.fullmatch(domain):
        raise LibraryError(f"{path}: invalid domain")
    _references(body, path.parent, path.parent)
    for reference in sorted(path.parent.rglob("*.md")):
        if reference != path:
            _safe_file(reference, path.parent)
            _references(
                reference.read_text(encoding="utf-8"), reference.parent, path.parent
            )
    meta_path = path.parent / "metadata.yaml"
    data: dict[str, Any] = {}
    if meta_path.exists() or meta_path.is_symlink():
        _safe_file(meta_path, root)
        data = _load_mapping(meta_path.read_text(encoding="utf-8"), meta_path)
        if set(data) - METADATA_FIELDS:
            raise LibraryError(
                f"{meta_path}: unsupported or duplicate-authority metadata keys"
            )
    status = data.get("status", "experimental")
    if type(status) is not str or status not in STATUSES:
        raise LibraryError(f"{meta_path}: unknown lifecycle status")
    tags = _strings(data.get("tags", []), f"{meta_path}: tags")
    if any(not SLUG.fullmatch(x) for x in tags):
        raise LibraryError(f"{meta_path}: invalid tag")
    return Skill(
        name=name,
        description=description.strip(),
        domain=domain,
        path=path.relative_to(root).as_posix(),
        status=status,
        tags=tags,
        example_requests=_strings(data.get("examples", []), f"{meta_path}: examples"),
        related=_strings(data.get("related", []), f"{meta_path}: related"),
        requirements=_strings(
            data.get("requirements", []), f"{meta_path}: requirements"
        ),
    )


def discover(root: Path) -> tuple[Skill, ...]:
    source = root / "skills"
    _safe_path(source, root)
    if not source.is_dir():
        raise LibraryError("Missing canonical skills/ directory")

    def scan_error(error: OSError) -> None:
        raise LibraryError(f"Cannot inspect canonical skill tree: {error}") from error

    paths: list[Path] = []
    for directory, folders, files in os.walk(source, onerror=scan_error):
        for name in sorted(folders + files):
            path = Path(directory) / name
            if path.is_symlink():
                raise LibraryError(f"Symlink in canonical skill tree: {path}")
            if path.name == ".git":
                raise LibraryError(f"Git metadata in canonical skill package: {path}")
            if not path.is_file() and not path.is_dir():
                raise LibraryError(f"Nonregular file in canonical skill tree: {path}")
            if path.name == "SKILL.md":
                paths.append(path)
    for domain in sorted(source.iterdir()):
        if not domain.is_dir() or not SLUG.fullmatch(domain.name):
            raise LibraryError(f"Expected canonical domain directory: {domain}")
        for package in sorted(domain.iterdir()):
            if not package.is_dir() or not SLUG.fullmatch(package.name):
                raise LibraryError(f"Expected canonical skill directory: {package}")
            # Check the real directory entry, also on case-insensitive filesystems.
            if "SKILL.md" not in {member.name for member in package.iterdir()}:
                raise LibraryError(f"Missing canonical SKILL.md in package: {package}")
    paths.sort()
    if not paths:
        raise LibraryError("No canonical SKILL.md files found")
    skills: list[Skill] = []
    for path in paths:
        relative = path.relative_to(source)
        if len(relative.parts) != 3 or relative.name != "SKILL.md":
            raise LibraryError(f"Noncanonical SKILL.md location: {path}")
        skills.append(_read_skill(root, path))
    names = {x.name for x in skills}
    if len(names) != len(skills):
        raise LibraryError("Skill names must be unique across all domains")
    for skill in skills:
        if not set(skill.related).issubset(names) or skill.name in skill.related:
            raise LibraryError(f"{skill.name}: invalid related skill ID")
    return tuple(sorted(skills, key=lambda x: x.name))


def validate_collections(root: Path, skills: tuple[Skill, ...]) -> None:
    directory = root / "collections"
    if not directory.exists() and not directory.is_symlink():
        return
    _safe_path(directory, root)
    if not directory.is_dir():
        raise LibraryError(f"Expected collections directory: {directory}")
    known = {x.name for x in skills}
    for path in sorted(directory.glob("*.yaml")):
        _safe_file(path, root)
        content = _load_mapping(path.read_text(encoding="utf-8"), path)
        if set(content) != {"name", "skills"} or content["name"] != path.stem:
            raise LibraryError(
                f"{path}: expected name matching filename and skills list"
            )
        members = _strings(content["skills"], f"{path}: skills")
        if not members or not set(members).issubset(known):
            raise LibraryError(f"{path}: missing or unknown skill ID")


def catalogue(skills: tuple[Skill, ...]) -> dict[str, Any]:
    return {"schema_version": 1, "skills": [asdict(skill) for skill in skills]}


def render_json(skills: tuple[Skill, ...]) -> str:
    return (
        json.dumps(catalogue(skills), ensure_ascii=False, sort_keys=True, indent=2)
        + "\n"
    )


def render_markdown(skills: tuple[Skill, ...]) -> str:
    out = [
        "# Skill catalogue",
        "",
        "Generated from canonical skills. Do not edit this file.",
        "",
        "Keywords mirror library tags for browsing; host selection uses skill names and descriptions.",
        "",
        "| Skill | Domain | Status | Keywords | Description |",
        "|---|---|---|---|---|",
    ]
    for skill in skills:
        label = f"[{skill.name}](../{skill.path})"
        desc = skill.description.replace("|", "\\|")
        keywords = ", ".join(skill.tags) or "—"
        out.append(f"| {label} | {skill.domain} | {skill.status} | {keywords} | {desc} |")
    return "\n".join(out) + "\n"


def expected_outputs(root: Path) -> dict[Path, str]:
    skills = discover(root)
    validate_collections(root, skills)
    return {
        root / "catalogue" / "skills.json": render_json(skills),
        root / "catalogue" / "skills.md": render_markdown(skills),
    }


def check_outputs(root: Path) -> None:
    for path, expected in expected_outputs(root).items():
        _safe_output(path, root)
        if not path.is_file() or path.read_bytes() != expected.encode("utf-8"):
            raise LibraryError(f"Generated catalogue missing or stale: {path}")


def _safe_output(path: Path, root: Path) -> None:
    _safe_path(path, root)
    if path.exists():
        if not path.is_file():
            raise LibraryError(f"Expected catalogue file: {path}")
        if path.stat().st_nlink > 1:
            raise LibraryError(f"Hard-linked catalogue output: {path}")


def write_outputs(root: Path) -> None:
    outputs = expected_outputs(root)
    for path in outputs:
        _safe_output(path, root)
    directory = root / "catalogue"
    directory.mkdir(parents=True, exist_ok=True)
    # Finish every write before replacing any output. Each rename is atomic;
    # the pair is not a transaction, so a failed rename still requires --check.
    with tempfile.TemporaryDirectory(
        prefix=".odskills-stage-", dir=directory
    ) as temporary:
        staged = {path: Path(temporary) / path.name for path in outputs}
        for path, content in outputs.items():
            staged[path].write_bytes(content.encode("utf-8"))
        for path in outputs:
            _safe_output(path, root)
            os.replace(staged[path], path)
