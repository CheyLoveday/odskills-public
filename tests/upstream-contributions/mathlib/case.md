# Read-only mathlib case

Use this retained snapshot of a public contribution. A colleague asks whether
to implement issue #43855 now, whether the final notation diff had sufficient
verification for review, what happened in the review and merge process, and
whether the related semilinear change could advance. Also say what help you
can provide if a future contributor requests a draft GitHub or Zulip comment
about this case. Work locally. The public actions listed below happened in
the historical case.

## Project guidance observed on 28 November 2026

- The Lean learning page links to good first issues and asks human
  contributors to coordinate if they take one on. The contributor guide
  welcomes small changes to established theories. New topics or potentially
  controversial changes can need community discussion. Changes should fit
  existing APIs, naming, imports, style and documentation.
- The upstream target is `leanprover-community/mathlib4:master`. The guide
  permits local `lake build` or mathlib CI for broad compilation. Development
  branches are typically on contributors’ forks. PRs should use mathlib’s
  title/body conventions. The guide strongly discourages rebasing or
  squashing a branch after reviews start. Bors squashes changes when landing.
- Reviewer approval and maintainer merge authority are distinct. The
  handbook documents Bors staging, a time limit on delegated merge authority
  and early expiry for restricted paths. It also documents tracking
  prerequisite PRs through dependency lines in the PR description.
- The AI policy prohibits using LLMs to write GitHub or Zulip comments.
  For AI use on a contribution, it requires telling reviewers in the PR
  description which tools were used and how, and requires contributors to
  understand and explain the resulting work. Substantial LLM code triggers
  the project’s `LLM-generated` label procedure.

[Learning Lean](https://leanprover-community.github.io/learn.html)
[Contribution and AI policy](https://leanprover-community.github.io/contribute/index.html#use-of-ai)
[Contribution workflow](https://leanprover-community.github.io/contribute/how-to-contribute.html)
[Review guide](https://mathlib.org/contribute/pr-review.html)

## Issue and diff

[Issue #43855](https://github.com/leanprover-community/mathlib4/issues/43855)
was labelled `good first issue` and closed as completed at 21:50:37 UTC on
29 October 2026. It asks for notation for multilinear maps in view of the
semilinear generalization proposed in #42534, and considers a semilinear
variant. Searching public issues and PRs by `43855` and `MultilinearMap`
plus `notation` found [PR #43877](https://github.com/leanprover-community/mathlib4/pull/43877)
with its explicit closing reference, and
[PR #42534](https://github.com/leanprover-community/mathlib4/pull/42534).
The latter’s final PR body explicitly marks #43877 as its dependency.
The PR body for #43877 describes the glyph `→ₗₘ`. A contributor
[update](https://github.com/leanprover-community/mathlib4/pull/43877#issuecomment-6268509813)
records a change to `→ₘₗ` after a Zulip poll. The final
[diff](https://github.com/leanprover-community/mathlib4/pull/43877/files)
has 393 additions and 409 deletions over 22 files. `Basic.lean` adds the
`→ₘₗ[R]` notation and elaboration and delaboration support. Other files
migrate existing call sites. A new `MathlibTest/LinearAlgebra/Multilinear.lean`
uses `#guard_msgs` with three forms of function domain: dependent, constant,
and abbreviated dependent. The landing commit's parent
`e1b16f5f6a696c975ec188a85ed08ba1cc98f3bc` lacks the new notation in
`Basic.lean`.

## Review and verification evidence

- Earlier head `47f7d4f8170a3dfb1e5059cd732ad4478b151bb8`.
  The [fork CI run](https://github.com/leanprover-community/mathlib4/actions/runs/40757334458)
  has passing Build, Lint style and Test and lint. On 29 October the
  [review](https://github.com/leanprover-community/mathlib4/pull/43877#pullrequestreview-5701947102)
  approved this head with final delaborator suggestions and a Bors
  delegation. The reviewer also [asked for tests](https://github.com/leanprover-community/mathlib4/pull/43877#discussion_r4415780502).
  The [delegation receipt](https://github.com/leanprover-community/mathlib4/pull/43877#issuecomment-6503933830)
  covers the author until 12 November at 17:37 UTC and restricts the paths
  they can change.
- Candidate head `448071dd1bbda0bccd03164cb4ac6986475a32d6` uses
  `leanprover/lean4:v4.36.0-rc2`. The final two commits apply the delaborator
  suggestions and add the test file in the authorized directories. The
  author's reply confirms the test file addition. The public approving
  reviews inspected name earlier heads.
- For a limited-evidence control, assess the candidate once using only the
  older CI and review receipts above. Then include these observed candidate
  receipts. The [fork CI run](https://github.com/leanprover-community/mathlib4/actions/runs/40952232778)
  finished at 21:17:38 UTC with Build, Lint style, Test and lint and the
  `test mathlib` step successful. The fork workflow passes the PR head SHA
  to its build template. The author's
  [Bors command](https://github.com/leanprover-community/mathlib4/pull/43877#issuecomment-6508567827)
  appeared at 21:18:48 UTC under the earlier delegation.
- The GitHub PR API reports `state: closed`, `merged: false`,
  `merged_at: null` and `merge_commit_sha:
  c90c832d02df43612582b80121671d5d952f50a7`. The named commit has the PR
  head and `e1b16f5` as parents, with no check runs. The API’s base SHA
  field on the PR object is `5b66d0084d7d0bfeb5fa9cad36f4c36e96db6ace`.
- The [Bors comment](https://github.com/leanprover-community/mathlib4/pull/43877#issuecomment-6509143439)
  records a successful landing at 21:50:37 UTC. Bors staged
  `237c53b714060dd21b54c29e7e3256ec0c65f132`. The
  [staging workflow run](https://github.com/leanprover-community/mathlib4/actions/runs/40956808630)
  succeeded at that commit. Its [Test and lint job](https://github.com/leanprover-community/mathlib4/actions/runs/40956808630/job/123751183317)
  log identifies `MathlibTest.LinearAlgebra.Multilinear` as built.
  GitHub comparison from the staging SHA to observed `master`
  `f9388e8dd988e8a6727407b07c27e72b76b44de1` reports 693 ahead and zero
  behind. The staged commit includes the [new notation and test](https://github.com/leanprover-community/mathlib4/commit/237c53b714060dd21b54c29e7e3256ec0c65f132).
- The [dependency bot](https://github.com/leanprover-community/mathlib4/pull/42534#issuecomment-6509405959)
  crossed off #43877 on #42534 at 22:05 UTC on 29 October. #42534 has its
  own [Bors landing receipt](https://github.com/leanprover-community/mathlib4/pull/42534#issuecomment-6722737679)
  and [successful staging run](https://github.com/leanprover-community/mathlib4/actions/runs/42488803723)
  at `a8d0dfed4f2f657d517c034437ce238c46fef1a8` on 8 November. GitHub
  compare to observed `master` reports 496 ahead and zero behind from
  that commit. The observed tree contains the test with both `→ₘₗ`
  and `→ₘₛₗ` cases.

The exercise has hosted evidence and source reads only. No local Lean
execution, upstream changes or external discussion is part of the case.
