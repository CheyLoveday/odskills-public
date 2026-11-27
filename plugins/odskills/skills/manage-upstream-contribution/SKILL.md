---
name: manage-upstream-contribution
description: Prepare, submit or track an upstream pull request under the contributor's authorization. Use to bind the submission to its qualified diff, interpret current GitHub CI and reviews, follow a merge, or advance dependent contributions. For a PR description alone use plan-development-work. For readiness evidence alone use qualify-upstream-contribution.
---

# Manage an upstream contribution

## When to use

Use for submission preparation, an authorized remote action or ongoing
tracking of an upstream contribution and its dependencies.

## Inputs

Use the requested lifecycle action, its authorization, the upstream and fork
or branch identity, any issue or PR URL, current base/head, and relevant
contract, readiness and dependency records. A status request needs the
current record and relevant commitments. A submission request also needs
sufficient evidence and a verified outgoing diff.

## Procedure

1. Confirm the repository, target branch, source owner/branch and revision
   to use. Search for an existing PR for the head or intent before creating
   one, including after an ambiguous submission response. For a draft or
   update, match the current base and head to the readiness evidence. Inspect
   the exact outgoing changes and public text against project rules and
   permitted disclosure. Include actual validation,
   material limitations, and applicable attribution or project declarations.
   Use issue-closing keywords only when the contribution is intended to close
   the issue and the target branch supports that behavior.
2. Follow the user's scope for each external effect. Read host state and
   prepare local drafts within the requested scope. Fork creation, pushing,
   opening or editing a PR, posting a reply, rerunning CI, rewriting a branch,
   requesting review, joining a queue and merging are distinct effects.
   Use existing authority for the requested action and verify its resulting
   URL, base, head and state. When authorization or a required gate is
   missing, give the requested local draft or a precise blocker. Use
   `qualify-upstream-contribution` when a readiness record needs repair.
3. Interpret status on the revision the host currently evaluates. Record
   required versus advisory checks, their producing source and whether they
   are pending, absent, skipped, cancelled, failed or successful. Check
   current branch rules, review threads and latest-approval requirements.
   Use the check panel or equivalent host evidence to distinguish the head
   from the test merge. On GitHub the head applies when the test merge has no
   status. A queued PR may also require checks on its merge-group revision.
   Older green checks and approvals carry only their observed scope. Diagnose
   the concrete blocker before deciding what change or authorized retry
   would address it.
4. For each material review item, record the request, pertinent diff or
   evidence, decision and next action. When a change is authorized, keep
   unrelated work out and refresh affected validation and review evidence
   against the new revision. Record author responses separately from reviewer
   acceptance and observed thread state. Track draft, open, queued, merged
   and closed-without-merge based on host evidence.
5. After a merge, confirm what landed on the destination branch and whether
   it satisfies each dependent change's actual prerequisite. A squash or
   rebase can change commit identities. Inspect the landed code or
   declaration when ancestry alone is inconclusive. Re-evaluate the child's
   base, outgoing diff, checks and authorization before retargeting, rebasing
   or submitting it. Preserve unrelated branch work.

## Outputs

Return the requested draft or lifecycle record with the PR URL where known,
revision-bound checks and review state, actions performed, open blockers and
permitted next action for each dependent contribution.

## Verification

Recheck the PR after an authorized mutation, and confirm what landed and
where before marking a dependency satisfied. If the effect is ambiguous,
read current state before retrying.

## Stop

For monitoring, follow the requested completion condition and record a concrete
blocker if it cannot be reached within the task. Stop at the requested
lifecycle boundary.

For GitHub behavior see [required status checks](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks),
[protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
and [linking an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).
