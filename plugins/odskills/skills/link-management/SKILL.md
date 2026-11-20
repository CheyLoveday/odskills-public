---
name: link-management
description: Audit and repair repository Markdown links, images and section anchors after edits, file moves, renames, archive changes or handovers. Use to find inbound references and add a repeatable link gate to existing checks. Preserve frozen sources; external URL reachability and visual rendering need separate checks.
---

# Maintain repository reading links

## When to use

Use for a selected repository's link/anchor audit or authorised repair after
edits, moves and handovers. A reader-surface gate can reuse this helper; the
selected repository owns which current files it checks and which archives stay
frozen. External URL availability and visual typesetting require separate checks.

## Inputs

Read repository instructions and current changes. Identify the entry README,
working instructions, discoverable skills and linked technical docs in scope.
Distinguish editable sources, generated views, frozen archives and external
destinations. For a relocation, establish the intended old-to-new path mapping
from actual source identity, not merely a similar filename.

## Procedure

1. Run the bundled read-only checker with an explicit root and selected inputs,
   using an existing environment with the pinned [requirements](requirements.txt)
   or an authorised selected development environment:

   ```sh
   python /path/to/link-management/scripts/check_links.py --root /path/to/repository --json README.md docs
   ```

   Paths resolve from their referring file; a leading slash means repository
   root. Parsed Markdown/reference links, images, HTML/custom anchors, duplicate
   heading anchors and supported source-line fragments are checked. Code examples
   are ignored. It never fetches a URL or rewrites a file; external URLs are
   explicitly skipped. Inspect unsupported/dynamic fragments and unresolved
   reference syntax separately rather than presenting them as verified rendering.
2. Find inbound references with `rg` when moving or renaming a destination.
   Repair only authorised editable readers. Do not delete a failing link, guess
   its destination, weaken a fragment check or rewrite frozen evidence to pass.
   Where needed, provide a separate current reader or label a historical limit.
3. Recheck the active surface and changed target headings. When requested or the
   same breakage recurs, wire the reusable checker into the existing normal test
   command; keep project-specific reader selection in that project.
4. Include a valid destination and broken-path/renamed-anchor control so neither
   an always-passing nor an always-rejecting gate can qualify itself. Retain
   missing inputs, unreadable scope and empty selection as failures or unsupported
   checks, not success.

## Outputs

Report selected scope, actual document/link counts, referring block locations,
concrete findings, repairs, external URLs skipped and frozen exclusions. Preserve
one editable implementation; refresh installed copies from the validated source
only under the corresponding adoption authority and compare bytes.

## Verification

The parser uses markdown-it-py 3.0.0's token API with CommonMark/table/strikethrough
rules and GitHub-style heading controls. See the exact
[parser source](https://github.com/executablebooks/markdown-it-py/blob/v3.0.0/markdown_it/main.py),
[token API](https://github.com/executablebooks/markdown-it-py/blob/v3.0.0/markdown_it/token.py)
and [GitHub section-link rules](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links).
File/anchor checks do not prove external reachability, visual rendering or content
fidelity. Runtime/parser and target-specific limits remain explicit.

## Stop

Stop after the selected audit, authorised repairs and proportionate gate. Preserve
user work, generated authorities and frozen sources; no publication, installation
or unrelated repository cleanup follows from a link check.
