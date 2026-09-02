# Document control

- Document type: Test Strategy
- Standard(s) cited: ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing)
- Product: VaultGrid
- Cycle / version: Product-level (not cycle-bound)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Confluence under VaultGrid → QA as the living product strategy (replace any previous STR-VAULTGRID draft).
2. QA Manager signs section 16; Product Owner acknowledges in-scope / out-of-scope.
3. Delete this “How to use this file” block after paste; keep Document control.
4. Do not add cycle dates or hours here — those belong in the IEEE 829 test plan.
5. A Senior QA Analyst must verify this document before it is used as a control of record.

# STR-VAULTGRID-001 — VaultGrid Test Strategy

## 1. Context / item under test

VaultGrid is a multi-tenant digital-evidence vault. Tenants are organisations. Evidence objects (files, metadata, hashes, chain-of-custody events) and audit streams must not cross tenant boundaries. Principals act in one of four roles: Admin, Investigator, Reporter, Read-only. Access is authorised from the JWT (`tenant_id`, `role`), not from tenant fields in the request body.

The item under test is the VaultGrid service as presented through the web application and the public HTTP API, including ingest integrity (SHA-256 and size), append-only audit, and region-bound storage (US, UK, Brazil, Australia). Supporting identity provider behaviour is in scope only at the boundary VaultGrid consumes (token claims). Payment, native mobile, and physical device seizure are out of product scope (`product/vaultgrid.md`).

Correctness for this product means: a user in tenant T cannot obtain evidence from tenant T′; a truncated or hash-mismatched upload is not stored as evidence; denied access is logged; exports stay inside the token tenant and the RBAC matrix.

## 2. Test objectives

1. Demonstrate that tenant isolation holds for UI and API, including UUID guessing (REQ-RBAC-01, REQ-RBAC-03, RSK-ISO-01).
2. Demonstrate that the role × action matrix is enforced, including self-elevation denial and stale-token rejection after revoke (REQ-RBAC-02, REQ-RBAC-04, REQ-RBAC-08).
3. Demonstrate that ingest rejects truncated bodies and client/server hash mismatch, and that custody events match stored bytes (REQ-INT-01–05, RSK-INT-01).
4. Demonstrate that allow and deny paths are audited with the required fields (REQ-AUD-01–04, RSK-AUD-01).
5. Demonstrate that export and report packages are role- and assignment-scoped (REQ-EXP-01–04, RSK-EXP-01).
6. Confirm that UAT scripts are executable in each declared home region without storing evidence outside that region (REQ-UAT-01–02).
7. Provide a repeatable regression set for isolation, integrity, and audit so later functional work cannot silently drop those paths.

## 3. In scope

- Functional behaviour of upload, view, download, notes, role administration, audit query, bulk export, and assigned-case report export, against `product/requirements.md`.
- Authorisation and isolation, including cross-tenant IDs and wrong-role actions.
- Integrity of stored bytes and hash records.
- Audit completeness for allow and deny.
- API authorisation using Bearer tokens.
- System-level regression of the above after authz or ingest changes.
- Facilitation and evidence of UAT in regions named by a cycle plan.
- Test documentation produced via QA Scribe (strategy, plan, cases, reports).

## 4. Out of scope

- Performance and soak testing of large-object ingest, except where a functional size limit is specified in a cycle’s requirements. Not applicable as a standing performance programme: no NFRs in the current catalogue.
- Penetration testing beyond functional authorisation (no exploit development, no social engineering).
- Source-code unit tests (development-owned component level; QA audits existence for isolation-sensitive units, does not author them).
- Third-party identity provider internals.
- Physical chain of custody before digital ingest.
- Billing, marketing site, and mobile native clients.
- Production forensic analysis of real investigations.

## 5. Test levels

| Level | Intent | Typical owners | Independence |
| --- | --- | --- | --- |
| Component | Tenant filter, hash function, audit append in isolation | Development | Low — authors of the code. QA reviews that isolation-sensitive modules are covered. |
| Integration | Token validation → authorisation decision → blob store → audit pipeline; region storage binding | Development with QA sampling of contracts | Medium |
| System | End-to-end UI and API: RBAC, isolation, ingest, export, audit queries | QA (functional) | High relative to code authors |
| Acceptance / UAT | Business fitness of investigation workflows per home region and role | Named business coordinators; QA prepares scripts and data | High — business owns fitness sign-off |

