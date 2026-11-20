# Agent instructions for odskills-public

Read the [README](README.md) first. This checkout is the public landing
page. Use the current [Releases](https://github.com/CheyLoveday/odskills-public/releases)
and their actual artifact names when answering availability questions.
If Releases contains no installable artifact, report that the public
release is unavailable.

## When a task selects a skill package

- Use the requested release or an explicitly supplied package. Record its
  version, checksum and the selected skill path. Check the whole package
  and follow the target host's or project's instructions.
- Read the selected `SKILL.md` and any resources it requires. Use the
  host's inventory for native discovery or the pinned path for explicit use.
- Report package verification, discovery or instruction loading, and the
  actual task result separately. Follow the user's authority for
  installations, dependencies, commands and external effects.

## When editing this repository

The landing pages are generated from maintainer sources. Propose content
changes to the [maintainer](SUPPORT.md) so the canonical source can be
updated and regenerated. Keep private sources, credentials and raw
session data out of public contributions. A documentation change does not
publish a skill archive or submit a plugin.

---

Generated, non-authoritative copy from `release/landing/AGENTS.md`.
Regenerate in the maintainer repository with `python tools/build_landing_docs.py --output NEW_DIRECTORY`.
Source SHA-256: `facfd78ff75db97c76c2dbf97766adee360afc6adf7cb7c04e96773136ac29e9`.
