# Testing a functional core and its shell

Load when selecting tests or demonstrating that an FCIS change preserves behaviour.

## Core

Use hand-authored expected values, finite invariant/property controls and edge cases. Vary type, missingness, ordering, duplicate membership, and boundary values. Avoid deriving the expected answer by calling the same implementation under test.

## Shell

Exercise at least one public entry point; inject relevant file/network/process failures where safe. For file intake or publication workflows, test exact selection, authority binding, no-clobber behaviour and cleanup when they are part of the contract. Report incomplete outcomes accurately. Mocks and fake transports establish controlled calling behaviour; hosted properties need actual observations if claimed. For scientific or proof-assurance work, keep those observations separate from scientific or mathematical correctness.

Check that parsing and encoding support the domain's numeric contract, including
growth of intermediate and output values. Valid inputs can produce a result
outside a serializer's default range or decimal-digit limit even when the pure
calculation is exact. Exercise that public path; either preserve the promised
range or state an explicit supported bound. Do not infer wire compatibility
from a large-integer unit test or silently change process-wide numeric settings.

Where the core receives or returns a lazy iterator, check the actual public path for effects performed during iteration, not only with in-memory inputs. An iterator may read files or other external state when consumed; assess the intended boundary rather than banning lazy iteration itself.

When explicit cleanup or cancellation is required, keep the object that performs
cleanup reachable until after the assertion. For a generator owning a file,
retaining only the file handle does not prevent generator finalization from
closing it: retain the generator itself while checking the file's closure.
Garbage collection or process exit can otherwise mask a missing `close` in the
public workflow. Check early stop and failure as well as exhaustion, and confirm
that a deliberately omitted cleanup is detected. This does not make the core
responsible for closing an iterator it only borrows.

## Discovery versus behaviour

A `tests/discovery` prompt fixture documents desired activation or non-activation; a static test can validate its shape but **cannot** establish model-selected skill triggering. Test real selection separately in Codex/ChatGPT and record the model/session, installed version and result. Behaviour tests should also assess the quality and scope of the actual produced artifact.

## Evidence

Report the commands run, expected and observed outcomes, and material untested behaviour. Preserve failing reproductions for regression. For reproducibility or assurance work, also record source/tool versions and distinguish unit, local I/O, hosted effects and expert acceptance as relevant to the task.
