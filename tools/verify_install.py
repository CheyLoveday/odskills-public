"""Compare complete copied skill packages without executing them or contacting a host."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat


def scan(folder: Path) -> tuple[dict[str, str], list[str]]:
    files: dict[str, str] = {}
    issues: list[str] = []
    try:
        real_directory = not folder.is_symlink() and folder.is_dir()
    except OSError as error:
        return files, [f"{folder}: {error.strerror}"]
    if not real_directory:
        return files, [f"{folder}: expected a real package directory"]

    def failed(error: OSError) -> None:
        issues.append(f"{error.filename}: {error.strerror}")

    for directory, directories, names in os.walk(
        folder, onerror=failed, followlinks=False
    ):
        for name in list(directories):
            path = Path(directory) / name
            if path.is_symlink():
                issues.append(f"{path}: symlink directory")
                directories.remove(name)
        for name in names:
            path = Path(directory) / name
            try:
                if not stat.S_ISREG(path.lstat().st_mode):
                    issues.append(f"{path}: expected a regular file")
                    continue
                digest = hashlib.sha256()
                with path.open("rb") as source:
                    for block in iter(lambda: source.read(1024 * 1024), b""):
                        digest.update(block)
                files[path.relative_to(folder).as_posix()] = digest.hexdigest()
            except OSError as error:
                failed(error)
    if "SKILL.md" not in files:
        issues.append(f"{folder}: missing readable SKILL.md")
    return files, issues


def compare(expected: dict[str, str], actual: dict[str, str]) -> dict[str, list[str]]:
    return {
        "missing": sorted(expected.keys() - actual.keys()),
        "extra": sorted(actual.keys() - expected.keys()),
        "changed": sorted(
            name
            for name in expected.keys() & actual.keys()
            if expected[name] != actual[name]
        ),
    }


def verify(source: Path, installed: Path) -> dict:
    expected, source_issues = scan(source)
    actual, installed_issues = scan(installed)
    differences = compare(expected, actual)
    issues = source_issues + installed_issues
    return {
        "ok": not issues and not any(differences.values()),
        "scope": "package_bytes_only",
        "source": str(source.absolute()),
        "installed": str(installed.absolute()),
        "source_files": expected,
        **differences,
        "issues": issues,
        "host_discovery": "NOT_RUN",
        "behavior": "NOT_RUN",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--installed", type=Path, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    report = verify(args.source, args.installed)
    if args.json:
        print(json.dumps(report, sort_keys=True))
    else:
        print(
            f"{'MATCH' if report['ok'] else 'MISMATCH'}: {len(report['source_files'])} source files; package bytes only"
        )
        for key in ("missing", "extra", "changed", "issues"):
            for value in report[key]:
                print(f"{key}: {value}")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
