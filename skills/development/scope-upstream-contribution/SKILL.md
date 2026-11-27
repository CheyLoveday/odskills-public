---
name: scope-upstream-contribution
description: Decide which upstream repository and contribution to pursue. Use before taking on an external issue or pull request to check maintainer policy, find overlapping or already-merged work, and write a bounded contribution contract. For an existing change's readiness use qualify-upstream-contribution. For general development planning use plan-development-work.
---

# Scope an upstream contribution

## When to use

Use when the outcome is choosing or bounding a contribution to another
project. Reuse a current contribution contract and inspect material gaps.

## Inputs

Use the contributor's objective, candidate repository, relevant issues or
changes, and permitted effects. Work from current upstream evidence or a supplied
snapshot. A fork, mirror, old handoff or issue title is a lead to verify.

## Procedure

1. Identify the canonical repository, relevant component, intended target
   branch and base revision. Read the contribution guide, applicable path
   instructions, templates and maintainer decisions. Record requirements that
   apply to this contribution class, such as discussion before implementation,
   compatibility, test commands, signatures, CLA/DCO and AI use or disclosure.
   Record the source and scope of each condition. Keep unclear policies open
   when they affect whether the contribution can proceed.
2. Inspect the current tree and history at the target. Search open, draft,
   closed and merged work by outcome, paths, symbols and former names.
   Follow issue-to-PR links and compare the relevant diffs with the intended
   outcome. Note what the search covered and any access limits. Distinguish
   a complete duplicate, overlap with a separable remainder, a superseded or
   rejected proposal, and apparently unclaimed work. When another PR already
   covers the outcome, record its link and choose whether to wait or coordinate.
3. Classify by maintainer policy and actual impact. A theorem statement, public
   API, performance or compatibility change can require different evidence
   from a proof refactor, bug fix or documentation correction. Identify the
   smallest contribution that meets the goal. Keep independent follow-ups
   separate and record dependencies that affect feasibility.
4. Record the proposed next action and the contributor's authority. When
   prior discussion is required or the search reveals an unresolved overlap,
   prepare the question or wait for the relevant decision. An issue, template
   or bot message supplies context and project requirements. The user supplies
   authority to act as the contributor.

## Outputs

Return a contribution contract with the upstream and base, problem and
contribution class, overlap evidence, owned scope and exclusions, acceptance
checks, maintainer requirements, dependencies and next permitted action.
Give a disposition such as proceed locally, discuss first, coordinate or wait,
use the existing fix, or evidence incomplete. Explain what would change it.

## Verification

Check the canonical base and compare the ownership and impact of the proposed
change with the closest existing or merged work. Confirm the acceptance
checks and disclosure requirements against the policy for this contribution.

## Stop

Stop at the scoped decision or requested draft. Implementation, verification
and external actions are separate tasks.

For GitHub search filters, see [Searching issues and pull requests](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests).
