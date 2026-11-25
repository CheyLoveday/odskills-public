# Test relaxed proof-system completeness

Freeze the source statement, the weaker retained assumptions and the proposed
intermediate implication. Identify what the relaxation discarded. Look for
an exact object that satisfies every retained assumption and violates the
conclusion. Check admissibility and the failure explicitly. The control
can show which additional source constraint the argument must use.

A countermodel to the relaxed implication refutes sufficiency of the retained
assumptions. It refutes the original theorem only when a valid source lift
exists and the target violation transfers. If no model is found, report the
actual domain and coverage of the search. A finite certificate needs a
separate reduction from the full population before it proves the universal
claim.
