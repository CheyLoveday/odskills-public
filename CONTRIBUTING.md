# Contributing

Choose one outcome. Update an existing skill if it already covers the outcome.
Give a new package a unique lowercase hyphenated ID and a `SKILL.md` with
`name` and `description` in YAML frontmatter. State when to use it, its inputs,
procedure, outputs, verification and stopping conditions. Put optional detail
in linked resources and add matching and non-matching discovery cases.

## Local checks

Use Python 3.12 with the pinned development requirements.

```sh
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python tools/build_catalogue.py
python tools/validate_library.py
python tools/build_catalogue.py --check
python tools/build_plugin.py --check
python -m unittest discover -s tests -p 'test_*.py' -v
```

After a package change, stage the intended skill files. Move the previous
generated `plugins/odskills` directory to a backup outside the checkout,
then regenerate it with `python tools/build_plugin.py --output plugins/odskills`
before running the plugin check. Commit the source and generated files together.

Use shareable inputs for tests and keep examples and dependency notices with
the affected package. When reporting a behavioral test, distinguish discovery,
instruction reads and the observed output.

## Evaluation labels

A skill can be available at any evaluation level. Lifecycle, such as
experimental, and behavioral evidence are recorded separately.

| Label | Meaning |
| --- | --- |
| Unrecorded | The catalogue has no evaluation entry for this skill. Check the package history for earlier tests. |
| Untested | The maintainer has recorded that behavioral tests are pending. Static and packaging checks may already have run. |
| More tests needed | Some behavioral evidence exists. The note names the observed scope and the main open test. |
| Tested | Behavioral tests passed for the scope in the note. The evidence link identifies the checks and their limits. |

Record the label in the package's optional `metadata.yaml` under `evaluation`.
Use `untested`, `more-tests-needed` or `tested` for its `status`.
For the two evidence-bearing labels, add a one-line `note` and set
`evidence: TESTING.md` when recording tests for a package. Keep the record
next to `SKILL.md` so it travels in standalone copies and plugin bundles.
Existing entries can still use a public HTTPS evidence link.

Record the tested revision or release, host and test scope in `TESTING.md`.
Keep observed results, failures and open tests visible. Include a shareable
replay when the inputs can travel with the package. Keep assessor expectations
out of the replay prompt. For a new package awaiting behavioral tests, record
`untested` and name the planned check. Review the entry when tested behavior
changes and retain the earlier results with their pins.

Omit `evaluation` where the evidence is unrecorded. The Markdown catalogue
links the label to the evidence. In the JSON catalogue, `TESTING.md` resolves
relative to the skill's `path` directory and an unrecorded evaluation is
`null`.
