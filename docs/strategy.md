---
generator: qa-scribe-strategy
skill_version: 1.0.0
---

# Document control

- Document type: Test Strategy
- Standard(s) cited: ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing)
- Product: VaultGrid (**fake product / fake data**)
- Cycle / version: Product-level (not cycle-bound)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Confluence as the living product strategy.
2. QA Manager signs section 16; Product Owner acknowledges scope.
3. Delete this “How to use this file” block after paste.
4. Do not add cycle dates or hours here — those belong in the test plan.
5. A Senior QA Analyst must verify this file before it is a control of record.

# STR-VAULTGRID-001 — VaultGrid Test Strategy

## 1. Context / item under test

VaultGrid is a **fictional** web application. Two companies (NORTHWIND, GLOBEX) share the same login page. Each user sees only their company’s cases. Testers work in the **browser**: lists, buttons, messages. Isolation means: Company A must not see Company B’s case titles.

## 2. Test objectives

1. Isolation: search and case list never show the other company’s titles (REQ-ISO-01, RSK-ISO-01).
2. Roles: Upload, Export, Manage users match `docs/roles.md`.
3. Login succeeds and fails correctly.
4. Empty Case title does not create a case.
5. Denied actions appear in Activity log.
6. Keep a small regression pack for isolation and role buttons after UI changes.

## 3. In scope

Web UI: login, case list, search, upload, manage users, export, activity log. Functional, authorisation-as-UI, regression of those screens. Documentation via QA Scribe.

## 4. Out of scope

API status codes as the primary oracle. Hash/crypto. Mobile app. Billing. Performance. Penetration testing beyond “wrong company must not appear in search.” Component unit tests (development-owned). Physical evidence handling.

## 5. Test levels

| Level | Intent | Owners |
| --- | --- | --- |
| Component | Units behind screens | Development |
| Integration | Login service ↔ case list | Dev + QA sample |
| System | End-to-end UI | QA |
| Acceptance / UAT | Business fitness | Business + QA support |

## 6. Test types

Functional (primary), security/authorisation as **what the UI shows**, regression, UAT when a plan names a window. Performance: not applicable — no NFR in the catalogue.

## 7. Test techniques to be used later

ISO/IEC/IEEE 29119-4 / ISTQB: EP (roles, companies), BVA (empty vs filled title), DT / ROLE-MATRIX (buttons), NEG (wrong password, other company’s title in search). Do not write every case in this strategy.

## 8. Risk-based approach

`docs/risks.md`. Critical isolation first. High role-bypass next. Medium validation and audit. Low cosmetic (export file name) last. Stopper defects (RSK-ISO-01 open) block go. Not-a-stopper leftovers may be go-with-risks with a named owner.

## 9. Environments, test data strategy, tools

Environment classes: Test (two companies, four roles), UAT (business). Data: synthetic companies and files only. Tools: Jira/Xray, Confluence, browser of record Chromium. Playwright optional later; not this product.

## 10. Independence and roles

System UI tests: QA, not the code author. UAT: business. Strategy sign-off: QA Manager. Residual risk: QA proposes, Product Owner accepts.

## 11. Entry and exit criteria (approach level)

**Entry:** build identifiable; two companies and four roles available; REQ IDs exist.  
**Exit:** Critical isolation executed with no open Severity 1; High leftovers named or closed; completion report exists.  
Not applicable: “testing ends Friday 17:00.” That is a plan date.

## 12. Incident / defect management model

| Severity | Meaning |
| --- | --- |
| 1 Stopper | Other company’s data visible; or Read-only can actually upload |
| 2 High | Wrong role reaches Manage users; Export button visible but no file |
| 3 Medium | Empty title creates a case; log gap |
| 4 Low / not a stopper | Cosmetic (wrong label, export.zip without date) |

Severity 1 suspends the item until a new build. Priority is fix order in the **plan**, not in this file.

## 13. Communication and catalogue of deliverables

Strategy (this file), cycle plan, one case pack + CSV, RTM, status report, completion report, two example defects (stopper vs not), prompt pack. Status uses a risk slice, not a vanity pass count.

## 14. Manual vs automated vs out of scope

Isolation search and role buttons: **manual** first. Login 401-style checks may be automated later. UAT: manual. Unit tests: out of QA authorship.

## 15. ISO/IEC 25010 evaluation checklist

| Characteristic | Evaluate? | Notes |
| --- | --- | --- |
| Functional suitability | Yes | Catalogue |
| Security | Yes | Isolation and buttons |
| Usability | Partial | Empty-title message |
| Performance | No | Not applicable: no NFR |
| Others | No | Not applicable: not requested |

## 16. Approvals

| Role | Name | Decision |
| --- | --- | --- |
| Senior QA Analyst (author) | Fabian Velasquez | Draft submitted |
| QA Manager | From organisation intake | Draft — human sign-off required |
| Product Owner | From organisation intake | Draft — human sign-off required |

The generator does not approve.
