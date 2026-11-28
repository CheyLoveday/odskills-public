# Mathlib contribution replay

The public case follows [issue #43855](https://github.com/leanprover-community/mathlib4/issues/43855),
[notation PR #43877](https://github.com/leanprover-community/mathlib4/pull/43877)
and its [dependent PR #42534](https://github.com/leanprover-community/mathlib4/pull/42534).
The purpose is to exercise target-specific communication policy and confirm
what landed when the host and the repository's merge bot report different
states.

## Initial case and revision

The 28 November 2026 assessment used the [case](case.md) with the guides at
`e1da43c46e439595320685024889d3498bfc69b1`. One fresh context used the
guides and one received only the case. Both identified the duplicate, bound
the candidate evidence to the correct revision, resolved the Bors/GitHub
disagreement, and offered internal notes under mathlib's comment policy.
The comparison did not establish added value on those decisions. The
initial case lacked the rule for an `easy` PR and did not ask for that
classification. A [focused follow-up](classification-follow-up.md) supplied
the rule and withheld `easy` for the 22-file diff and its new test file.

The revision makes two decisions explicit. Scope and manage check the
intended venue's drafting rules before producing public prose, including
drafts prepared locally. Manage checks the repository's merge driver and
verifies the destination branch when the landing is reported or the sources
disagree. The [mathlib AI policy](https://leanprover-community.github.io/contribute/index.html#use-of-ai)
and [PR lifecycle guide](https://leanprover-community.github.io/contribute/how-to-contribute.html#lifecycle-of-a-pr)
are the project sources.

## Revised-guidance results

Codex ran in separate fresh contexts with explicit entrypoint reads on
28 November 2026. The evaluators had the selected fixtures and guides.
The author retained the [criteria](expectations.md) separately and
assessed the returned decisions. Fixture reads were local.

| Replay | Observed decision |
| --- | --- |
| Complete case | Use the existing `→ₘₗ` fix. The older `47f7d4f` CI and review did not qualify the changed `448071dd` candidate. Matched fork CI supported the candidate for review, with exact-final-head approving review unobserved. GitHub's `c90c832` was its test merge. Bors tested and landed `237c53b` on `master`, which satisfied the dependency for #42534. #42534 later landed separately as `a8d0dfe`. The response offered internal facts for any future comment. |
| [Restricted evidence](restricted-evidence.md) | Bors reported a landing and had a successful staging run. The destination could not be inspected. The output kept landing verification and #42534's prerequisite pending, and supplied internal factual notes for the comment request. |
| [Synthetic lifecycle](../lifecycle.md) | An old check and approval left the parent and child waiting. The observed destination tree later satisfied the child prerequisite, and the child still needed a new base assessment. The response gave internal notes because the fixture supplied no venue rule. |

A second synthetic replay supplied one extra fact from the fictional
repository's contributor guide: agent-assisted private drafts were allowed,
with no applicable disclosure requirement for the private draft. The
evaluator supplied the requested private draft, kept the receipt unverified
for the current head and performed no remote action.

The author also inspected the captured full-case source evidence. Exact
fork CI and the Bors staging run each recorded building
`MathlibTest.LinearAlgebra.Multilinear`. The staged commit is in the recorded
`master` history, and the dependent PR has its own staging and landing
receipts. [Fork CI](https://github.com/leanprover-community/mathlib4/actions/runs/40952232778/job/123735398246),
[staging CI](https://github.com/leanprover-community/mathlib4/actions/runs/40956808630/job/123751183317),
[destination comparison](https://github.com/leanprover-community/mathlib4/compare/237c53b714060dd21b54c29e7e3256ec0c65f132...f9388e8dd988e8a6727407b07c27e72b76b44de1),
[dependent landing](https://github.com/leanprover-community/mathlib4/pull/42534#issuecomment-6722737679)

Countercontrols reject a conclusion based only on old CI, a conclusion that
the change never landed based only on the GitHub flag, substituting the test
merge for the landed SHA, confirming an unread destination or preparing a
paste-ready mathlib comment. In the restricted replay, a pending disposition
is the expected outcome. The complete replay still needs to accept the
verified landing.

## Replay identity

Use the case and the three `SKILL.md` entrypoints for the full replay.
Use the restricted fixture with the scope and manage entrypoints for the
adverse replay. Keep the criteria with the assessor.

| Input | SHA-256 |
| --- | --- |
| Full case | `851938d35350fd13eb59bc69a152723ac20a2be1efd874b42e4d07ebd03a1623` |
| Restricted case | `dfba80528ff9cda90ec061a4868feaca29ab8784d244536a5d40cdbbee9feede` |
| Scope skill | `26c818ca712ebd68ab5f41a790653783de8cfe25282f1b3665b10ef31668e933` |
| Qualify skill | `ba2e7f9c882817dfa1aa042c3c3a1df4ea24d9915170c3649c408d1c1712995a` |
| Manage skill | `6dc9d10316f6f8f090164899e6e2fe40dfdfcd6705d1860dd5563d1e19607945` |

The revised replay reused public evidence. It involved no mathlib writes,
Lean execution or native discovery. The earlier matched comparison applies
to the earlier version.

The repository checks passed under Python 3.12, including all 53 unit tests,
validation of 24 skills, the 127-file generated plugin and the focused
Markdown link check.
