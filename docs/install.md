# Install and verify odskills

Start from a reviewed [repository revision](https://github.com/CheyLoveday/odskills-public)
or [release](https://github.com/CheyLoveday/odskills-public/releases). Record
its full Git commit. Keep the entire selected skill folder so relative
references, scripts and assets remain available.

| What you need | Route |
| --- | --- |
| An agent can read a named package, including an Open Math OS handoff | [Portable source](#use-a-portable-package) |
| One skill discoverable in Codex | [Standalone installation](#install-one-skill) |
| The complete library as namespaced skills | [Codex plugin](#install-the-codex-plugin) |

## Use a portable package

Give the agent the source revision, the path under `skills/` and the task.
For example, ask it to read
`skills/mathematics/audit-computational-evidence/SKILL.md` at that revision
and follow its links within the folder. An agent that receives files without
a checkout can use the same folder extracted from a source archive. This
route works through an explicit read of the instructions in the consumer's
own workspace.

## Install one skill

Use the [repository-local copy example](../README.md#use-one-pinned-skill)
or ask Codex's bundled `skill-installer` to install the exact GitHub
package. A suitable request is:

> Use skill-installer to install
> `skills/mathematics/audit-computational-evidence` from
> `CheyLoveday/odskills-public` at [full commit] into [project]/.agents/skills.

The bundled script accepts the same inputs as `--repo`, `--ref`, `--path`
and `--dest`. It offers `--method download` for the GitHub archive and
`--method git` for Git transport. Its default destination is the selected
Codex profile's `skills/` directory for user scope. Choose a fresh
destination for a version change and keep the old folder outside skill
discovery directories for rollback.

Run `tools/verify_install.py --source <pinned-skill-folder> --installed
<consumer-skill-folder>` with Python 3.12 to check complete package bytes.
Start a fresh session in the consumer project and check the skill in
`/skills`. Use an explicit skill request for the first task.

## Install the Codex plugin

Use a pinned checkout or extracted source archive that contains
`.agents/plugins/marketplace.json` and `plugins/odskills/`. From that root,
run:

```sh
odskills_marketplace=$(pwd -P)
codex plugin marketplace add "$odskills_marketplace"
codex plugin add odskills@odskills-public --json
codex plugin list --marketplace odskills-public --json
```

To register directly from GitHub, use the reviewed pin for the package
you want in place of the local marketplace registration. The example
below is a previously tested baseline. To install Lamport-Plus, use the
[Lamport-Plus pin instructions](#lamport-plus). Then run the same `add`
and `list` commands above.

```sh
codex plugin marketplace add CheyLoveday/odskills-public --ref 6fd47e703453ac1b3f2c1a56ae767cc6f188f292
```

Compare the returned version with `plugins/odskills/SOURCE.json` and
confirm the installed entry is enabled. In a source checkout with the
[development requirements](../CONTRIBUTING.md#local-checks), use
`python tools/build_plugin.py --check --output <installedPath>` to verify all
installed bundle bytes. Start a fresh Codex session and use, for example,
`$odskills:audit-computational-evidence`. Leave the source pin available
for future installs. If multiple odskills copies are available, use the
loaded path to identify which supplied the instructions.

The marketplace uses the [OpenAI local marketplace
format](https://developers.openai.com/plugins/build/plugins#marketplace-metadata).
After registering the marketplace, restart ChatGPT desktop so it reads the
source. In Plugins Directory select **odskills public skills** and install
**odskills** from that source. The [Codex CLI checks below](#checks) are the
observed host results. Direct ChatGPT desktop verification remains open.

### Replace or roll back the plugin

Keep the reviewed source revisions or archives outside the plugin cache.
To replace this marketplace's installation with a different pin, remove its
selected plugin and registration, then run the install procedure from the
other pinned root.

```sh
codex plugin remove odskills@odskills-public
codex plugin marketplace remove odskills-public
```

Recheck the enabled version and the installed bytes after replacement.
Native uninstall removes the cached copy, so use the retained source for
rollback. Earlier source releases with no repository marketplace can still
provide standalone packages. Their plugin payload can be exposed through
its own [local marketplace
entry](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually).

## Lamport-Plus

For the standalone skill, follow [Install one skill](#install-one-skill)
with the complete `skills/mathematics/lamport-plus` folder at a reviewed
commit containing that package. Use the project destination
`.agents/skills/lamport-plus/` and compare it with the pinned source using
`tools/verify_install.py`. In a fresh Codex session invoke `$lamport-plus`.

For the Git-backed plugin, replace `REVIEWED_LAMPORT_PLUS_COMMIT` with the
full reviewed commit whose `plugins/odskills/SOURCE.json` includes
Lamport-Plus. See [plugin verification](#install-the-codex-plugin).

```sh
codex plugin marketplace add CheyLoveday/odskills-public --ref REVIEWED_LAMPORT_PLUS_COMMIT
codex plugin add odskills@odskills-public --json
codex plugin list --marketplace odskills-public --json
```

In a fresh Codex session invoke `$odskills:lamport-plus`. In ChatGPT desktop, select
**odskills public skills** in Plugins Directory after registering the reviewed
marketplace and restarting. Install **odskills** from that source. The
desktop route requires its own discovery and application check.

For a first task, ask for the exact integer parity proof in learning mode.
Check that the proof constructs the odd-square witness, preserves the
integer domain and offers a transfer question. The [worked example](../skills/mathematics/lamport-plus/examples/elementary-proof.md)
shows the intended mathematical scope. For rollback, keep the previous
reviewed package outside discovery paths, then follow the
[standalone replacement](#install-one-skill) or [plugin rollback](#replace-or-roll-back-the-plugin)
procedure for the relevant route.

## Mathematical reframing

The standalone `reframe-mathematical-bottleneck` skill is available in
[v0.1.0-alpha.4](https://github.com/CheyLoveday/odskills-public/releases/tag/v0.1.0-alpha.4).
For a [standalone installation](#install-one-skill) use
`skills/mathematics/reframe-mathematical-bottleneck` at the reviewed pin.
Invoke `$reframe-mathematical-bottleneck` for the standalone skill or
`$odskills:reframe-mathematical-bottleneck` for the plugin. The complete
package includes the seven method cards and three runbooks.

## First application

Ask `audit-computational-evidence` to check a claimed exclusion for all
`n = 1 + 2t` with `t ≥ 0`. The predicate has period 6 and accepts residue 3.
The receipt only reports that `n = 1` failed. A correct result identifies
the reachable residues `1, 3, 5` and the passing lift `n = 3`. If you also
supply period zero and an empty input roster, the audit should reject that
certificate. Verify which installed instruction and reference the agent
actually read.

## Checks

The local checks on 23 November 2026 used Codex CLI 0.169.1 and Python
3.12 on macOS. The bundle tested was
`0.1.0-experimental.h352ddd730dcd` built from the
[landed periodic-proof source](https://github.com/CheyLoveday/odskills-public/commit/6cc1978ebb4ffb25e227eee1c76d2ebe9511cd1b).

- The published alpha.3 archive passed its checksum. A copied skill from
  that archive was discovered in a clean project. The verifier rejected a
  partial copy and the copy recipe refused an occupied destination.
- Project-local copies and GitHub downloads matched and exposed all 18
  packages. The Git installer also matched and exposed a user-scoped
  package in a disposable profile, and refused a duplicate destination.
- The plugin installed from a local bundle, a downloaded GitHub source
  archive with no checkout, and a Git-backed marketplace pinned at
  `6fd47e7`. Each install matched all 85 files
  and exposed all 18 namespaced skills. Removal, rollback to the reviewed
  older payload and reinstallation passed with fresh byte checks.
- Fresh read-only Codex sessions read and applied the project-local,
  explicitly referenced plugin-cache, and portable handoff packages.
  The installed link checker passed the valid-anchor case and rejected a
  stale anchor from three package paths.
