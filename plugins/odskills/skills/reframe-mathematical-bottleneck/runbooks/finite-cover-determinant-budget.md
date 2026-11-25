# Finite-cover determinant budget

Use when the proposed representation is a finite cover and the proof
relies on a determinant or a rank split.

| Obligation | Evidence to record |
| --- | --- |
| Source and cover | Source-to-base map, domain, number of sheets or rank bound, multiplicity convention, and separate treatment of ramification and exceptions |
| Analytic estimate | Exactly which functions, norms, domains and derivative or interpolation bounds are available uniformly. State any extra regularity needed by the determinant argument |
| Integral clearing | Matrix orientation, entries and ring. Give the clearing factors and their effect on both size and divisibility. Check that the cleared determinant or minors are integral |
| Modular estimate | A proved divisor or valuation bound for the same cleared integer. Combine divisors with their shared factors accounted for |
| Real estimate | An upper bound for the same cleared quantity with uniform constants and regime restrictions |
| Rank-deficient branch | The exact vanishing threshold, recovered relation, and any primitive, saturation or lattice-index step needed to use it |
| Full-rank branch | The arithmetic or counting consequence with its proof. Record an open obligation if the only consequence is nonvanishing |

For an integer determinant $D$ divisible by a proved positive integer $M$,
a strict upper bound $|D|<M$ forces $D=0$. If the bound reaches $M$, retain
the equality case and all other admissible full-rank cases. For a
rectangular matrix specify which minors must vanish for the rank threshold.
When lifting rows or columns, verify independence and the cost of passing to
primitive minors before declaring a stronger height bound.

Finish by substituting the consequences for both branches and the exceptional
population into the original inequality. If any part remains open, state the
conditional net bound and name the branch and estimate that prevent closure.