Every release train that changes authz, ingest, or audit must include **system** level cases for Crit/High risks. UAT runs when the cycle plan names regions.

## 6. Test types

| Type | In this strategy? | Notes |
| --- | --- | --- |
| Functional | Yes | Primary type at system level |
| Security / authorisation | Yes | Functional authz, isolation, IDOR; not a full pentest |
| Integrity | Yes | Hash, size, custody |
| API | Yes | Same oracles as UI where the API is the control |
| Regression | Yes | Isolation, integrity, audit packs after relevant changes |
| UAT | Yes | Regional, role-based scripts |
| Performance | No (standing) | Only if a cycle adds an explicit NFR |
| Accessibility | No | Not applicable: no a11y requirements in the catalogue |
| Disaster recovery | No | Not applicable: no DR requirements in the catalogue |

## 7. Test techniques to be used later

Case design (in test case specifications, not in this document) shall use ISO/IEC/IEEE 29119-4 and ISTQB techniques:

- Equivalence partitioning (EP) on roles, tenants, token states, file classes.
- Boundary value analysis (BVA) on size and declared Content-Length vs bytes received.
- Decision tables (DT) on role × action from `product/rbac-matrix.md`.
- State transition (ST) on role grant → revoke → retry, and ingest → download → export custody.
- Negative testing (NEG) on bypass, mismatch, truncated, expired token.
- Role × tenant permission matrix (ROLE-MATRIX) as a specialised decision table.
- Integrity tags (INTEGRITY) on hash and custody assertions.

Exploratory sessions may supplement, time-boxed in the **plan**, on High risks only after scripted Crit cases exist. This strategy does not list individual `TC-` IDs.

## 8. Risk-based approach

Product risks live in `product/risks.md`. Likelihood × impact yields Critical, High, Medium, Low. That rank drives **coverage depth** and **case priority**, not the tester’s interest in the UI.

| Rank | Depth | Priority mapping for later cases |
| --- | --- | --- |
| Critical (RSK-ISO-01, RSK-INT-01) | Full: happy, negative, boundary, permission-bypass, integrity. Not deferred. | Case priority 1 |
| High | Full functional + negative. Deferral only via a plan’s “features not to be tested” with residual risk named. | Priority 2 |
| Medium | Representative partitions; may be sampled if a plan’s hours are insufficient. | Priority 3 |
| Low | Smoke or teardown only | Priority 4 |

Order of work in any cycle: isolation and ingest integrity first, then audit deny-path, then export over-share, then remaining functional. A cycle that ships UI chrome but skips Crit isolation cases has not followed this strategy.

ISO/IEC 25010 is used only as a reminder of **what to evaluate** (especially security and functional suitability). It is not the document type.

## 9. Environments, test data strategy, tools

**Environment classes** (instances are named in the plan, not here):

- Development — component/integration; not used for isolation sign-off.
- Test / system — independent tenant pairs (at least two tenants) with all four roles. Used for Crit/High execution.
- UAT per home region — business data, still synthetic.

**Test data:** synthetic organisations, synthetic files, fictional hashes only. Minimum data set: two tenants, four roles each, one assigned and one unassigned case for Reporter, files at 0-byte (reject or policy), small valid file, file at maximum allowed size if a limit exists, truncated transfer, hash-mismatch payload. Teardown of UAT files is a Low residual (RSK-DAT-01) unless a cycle raises it.

**Tools:** Jira/Xray as the case repository; Confluence for signed strategy/plan/reports; optional Postman collections and Playwright scripts as **supporting** automation. They are not this product. QA Scribe generates documentation; it does not execute tests.

## 10. Independence and roles

| Activity | Who |
| --- | --- |
| Component tests | Development |
| System functional and authz | QA Analysts, independent of the code authors |
| Test design and documentation | Senior QA Analyst |
| Risk ranking and residual risk at exit | Senior QA Analyst proposes; QA Manager and Product Owner accept |
| UAT execution | Business coordinators in each region |
| Defect severity on isolation/integrity | QA with Security Champion consultation |
| Sign-off of strategy | QA Manager |
| Sign-off of cycle plan and completion | QA Manager, Product Owner, Engineering Lead |

QA does not approve its own work as the sole signature on a release. Development does not execute the isolation bypass cases that sign the release.

## 11. Entry and exit criteria (approach level)

