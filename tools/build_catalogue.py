"""Generate or check deterministic library-wide catalogue files."""

from __future__ import annotations

import argparse
from pathlib import Path

from library import LibraryError, check_outputs, write_outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Refuse stale generated files")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        if args.check:
            check_outputs(root)
        else:
            write_outputs(root)
    except (LibraryError, OSError, UnicodeError) as error:
        parser.exit(1, f"catalogue error: {error}\n")
    print("Catalogue checked" if args.check else "Catalogue generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
