# Document control

- Document type: Design prompt pack (generator contract)
- Standard(s) cited: Output MUST conform to IEEE 829 / ISO 29119-3 test case fields and ISO 29119-4 / ISTQB techniques. This file is a generator contract, not a test document.
- Product: VaultGrid
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste a single prompt section into Cursor when generating **additional** RBAC/isolation cases; attach `product/requirements.md`, `product/risks.md`, and `product/rbac-matrix.md`.
2. Do not import this file into Xray. Import only the case pack a human accepts.
3. A Senior QA Analyst reviews every generated case against `standards/rubrics/cases.md`.
4. Delete this “How to use this file” block after storing the contract in a prompt library.
5. Keep every constraint. If a constraint does not apply: `Not applicable: <reason>`.

# PRM-RBAC-001 — RBAC and isolation case generator contract

## 1. Mission

Generate VaultGrid test cases for multi-tenant RBAC and customer data isolation (API and UI). Cover Admin, Investigator, Reporter, Read-only. Order by product risk: RSK-ISO-01 and RSK-ISO-02 before Low happy paths. Produce Markdown tables plus CSV. Next identifier after TC-RBAC-010.

## 2. Mandatory case fields

Every case MUST include:

- Test case identifier `TC-RBAC-<nnn>` (three digits)
- Objective / test condition (one behaviour)
- Trace to requirement ID (`REQ-RBAC-*` or `REQ-API-*` from the catalogue — do not invent)
- Trace to risk ID (`RSK-ISO-*`, `RSK-RBAC-*`, `RSK-API-*` from the register — do not invent)
- Preconditions / environmental needs
- Inputs: test data, role, tenant, token/context
- Procedure: ≤ 8 short independent steps
- Expected outcomes (HTTP code when API; 404 vs 403 rule below)
- Dependencies (`None` or other TC ids)
- Priority derived from risk: Critical→1, High→2, Medium→3, Low→4
- Postconditions or `Not applicable: <reason>`
- Technique tag(s) from: EP | BVA | DT | ST | NEG | ROLE-MATRIX | INTEGRITY

## 3. Techniques to apply

This pack MUST use **ROLE-MATRIX** and **NEG** on every permission-bypass case. Also apply **DT** for role × action cells, **ST** for grant→revoke→retry, **EP** for token/tenant partitions. INTEGRITY is not applicable unless the case also asserts hash fields.

## 4. ID scheme

Pattern: `TC-RBAC-<nnn>`. Last issued: TC-RBAC-010. Continue at TC-RBAC-011. Do not reuse IDs. Areas ISO/API may use `TC-ISO-` / `TC-API-` only if the case is not primarily RBAC.

## 5. Risk-first ordering

Produce in this RSK order:

1. RSK-ISO-01 (cross-tenant disclosure) — Priority 1
2. RSK-ISO-02 (403 vs 404 oracle) — Priority 2
3. RSK-API-01 (IDOR / body tenant) — Priority 2
4. RSK-RBAC-01 (privilege escalation) — Priority 2
5. RSK-RBAC-02 (stale token) — Priority 2
6. Remaining matrix cells (home-tenant Allow paths) last

## 6. Forbidden outputs

- Vague steps (“click around”, “verify it looks good”, “test RBAC”)
- Mixed features in one case (e.g. upload + export + audit in a single TC)
- Missing expected result
- Missing requirement or risk trace
- Invented REQ/RSK IDs, dates, or people
- Strategy or plan prose inside the case pack
- Real customer data, real hashes, real Jira keys
- Cross-tenant expected **403** (existence oracle). Cross-tenant MUST be **404** with no metadata
- More than 8 procedure steps
- Happy-path-only pack when isolation risks are in scope

## 7. Layout

Markdown: document control + how-to + one heading per case with the field table, Procedure, Expected outcomes.

CSV header exactly:

```text
Summary,Priority,Preconditions,Steps,Expected Result,Requirement Keys,Labels,Technique
```

Summary starts with the identifier. Requirement Keys semicolon-separated. Labels include area, RSK id, `qa-scribe`.

Oracle reminder: home-tenant wrong role → **403**. Other-tenant UUID → **404**. Unauthenticated → **401**.

## 8. Human gate

Generated cases remain **Draft — human sign-off required** until a named QA Analyst or QA Manager signs. This prompt does not authorise execution. Stamp outputs `generator: qa-scribe-cases` with the current cases skill version.

## Prompt block (copy into the agent)

You are generating VaultGrid Cycle 59 test cases. Load PRM-RBAC-001 constraints. Use only IDs from product/requirements.md, product/risks.md, and Allow/Deny from product/rbac-matrix.md. Risk-first. ROLE-MATRIX and NEG on bypass cases. IEEE 829 / 29119-3 fields on every case. Write Markdown and CSV. Stop if a required ID is missing.
