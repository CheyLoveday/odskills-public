"""Offline tests for the reusable, cross-domain library contract."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from library import (  # noqa: E402
    LibraryError,
    check_outputs,
    discover,
    parse_frontmatter,
    render_json,
    render_markdown,
    validate_collections,
    write_outputs,
)
from validate_library import validate_cases, validate_scripts  # noqa: E402


def skill_source(name: str, extra: str = "") -> str:
    return (
        f"---\nname: {name}\ndescription: A small test-only outcome.\n---\n"
        "## When to use\nTest.\n## Inputs\nInput.\n## Procedure\nDo it.\n"
        "## Outputs\nOutput.\n## Verification\nCheck.\n## Stop\nStop.\n"
        + extra
    )


def add_skill(root: Path, domain: str, name: str, extra: str = "") -> None:
    folder = root / "skills" / domain / name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "SKILL.md").write_text(skill_source(name, extra), encoding="utf-8")


class LibraryContractTests(unittest.TestCase):
    def test_frontmatter_parses_supplied_text_without_filesystem_reads(self) -> None:
        with patch.object(Path, "read_text", side_effect=AssertionError("Unexpected file read")):
            front, body = parse_frontmatter(skill_source("example-skill"), Path("absent/SKILL.md"))
        self.assertEqual(front, {"name": "example-skill", "description": "A small test-only outcome."})
        self.assertIn("## Procedure\nDo it.", body)

    def test_frontmatter_preserves_line_ending_independence(self) -> None:
        text = skill_source("example-skill")
        self.assertEqual(parse_frontmatter(text), parse_frontmatter(text.replace("\n", "\r\n")))

    def test_actual_catalogue_is_current(self) -> None:
        check_outputs(ROOT)
        skills = discover(ROOT)
        self.assertTrue(skills)
        self.assertEqual(json.loads(render_json(skills))["schema_version"], 1)
        markdown = render_markdown(skills)
        for skill in skills:
            self.assertIn(f"../{skill.path}", markdown)
            row = next(
                line for line in markdown.splitlines() if f"../{skill.path})" in line
            )
            for tag in skill.tags:
                self.assertIn(tag, row)
        validate_cases(ROOT, {x.name for x in skills})

    def test_second_domain_needs_no_registry_change(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "functional-core-design")
            add_skill(root, "mathematics", "exact-proof-review")
            names = [x.name for x in discover(root)]
            self.assertEqual(names, ["exact-proof-review", "functional-core-design"])
            write_outputs(root)
            check_outputs(root)

    def test_duplicate_name_across_domains_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "same-skill")
            add_skill(root, "statistics", "same-skill")
            with self.assertRaisesRegex(LibraryError, "unique"):
                discover(root)

    def test_broken_reference_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill", "\nSee [missing](references/not-there.md).\n")
            with self.assertRaisesRegex(LibraryError, "missing file"):
                discover(root)

    def test_unknown_related_id_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            (root / "skills" / "development" / "local-skill" / "metadata.yaml").write_text(
                "related:\n  - unknown-skill\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(LibraryError, "related skill"):
                discover(root)

    def test_invalid_lifecycle_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            (root / "skills" / "development" / "local-skill" / "metadata.yaml").write_text(
                "status: certified\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(LibraryError, "lifecycle"):
                discover(root)

    def test_unknown_collection_member_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            collection = root / "collections"
            collection.mkdir()
            (collection / "test-set.yaml").write_text(
                "name: test-set\nskills:\n  - missing-skill\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(LibraryError, "unknown skill"):
                validate_collections(root, discover(root))

    def test_stale_catalogue_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            write_outputs(root)
            (root / "catalogue" / "skills.md").write_text("manually edited", encoding="utf-8")
            with self.assertRaisesRegex(LibraryError, "stale"):
                check_outputs(root)

    def test_symlinked_skill_content_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            external = root / "external.md"
            external.write_text("unexpected", encoding="utf-8")
            (root / "skills" / "development" / "local-skill" / "linked.md").symlink_to(external)
            with self.assertRaisesRegex(LibraryError, "Symlink"):
                discover(root)

    def test_expected_frontmatter_and_sections_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            path = root / "skills" / "development" / "local-skill" / "SKILL.md"
            path.write_text("---\nname: local-skill\n---\n## When to use\nHere\n", encoding="utf-8")
            with self.assertRaises(LibraryError):
                discover(root)

    def test_nested_reference_links_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill", "\n[Guide](references/guide.md)\n")
            references = root / "skills/development/local-skill/references"
            references.mkdir()
            (references / "guide.md").write_text("[Missing](missing.md)\n", encoding="utf-8")
            with self.assertRaisesRegex(LibraryError, "missing file"):
                discover(root)

    def test_reference_can_link_within_its_package(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill", "\n[Guide](references/guide.md)\n")
            package = root / "skills/development/local-skill"
            (package / "references").mkdir()
            (package / "assets").mkdir()
            (package / "assets/example.txt").write_text("example", encoding="utf-8")
            (package / "references/guide.md").write_text(
                "[Example](../assets/example.txt)\n", encoding="utf-8"
            )
            self.assertEqual(discover(root)[0].name, "local-skill")

    def test_duplicate_yaml_keys_rejected(self) -> None:
        for location in ("frontmatter", "metadata", "collection"):
            with self.subTest(location=location), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                add_skill(root, "development", "local-skill")
                package = root / "skills/development/local-skill"
                if location == "frontmatter":
                    path = package / "SKILL.md"
                    path.write_text(
                        path.read_text().replace(
                            "name: local-skill", "name: local-skill\nname: local-skill"
                        ), encoding="utf-8"
                    )
                elif location == "metadata":
                    (package / "metadata.yaml").write_text(
                        "status: experimental\nstatus: stable\n", encoding="utf-8"
                    )
                else:
                    (root / "collections").mkdir()
                    (root / "collections/example.yaml").write_text(
                        "name: example\nskills: [unknown]\nskills: [local-skill]\n",
                        encoding="utf-8"
                    )
                with self.assertRaisesRegex(LibraryError, "duplicate key"):
                    skills = discover(root)
                    validate_collections(root, skills)

    def test_unsafe_yaml_tag_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            (root / "skills/development/local-skill/metadata.yaml").write_text(
                "status: !!python/object:unknown.Type {}\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(LibraryError, "YAML"):
                discover(root)

    def test_symlinked_canonical_root_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            (root / "skills").rename(root / "original")
            (root / "skills").symlink_to("original", target_is_directory=True)
            with self.assertRaisesRegex(LibraryError, "[Ss]ymlink|[Uu]nsafe"):
                discover(root)

    def test_symlinked_collections_root_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            (root / "original").mkdir()
            (root / "original/example.yaml").write_text(
                "name: example\nskills: [local-skill]\n", encoding="utf-8"
            )
            (root / "collections").symlink_to("original", target_is_directory=True)
            with self.assertRaisesRegex(LibraryError, "[Ss]ymlink|[Uu]nsafe"):
                validate_collections(root, discover(root))

    def test_generation_refuses_output_directory_escape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "library"
            external = parent / "outside"
            external.mkdir()
            add_skill(root, "development", "local-skill")
            (root / "catalogue").symlink_to(external, target_is_directory=True)
            with self.assertRaisesRegex(LibraryError, "[Uu]nsafe|[Ss]ymlink"):
                write_outputs(root)
            self.assertEqual(list(external.iterdir()), [])

    def test_generation_checks_all_output_paths_before_writing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "library"
            add_skill(root, "development", "local-skill")
            write_outputs(root)
            json_path = root / "catalogue/skills.json"
            before = json_path.read_bytes()
            external = parent / "outside.md"
            external.write_text("preserved", encoding="utf-8")
            (root / "catalogue/skills.md").unlink()
            (root / "catalogue/skills.md").symlink_to(external)
            source = root / "skills/development/local-skill/SKILL.md"
            source.write_text(source.read_text().replace("small test-only", "changed"))
            with self.assertRaisesRegex(LibraryError, "[Uu]nsafe|[Ss]ymlink"):
                write_outputs(root)
            self.assertEqual(json_path.read_bytes(), before)
            self.assertEqual(external.read_text(), "preserved")

    def test_check_refuses_linked_output_even_if_content_matches(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            write_outputs(root)
            path = root / "catalogue/skills.md"
            path.rename(root / "original.md")
            path.symlink_to(root / "original.md")
            with self.assertRaisesRegex(LibraryError, "[Uu]nsafe|[Ss]ymlink"):
                check_outputs(root)

    def test_catalogue_check_compares_exact_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            write_outputs(root)
            path = root / "catalogue/skills.md"
            path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
            with self.assertRaisesRegex(LibraryError, "stale"):
                check_outputs(root)

    def test_nested_python_script_syntax_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            add_skill(root, "development", "local-skill")
            scripts = root / "skills/development/local-skill/scripts/helpers"
            scripts.mkdir(parents=True)
            (scripts / "broken.py").write_text("def broken(\n", encoding="utf-8")
            with self.assertRaises(SyntaxError):
                validate_scripts(root)


if __name__ == "__main__":
    unittest.main()
