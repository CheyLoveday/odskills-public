# Mathematical reframing testing

## Observed run on 26 November 2026

The map-first runbook was applied in a fresh Codex session on the alpha.5
GitHub pin `50f9bbb74eb2740749bc49cf3a5cd00575008077`. The case required
a graph-incidence bound uniformly below exponent `1/2` for integers
`N ≥ 2`. The session joined the left estimates over the left-vertex
projection while counting original edge IDs. It rejected a match to the
right branch based only on shared sample labels.
The full exponent `19/40`, with slack `1/40`, stayed conditional on a
uniform bound for the full right fibre. A separate routine algebra prompt
was answered directly without reading the runbook.
[Runbook trial and release replay](https://github.com/CheyLoveday/odskills-public/pull/6)

## Replay

Ask a fresh session to apply the
[map-first closure runbook](runbooks/map-quantitative-theorem-closure.md)
to this synthetic case. Give the prompt alone and retain the checks below
for assessment.

> All original directed edges, each with its own ID, lie in branch L or R.
> Seek a uniform count with exponent strictly below 1/2 for integers N ≥ 2.
> L contains at most N^(1/4) left vertices, each incident to at most N^(1/5)
> original L edges. R has at most N^(3/10) labels. A bound of N^(1/10) per
> label applies to samples only. In label 7 the actual edge and the sample
> have different IDs, and there is no map covering the actual fibre. A
> draft bound of N^(7/40) covers each full R fibre. An alternative draft
> attains the same bound on R with an extra unproved sparsity premise.
> Return the justified and rejected joins, exact slack, conditional total
> and remaining obligation.

Check that L has exponent `9/20`, the sample match fails, and the full
bound stays conditional on a uniform proof for R. Either valid R route
would pay that obligation on its proved scope.

## Scope

This is evidence for the map-first case and the nearby routine-algebra
control. For the original chart-budget case and its comparison, see the
[initial reframing evaluation](https://github.com/CheyLoveday/odskills-public/pull/5).
