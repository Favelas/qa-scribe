---
generator: qa-scribe-plan
skill_version: 1.0.0
---

# Document control

- Document type: Test Plan
- Standard(s) cited: IEEE 829-2008 Test Plan; ISO/IEC/IEEE 29119-3 Test Plan; ISTQB test plan / entry-exit / staffing
- Product: VaultGrid
- Cycle / version: Cycle 59 (build vaultgrid-2026.59.x)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Confluence under VaultGrid → Cycle 59; attach `examples/rtm/cycle-59-rtm.csv`.
2. Named approvers in section 15 sign before execution starts.
3. Delete this “How to use this file” block after paste; keep Document control and all 15 IEEE sections.
4. Import remaining tasks into Jira; do not change hours without a plan amendment.
5. A Senior QA Analyst and QA Manager must verify this plan before it is used as a control of record.

# 1. Test plan identifier

**PLN-VAULTGRID-C59-001** — VaultGrid Cycle 59 Test Plan.

Related strategy: **STR-VAULTGRID-001** (`examples/strategy/vaultgrid-strategy.md`). This plan applies that approach to Cycle 59 only. It does not replace the strategy.

# 2. Introduction

Cycle 59 delivers RBAC matrix freeze, API cross-tenant 404 behaviour, truncated/hash-mismatch ingest rejection, audit of denied access, and assigned-case export. UAT runs in US, UK, Brazil, and Australia.

References: `product/vaultgrid.md`, `product/requirements.md`, `product/rbac-matrix.md`, `product/risks.md`, intake `inputs/examples/plan.cycle-59.yaml`.

Glossary: Tenant = isolation boundary. Home region = storage locality. JWT claims `tenant_id` and `role` are the authorisation source.

# 3. Test items

| Item | Version / identity | Notes |
| --- | --- | --- |
| VaultGrid API | vaultgrid-2026.59.0 and subsequent 2026.59.x patches | Primary item |
| VaultGrid web UI | Same train | Role actions as exposed in UI |
| Authz decision service | Bundled in 2026.59.0 | Token vs matrix |
| Ingest/hash service | Bundled in 2026.59.0 | SHA-256, size, truncate |
| Audit pipeline | Bundled in 2026.59.0 | Append-only |
| Regional UAT stacks | US-uat, UK-uat, BR-uat, AU-uat | Home-region tenants |

Items not in this cycle: billing adapters, mobile clients. Not applicable: hardware appliances — VaultGrid is software-only in this fiction.

# 4. Features to be tested

| Feature | REQ IDs | Risk IDs |
| --- | --- | --- |
| Tenant isolation including UUID 404 | REQ-RBAC-01, REQ-RBAC-03, REQ-API-01 | RSK-ISO-01, RSK-ISO-02, RSK-API-01 |
| Role × action matrix | REQ-RBAC-02, REQ-RBAC-05–07 | RSK-RBAC-01 |
| Role assignment and revoke | REQ-RBAC-04, REQ-RBAC-08 | RSK-RBAC-01, RSK-RBAC-02 |
| Ingest hash and truncate | REQ-INT-01–03, REQ-INT-05 | RSK-INT-01 |
| Chain of custody events | REQ-INT-04 | RSK-INT-02 |
| Audit allow/deny and immutability | REQ-AUD-01–04 | RSK-AUD-01, RSK-AUD-02 |
| Export scoping and hashes in package | REQ-EXP-01–04 | RSK-EXP-01, RSK-EXP-02 |
| API 401 | REQ-API-03 | (authn; supports isolation tests) |
| Regional UAT / residency | REQ-UAT-01, REQ-UAT-02 | RSK-UAT-01 |

# 5. Features not to be tested

| Feature | Reason | Residual risk |
| --- | --- | --- |
| Performance of files > 5 GB | No NFR in catalogue; ingest of huge objects not scheduled | Not applicable: no RSK-PERF in register. Known product gap: hash-on-download for very large files is not claimed this cycle. |
| Notes-ACL separate from case assignment | Engineering deferred notes ACL to Cycle 60 | **RSK-EXP-01** remains High — see section 14 |
| Accessibility audit | No requirement | Not applicable: no a11y REQ |
| IdP internals | Out of strategy scope | Not applicable |

# 6. Approach

