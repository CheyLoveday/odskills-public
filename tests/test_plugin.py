"""Check the derived plugin contract without installing a plugin or calling a model."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_plugin as PLUGIN  # noqa: E402
from library import LibraryError, discover  # noqa: E402


def fixture(root):
    package = root / "skills/testing/example-skill"
    package.mkdir(parents=True)
    (package / "SKILL.md").write_text(
        "---\nname: example-skill\ndescription: Inspect one selected input.\n---\n"
        "## When to use\nInspect.\n## Inputs\nOne file.\n## Procedure\nRead it.\n"
        "## Outputs\nReport.\n## Verification\nCheck.\n## Stop\nDo not edit.\n"
    )
    return package


class PluginTests(unittest.TestCase):
    def test_public_marketplace_points_to_the_generated_bundle(self):
        marketplace = json.loads(
            (ROOT / ".agents/plugins/marketplace.json").read_text()
        )
        manifest = json.loads((ROOT / "plugins/odskills/plugin.json").read_text())
        self.assertEqual(marketplace["name"], "odskills-public")
        (entry,) = marketplace["plugins"]
        self.assertEqual(entry["name"], manifest["name"])
        self.assertEqual(
            entry["source"], {"source": "local", "path": "./plugins/odskills"}
        )
        self.assertEqual(
            entry["policy"],
            {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        )

    def test_generated_plugin_matches_every_canonical_file_and_native_id(self):
        expected = PLUGIN.render(ROOT)
        PLUGIN.check(ROOT / "plugins/odskills", expected)
        provenance = json.loads(expected["SOURCE.json"])
        self.assertEqual(provenance["canonical_package_count"], len(discover(ROOT)))
        for target, entry in provenance["canonical_files"].items():
            self.assertEqual(expected[target], (ROOT / entry["source"]).read_bytes())
            self.assertEqual(
                hashlib.sha256(expected[target]).hexdigest(), entry["sha256"]
            )
        names = {path.split("/")[1] for path in expected if path.startswith("skills/")}
        self.assertEqual(names, {skill.name for skill in discover(ROOT)})
        self.assertFalse(
            any(
                path in expected
                for path in ("mcp.json", ".mcp.json", ".app.json", "hooks/hooks.json")
            )
        )
        manifest = json.loads(expected["plugin.json"])
        self.assertEqual(manifest["name"], "odskills")
        self.assertEqual(
            manifest["repository"], "https://github.com/CheyLoveday/odskills-public"
        )
        self.assertEqual(manifest["version"], provenance["version"])
        self.assertNotIn("apps", manifest)
        self.assertNotIn("hooks", manifest)

    def test_cross_project_discovery_remains_explicit_only(self):
        config = (
            ROOT
            / "plugins/odskills/skills/discover-cross-project-connections"
            / "agents/openai.yaml"
        )
        policy = yaml.safe_load(config.read_text(encoding="utf-8"))["policy"]
        self.assertIs(policy["allow_implicit_invocation"], False)

    def test_render_is_deterministic_and_resource_changes_invalidate_version(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            package = fixture(root)
            (package / "asset.bin").write_bytes(b"\x00\xff\x80")
            first = PLUGIN.render(root)
            self.assertEqual(first, PLUGIN.render(root))
            (package / "asset.bin").write_bytes(b"different\x00")
            second = PLUGIN.render(root)
            self.assertNotEqual(
                json.loads(first["plugin.json"])["version"],
                json.loads(second["plugin.json"])["version"],
            )
            self.assertEqual(second["skills/example-skill/asset.bin"], b"different\x00")

    def test_check_rejects_extra_effect_configuration_missing_and_modified_resources(
        self,
    ):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture(root)
            expected = PLUGIN.render(root)
            destination = root / "plugin"
            PLUGIN.write(destination, expected, root)
            for name in ("mcp.json", ".app.json", "hooks/hooks.json"):
                with self.subTest(name=name):
                    added = destination / name
                    added.parent.mkdir(parents=True, exist_ok=True)
                    added.write_text("{}")
                    with self.assertRaises(LibraryError):
                        PLUGIN.check(destination, expected)
                    added.unlink()
            target = destination / "skills/example-skill/SKILL.md"
            target.write_text("changed")
            with self.assertRaises(LibraryError):
                PLUGIN.check(destination, expected)
            target.unlink()
            with self.assertRaises(LibraryError):
                PLUGIN.check(destination, expected)

    def test_new_output_refuses_existing_directory_file_and_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture(root)
            expected = PLUGIN.render(root)
            existing = root / "existing"
            existing.mkdir()
            marker = existing / "user.txt"
            marker.write_text("preserve")
            with self.assertRaises(FileExistsError):
                PLUGIN.write(existing, expected, root)
            self.assertEqual(marker.read_text(), "preserve")
            for name in ("file", "broken-link"):
                destination = root / name
                if name == "file":
                    destination.write_text("preserve")
                else:
                    destination.symlink_to(root / "absent")
                with self.assertRaises(FileExistsError):
                    PLUGIN.write(destination, expected, root)
                self.assertTrue(
                    destination.is_symlink() or destination.read_text() == "preserve"
                )
            with self.assertRaises(LibraryError):
                PLUGIN.write(
                    root / "skills/testing/example-skill/generated", expected, root
                )

    def test_scan_rejects_symlinks_special_files_and_unreadable_subtrees(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture(root)
            expected = PLUGIN.render(root)
            destination = root / "plugin"
            PLUGIN.write(destination, expected, root)
            extra = destination / "linked"
            extra.symlink_to(root / "skills")
            with self.assertRaises(LibraryError):
                PLUGIN.check(destination, expected)
            extra.unlink()
            if hasattr(os, "mkfifo"):
                os.mkfifo(extra)
                with self.assertRaises(LibraryError):
                    PLUGIN.check(destination, expected)
                extra.unlink()

            def walk(path, *, onerror, followlinks):
                onerror(PermissionError(13, "denied", str(path / "skills")))
                return iter(())

            with patch.object(PLUGIN.os, "walk", walk), self.assertRaises(LibraryError):
                PLUGIN.check(destination, expected)

    def test_source_guard_refuses_untracked_and_ignored_inputs_but_accepts_staged(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            package = fixture(root)
            env = dict(
                os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1"
            )
            subprocess.run(["git", "init", "-q"], cwd=root, env=env, check=True)
            with self.assertRaises(LibraryError):
                PLUGIN.require_tracked_source(root)
            subprocess.run(["git", "add", "skills"], cwd=root, env=env, check=True)
            PLUGIN.require_tracked_source(root)
            (root / ".gitignore").write_text("*.local\n")
            ignored = package / "private.local"
            ignored.write_text("owned adverse fixture")
            with self.assertRaises(LibraryError):
                PLUGIN.require_tracked_source(root)

    def test_public_cli_check_rejects_a_wrong_package_and_write_preserves_it(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "occupied"
            destination.mkdir()
            marker = destination / "user.txt"
            marker.write_text("preserve")
            for args in (["--check"], []):
                run = subprocess.run(
                    [
                        sys.executable,
                        str(ROOT / "tools/build_plugin.py"),
                        *args,
                        "--output",
                        str(destination),
                    ],
                    text=True,
                    capture_output=True,
                    timeout=10,
                )
                self.assertEqual(run.returncode, 1, run.stdout + run.stderr)
                self.assertEqual(marker.read_text(), "preserve")
                self.assertEqual(list(destination.iterdir()), [marker])


if __name__ == "__main__":
    unittest.main()
