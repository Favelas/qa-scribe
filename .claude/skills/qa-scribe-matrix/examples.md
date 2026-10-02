# Matrix skill — examples

Pointer to the blank structure: `standards/risk-based-test-matrix-template.md`. No `docs/` golden until a human promotes one.

## Excerpt — allocation (acceptable)

RSK-ISO-01 is Critical / Yes — stopper. System + Security/authz + Functional = Extensive (NEG + EP). Case IDs: TC-ISO-001 if the pack exists, otherwise Planned. Residual if untested: do not ship.

## Excerpt — fail (this is a cycle RTM leaking into the matrix)

REQ-ISO-01 → TC-ISO-001, owner Maya Chen, Cycle 59 result planned. **Reject.** REQ → TC with named owners and cycle results belong in the plan RTM.

## Excerpt — fail (invented cases)

RSK-RBAC-01 → TC-RBAC-099, TC-RBAC-100 created “so the cell is not empty”. **Reject.** Write Planned until a case pack exists.

## Excerpt — fail (numeric scores)

Likelihood 4 × Impact 5 = 20. **Reject.** Copy Level from the register; do not invent L×I numbers.

## Excerpt — depth (acceptable)

High stopper-if-upload-succeeds (RSK-RBAC-01): Standard on System + Security/authz, ROLE-MATRIX + NEG. Low export file name: Cursory, last in the table.
