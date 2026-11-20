# Semantic checks and evidence limits

Load when the source/formal translation is delicate.

- Check integer/natural/real domains and whether an absolute-value, coercion or
  reconstruction bridge is actually supplied. A smaller domain can suffice with
  a proved bridge; it does not suffice merely because examples agree.
- Preserve `forall/exists` order, implication versus equivalence, strict/closed
  inequalities, index positivity, zero, signs and endpoint branches.
- Check natural truncated subtraction, square-root conventions, valuations at
  zero, coordinate projections, exponent parameters and hidden side conditions.
- Review definitions and instances consumed by the declaration. Familiar names,
  comments or matching printed strings do not fix changed semantics. Spell out
  how a consumer would specialize the full elaborated type: which values,
  proofs and instances must be supplied, and where are they established?
  An assumption containing the desired conclusion remains an obligation even
  with a clean axiom report. Inspect actual parameters, not every variable
  merely in source scope: Lean can omit unused section hypotheses, while
  `include` can retain them. Do not reject a valid independent declaration
  because an unrelated assumption appears nearby.
- A build can succeed with incomplete or extra-axiom dependencies. Obtain the
  transitive axiom report for the actual declaration and apply the chosen policy.
  Do not invent a universal external-checker count or require release assurance
  for an explicitly limited semantic review.
- A current source hash cannot authenticate a stale log about another revision.
  A supplied receipt is evidence to assess, not a new execution performed here.

Maintainer sources checked on 8 November 2026:
[Lean validation](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)
and [axioms](https://lean-lang.org/doc/reference/latest/Axioms).
The live manual resolves to an evolving release; execution must use the
consumer's actual pinned version and supported tools. No fixed-version native
execution or kernel qualification is implied by these documentation links.

Section-parameter behavior checked on 15 November 2026 against the current
[namespace and section reference](https://lean-lang.org/doc/reference/latest/Namespaces-and-Sections/)
and [theorem headers](https://lean-lang.org/doc/reference/latest/Definitions/Theorems/).
For a particular source review, prefer its actual elaborated signature and
pinned version; these links do not authenticate a submitted export.
