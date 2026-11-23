# Select modular probes for periodic exclusions

Use when a current source population is described by periodic constraints
and another necessary condition might separate the remaining cases.

1. Freeze the shared coordinate, source hypotheses, reporting period and
   complete survivor set. Start with the original intended exclusion. Derive
   how an actual source projects to each candidate modular condition.
2. Evaluate a candidate probe on the reachable states of this population.
   For an index progression `n = r + L t` and a verified period `h`, there
   are `h / gcd(h, L)` lifts modulo `h`. Enumerate them within the chosen
   budget. A return of the full recurrence state certifies a period.
   Include parity or sign guards in the period argument.
3. Compare the reachable target values with the necessary image. Prefer
   probes that distinguish the actual surviving phases at a replayable cost.
   Record unresolved lifts. To combine filters, retain the same index and
   check all lifts on a common period. Independent local preimages can be
   used for exclusion as described in the
   [joint-source contracts](source-quotient-contracts.md).
4. Remove one condition at a time and recompute coverage. Retain the reduced
   certificate when the exclusion still holds. A returned phase establishes
   that the condition matters within this chosen certificate. Proving that
   fewer conditions are impossible requires a separate argument.
5. If the same probe appears to exclude a wider population, state the new
   target and prove its own domain reduction. A rejected representative can
   have a passing later lift. A surviving phase after dropping a guard gives
   a direct check on the proposed extension.

Cap exploratory selection and verification separately. At the cap, return
the proved exclusions and the exact unchecked or surviving cases.
