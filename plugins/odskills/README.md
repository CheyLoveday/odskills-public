# odskills generated plugin

Generated, non-authoritative deployment artifact. Do not edit directly.
Canonical source: `skills/<domain>/<skill-id>/` in CheyLoveday/odskills-public.
Regenerate: `python tools/build_plugin.py --output plugins/odskills`.
Check: `python tools/build_plugin.py --check`.
`SOURCE.json` records every source path/SHA-256, generator SHA-256 and
the combined input fingerprint; version changes with either input.

All packages remain experimental. Native IDs and package bytes are
preserved, with a flat `skills/<id>/` layout. No MCP server, hooks, apps,
credentials or dependency installation is included. The source repo's
AGENTS.md is not adopted by installing this plugin. Consumers retain
their own authority and acceptance requirements. Helper requirements
remain declared within their packages. Installation and enumeration
do not establish successful application or ChatGPT UI verification.
