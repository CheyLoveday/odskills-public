# Predicate, filter and coverage checks

Load for sieves, prime/valuation conditions, exact roots, normalization or a
bounded-to-general bridge.

- Distinguish `q divides N` from valuation exactly one. A divisibility filter
  cannot stand in for a claim about every prime exponent without justification.
- A powerful positive integer has every prime exponent at least two. Such an
  integer need not be a square or cube: exponents five and mixed two/three are
  important controls. A square-or-cube cofactor test needs explicit roughness,
  size and factorization reasoning for its *restricted* cofactor population.
- Derive a lift from the defining polynomial and its actual derivative. For a
  simple root modulo a prime, substitute the candidate back modulo the prime
  square; establish invertibility first. Multiple roots and exceptional primes
  need separate treatment. A convention or missing factor can invalidate an
  otherwise convincing survivor count.
- Isolate constant terms, coefficient bases, signs, endpoint conventions and
  old/new parameters. If paper and code agree but a comment is wrong, identify
  that scope; do not modify correct mathematics to match a faulty comment.
- A finite search needs an exact reduction and complete source-domain coverage
  to support the stated finite conclusion. Overlapping shards, missing classes,
  early stopping or unchanged counts are not themselves a coverage argument.
- For a symmetry reduction, define the action on the complete object and any
  joined witness. Check eligibility, the needed predicate invariance and coverage
  under that actual action. Row permutation and simultaneous row/column
  relabeling are different actions. Summed orbit weights do not establish union
  coverage; stabilizers and overlapping representatives can alter multiplicity.
- A finite check can establish a larger or infinite claim when an exact
  independently justified reduction covers that domain. For example, if every
  admissible point has a verified convex decomposition into checked cases and
  the objective preserves the required bound, verify those obligations and the
  complete generating set. A fixed denominator or matching sample count alone
  supplies no such bridge. Preserve a legitimate reduction when another
  certificate or checker is defective.
- A retained receipt needs original source/input/checker identities and actual
  completion. Preserve old outputs; use a new destination for a new run.
  A filename or label does not bind a source version.

## Periodic exclusions

For a claim about every index `n = r + L t` with positive step `L`, retain
a proved positive period `h` of the tested predicate, including any parity
or sign guard. The reachable residues are `r + L t mod h` for
`0 ≤ t < h / gcd(h,L)`. A rejected
representative excludes its whole progression only if every reachable
residue fails. A verified return of the full recurrence state supplies a
period. A shorter period for a projected predicate needs its own argument.
Test a mixed progression where the representative fails and another lift
passes.

If a witness also appears to eliminate a larger population, keep the
original target and check that consequence separately. Read the actual
prior survivor set with its reporting period. Prove every lift projects
into the tested residues, keeping the same source index across filters.
For example, projection by reducing only the stored representatives modulo
a new period is justified when that period divides the old one. Otherwise
cover the lifts on a common period. Count the union once. Drop a guard or
filter and record which residues return, and distinguish locally admitted
residues from actual integer solutions.

Before accepting an empty survivor set, check the period and complete input
roster against the declared population. A zero period or an empty roster for
a nonempty population leaves coverage unproved. An empty eligible population
requires its own proof. Exercise all three verifier controls:

| Submitted certificate | Required verdict |
| --- | --- |
| Zero reporting period with an empty final mask | Reject invalid period |
| Positive period with an empty input roster for a nonempty population | Reject incomplete coverage |
| Positive period with every eligible phase checked and zero survivors | Accept the scoped exclusion when the arithmetic also checks |

Give the proof from the finite result to the uniform statement, then give
the implication from each original source witness into that statement.
Record evidence for each step at its own scope.

## Enclosures and unresolved cases

For interval or validated-numeric evidence, first establish what is enclosed
and why. An exact rational endpoint is not proof that the enclosure contains
the intended value. Using a verified enclosure `lo <= f <= hi` alone,
`hi <= 0` certifies `f <= 0`, while `lo > 0` refutes it. A crossing interval
leaves that enclosure-based conclusion unresolved. Adapt endpoint
strictness to the actual predicate. Refine within the authorized budget or
retain UNKNOWN, and account for unresolved cases in coverage. A separate exact
evaluation can resolve the mathematical value without retroactively changing
what the submitted enclosure proved. Accept other valid enclosures.

Separate observed facts, mathematical derivations and suspected causes. When a
checker fails, retain both the defective and corrected evidence. A nearby toy
control can expose a mechanism without certifying the original large computation.
