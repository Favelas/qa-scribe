# Strategy skill — examples

Pointer to the golden strategy: `examples/strategy/vaultgrid-strategy.md`.

## Excerpt — risk-based approach (acceptable)

VaultGrid product risk drives depth. RSK-ISO-01 (cross-tenant disclosure) and RSK-INT-01 (tampered ingest) are Critical: every cycle that touches authz or upload must include permission-bypass and hash-mismatch cases. Low risks such as leftover synthetic files (RSK-DAT-01) are sampled at teardown, not designed as a large functional pack.

## Excerpt — fail (this is a plan leaking into a strategy)

Cycle 59 ends 3 October 2026. Maya Chen has 40 hours on RBAC. **Reject.** Move dates and hours to the test plan.

## Excerpt — approach-level exit (acceptable)

Exit the approach for a release train only when: Critical isolation and integrity risks in scope have executed cases with no open Severity 1 defects, and any remaining High has a named owner. This is not a weekday clock-time.

## Ready-to-paste

`ready-to-paste/vaultgrid-strategy.md` is the Confluence-cleaned golden.
