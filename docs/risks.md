# Product risks (short)

- Document type: Product risk register
- Standard(s) cited: ISTQB risk-based testing
- Product: VaultGrid (**fake data**)
- Cycle / version: Product-level; Cycle 59 uses this set
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Case **priority** follows this table, not personal preference.
2. **Stopper** = do not ship while open. **Not a stopper** = can ship with a named leftover.
3. Delete this block after paste.
4. Fake IDs only.
5. QA Manager and Product Owner accept residual risk at exit.

| ID | Risk (plain English) | Level | Stopper? | Test depth |
| --- | --- | --- | --- | --- |
| RSK-ISO-01 | Company A sees Company B’s case title in search or list | **Critical** | **Yes — stopper** | Must run every cycle that touches search |
| RSK-RBAC-01 | Read-only can Upload (button shown and upload works) | **High** | Yes if upload succeeds | Button + try upload |
| RSK-RBAC-02 | Investigator can open Manage users | **High** | Yes if they can change roles | Menu hidden |
| RSK-VAL-01 | Empty title still creates a case | **Medium** | No | BVA on title |
| RSK-RBAC-03 | Read-only still **sees** Export (click may fail) | **High** | No if no file is produced — leftover for go-with-risks | Button hidden |
| RSK-AUD-01 | Denied try is missing from Activity log | **Medium** | No | After a deny, open log |
| RSK-UX-01 | Export file name has no date (`export.zip` only) | **Low** | **No — not a stopper** | One export check |

Ranking: Critical/High before Medium/Low. A report that looks “all green” while RSK-ISO-01 is open is a fail of the report, not a pass of the product.