These gates apply to the **approach**, not to a weekday clock time.

**Entry (to treat a build as in-scope for system test):**

- Build is deployed to the Test class environment and is identifiable by version.
- Product risks for the change are ranked in the register (no unranked Crit candidates).
- At least two tenants and four roles are available with known credentials (synthetic).
- Requirements in play have IDs (REQ-…).
- Audit log is readable by Admin in the Test environment.

**Exit (to recommend that testing of a release train is complete at strategy level):**

- All Critical product risks in scope have executed system cases and no open Severity 1 defects.
- High risks in scope are either executed with no open Severity 2 without a compensating control, or explicitly accepted by Product Owner with ID.
- Isolation, integrity, and audit deny-path regression packs are green or waived with documented residual risk.
- UAT, when required by the cycle plan, has regional signatures.
- Completion report exists (IEEE 829 summary / 29119-3 completion) — produced **per cycle**, not as part of this strategy file.

Not applicable: “testing ends Friday 17:00.” That is a plan schedule, not an approach criterion.

## 12. Incident / defect management model

Defects are recorded in Jira. Severity is impact; priority is order of fix. IEEE 1044 category (logic, interface, data, documentation) may be added when reporting.

| Severity | Definition (VaultGrid) |
| --- | --- |
| 1 Critical | Cross-tenant disclosure, accepted tampered/truncated evidence, audit pipeline off or mutable |
| 2 High | Home-tenant privilege escalation, export over-share, custody hash mismatch on download, deny not logged |
| 3 Medium | Functional failure without isolation/integrity/audit loss; workaround exists |
| 4 Low | Cosmetic; no security or evidence-integrity effect |

Priority 1 defects suspend system test of the affected item (see cycle plans for operationalisation). Isolation and integrity Severity 1 never sit as “known issues” without a no-go.

## 13. Communication and catalogue of deliverables

| Deliverable | Standard | When |
| --- | --- | --- |
| Test strategy (this document) | 29119-3 Test Strategy | Product-level; revise when approach changes |
| Test plan | IEEE 829 / 29119-3 Test Plan | Each cycle |
| Test cases + CSV | 829 / 29119-3 specification | Each in-scope area |
| Design prompt packs | Generator contract | When more cases will be generated |
| RTM | Plan annex | Each cycle |
| Test status report | 29119-3 status | During the cycle |
| Test completion / summary | 29119-3 completion + IEEE 829 summary | End of cycle |

Status is discussed in the QA channel with a risk slice, not a raw pass count. Completion goes to Product Owner and QA Manager.

## 14. Manual vs automated vs out of scope

| Class | Handling |
| --- | --- |
| Isolation bypass, hash mismatch, audit deny, export scope | **Manual** first; automate later only if oracles are stable. Judgement on audit field completeness stays manual. |
| Repeatable API 401/403/404 smoke | Candidate for automation (Postman/Playwright) after the manual oracle is signed |
| UAT regional fitness | Manual, business-owned |
| Exploratory on High risks | Manual, time-boxed in the plan |
| Component unit tests | Out of QA authorship |
| Load testing | Out of scope unless a cycle adds NFRs |

Automation never replaces the human gate on residual risk.

## 15. ISO/IEC 25010 evaluation checklist (optional overlay)

| Characteristic | Evaluate? | Notes |
| --- | --- | --- |
| Functional suitability | Yes | Requirements catalogue |
| Performance efficiency | No | Not applicable: no performance NFRs in catalogue |
| Compatibility | Partial | API contract and browser of record named in the plan |
| Usability | No | Not applicable: no usability study in catalogue |
| Reliability | Partial | Ingest failure behaviour (reject vs store) |
| Security | Yes | Authz, isolation, audit |
| Maintainability | No | Not applicable: not a QA evaluation target here |
| Portability | Partial | Regional deployments as UAT, not a portability programme |

## 16. Approvals (strategy)

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| Senior QA Analyst (author) | Fabian Velasquez | Draft submitted | Unspecified until signed |
| QA Manager | From cycle/organisation intake | Draft — human sign-off required | |
| Product Owner | From cycle/organisation intake | Draft — human sign-off required | |

Names of QA Manager and Product Owner are not invented in this product-level file. Cycle plans name the people who sign that cycle. This strategy is not approved by the generator.

**Human gate:** A QA Manager must verify and sign this strategy before it is used to govern test design. AI output is a draft.