Apply STR-VAULTGRID-001. Cycle 59 system test order: isolation and IDOR (Crit) → ingest integrity (Crit) → stale role (High) → audit deny (High) → export scope (High, with known residual) → remaining matrix cells → UAT.

Techniques: ROLE-MATRIX, NEG, EP, BVA, DT, ST, INTEGRITY as in the case packs under `examples/cases/`. API and UI share oracles; API is mandatory for 404/403 distinctions.

UAT: business coordinators execute regional scripts after system test of Crit isolation/integrity is green on 2026.59.x. QA provides data and stands by.

Independence: Maya Chen and Luis Ortega do not test code they authored (they are QA). Tomas Novak does not execute bypass cases used for exit.

# 7. Item pass/fail criteria

- **API/UI build:** Pass for a requirement when all linked Priority 1–2 cases for that REQ are executed and passed, or failed only with a defect accepted under section 14.
- **Isolation item:** Fail the item if any cross-tenant case returns 200/403-with-body or leaks metadata.
- **Integrity item:** Fail the item if a truncated or mismatched upload creates an evidence object.
- **Cycle:** Pass/fail of the cycle is **not** decided here; it is the completion report. This section decides **items**.

# 8. Suspension and resumption criteria

**Suspend** system test of the affected item when:

- A Severity 1 defect is opened (isolation break, accepted bad ingest, audit off).
- Test environment cannot host two tenants or audit query fails for more than four hours during an execution day.
- A UAT region is unavailable for its entire booked window and no fallback window exists inside the deadline.

**Resume** when a new 2026.59.x build is deployed, the defect is verified fixed or downgraded with Product Owner written acceptance, and Maya Chen or Luis Ortega records environment health (login, two-tenant ping, audit write) in the execution log.

# 9. Test deliverables

| Deliverable | Location / ID |
| --- | --- |
| This plan | PLN-VAULTGRID-C59-001 |
| Case packs | TC-RBAC, TC-INT, TC-AUD (Markdown + CSV) |
| RTM | `examples/rtm/cycle-59-rtm.csv` |
| Prompt pack | PRM-RBAC-001 |
| Status reports | RPT-STS-VAULTGRID-C59-* |
| Completion report | RPT-SUM-VAULTGRID-C59-001 |
| Defects | DEF-C59-* in Jira (fictional IDs in examples) |
| Execution logs | Xray test runs (project VG) |
| Signed UAT | Regional coordinator emails filed in Confluence |

# 10. Remaining test tasks

| Task | Owner | By |
| --- | --- | --- |
| Freeze case packs and import CSV to Xray | Fabian Velasquez | 12 Sep 2026 |
| Provision NORTHWIND / GLOBEX tenants on Test | Tomas Novak | 12 Sep 2026 |
| Synthetic files and hash fixtures | Luis Ortega | 12 Sep 2026 |
| Execute isolation + integrity | Maya Chen, Luis Ortega | 15–26 Sep 2026 |
| Execute audit + export | Luis Ortega | 18–26 Sep 2026 |
| Daily status (RPT-STS) | Fabian Velasquez | Each execution day |
| UAT facilitation | Fabian Velasquez | Regional windows |
| Completion report | Fabian Velasquez | 2 Oct 2026 |

# 11. Environmental needs

- Test class: `test.vaultgrid.example` (fictional) with tenants NORTHWIND and GLOBEX, all four roles, Admin audit access.
- UAT: US-uat, UK-uat, BR-uat, AU-uat; one tenant per region; data residency assertion available to Admin.
- Tools: Jira/Xray project VG, Confluence, browser of record Chromium current stable, HTTP client for API cases.
- Accounts: named testers use personal synthetic users; no shared “admin/admin”.
- Data: synthetic only; no real evidence.

# 12. Responsibilities / staffing and training

No new tool training this cycle. Regional coordinators receive a 60-minute UAT script walkthrough on 21 Sep 2026 (Fabian Velasquez).

