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
