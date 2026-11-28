# Required-check revisions fixture

Use this synthetic host snapshot as the complete available evidence. The user
asks for a read-only diagnosis of #90 in `northstar/atlas-lean`, with no
requests, reruns or queue changes.

- M1 before queue entry. Target is `main` at `base-40` and the current PR head
  is `head-41`. The test merge `test-41` exists and has no statuses or check
  runs. The PR check box says “Checks for the latest head commit”. It shows
  the single required `lean / build` check succeeded on `head-41` from the
  expected GitHub App. A stale run on `head-39` failed with the same check name.
  GitHub reports the PR eligible to enter the queue. Nobody has queued it yet.
- M2 after a maintainer queues it. The queue shows group revision `queue-42`
  for #90 and still expects `lean / build`. The Actions workflow is configured
  for `pull_request` only and no matching check has reported on `queue-42`.
  GitHub still shows the green head check. The queue entry is waiting.

Explain each event and give the next permitted action.
