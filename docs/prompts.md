---
generator: qa-scribe-prompts
skill_version: 1.0.0
---

# Document control

- Document type: Design prompt pack (generator contract, not testware)
- Standard(s) cited: Output MUST conform to IEEE 829 / ISO 29119-3 test case fields and ISO 29119-4 / ISTQB techniques. This file is a generator contract, not a test document.
- Product: VaultGrid (**fake data**)
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Cursor to generate **more UI cases** in the same layout as `docs/cases.md`.
2. Do not import this file to Xray.
3. A QA Analyst reviews generated cases.
4. Delete this block after storing in a prompt library.
5. UI oracles only (buttons, lists, messages). Do not require HTTP codes.

# PRM-UI-001

## 1. Mission

More VaultGrid **browser** cases. Isolation = Company A must not see Company B titles. Roles = who sees Upload / Export / Manage users.

## 2. Mandatory case fields

Identifier `TC-<AREA>-<nnn>`; objective; REQ; RSK; preconditions; inputs (role, company); ≤8 steps; expected **on screen**; dependencies; priority from risk; postconditions; technique tags.

## 3. Techniques

ROLE-MATRIX, NEG, EP, BVA. Next ID after TC-AUD-001.

## 4. ID scheme

`TC-ISO-`, `TC-RBAC-`, `TC-AUTH-`, `TC-VAL-`, `TC-AUD-`.

## 5. Risk-first

RSK-ISO-01 then RSK-RBAC-* then Medium/Low.

## 6. Forbidden

Vague “check the page”; mixed features; missing expected; invented REQ/RSK; API-only oracles; real customer data; more than 8 steps.

## 7. Layout

Markdown tables + CSV header: Summary, Priority, Preconditions, Steps, Expected Result, Requirement Keys, Labels, Technique.

## 8. Human gate

Draft until a QA Analyst signs. Stamp `generator: qa-scribe-cases`.
