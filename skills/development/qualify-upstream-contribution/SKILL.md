---
name: qualify-upstream-contribution
description: Assess whether a concrete upstream change is ready for submission or review. Use to reconcile repository-required checks, Lean or other specialist evidence, and independent review against the exact candidate revision. For reviewing a diff alone use review-code-change. For submitting or tracking a pull request use manage-upstream-contribution.
---

# Qualify an upstream contribution

## When to use

Use when a contributor needs a readiness verdict for a specific patch, with
a concrete target and evidence to inspect or obtain.

## Inputs

Use the contribution contract if available, the target's current requirements,
the candidate diff and its source state, and any check or review receipts.
A supplied contract and trustworthy matched evidence can be sufficient.
Establish missing requirements from the repository when possible.

## Procedure

1. Bind the candidate to the upstream repository and target branch, base
   and head SHAs, and the relevant toolchain, dependency pins and platform.
   Inspect the outgoing diff. Describe dirty inputs separately and identify
   any diff or working-tree state needed to interpret local checks. For hosted
   CI distinguish a head run, a test merge with its inputs and a queue run.
2. Map the contract and repository requirements to concrete evidence. Record
   what each check exercised, its input identity, command or run link, result
   and any skips or exclusions. Use target-documented commands and a
   discriminating test at the affected caller boundary where appropriate.
   Inspect candidate scripts and workflows before executing them, and stay
   within the user's authority for execution and remote effects.
3. Seek specialist evidence only when the change needs it. For example,
   `audit-lean-correspondence` can supply statement and axiom checks,
   `profile-lean-kernel` can supply matched measurements, and
   `audit-computational-evidence` can check finite verification coverage.
   `select-code-tests` can help choose checks. Reconcile the actual
   deliverables and scope, including limitations. A passing build alone
   establishes build success for its inputs.
4. If independent review is required or requested, bind it to the actual
   diff and acceptance criteria. Use an existing matched review or request
   an independent review through the authorized channel when available.
   `review-code-change` can supply the review method. Record unresolved
   findings and the observer's independence. Author self-review, reviewer
   requests and drafted review briefs each have their own evidence status.
5. Reconcile every applicable gate. Track pass, fail, pending, unavailable,
   skipped, stale and not applicable with reasons. An empty test selection
   cannot demonstrate the behavior the test was meant to exercise. After a
   head, base, environment or requirement change, recheck affected evidence
   and retain older receipts for their original scope. Carry evidence forward
   only with a concrete justification that its checked inputs and scope are
   still valid. Where useful, run permitted missing checks or name exactly
   what remains to be obtained.

## Outputs

Return the qualified snapshot, a requirements-to-evidence record, material
findings and a readiness verdict for the requested next step. State which
results were inspected or newly observed and which gates still apply. Report
local readiness and hosted requirements with their own evidence.

## Verification

Tie each supported readiness condition to the source and scope that establish
it. A missing required check or review leaves readiness unestablished.

## Stop

Stop at assessment and requested verification. External submission, review
requests and merge actions require the corresponding authority.
