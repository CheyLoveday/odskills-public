# Joint-source and predictive-quotient contracts

For maps `α : S → A`, `β : S → B`, the true joint image `J = {(α s, β s) | s ∈ S}` lies in `α(S) × β(S)`. The reverse inclusion needs a **common-witness theorem**. Counterexample: `S = {false,true}`, `α(s)=s`, `β(s)=!s`; both marginals contain `true`, but `(true,true)` is not jointly realizable.

For exclusion, it is enough to show the required observations are absent
from an outer approximation of the joint image. Independent local preimages
enlarge the admissible set. An empty intersection of the necessary conditions
still excludes the original source if every condition uses the same index or
other shared coordinate. A surviving tuple establishes local compatibility.
Existence or counting in the original source requires a lifting argument.

For periodic tests, see [selecting modular probes](modular-probes.md).

For a compressed dynamical system `q : X → Y`, the equation `q (F x) = G (q x)` is forward simulation. If it holds on a restricted domain, prove initial membership and closure under `F`. Lifting asks whether a compressed state or trajectory has a compatible source preimage. Recovering the original source from `q x` requires uniqueness on the relevant domain, or additional information. To extract an observable `h`, it suffices to show `h = h' ∘ q` on that domain.

**Rule 110:** packed-cell arithmetic, restricted-image identities and arbitrary-step source equivalence are three different proof obligations.

**Erdős powerful integers:** adjacent Pell traces of one triple share the middle powerful term, squarefree kernel and recovery map. Independent primewise or pairwise admissibility does not prove global source realizability.

**Diophantine Z-in-Q:** paired determinant rows, Selmer trace functionals and normalizations require actual arithmetic classes, stage maps and integral bases. A unit ratio of coordinates is not an arithmetic construction. Source-coupling may prevent spurious independent choices; it does not establish the required witness.
