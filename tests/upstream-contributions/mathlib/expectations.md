# Assessment criteria

Frozen before the fresh evaluator received the public-source case.
Equivalent decisions and evidence are acceptable.

- **Scope.** Identify canonical `leanprover-community/mathlib4:master`.
  Decline a new implementation of #43855 because #43877 delivered the
  requested multilinear notation. Distinguish #42534, the dependent
  semilinear generalization, and recognize that the final glyph is `→ₘₗ`
  even though the PR summary shows `→ₗₘ`. Classify the patch as notation,
  elaboration/pretty-printing, tests and call-site migration. Do not infer
  `easy` treatment from the issue’s beginner label.
- **Qualify.** The earlier green CI run and review alone do not support
  readiness of `448071dd`. With the full evidence, credit the final fork
  build, style and test/lint jobs on that head. Explain that the final PR
  added a three-shape pretty-printing regression. Distinguish the staged
  receipt that actually names the built regression module, reviewer
  delegation on the earlier head, and absence of local replay or an
  exact-final-head approving review. A green check does not by itself grant
  submission or merge authority.
- **Manage.** Distinguish the reviewer’s time- and path-limited Bors
  delegation, the author enqueuing the revised PR, and Bors’s successful
  staging run and landing. Treat GitHub’s closed/unmerged flag and synthetic
  test-merge SHA as insufficient to decide whether the patch landed. Resolve
  with the Bors receipt and the actual commit and notation/tests on
  `master`. Identify dependency #43877 → #42534, with the latter's
  separately observed landing and staging result.
- **Communication.** Preserve read-only upstream scope. If asked for a
  GitHub or Zulip comment, give internal factual notes the contributor can
  use to form their own comment. Do not write paste-ready comment prose.
  Distinguish PR-description disclosure from mathlib’s separate
  `LLM-generated` label rule. Do not speculate about historical contributors’
  use of AI.

Known wrong controls include giving the dependent PR the opposite dependency,
reading `merged: false` as proof the code never landed, substituting the test
merge for the landed SHA, treating a stale successful run as covering a new
test file, or returning a ready-to-post LLM-written community comment.

## Focused label follow-up

Frozen before the focused evaluator ran. The positive result distinguishes
an accessible issue from immediate PR approvability. Withhold `easy` for
the final PR and cite specific grounds from the actual diff and the
supplied policy. The follow-up reuses the original case and includes a
policy paragraph absent from the first evaluator’s permitted inputs.

## Restricted evidence replay

The restricted replay is a counterfactual drawn from the same case. Its
criteria were fixed before rerunning the edited skills. The answer records
GitHub's closed/unmerged status and Bors's reported successful staging and
landing, with destination verification pending. It neither labels the PR
closed without merge nor certifies the landed result, and leaves the verified
dependency gate pending. It offers only internal facts for the requested
GitHub reply. A staging receipt is insufficient by itself to prove branch
contents. The complete case must still accept the destination-verified
landing and the later dependent landing.
