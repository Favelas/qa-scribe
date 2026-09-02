# Test strategy template

- Document type: Test Strategy template
- Standard(s) cited: ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing)
- Product: VaultGrid (replace with intake product)
- Cycle / version: Product-level (not cycle-bound)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Duplicate this file or let `qa-scribe-strategy` fill it from intake.
2. Paste the result into Confluence as the living product strategy.
3. QA Manager signs; Product Owner acknowledges scope.
4. Delete this “How to use this file” block after paste.
5. If a section has no data, keep the heading and write `Not applicable: <reason>`.

---

Required headings (keep this order). Optional ISO/IEC 25010 overlay is a checklist at the end, not a replacement for these sections.

## Document control

| Field | Value |
| --- | --- |
| Identifier | STR-\<PRODUCT\>-\<nnn\> |
| Document type | Test Strategy |
| Standard(s) cited | ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing) |
| Product | |
| Cycle / version | Product-level (not cycle-bound) |
| Author role | Senior QA Analyst |
| Status | Draft — human sign-off required |
| Generator | qa-scribe-strategy |
| Skill version | 1.0.0 |

## 1. Context / item under test

Describe the system, tenants, users, and what “correct” means for isolation and integrity. No sprint dates.

## 2. Test objectives

Measurable objectives (authorisation correctness, isolation, integrity, audit completeness, UAT fitness). Not “ship Cycle 59”.

## 3. In scope

Product areas and quality characteristics that testing will address over time.

## 4. Out of scope

Explicit exclusions with reason.

## 5. Test levels

| Level | Intent | Typical owners | Independence |
| --- | --- | --- | --- |
| Component | Units and services in isolation | Development | Low (dev-owned) |
| Integration | Contracts, identity, storage, audit pipeline | Dev + QA | Medium |
| System | End-to-end functional, authz, integrity, API | QA | High relative to authors of the code |
| Acceptance / UAT | Business fitness per region/role | Business + QA support | High |

## 6. Test types

Functional, security/authorisation, regression, API, UAT, integrity, audit. State which are in the strategy and which are out.

## 7. Test techniques (to be used later)

Point to ISO/IEC/IEEE 29119-4 / ISTQB: EP, BVA, DT, ST, NEG, ROLE-MATRIX, INTEGRITY. Do **not** write the cases here.

## 8. Risk-based approach

How product risk (see risk register) maps to coverage depth and case priority. Critical/High before Low happy paths.

## 9. Environments, test data strategy, tools

Classes of environment (dev, test, UAT per region). Data: synthetic only. Tools: testware repo, Xray/Jira, Postman/Playwright as **supporting** tools if the organisation uses them — not as this product.

## 10. Independence and roles

Who tests what. No named hour allocations.

## 11. Entry and exit criteria (approach level)

Approach-level gates (build is deployable, risks ranked, environments available, residual Crit/High accepted or closed). **No** “Friday 17:00 this sprint”.

## 12. Incident / defect management model

Severity vs priority. IEEE 1044 category overlay is allowed when classifying. Escalation path without cycle dates.

## 13. Communication and catalogue of deliverables

Strategy, plan (per cycle), cases, RTM, status reports, completion reports, prompt packs.

## 14. Manual vs automated vs out of scope

What stays manual (judgement, UAT, exploratory on authz), what may be automated later, what is not tested.

## 15. ISO/IEC 25010 evaluation checklist (optional overlay)

| Characteristic | Evaluate in this product? | Notes |
| --- | --- | --- |
| Functional suitability | Yes / No | |
| Performance efficiency | | |
| Compatibility | | |
| Usability | | |
| Reliability | | |
| Security | | |
| Maintainability | | |
| Portability | | |

If unused: `Not applicable: 25010 overlay not requested in intake.`

## 16. Approvals (strategy)

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| QA Manager | From intake or Not applicable: name not supplied | | |
| Product Owner | | | |

Human sign-off is mandatory. The generator does not approve.
