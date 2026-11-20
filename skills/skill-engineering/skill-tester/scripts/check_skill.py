#!/usr/bin/env python3
"""Static skill entrypoint validation; no target code execution or behavioral claim."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]


class UniqueKeysLoader(yaml.SafeLoader):  # type: ignore[misc]
    # PyYAML has no bundled type stubs; this small boundary is tested with
    # duplicate keys, wrong scalar types and unsupported constructor tags.
    pass


def unique_mapping(loader: UniqueKeysLoader, node: yaml.MappingNode) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if key in result:
            raise ValueError("duplicate-frontmatter-key")
        result[key] = loader.construct_object(value_node, deep=True)
    return result


UniqueKeysLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def check_skill(folder: Path) -> dict[str, Any]:
    issues: list[str] = []
    result: dict[str, Any] = {
        "kind": "SKILL_STATIC_CHECK",
        "scope": "entrypoint_structure_only",
        "skill": str(folder),
        "skill_file_sha256": None,
        "behavior": "NOT_RUN",
        "issues": issues,
        "ok": False,
    }
    path = folder / "SKILL.md"
    try:
        if not stat.S_ISREG(path.stat().st_mode):
            issues.append("nonregular-skill-entrypoint")
            return result
        raw = path.read_bytes()
        result["skill_file_sha256"] = hashlib.sha256(raw).hexdigest()
        text = raw.decode("utf-8")
    except (OSError, UnicodeError):
        issues.append("unreadable-skill-entrypoint")
        return result
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.DOTALL)
    if match is None:
        issues.append("missing-or-unclosed-frontmatter")
        return result
    try:
        frontmatter = yaml.load(match[1], Loader=UniqueKeysLoader)
    except (yaml.YAMLError, ValueError, TypeError, RecursionError):
        issues.append("invalid-or-duplicate-frontmatter")
        return result
    if type(frontmatter) is not dict:
        issues.append("frontmatter-not-a-mapping")
        return result
    name, description = frontmatter.get("name"), frontmatter.get("description")
    if (
        type(name) is not str
        or re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is None
        or len(name) > 64
    ):
        issues.append("invalid-skill-name")
    elif name != folder.name:
        issues.append("folder-name-mismatch")
    if type(description) is not str or not description.strip():
        issues.append("invalid-description")
    if not text[match.end() :].strip():
        issues.append("empty-instructions")
    result["ok"] = not issues
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("skills", nargs="+", type=Path)
    args = parser.parse_args(argv)
    results = [check_skill(path) for path in args.skills]
    ok = all(row["ok"] for row in results)
    if args.json:
        print(
            json.dumps(
                {"ok": ok, "scope": "static_only", "results": results}, sort_keys=True
            )
        )
    else:
        for row in results:
            state = "STATIC_OK" if row["ok"] else "STATIC_FAILED"
            print(
                f"{row['skill']}: {state}; behavior=NOT_RUN; {', '.join(row['issues'])}"
            )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
