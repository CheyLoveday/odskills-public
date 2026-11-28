# Scoping fixture

All repositories, discussions and commit labels in this fixture are synthetic.
Use this snapshot as the complete available evidence. Give a contributor brief
for each candidate. The user asks for local preparation only.

## Source snapshot

- The user names `northstar/atlas-lean`, mirrored at `northstar/atlas-archive`.
  The mirror's README directs changes to `northstar/atlas-lean`.
- The canonical repository uses `main`, at revision `base-23`.
- Its contributor guide requires maintainer agreement before a public API
  removal. Documentation corrections can go directly to a PR. All changes need
  the repository's docs build. The guide allows AI-assisted contributions
  provided the contributor reviews all changes and declares AI assistance in
  the PR. No such declaration has been prepared.
- Open issue #60 asks for the legacy theorem alias `Atlas.oldFold` to be removed.
  Open PR #73 removes that declaration from the same source file and is awaiting
  review. Merged PR #71 renamed a related example without touching the alias.
- Open issue #61 reports a broken link to the `fold_map` example. The broken
  target still appears once in `docs/folds.md` on `base-23`. An open and
  closed issue, PR and history search by file path and old and current target
  name found #61 and the superficially similar merged #71. The actual diff of
  #71 changed a different link in a different file.
- The contributor only asked to repair the broken example link and is
  considering whether to pick up the old alias removal as a separate follow-up.

## Candidate requests

- S1. Give the next-action contract for the documentation correction.
- S2. Advise whether to start implementing the alias removal as a parallel PR.
