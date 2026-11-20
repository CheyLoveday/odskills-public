"""Validate canonical skills, optional collections, generated outputs and case fixtures."""

from __future__ import annotations

import ast
import json
from pathlib import Path

from library import LibraryError, check_outputs, discover


def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise LibraryError(f"Duplicate discovery JSON key: {key}")
        result[key] = value
    return result


def validate_cases(root: Path, names: set[str]) -> None:
    path = root / "tests" / "discovery" / "prompts.json"
    cases = json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=_unique_json_object
    )
    if type(cases) is not list or not cases:
        raise LibraryError(f"{path}: expected nonempty list")
    ids: set[str] = set()
    for item in cases:
        if (
            type(item) is not dict
            or set(item)
            != {"id", "prompt", "target_skill", "should_activate", "reason"}
            or any(
                type(item[key]) is not str or not item[key].strip()
                for key in ("id", "prompt", "target_skill", "reason")
            )
            or type(item["should_activate"]) is not bool
            or item["id"] in ids
            or item["target_skill"] not in names
        ):
            raise LibraryError(f"{path}: invalid or duplicate case")
        ids.add(item["id"])
    for name in names:
        present = {
            item["should_activate"] for item in cases if item["target_skill"] == name
        }
        if present != {True, False}:
            raise LibraryError(
                f"{path}: missing positive or non-triggering cases for {name}"
            )


def validate_scripts(root: Path) -> None:
    for path in (root / "skills").rglob("*.py"):
        if "scripts" not in path.relative_to(root / "skills").parts[2:-1]:
            continue
        if path.is_symlink():
            raise LibraryError(f"Linked script not permitted: {path}")
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        skills = discover(root)
        check_outputs(root)
        validate_cases(root, {skill.name for skill in skills})
        validate_scripts(root)
    except (LibraryError, OSError, UnicodeError, ValueError, SyntaxError) as error:
        print(f"Validation failed: {error}")
        return 1
    print(
        f"Validated {len(skills)} canonical skill(s), catalogue and discovery fixtures"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