| Name | Role | Owns | Hours | Dates |
| --- | --- | --- | --- | --- |
| Fabian Velasquez | Senior QA Analyst | Plan, design quality, status/completion, UAT facilitation, sign-off package | 32 | 8 Sep–3 Oct 2026 |
| Maya Chen | QA Analyst | RBAC + isolation execution and first-line defects | 40 | 15–26 Sep 2026 |
| Luis Ortega | QA Analyst | Integrity, audit, API, export execution | 40 | 15–26 Sep 2026 |
| Priya Shah | Product Owner | Scope, residual risk acceptance, UAT intake | 12 | 8 Sep–3 Oct 2026 |
| Tomas Novak | Engineering Lead | Builds, environment, defect triage | 8 | 8 Sep–3 Oct 2026 |
| Amina Diallo | Security Champion | Authz/integrity severity consult | 8 | 15–26 Sep 2026 |
| Jordan Hale | US UAT coordinator | US UAT scripts | 16 | 22–24 Sep 2026 |
| Elena Rossi | UK UAT coordinator | UK UAT scripts | 16 | 23–25 Sep 2026 |
| Rafael Costa | Brazil UAT coordinator | BR UAT scripts | 16 | 24–26 Sep 2026 |
| Sophie Nguyen | Australia UAT coordinator | AU UAT scripts | 16 | 28–30 Sep 2026 |

Total allocated: **204 hours**.

# 13. Schedule

| Activity | Start | End |
| --- | --- | --- |
| Design freeze and Xray import | 8 Sep 2026 | 12 Sep 2026 |
| System test execution | 15 Sep 2026 | 26 Sep 2026 |
| UAT United States | 22 Sep 2026 | 24 Sep 2026 |
| UAT United Kingdom | 23 Sep 2026 | 25 Sep 2026 |
| UAT Brazil | 24 Sep 2026 | 26 Sep 2026 |
| UAT Australia | 28 Sep 2026 | 30 Sep 2026 |
| Exit review / completion report | 2 Oct 2026 | 2 Oct 2026 |
| **Cycle deadline (go / go-with-risks / no-go)** | | **3 Oct 2026 17:00 UTC** |

# 14. Risks and contingencies

| Cycle risk | Product RSK | Mitigation | Trigger | Test refs |
| --- | --- | --- | --- | --- |
| Cross-tenant leak in 59.0 | RSK-ISO-01 | Execute TC-RBAC-001–004 before any UAT; Severity 1 suspends | Any 200/body on foreign UUID | TC-RBAC-003, TC-RBAC-004 |
| Existence oracle 403 vs 404 | RSK-ISO-02 | Compare foreign UUID vs random UUID | Distinct bodies or codes | TC-RBAC-005 |
| Tampered ingest accepted | RSK-INT-01 | Hash-mismatch and truncate cases day 1 of execution | Object created on reject path | TC-INT-002, TC-INT-003 |
| Stale Investigator token | RSK-RBAC-02 | ST case after revoke | Download still 200 | TC-RBAC-008 |
| Deny not audited | RSK-AUD-01 | Pair every 403/404 with audit assertion | Missing deny event | TC-AUD-002 |
| Reporter over-export (notes ACL deferred) | RSK-EXP-01 | Test assignment scope; **accept residual High** if notes still appear; compensating control: Admin reviews export templates | Notes from unassigned logic | TC-EXP-002 (see cases/export.csv) |
| Region residency miss | RSK-UAT-01 | Admin region assertion in each UAT window | Storage region ≠ home | UAT scripts per region |
| Staff absence | — | Cross-train Maya/Luis on each other’s Crit packs | >1 day unplanned absence | Contingency: Fabian executes Crit only |

# 15. Approvals

| Role | Name | Hours (if testing) | Signature | Date |
| --- | --- | --- | --- | --- |
| Senior QA Analyst (author) | Fabian Velasquez | 32 | Draft — human sign-off required | |
| QA Manager | Nadia Okonkwo | — | Draft — human sign-off required | |
| Product Owner | Priya Shah | 12 | Draft — human sign-off required | |
| Engineering Lead | Tomas Novak | 8 | Draft — human sign-off required | |

**Human gate:** This plan is not in force until the QA Manager signs. The generator does not approve.

## Annex A — Requirements traceability matrix

Canonical CSV: [`examples/rtm/cycle-59-rtm.csv`](../rtm/cycle-59-rtm.csv). Summary: every Cycle 59 REQ maps to at least one `TC-` ID. Result column is `planned` until execution.

## Annex B — Named allocation

See section 12 table (204 hours). That table is the allocation of record.
