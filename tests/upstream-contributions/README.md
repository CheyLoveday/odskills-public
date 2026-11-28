# Upstream contribution evaluation

27 November 2026. The cases use fictional repositories, revisions and
receipts. Codex evaluators ran in separate fresh contexts with the requested
local reads and no parent conversation. The author selected the acceptance
criteria before drafting and compared the returned decisions against them.
The evaluators shared the host and filesystem. They were instructed to read
only the supplied files and received no acceptance criteria.

The [mathlib replay](mathlib/README.md) separately exercises actual public
contribution records and the revised venue and merge guidance.

## Decisions observed

| Case | Result |
| --- | --- |
| [Scope](scoping.md) | S1 proceeded locally with the one-link docs fix at `base-23`, distinguished merged #71, and recorded the docs build and disclosure. S2 waited for open #73 and identified the rule requiring maintainer agreement for API removal. |
| [Qualification](qualification.md) | Q1 accepted readiness on `head-17/base-23/toolchain-4`. Q2 withheld it despite a dirty build and a green dashboard. The output identified the empty regression selection and the stale review and theorem receipts. |
| [Lifecycle](lifecycle.md) | L1 kept the open parent and its child waiting. It identified the old approval and missing current build and left the reply as a draft. L2 verified the expected declaration on `base-33` after the squash and kept the child pending a changed-base assessment. |
| [Composition](composition.md) | H1 used the existing C4 contract and matched docs evidence to produce a local brief. H2 identified the unavailable build for the changed link at `head-35` and withheld readiness. Neither needed a new scoping pass or another specialist. |
| [Check revisions](check-revisions.md) | M1 accepted the host-selected `head-41` check despite the empty test merge and stale failure. M2 identified the absent `queue-42` check and missing `merge_group` trigger. The diagnosis stayed read-only. |

All first-round decisions matched the [acceptance criteria](expectations.md).
The first lifecycle response emphasized the missing check on the test merge
without discussing possible head fallback. The evidence still contained no
passing build on the current head. The lifecycle guidance was clarified and
the separate check-revisions case exercised both fallback and queue checks.
A fresh evaluator then replayed the original four cases with the revised
guidance. All eight decisions again matched the criteria. Its L1 answer
explicitly distinguished the absent result on the test merge from the absence
of a passing check on the current head.

The author also applied the criteria to deliberately wrong outcomes. The
checks rejected crediting Q2's stale green dashboard or empty regression,
holding Q1 despite its matched receipts, denying L2's observed squash merge
because of ancestry, using the old child readiness receipt on the new base,
treating M1 as blocked by the empty test merge, treating M2 as green on
head-only evidence, and reporting a push in H1. These were manual controls
on the decision criteria.

## Routing and replay

A separate fresh evaluator received the six upstream prompts from
[discovery prompts](../discovery/prompts.json) without labels, and the
descriptions of the three new skills, `plan-development-work` and
`review-code-change`. Its choices in alphabetical prompt order were scope,
plan, manage, qualify, review and plan. All three positive prompts selected
the intended skill. All three near misses selected an existing specialist.
This exercises description-level routing with a supplied shortlist.

To replay a case, give a fresh evaluator the case and corresponding
`SKILL.md` and ask for the requested decisions using only local reads of those
files. For composition, supply qualify and manage together. Keep
`expectations.md` with the assessor. The fixture establishes decisions on the
supplied evidence. Native host activation, live GitHub actions, live Lean
verification and comparative value remain unverified.

## Source identity and local checks

The source base was `90be14e2acfd2cb33a3d6438aca0d202597be442` of
`CheyLoveday/odskills-public`. SHA-256 hashes bind the explicitly supplied
entrypoints. Shipped files differ from the final trial only in whitespace.

| Package | First trial | Final trial | Shipped |
| --- | --- | --- | --- |
| Scope | `5e660a2bfbb86fc8c4a5b8c1fef004a873bac6c396a085615eebc1caefc923d6` | `c21dc3690d780c7ce38d2109e3f863a292e8889b19b6b031281aa05476239e9f` | `e9bc19134aae83147200fe80180627ea8ed1c5b80a00f919dc8dbfddc0a53c74` |
| Qualify | `987db84386e9a3729b42770b32734c63afc9c485d69f033dd7bd4cac033a1535` | `122bd4f86623d0b22ec4de3c2416ceebf49900164031de227b7e9d946c9ec632` | `ba2e7f9c882817dfa1aa042c3c3a1df4ea24d9915170c3649c408d1c1712995a` |
| Manage | `575787fa940e0dd5f99e443058aef6015b2e24581dea6d64a538a774d81e2409` | `9067380f6efb5a933c77c6acbac5f60ae56a337117ca0e68de4bf2996d4ca2b5` | `db61470f96c4a8b941f212ff11bc1bde6d8b140afcd4722fdc1c6b3ad43184df` |

GitHub.com documentation checked on 27 November 2026 supports the search
filters, required-check revision selection, merge-queue event, protection
rules, issue-closing behavior and changed commit identity after squash or
rebase. The target repository's configured rules still govern a live case.
[Search](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests)
[Required checks and merge groups](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)
[Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
[Issue linking](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
[Merge methods](https://docs.github.com/en/pull-requests/reference/pull-request-merges)

A native read-only CLI probe using Codex CLI 0.169.1 stopped before a turn
started. It exited 1 with an in-process app-server initialization error
(`Operation not permitted`) under the enclosing sandbox. The separate
fresh-context evaluator lane completed. Native discovery remains unverified.
A shell source review initially failed because the zsh loop variable
`path` changed shell command lookup. Renaming the variable to `skill_file`
restored the read with no changes to source files.

Python 3.12 passed catalogue generation and check, library validation for
24 skills, the byte-for-byte plugin check for 127 files, and all 53 repository
unit tests. The standalone skill checker passed all three entrypoints.
The link checker passed the README, catalogue, new packages and test record
with 50 local links across 15 documents. It skipped 10 external destinations.
