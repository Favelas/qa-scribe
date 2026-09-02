# VaultGrid product risks

- Document type: Product risk register (intake source)
- Standard(s) cited: ISTQB risk-based testing; used to drive coverage depth in ISO/IEC/IEEE 29119-3 strategy and plan
- Product: VaultGrid
- Cycle / version: Product-level register; Cycle 59 plan selects a subset
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Every test case traces to at least one `RSK-` ID. Case **priority** follows this register, not personal preference.
2. Paste into the cycle risk review; QA Manager and Product Owner sign residual risk at exit.
3. Do not invent `RSK-` IDs. If a new failure mode appears, run `qa-scribe-intake` and add it here first.
4. Delete this “How to use this file” block after paste.
5. Never store real incident identifiers or real customer names in this register.

---

Likelihood and impact are qualitative (ISTQB product-risk ranking). **Test depth** is the strategy rule: Critical and High are designed and executed before Medium and Low happy paths.

| ID | Risk | Area | Likelihood | Impact | Level | Test depth |
| --- | --- | --- | --- | --- | --- | --- |
| RSK-ISO-01 | Evidence or metadata from tenant T′ is returned to a user in tenant T | Isolation | Medium | Catastrophic | **Critical** | Permission-bypass, IDOR, negative API; mandatory for every cycle that touches authz |
| RSK-ISO-02 | Distinct 403 vs 404 responses reveal that a UUID exists in another tenant | Isolation | Medium | High | **High** | Cross-tenant UUID vs unknown UUID comparison |
| RSK-RBAC-01 | User elevates own role to Admin or assigns a privileged role without Admin rights | RBAC | Low | Catastrophic | **High** | Negative role-assignment; DT on Admin-only actions |
| RSK-RBAC-02 | Revoked Investigator still downloads originals with a stale token | RBAC / session | Medium | High | **High** | State transition: role granted → revoked → download |
| RSK-INT-01 | Truncated or tampered file is stored as authentic evidence | Integrity | Medium | Catastrophic | **Critical** | BVA on size; NEG hash mismatch; truncated body |
| RSK-INT-02 | Stored SHA-256 does not match bytes later downloaded | Integrity | Low | Catastrophic | **High** | Integrity round-trip; custody event vs blob |
| RSK-AUD-01 | Denied access is not logged, leaving no forensic trail | Audit | Medium | High | **High** | NEG + audit assertion on 403/404 |
| RSK-AUD-02 | Tenant role can alter or delete audit events | Audit | Low | High | **Medium** | NEG on update/delete audit API |
| RSK-API-01 | IDOR: evidence UUID from another tenant is readable when sent in path or body | API | Medium | Catastrophic | **High** | ROLE-MATRIX × tenant; same as isolation API tests |
| RSK-EXP-01 | Reporter export includes investigator notes or unassigned-case objects (over-export) | Export | Medium | High | **High** | Assigned vs unassigned; notes present/absent |
| RSK-EXP-02 | Export package omits hashes, breaking receiving-agency verification | Export | Low | Medium | **Medium** | Export package schema; hash field present |
| RSK-UAT-01 | UAT in a region stores or displays evidence outside the tenant home region | UAT / residency | Low | High | **Medium** | Per-region UAT checks; storage region assertion |
| RSK-DAT-01 | Synthetic UAT files remain in a region after the cycle and pollute the next run | Test data | Medium | Low | **Low** | Data teardown; out of functional depth unless exit criteria require clean UAT |
| RSK-SES-01 | After a region switch in the client, the session still authorises the previous tenant | Session | Low | High | **Medium** | ST on region/tenant switch |

## Ranking rule used by generators

1. Design and schedule **Critical** then **High** first.
2. Medium and Low may be sampled or deferred if hours in the **plan** intake are insufficient — that deferral is recorded as residual risk, not silently dropped.
3. A report that shows “all cases passed” while any Critical or High item is untested or still open is a **fail** of the report skill, not a pass of the product.
