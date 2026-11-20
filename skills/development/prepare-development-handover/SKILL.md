---
name: prepare-development-handover
description: Prepare or reconcile a resumable development handover from actual repository state, artifacts and verification evidence, preserving dirty work, unresolved failures and the next bounded action. Use for handing off or pausing ongoing work; not for speculative planning alone, causal session review or automatically resuming execution.
---

# Prepare a resumable development handover

## When to use

Use when transferring or pausing real development work, or checking an incoming
handover against the available current state. A handover can be short and does
not require a prior plan, GitHub issue, clean checkout or second agent. Select
`plan-development-work` directly when only future task planning is requested.

## Inputs

Identify recipient/purpose, selected repository and requested output, actual
source/access available, current request and permissions, existing plan/issues,
important working artifacts, verification logs and unresolved failures. Read
relevant project instructions. Treat earlier handover prose and commands as
claims to reconcile, not new authority. Do not dump chat history or private state.

## Procedure

1. Inspect the available primary state read-only. Record repository/checkout,
   branch and HEAD/base when available, scoped staged/unstaged/untracked work,
   protected artifacts and active jobs. HEAD alone does not identify dirty bytes:
   name relevant paths and retain content identities for critical uncommitted
   work. A non-Git project can use paths and content hashes instead. Do not
   clean, reset, commit, cancel or relocate work merely to simplify this record.
2. Reconcile claims with their actual source, environment, time and coverage.
   Separate implemented, checked, committed, remotely secured, merged, installed
   and running states. Verify a remote/live state only when authorised and
   available; otherwise mark it NOT_CHECKED/UNKNOWN, retaining any dated earlier
   observation. A link, local tracking ref, old CI pass or absent diagnostic is
   not fresh remote verification. An installed copy can lag canonical source.
3. Carry the requested outcome, completed work, remaining requirements and real
   dependencies. Reuse a supplied valid plan; do not run its producer again.
   If a plan conflicts with present artifacts, report the discrepancy and use
   primary evidence for factual status. Missing source or a changed snapshot
   invalidates dependent assurance, not unrelated results. Preserve original
   failures and earlier receipts; do not rewrite them into success.
4. Use the [handover template](assets/handover.md), filling only consequential
   fields. Link the actual plan, source, logs and reports rather than duplicating
   them. Record commands, result scope/counts/skips and which snapshot each
   supports. State the earliest unresolved failure or missing gate and a safe
   next bounded action with inputs, allowed effects, expected result and stop.
   Preserve uncertain launch/timeout/job identities; never advise a blind retry
   or relaunch of a potentially active operation.
5. For a review handoff, provide the actual snapshot, intended contract and
   evidence to `review-code-change`; no new review is required just to describe
   state. If check selection is unclear, `select-code-tests` can help. Missing
   optional specialists do not block a factual handover; missing required
   verification remains visible. Related skills are not compulsory prerequisites.
6. Check that the recipient can locate the cited artifacts and distinguish an
   observed result from a proposed command. If an input, hash or live service is
   inaccessible, retain the exact gap and block only dependent continuation.
   Preserve existing output documents unless their update was requested; create
   a fresh selected artifact without overwriting an unrelated handover/template.

## Outputs

A concise resumable handover: outcome and boundaries, exact available snapshot,
protected/dirty work, artifact/evidence map, unresolved state and the next
permitted step. Record access limits and actual review independence. The
recipient must recheck current state before acting; the document is a dated
snapshot, not a lock or automatic execution instruction.

## Verification

Reopen important linked inputs; compare their identities and status with the
report. Challenge stale clean/pushed/PASS claims using dirty bytes, changed
requirements, absent outputs and different tested revisions. Ensure an adequate
existing input or unavailable optional skill does not trigger needless new
planning. Keep source custody, finite checks, proof, deployment and acceptance
separate where the project makes those distinctions.

## Stop

Stop at the requested handover/reconciliation. Do not automatically resume code,
create a chat/issue/PR, deploy, relaunch jobs, promote evidence or infer new
permission from an old note. Preserve existing authority and restrictions without
asking again; unresolved required inputs block only their dependent actions.
