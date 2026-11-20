"""Build or check one derived, skills-only odskills plugin; never install it."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess

from library import LibraryError, discover
from validate_library import validate_scripts

ROOT = Path(__file__).resolve().parents[1]


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def render(root: Path) -> dict[str, bytes]:
    skills = discover(root)
    validate_scripts(root)
    output: dict[str, bytes] = {}
    inputs: dict[str, dict[str, str]] = {}
    for skill in skills:
        package = (root / skill.path).parent
        for path in sorted(package.rglob("*")):
            if path.is_file():
                target = (
                    "skills/" + skill.name + "/" + path.relative_to(package).as_posix()
                )
                raw = path.read_bytes()
                output[target] = raw
                inputs[target] = {
                    "source": path.relative_to(root).as_posix(),
                    "sha256": digest(raw),
                }
    generator_hash = digest(Path(__file__).read_bytes())
    snapshot = {"canonical_files": inputs, "generator_sha256": generator_hash}
    fingerprint = digest(json_bytes(snapshot))
    version = "0.1.0-experimental.h" + fingerprint[:12]
    output["plugin.json"] = json_bytes(
        {
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "name": "odskills",
            "version": version,
            "description": "Experimental reusable development, mathematical audit and skill-engineering workflows.",
            "author": {"name": "Chey Loveday"},
            "repository": "https://github.com/CheyLoveday/odskills-public",
            "extensions": {
                "com.openai": {
                    "interface": {
                        "displayName": "odskills (experimental)",
                        "shortDescription": "Reusable coding, mathematical audit and skill-engineering methods",
                    }
                }
            },
        }
    )
    output["SOURCE.json"] = json_bytes(
        {
            "schema_version": 1,
            "version": version,
            "input_sha256": fingerprint,
            **snapshot,
            "generation_command": "python tools/build_plugin.py --output plugins/odskills",
            "canonical_package_count": len(skills),
        }
    )
    output["README.md"] = (
        "# odskills generated plugin\n\n"
        "Generated, non-authoritative deployment artifact. Do not edit directly.\n"
        "Canonical source: `skills/<domain>/<skill-id>/` in CheyLoveday/odskills-public.\n"
        "Regenerate: `python tools/build_plugin.py --output plugins/odskills`.\n"
        "Check: `python tools/build_plugin.py --check`.\n"
        "`SOURCE.json` records every source path/SHA-256, generator SHA-256 and\n"
        "the combined input fingerprint; version changes with either input.\n\n"
        "All packages remain experimental. Native IDs and package bytes are\n"
        "preserved, with a flat `skills/<id>/` layout. No MCP server, hooks, apps,\n"
        "credentials or dependency installation is included. The source repo's\n"
        "AGENTS.md is not adopted by installing this plugin. Consumers retain\n"
        "their own authority and acceptance requirements. Helper requirements\n"
        "remain declared within their packages. Installation and enumeration\n"
        "do not establish successful application or ChatGPT UI verification.\n"
    ).encode()
    return output


def check(destination: Path, expected: dict[str, bytes]) -> None:
    if destination.is_symlink() or not destination.is_dir():
        raise LibraryError(f"Missing real plugin directory: {destination}")
    actual: dict[str, bytes] = {}

    def scan_error(error: OSError) -> None:
        raise LibraryError(f"Unreadable plugin directory: {error}") from error

    for directory, folders, files in os.walk(
        destination, onerror=scan_error, followlinks=False
    ):
        for name in folders + files:
            path = Path(directory) / name
            if path.is_symlink():
                raise LibraryError(f"Symlink in plugin: {path}")
            if name in files:
                if not stat.S_ISREG(path.stat().st_mode):
                    raise LibraryError(f"Nonregular plugin file: {path}")
                actual[path.relative_to(destination).as_posix()] = path.read_bytes()
    if actual != expected:
        missing = sorted(expected.keys() - actual.keys())
        extra = sorted(actual.keys() - expected.keys())
        changed = sorted(
            name
            for name in expected.keys() & actual.keys()
            if expected[name] != actual[name]
        )
        raise LibraryError(
            f"Stale/altered plugin: missing={missing}, extra={extra}, changed={changed}"
        )


def require_tracked_source(root: Path) -> None:
    command = [
        "git",
        "status",
        "--porcelain",
        "--ignored",
        "--untracked-files=all",
        "--",
        "skills",
    ]
    result = subprocess.run(command, cwd=root, text=True, capture_output=True)
    if result.returncode or any(
        line[:2] in {"??", "!!"} for line in result.stdout.splitlines()
    ):
        raise LibraryError(
            "Plugin writes require tracked canonical inputs without untracked/ignored package files; review and stage intended source files first."
        )


def write(destination: Path, files: dict[str, bytes], root: Path) -> None:
    if destination.resolve().is_relative_to((root / "skills").resolve()):
        raise LibraryError("Plugin output must stay outside canonical skills/.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.mkdir(exist_ok=False)
    for relative, raw in sorted(files.items()):
        path = destination / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as output:
            output.write(raw)
    check(destination, files)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "plugins/odskills")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        if not args.check:
            require_tracked_source(ROOT)
        expected = render(ROOT)
        if args.check:
            check(args.output, expected)
        else:
            write(args.output, expected, ROOT)
    except (LibraryError, OSError, UnicodeError, ValueError, SyntaxError) as error:
        print(f"Plugin {'check' if args.check else 'build'} failed: {error}")
        return 1
    print(
        f"Plugin {'checked' if args.check else 'built'}: {args.output}; {len(expected)} files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
