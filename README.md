# odskills

Reusable agent workflows for software development, mathematics and Lean.
Skills use portable `SKILL.md` packages.

**Public availability.** This repository is a documentation landing page.
There is no public skill archive or installable plugin here yet. When a
package is published, its version, checksums and usage guide will be listed
under [Releases](https://github.com/CheyLoveday/odskills-public/releases).

## Use one pinned skill

Start with a published release or a package provided to you with permission.

1. **Verify the package.** Record its source and version. Compare the archive
   checksum with the publisher's checksum before extracting. Select one
   skill in its catalogue and keep the whole directory together.
2. **Make it available.** For a host with native skill discovery, follow the
   package's instructions in a disposable project or profile first. In
   the Codex CLI, use `/skills` to check the intended skill. For a handoff,
   such as Open Math OS, name the pinned `SKILL.md` and make its required
   files readable in the task workspace.
3. **Check actual use.** Give the agent one small task with a known expected
   result. Check which instructions it read and whether the output meets
   that expectation. Record byte verification, discovery or explicit
   loading, and application separately.

For an upgrade, keep the verified previous package outside active discovery
paths. Follow the release's rollback instructions and verify the restored
version before using it again.

[Agent instructions](AGENTS.md) · [Support](SUPPORT.md) ·
[Privacy](PRIVACY.md) · [Terms](TERMS.md) · [MIT licence](LICENSE)

---

Generated, non-authoritative copy from `release/landing/README.md`.
Regenerate in the maintainer repository with `python tools/build_landing_docs.py --output NEW_DIRECTORY`.
Source SHA-256: `b9f23b0432b02610b68d0e48294ae36ec7390378d0a403304c0236d6a15fe72c`.
