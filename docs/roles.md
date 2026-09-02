# Who sees which buttons (UI)

- Document type: Role × screen matrix
- Standard(s) cited: Used with ISTQB / 29119-4 ROLE-MATRIX and decision table; not a 29119-3 document
- Product: VaultGrid (**fake data**)
- Cycle / version: Cycle 59 freeze
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. This table is the oracle for ROLE-MATRIX cases. **Show** = button or menu is visible. **Hide** = not on screen.
2. Isolation is not a button: it is “Search must not list the other company.” See REQ-ISO-01.
3. Delete this block after paste.
4. Fake roles only.
5. Human signs before a real matrix is used.

| Screen / control | Admin | Investigator | Reporter | Read-only |
| --- | --- | --- | --- | --- |
| Case list (own company) | Show | Show | Show (assigned) | Show (assigned) |
| Search | Show | Show | Show | Show |
| Upload | Show | Show | Hide | Hide |
| Manage users | Show | Hide | Hide | Hide |
| Export | Show | Hide | Show (assigned) | Hide |
| Activity log | Show | Hide | Hide | Hide |

**Isolation:** any role in NORTHWIND: Search for a GLOBEX case title → **zero rows**. Fail if a GLOBEX title appears.
