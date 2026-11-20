"""Exercise byte verification and the public failure status on disposable packages."""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools/verify_install.py"
spec = importlib.util.spec_from_file_location("install_verification", TOOL)
VERIFY = importlib.util.module_from_spec(spec)
exec(compile(TOOL.read_text(), str(TOOL), "exec"), VERIFY.__dict__)


class InstallVerificationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source = self.root / "source/skill"
        self.source.mkdir(parents=True)
        (self.source / "SKILL.md").write_bytes(b"selected entrypoint\n")
        (self.source / "assets").mkdir()
        (self.source / "assets/opaque.bin").write_bytes(b"\x00\xff\x80\n")
        self.installed = self.root / "destination with spaces/skill"
        shutil.copytree(self.source, self.installed)

    def cli(self):
        return subprocess.run(
            [
                sys.executable,
                str(TOOL),
                "--source",
                str(self.source),
                "--installed",
                str(self.installed),
                "--json",
            ],
            text=True,
            capture_output=True,
            timeout=3,
        )

    def test_actual_cli_accepts_complete_bytes_without_executing_package(self):
        result = self.cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report["ok"])
        self.assertEqual(len(report["source_files"]), 2)
        self.assertEqual(report["host_discovery"], "NOT_RUN")
        self.assertEqual(report["behavior"], "NOT_RUN")
        self.assertFalse((self.installed / "__pycache__").exists())

    def test_detects_changed_missing_extra_and_wrong_case_files(self):
        (self.installed / "SKILL.md").write_text("different")
        (self.installed / "assets/opaque.bin").rename(
            self.installed / "assets/OPAQUE.bin"
        )
        result = self.cli()
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertFalse(report["ok"])
        self.assertEqual(report["changed"], ["SKILL.md"])
        self.assertEqual(report["missing"], ["assets/opaque.bin"])
        self.assertEqual(report["extra"], ["assets/OPAQUE.bin"])

    def test_both_missing_or_empty_packages_do_not_match_successfully(self):
        for folder in (self.source, self.installed):
            shutil.rmtree(folder)
        result = self.cli()
        self.assertEqual(result.returncode, 1)
        for folder in (self.source, self.installed):
            folder.mkdir()
        self.assertFalse(VERIFY.verify(self.source, self.installed)["ok"])

    def test_symlinks_and_nonregular_entries_are_not_read(self):
        marker = self.installed / "assets/opaque.bin"
        marker.unlink()
        marker.symlink_to(self.source / "assets/opaque.bin")
        result = self.cli()
        self.assertEqual(result.returncode, 1, result.stderr)
        marker.unlink()
        if hasattr(os, "mkfifo"):
            os.mkfifo(marker)
        else:
            marker.mkdir()
        result = self.cli()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertFalse(json.loads(result.stdout)["ok"])

    def test_unreadable_scan_cannot_turn_into_partial_success(self):
        def walk(path, *, onerror, followlinks):
            onerror(PermissionError(13, "denied", str(path / "assets")))
            return iter(())

        with patch.object(VERIFY.os, "walk", walk):
            report = VERIFY.verify(self.source, self.installed)
        self.assertFalse(report["ok"])
        self.assertTrue(report["issues"])

    def test_unreadable_root_and_linked_directory_do_not_match(self):
        with patch.object(Path, "is_dir", side_effect=PermissionError(13, "denied")):
            self.assertFalse(VERIFY.verify(self.source, self.installed)["ok"])
        (self.installed / "assets/linked").symlink_to(
            self.source / "assets", target_is_directory=True
        )
        self.assertFalse(VERIFY.verify(self.source, self.installed)["ok"])
        root_link = self.root / "linked-package"
        root_link.symlink_to(self.source, target_is_directory=True)
        self.assertFalse(VERIFY.verify(self.source, root_link)["ok"])

    def test_authorised_upgrade_replaces_obsolete_files_and_retains_rollback(self):
        # Compare against the old pin before replacement; local drift must stop it.
        self.assertTrue(VERIFY.verify(self.source, self.installed)["ok"])
        old_source = self.root / "old-pin/skill"
        shutil.copytree(self.source, old_source)
        (self.installed / "local-note.txt").write_text("user work")
        self.assertFalse(VERIFY.verify(self.source, self.installed)["ok"])
        (self.installed / "local-note.txt").unlink()
        backup = self.installed.with_name("skill.backup")
        self.installed.rename(backup)
        old = {
            p.relative_to(backup): p.read_bytes()
            for p in backup.rglob("*")
            if p.is_file()
        }
        (self.source / "assets/opaque.bin").unlink()
        (self.source / "assets/new.txt").write_text("new revision")
        shutil.copytree(self.source, self.installed)
        self.assertTrue(VERIFY.verify(self.source, self.installed)["ok"])
        self.assertFalse((self.installed / "assets/opaque.bin").exists())
        self.assertEqual(
            {
                p.relative_to(backup): p.read_bytes()
                for p in backup.rglob("*")
                if p.is_file()
            },
            old,
        )
        # A failed new deployment stays separate while the exact old pin is restored.
        (self.installed / "assets/new.txt").write_text("incomplete new output")
        self.assertFalse(VERIFY.verify(self.source, self.installed)["ok"])
        failed = self.installed.with_name("skill.failed")
        self.installed.rename(failed)
        backup.rename(self.installed)
        self.assertTrue(VERIFY.verify(old_source, self.installed)["ok"])
        self.assertTrue((failed / "assets/new.txt").exists())


if __name__ == "__main__":
    unittest.main()
