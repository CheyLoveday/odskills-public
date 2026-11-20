# Structural transformations and their limits

Use a mechanism only when its preconditions fit the actual output. These are
options, not a sequence or an exhaustive catalogue.

## Compute less information

For a count or scalar, look for a recurrence, sufficient summary, prefix sum or
closed expression rather than building every contributing object. For sorted
timestamps, a moving window can count pairs by adding the number of earlier
eligible indices; equal values still contribute distinct index pairs. The
monotone boundary argument must use the requested strict or inclusive endpoint.
Sorting costs time and storage and may need a copy to preserve the input. A
count-only structure cannot answer a later identity query without retaining or
reconstructing the missing information.

## Reparametrize or transpose the work

A unique parametrization can replace a sparse ambient scan. Moving a query loop
outside a reusable computation can remove repeated work. Establish the forward
cover and endpoint bounds; uniqueness or weights are additionally needed when
counting. Distinct local constraints may need the same witness: nonempty local
answers alone do not prove their conjunction has a witness. A projection that
suffices to prove exclusion may not reconstruct an actual solution.

## Reuse invariant work

Factor parameter-independent support/base terms from repeated evaluations;
consider neighboring-value recurrences or prefix queries. Compare preparation,
lookup, synchronization, memory and invalidation costs with the actual reuse
count. A cache must distinguish every result-affecting input/state and preserve
validation and returned ownership. Numerical recurrence stability is an extra
obligation; exact statistical definitions do not make floating arithmetic exact.

## Change representation

Sparse occupied objects can beat a dense table over a wide range; a genuinely
small bounded support can reverse that decision. Packed lanes or coefficient
encodings need bounds on every intermediate coefficient/carry and a valid
decoding argument. Native widths must accommodate intermediate sums/products,
not merely the largest input. Retain an exact fallback or explicit unsupported
status when the required bounds fail; do not silently narrow.

## Use approximation to propose, then verify

An approximate root or candidate can seed a search if exact correction or a
justified enclosure validates the result. A sign-change scan can miss tangent
roots, narrow components or disconnected sets. UNKNOWN is not rejection. State
which correction/coverage condition makes the procedure complete, or keep it
explicitly heuristic. Numerical conditioning, tolerances and statistical error
are distinct from the computational speed of a proposal.
