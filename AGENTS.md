# Agent instructions for odskills-public

Read the [README](README.md) first. This checkout is the public landing
page. Use the current [Releases](https://github.com/CheyLoveday/odskills-public/releases)
and their actual artifact names when answering availability questions.
If Releases contains no installable artifact, report that the public
release is unavailable.

## When a task selects a skill package

- Use the authorised source checkout or supplied package. Record the commit
  or package version and the selected skill path. Verify archive checksums
  when applicable. Follow the host's or project's instructions.
- Read the selected `SKILL.md` and any resources it requires. Use the
  host's inventory for native discovery or the pinned path for explicit use.
- Report package verification, discovery or instruction loading, and the
  actual task result separately. Follow the user's authority for
  installations, dependencies, commands and external effects.

## When editing this repository

Update the canonical maintainer sources and regenerate these pages when
requested. Use [Support](SUPPORT.md) to propose changes if you have access to
this landing page alone. Keep private sources, credentials and raw session
data out of public contributions.

---

Generated, non-authoritative copy from `release/landing/AGENTS.md`.
Regenerate in the maintainer repository with `python tools/build_landing_docs.py --output NEW_DIRECTORY`.
Source SHA-256: `7e01a26d8838286c923e6ca1766738b06b2b208a29ffca9b4f99dc3de3fc683c`.
