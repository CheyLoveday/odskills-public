# odskills

odskills is a private library of reusable agent workflows for software
development, mathematics and Lean. Use a portable `SKILL.md` package from an
authorised source. This repository hosts the public documentation.

[Releases](https://github.com/CheyLoveday/odskills-public/releases) is the place
for public downloads. Skill packages and the plugin are currently private.

## Use one pinned skill

1. **Pin the source.** Select one skill from an authorised checkout at a
   specific commit or a supplied package at a specific version. For an archive,
   verify the publisher's checksum before extracting. Keep the skill folder
   together with its references and helpers.
2. **Make it available.** In a handoff such as Open Math OS, give the agent the
   source pin and readable `SKILL.md` path. For native discovery, follow the
   host's installation instructions and verify the skill in its inventory,
   such as `/skills` in the Codex CLI.
3. **Check actual use.** Give the agent a small task with a known result.
   Check which instructions it read and whether the output meets the expected
   result. Record verification, discovery or loading, and application separately.

Keep the previous verified package outside active discovery paths if you
upgrade. To roll back, restore its pin and check what the host loads.

[Agent instructions](AGENTS.md) · [Support](SUPPORT.md) ·
[Privacy](PRIVACY.md) · [Terms](TERMS.md) · [MIT licence](LICENSE)

---

Generated, non-authoritative copy from `release/landing/README.md`.
Regenerate in the maintainer repository with `python tools/build_landing_docs.py --output NEW_DIRECTORY`.
Source SHA-256: `be630e184f52f23781d6d2bb3e384d84f4f921e5d19c63d9ce2968d930ea8160`.
