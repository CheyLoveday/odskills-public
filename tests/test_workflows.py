"""Exercise public tooling with isolated sources, outputs and working directories."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_library import add_skill
from validate_library import validate_cases
from library import LibraryError

ROOT = Path(__file__).resolve().parents[1]


def cases_for(name: str) -> list[dict[str, object]]:
    return [
        {
            "id": f"{name}-{activate}",
            "prompt": "An independent test prompt.",
            "target_skill": name,
            "should_activate": activate,
            "reason": "Test-only structural fixture, not a model outcome.",
        }
        for activate in (True, False)
    ]


class WorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "library"
        self.cwd = Path(temporary.name) / "unrelated-working-directory"
        self.cwd.mkdir()
        shutil.copytree(
            ROOT / "tools",
            self.root / "tools",
            ignore=shutil.ignore_patterns("__pycache__"),
        )
        add_skill(self.root, "development", "example-skill")
        prompts = self.root / "tests/discovery/prompts.json"
        prompts.parent.mkdir(parents=True)
        prompts.write_text(json.dumps(cases_for("example-skill")), encoding="utf-8")

    def run_tool(
        self, script: str, *arguments: str
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.root / "tools" / script), *arguments],
            cwd=self.cwd,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )

    def assert_success(self, result: subprocess.CompletedProcess[str]) -> None:
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_cross_domain_public_workflow_from_another_directory(self) -> None:
        add_skill(self.root, "mathematics", "exact-review")
        prompts = self.root / "tests/discovery/prompts.json"
        prompts.write_text(
            json.dumps(cases_for("example-skill") + cases_for("exact-review")),
            encoding="utf-8",
        )
        self.assert_success(self.run_tool("build_catalogue.py"))
        catalogue = self.root / "catalogue"
        data = json.loads((catalogue / "skills.json").read_bytes())
        self.assertEqual(
            [item["name"] for item in data["skills"]], ["exact-review", "example-skill"]
        )
        self.assertEqual(
            {item["domain"] for item in data["skills"]}, {"development", "mathematics"}
        )
        before = {path.name: path.read_bytes() for path in catalogue.iterdir()}
        self.assert_success(self.run_tool("build_catalogue.py", "--check"))
        self.assert_success(self.run_tool("validate_library.py"))
        self.assert_success(self.run_tool("build_catalogue.py"))
        self.assertEqual(
            {path.name: path.read_bytes() for path in catalogue.iterdir()}, before
        )
        self.assertEqual(list(self.cwd.iterdir()), [])

    def test_stale_checks_fail_without_rewriting_outputs(self) -> None:
        self.assert_success(self.run_tool("build_catalogue.py"))
        path = self.root / "catalogue/skills.md"
        path.write_bytes(b"manually edited\n")
        result = self.run_tool("build_catalogue.py", "--check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("stale", result.stderr)
        result = self.run_tool("validate_library.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("stale", result.stdout)
        self.assertEqual(path.read_bytes(), b"manually edited\n")

    def test_invalid_yaml_fails_with_a_clear_cli_error(self) -> None:
        (self.root / "skills/development/example-skill/metadata.yaml").write_text(
            "status: experimental\nstatus: stable\n", encoding="utf-8"
        )
        result = self.run_tool("build_catalogue.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate key", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertFalse((self.root / "catalogue").exists())

    def test_malformed_mapping_tag_is_a_clear_cli_failure(self) -> None:
        (self.root / "skills/development/example-skill/metadata.yaml").write_text(
            "!!map []\n", encoding="utf-8"
        )
        result = self.run_tool("build_catalogue.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("expected a mapping node", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertFalse((self.root / "catalogue").exists())

    def test_invalid_discovery_fixtures_rejected(self) -> None:
        good = cases_for("example-skill")
        invalid = {
            "duplicate IDs": [good[0], good[0]],
            "unknown skill": [{**good[0], "target_skill": "unknown"}, good[1]],
            "integer boolean": [{**good[0], "should_activate": 1}, good[1]],
            "missing negative": [good[0]],
        }
        for label, cases in invalid.items():
            with self.subTest(case=label):
                (self.root / "tests/discovery/prompts.json").write_text(
                    json.dumps(cases)
                )
                with self.assertRaises(LibraryError):
                    validate_cases(self.root, {"example-skill"})

    def test_duplicate_discovery_fields_are_a_clear_cli_failure(self) -> None:
        self.assert_success(self.run_tool("build_catalogue.py"))
        path = self.root / "tests/discovery/prompts.json"
        path.write_text(
            path.read_text().replace(
                '"target_skill": "example-skill"',
                '"target_skill": "missing-skill", "target_skill": "example-skill"',
                1,
            )
        )
        result = self.run_tool("validate_library.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Duplicate discovery JSON key", result.stdout)
        self.assertNotIn("Traceback", result.stdout + result.stderr)

    def test_hardlinked_catalogue_is_a_clear_cli_failure_without_source_damage(
        self,
    ) -> None:
        self.assert_success(self.run_tool("build_catalogue.py"))
        source = self.root / "skills/development/example-skill/SKILL.md"
        before = source.read_bytes()
        output = self.root / "catalogue/skills.json"
        output.unlink()
        os.link(source, output)
        result = self.run_tool("build_catalogue.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Hard-linked catalogue output", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual(output.read_bytes(), before)
