# Explicit effects and authority boundaries

Load when functions perform I/O, networking, subprocess execution, database writes, time/randomness, LLM calls, authentication, concurrency or external validation.

## Procedure

1. Identify which inputs the shell acquires and which effects it owns. When trust or acceptance criteria matter, distinguish supplied claims from independently selected authority.
2. Isolate each effect in a named narrow function or an actual shared shell. Inject values used by pure transformations; do not hide the current clock, random generator or environment in a helper.
3. For long-running or resource-sensitive operations, make relevant limits, timeouts and resource lifetimes explicit. Distinguish measured or enforced limits from estimates.
4. For security-sensitive file intake, protect selected members, reject unsafe path/link substitutions and check identities as the contract requires. A hash checks bytes, not who produced them or whether selection was complete.
   When the contract requires a complete dependency set, establish membership and external dependency availability from suitable authority or fail closed; a namespace or package pin alone does not prove a referenced member exists. If resolution is deliberately deferred, report completeness as unverified rather than inferring it from a successful snapshot.
5. For persistent mutations or publication workflows, address idempotence, atomicity, recovery and explicit failure states where needed. Do not convert an unknown remote effect into success or an assumed safe retry.
   Distinguish creating a new artifact from replacing an authorized existing one. Reserve new destinations with create-only operations; inspect aliasing before destructive writes. Where replacement is required, stage complete content rather than truncating the destination in place. An atomic rename of one file does not make several files a transaction or establish crash durability.
6. Exercise relevant success and failure paths with controlled effects. Mocks establish calling logic; claims about isolation, durability or authentication need separate observations when those properties are in scope.

## Minimal composition

```python
def prepare(inputs: list[str]) -> tuple[str, ...]:
    return tuple(sorted(set(inputs)))

def read_and_prepare(reader, scope: str) -> tuple[str, ...]:
    return prepare(reader(scope))
```

The core `prepare` is deterministic; the shell `read_and_prepare` performs the read. In real code keep an established public entry point and do not introduce a wrapper unless it exposes a useful boundary.
