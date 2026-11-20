# Proof-form reduction choices

Keep separate: **(1)** the source theorem and meaning, **(2)** the constructed proof term, **(3)** the checker/export representation and cost. A theorem may elaborate against an opaque imported definition but be expensive under flat private-export checking.

When `f = g` is known for structured maps, rewrite at the map level before comparing `f x` and `g x` under projections. This may avoid large weak-head-normalization searches; measure against the actual checker before claiming improvement.

For composed linear maps, look for a proved equality at the map boundary. Use it before a coercion exposes the underlying implementation if the checker is unfolding that representation.

Rule 110 proofs show why exact compressed step arithmetic, initializer transport, arbitrary-step induction and final specification agreement are different lemmas. Erdős powerful number work adds the nonnegotiable **shared source triple** and a separate unrestricted-index coverage obligation.
