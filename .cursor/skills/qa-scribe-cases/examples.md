# Cases skill — examples

Goldens:

- `examples/cases/rbac-tenant-isolation.md`
- `examples/cases/hash-chain-of-custody.md`
- `examples/cases/audit-log.md`
- `examples/cases/export.csv`

## Excerpt — acceptable cross-tenant objective

Confirm that an Investigator in tenant NORTHWIND, presenting a valid evidence UUID that belongs to tenant GLOBEX, receives HTTP 404 with no metadata, and that an audit event with outcome deny is written for NORTHWIND.

## Excerpt — fail

“Verify RBAC works for all roles.” Multiple behaviours, no ID, no expected HTTP. **Reject.**

## Ready-to-paste

`ready-to-paste/rbac-tenant-isolation.md`
