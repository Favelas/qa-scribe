---
generator: qa-scribe-plan
skill_version: 1.0.0
---

# Document control

- Document type: Test Plan
- Standard(s) cited: IEEE 829-2008 Test Plan; ISO/IEC/IEEE 29119-3 Test Plan; ISTQB test plan / entry-exit / staffing
- Product: VaultGrid (**fake data**)
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Confluence; attach `docs/rtm.csv`.
2. Named approvers sign section 15 before execution.
3. Delete this “How to use this file” block after paste.
4. Keep all 15 IEEE sections.
5. A Senior QA Analyst and QA Manager must verify before this is a control of record.

# 1. Test plan identifier

**PLN-VAULTGRID-C59-001** — Cycle 59. Related strategy: **STR-VAULTGRID-001** (`docs/strategy.md`).

# 2. Introduction

This cycle freezes the UI role buttons and search isolation for two fake companies. It applies the strategy to **this cycle only**. References: `docs/product.md`, `docs/requirements.md`, `docs/roles.md`, `docs/risks.md`.

# 3. Test items

| Item | Version |
| --- | --- |
| VaultGrid web UI | vaultgrid-2026.59.x |
| US UAT stack | US-uat (synthetic) |

# 4. Features to be tested

REQ-AUTH-01–02, REQ-ISO-01, REQ-RBAC-01–05, REQ-VAL-01, REQ-AUD-01.

# 5. Features not to be tested

API contracts, hashing, mobile. Residual: Read-only may still **see** Export (RSK-RBAC-03) if hide-button slips — named in completion if still open. Export file name format (RSK-UX-01) is Low, not a stopper.

# 6. Approach

Apply STR-VAULTGRID-001. Order: isolation search (Crit) → role buttons (High) → login and empty title → activity log → Low cosmetic. Techniques: ROLE-MATRIX, NEG, EP, BVA. Oracles are **on screen**. One UAT window (US).

# 7. Item pass/fail criteria

A requirement passes when its Priority 1–2 cases pass, or fail only with a defect accepted in section 14. Isolation fails the item if any GLOBEX title appears for a NORTHWIND user.

# 8. Suspension and resumption criteria

**Suspend** if Severity 1 (other company visible, or Read-only upload succeeds). **Resume** on a new 2026.59.x build after retest of TC-ISO-001.

# 9. Test deliverables

This plan, `docs/cases.md` + `docs/cases.csv`, `docs/rtm.csv`, status and completion reports, DEF-STOP-01 and DEF-NS-01 examples.

# 10. Remaining test tasks

| Task | Owner | By |
| --- | --- | --- |
| Import CSV to Xray | Fabian Velasquez | 12 Sep 2026 |
| Two-company Test data | Tomas Novak | 12 Sep 2026 |
| Execute pack | Maya Chen | 15–24 Sep 2026 |
| US UAT | Jordan Hale | 22–23 Sep 2026 |
| Completion report | Fabian Velasquez | 2 Oct 2026 |

# 11. Environmental needs

Test: NORTHWIND and GLOBEX, four roles, Chromium. UAT: US-uat, synthetic files only. No real evidence.

# 12. Responsibilities / staffing and training

No new tool training.

| Name | Role | Owns | Hours | Dates |
| --- | --- | --- | --- | --- |
| Fabian Velasquez | Senior QA Analyst | Plan, reports, sign-off pack | 24 | 8 Sep–3 Oct 2026 |
| Maya Chen | QA Analyst | UI execution | 32 | 15–24 Sep 2026 |
| Priya Shah | Product Owner | Scope, residual | 8 | 8 Sep–3 Oct 2026 |
| Tomas Novak | Engineering Lead | Builds, Test data | 6 | 8 Sep–3 Oct 2026 |
| Jordan Hale | US UAT coordinator | US UAT script | 8 | 22–23 Sep 2026 |
| Nadia Okonkwo | QA Manager | Approval | 0 | — |

Total: **78 hours**.

# 13. Schedule

| Activity | Start | End |
| --- | --- | --- |
| Design freeze | 8 Sep 2026 | 12 Sep 2026 |
| System test | 15 Sep 2026 | 24 Sep 2026 |
| UAT United States | 22 Sep 2026 | 23 Sep 2026 |
| Exit review | 2 Oct 2026 | 2 Oct 2026 |
| **Cycle deadline** | | **3 Oct 2026 17:00 UTC** |

# 14. Risks and contingencies

| Cycle risk | Product RSK | Mitigation | Test refs |
| --- | --- | --- | --- |
| A sees B in search | RSK-ISO-01 | Run TC-ISO-001 first; Sev 1 suspends | TC-ISO-001 |
| Read-only upload | RSK-RBAC-01 | Button hidden; try URL only if button shown | TC-RBAC-001 |
| Export button still visible to Read-only | RSK-RBAC-03 | Record leftover if click is denied | TC-RBAC-005 |
| Staff absence | — | Fabian executes Crit only | TC-ISO-001 |

# 15. Approvals

| Role | Name | Hours | Signature |
| --- | --- | --- | --- |
| Senior QA Analyst | Fabian Velasquez | 24 | Draft — human sign-off required |
| QA Manager | Nadia Okonkwo | — | Draft — human sign-off required |
| Product Owner | Priya Shah | 8 | Draft — human sign-off required |
| Engineering Lead | Tomas Novak | 6 | Draft — human sign-off required |

## Annex A — RTM

`docs/rtm.csv`. Result is `planned` until execution.

## Annex B — Allocation

Section 12 is the allocation of record (78 hours).
