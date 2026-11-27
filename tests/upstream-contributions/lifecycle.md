# Lifecycle fixture

This is a synthetic snapshot. Work offline. The user says, “Track #80 through
the provided events and tell me whether #81 can advance. Please leave replies
as drafts.” The existing PRs already exist and are in `northstar/atlas-lean`.
The user has granted authority only to read status and draft possible replies.

- L1 at 10:00. Parent #80 is open with head `head-31`. It has an approval
  and green build on the previous head `head-30`. Its required build has no
  result on the current test merge revision `test-31`; the branch requires
  approval of the latest reviewable push. The merge queue is enabled, and
  there is no queue entry. A reviewer asks for the public regression receipt.
  Dependent #81 targets the parent branch. It needs the concrete public
  declaration introduced by #80.
- L2 at 11:00. New snapshot from the PR and base. #80 was squash-merged as
  `squash-32`; current `main` is `base-33` and its tree contains the required
  declaration with the expected public signature. The former `head-31` is
  not an ancestor of `main`. #81 still targets the old parent branch and
  has only a readiness record for that base. No new authority was granted.

For each event, report the lifecycle state, the concrete blocker or evidence,
the child disposition and any next permitted action.
