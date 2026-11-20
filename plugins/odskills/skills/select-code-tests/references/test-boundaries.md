# Test boundaries and independently checkable evidence

Load when choosing the *kind* of verification or deciding whether existing tests cover a claimed interface. This is advisory; the consumer's acceptance and permission rules govern actual execution.

| Change / claim | Minimum discriminating evidence | Escalate when |
|---|---|---|
| Pure function, statistical computation or mathematical kernel | Independent examples/nonexamples, boundary/invalid cases, invariants or independently implemented oracle | Other modules or effects may alter the public outcome |
| Parser, serializer, CLI, filesystem or database boundary | Real parser/subprocess behaviour, exact bytes, stable error/exit classes, partial failure and recovery controls | The supported contract includes installed or end-to-end use |
| Public user workflow / installed library | Known-answer user entry point, supported environment, distribution artifact installed outside the checkout as applicable | Supported platforms, versions or downstream consumers differ |
| Change touching shared contracts or uncertain dependencies | Maintained impact selection plus appropriate full fallback | Map is stale, selected collection empty, core wiring changed or project rules require it |

* Unit/integration/E2E describe **the boundary observed**, not automatically a higher truth status. Do not substitute a mock-only test for a claim about real subprocesses, packaging, networking or storage.
* Source-tree tests can pass while a wheel/sdist omits data or breaks imports. The installed artifact needs its own public smoke check when package distribution is in scope.
* A test's expected value should not be produced solely by the implementation being checked. Use known answers, distinct algorithms, known mutations or matched adverse inputs as appropriate. For a claimed repair, check that the regression rejects the defective behavior and reaches the production path. Patching the function under test can test only the replacement; a saved dispatch alias, import or installed copy may still execute old behavior. A small unpatched public-path check in a fresh process can distinguish this without expanding a source-only task into a release campaign. Legitimate mocks of external effects remain useful.
* Preserve the source, environment, commit and test selection. Empty-selected modules, unaccounted `-k`/`-m` filters, skipped required lanes or stale receipts cannot establish the claimed acceptance. A documented filtered lane or permitted skip can satisfy its specified scope; it does not establish excluded coverage.
* For numerical results, passing code tests does not prove the underlying mathematical theorem or an estimator's sampling-model assumptions.

## Grounded examples (source revisions)

- Payload/CLI behavior differs from event idempotence, lock ownership and crash
  recovery. Keep synthetic mutable state in disposable scratch.
- Change-to-test selection needs explicit full-suite fallback and nonzero
  collection; filenames alone cannot establish coverage.
- Installed-artifact testing checks the interface users invoke outside the
  source tree; a specific project's platform matrix is not a universal rule.
