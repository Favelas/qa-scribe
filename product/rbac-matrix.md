# VaultGrid RBAC matrix

- Document type: Role × action permission matrix (intake source)
- Standard(s) cited: Used with ISO/IEC/IEEE 29119-4 decision table and role-matrix techniques; not itself a 29119-3 document
- Product: VaultGrid
- Cycle / version: Product-level (Cycle 59 freezes this matrix)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Use this grid as the oracle for ROLE-MATRIX and DT cases. Allow / Deny here is the expected result.
2. Paste into Confluence next to the test strategy; Product Owner signs that the freeze is current.
3. Do not add roles that are not in this file. If the user names a new role, stop and run `qa-scribe-intake`.
4. Delete this “How to use this file” block after paste.
5. Never substitute a real customer’s role names.

---

Legend: **A** = Allow. **D** = Deny. Expected HTTP for Deny on an existing **home-tenant** object is **403**. Expected HTTP for an object UUID that belongs to **another tenant** is **404** (REQ-RBAC-03), regardless of role.

| Action | Admin | Investigator | Reporter | Read-only |
| --- | --- | --- | --- | --- |
| Manage users and roles in home tenant | A | D | D | D |
| Set retention policy in home tenant | A | D | D | D |
| Upload evidence in home tenant | A | A | D | D |
| View evidence metadata (home tenant, assigned or tenant-wide per role) | A (tenant-wide) | A (assigned cases + tenant search) | A (assigned cases only) | A (assigned cases only) |
| Download original bytes | A | A (assigned cases) | D | D |
| Add investigator notes | A | A (assigned cases) | D | D |
| Generate case report (assigned) | A | D | A | D |
| Bulk export (tenant-wide package) | A | D | D | D |
| Export assigned-case report package | A | D | A | D |
| Read own tenant audit (filter by object) | A | D | D | D |
| Read own view-actions in audit | A | A | A | A |
| Update or delete audit events | D | D | D | D |
| Access other tenant’s objects | D | D | D | D |

## Token rules that the matrix assumes

- `role` and `tenant_id` come from the validated JWT, not from the request body (REQ-API-01, REQ-API-02).
- A revoked role must fail subsequent calls even if a previously issued token still names the old role (REQ-RBAC-08). Test design should treat this as a state-transition case (ST).

## Cross-tenant expected result (all roles)

| Input | Expected |
| --- | --- |
| Authenticated user, valid UUID of another tenant | 404, empty body, audit outcome = deny in **acting** tenant |
| Authenticated user, well-formed UUID that does not exist in any tenant | 404, empty body, audit outcome = deny |
| Unauthenticated | 401, no audit actor beyond anonymous/unauthenticated token id if the gateway logs it |
