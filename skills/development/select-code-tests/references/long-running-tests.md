# Long-running test decision and shard controls

Load only if a concrete suite is costly or partitioned execution is proposed. This reference **does not implement** a test sharder or authorize expensive, remote or concurrent execution.

## Decide whether to partition

1. Record a baseline at the exact revision and selected test-ID inventory. Measure wall time and relevant setup, CPU, memory, disk, outlier, flakiness or contention costs. Define what a cold or warm run means; repeated fresh processes do not imply cold system caches. Mark unavailable measurements as NOT_RUN instead of inventing a complete baseline.
2. Check lower-cost alternatives: use focused iteration with the project's required acceptance fallback, existing slow markers, stable fixtures, supported caches and safe cleanup of **completed disposable** test scratch.
3. Shard only independent tests when the measured benefit exceeds process startup, setup, scheduling and maintenance costs. Stateful, serial-only and order-dependent tests may need isolation or must remain serial.
4. Partition the exact intended test-ID set so each expected ID appears **once**, without omissions or duplicate execution claims. Every nonempty planned shard must actually collect the expected tests; reject silent filters, stale inventories and mismatched parameters.
5. Bind each shard to common source/test inventory, revision, environment and run identity. Retain original failures, timeouts, cancellations, retry counts and skipped outcomes. Aggregate deterministically and fail when any required shard is absent or unsuccessful.
6. Validate the orchestration on tiny adversarial cases: duplicate/missing ID, empty shard, crash, mixed run identity, timeout, flaky retry, shared-temp corruption and out-of-order results.

## Scope distinctions

* Test-ID coverage is not **mathematical input-domain coverage**. A theorem about a finite computation requires its own source reduction, complete domain partition and proof obligations.
* Deterministic experiment-data shards are not automatically a ready-to-run
  test-ID sharder; they partition different things.
* Large accumulated test scratch motivates measuring and cleaning completed
  disposable runs. Disk usage alone does not show that sharding improves runtime.
* A correctly justified **do not shard** decision is an acceptable result.
