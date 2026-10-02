---
name: qa-scribe-matrix
description: Writes a product-level risk-based test matrix that allocates register risks to test levels, types, techniques, and coverage depth (ISTQB RBT). Use when the user asks for a risk-based test matrix, RBT matrix, risk coverage matrix, risk × test type table, or how to allocate tests to risks — not a risk register, not a cycle RTM, not a role × screen matrix.
---

# QA Scribe — risk-based test matrix

Version: **1.0.0**

Turn a ranked product risk register into the **working allocation table**: which levels, types, and techniques run for each `RSK-`, at what coverage depth, tracing to existing `TC-` IDs or `Planned`. Product-level. Not this cycle’s calendar.

## When this skill applies

Trigger terms: risk-based test matrix, RBT matrix, risk coverage matrix, risk × test type, risk × test level, allocate tests to risks, MTX-.

If the user wants **what could go wrong** (new `RSK-` rows), **switch to `qa-scribe-risks`**. If they want **REQ → TC for this cycle**, that is the plan RTM (`qa-scribe-plan` Annex A). If they want **who sees which button**, that is the role × screen matrix (`docs/roles.md` / ROLE-MATRIX cases). Do not mix.

## Human still signs

Status remains `Draft — human sign-off required`. If the risk register is still a candidate, this matrix stays Draft and must not be treated as a signed control of record. QA Manager signs allocation depth; Product Owner acknowledges residual None/Planned on High. You do not.

## Standards cited (exact)

ISTQB risk-based testing (product risk → test depth / priority / allocation). There is no ISO/IEC/IEEE document number for a risk-based test matrix — do not cite one. Technique tags: ISO/IEC/IEEE 29119-4 / ISTQB (EP, BVA, DT, ST, NEG, ROLE-MATRIX, INTEGRITY).

## Intake schema

Run `qa-scribe-intake` if required keys are missing. **Do not invent** risks, REQ IDs, case IDs, dates, hours, or people.

Required: `product_name`, `risk_register_ref` (path or pasted `RSK-` rows with Level, Stopper?, Test depth), `requirements_ref` (path or pasted `REQ-` IDs).

Optional: `strategy_id` or strategy test types/levels; `case_pack_ref` (to fill Case IDs); which test types are in/out of scope.

Forbidden in this document: cycle deadline, named hour allocations, sprint calendar, invented `TC-` identifiers, numeric probability/impact scores with no stated basis, new `RSK-` rows that are not on the register.

## Document control block

Start every file with:

- Document type: Risk-based test matrix
- Standard(s) cited: (exact names above)
- Product: from intake
- Cycle / version: Product-level (not cycle-bound)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required
- How to use this file: 5 lines (where to paste, who signs, what to delete)

YAML stamp:

```yaml
generator: qa-scribe-matrix
skill_version: 1.0.0
```

## Required heading list (keep order)

Copy from `standards/risk-based-test-matrix-template.md`:

1. Purpose and relationship
2. Inputs
3. Coverage-depth legend
4. Risk × test type matrix
5. Risk × test level matrix
6. Allocation table
7. Coverage gaps
8. Ordering rule
9. Approvals
10. Annex A — Allocation CSV (optional) or `Not applicable: Markdown table in §6 is the control copy.`

If a section has no data: keep the heading; write `Not applicable: <reason>`.

## Allocation rules

- One row per in-scope register risk. Rank Critical/High before Medium/Low.
- Copy Level, Stopper?, Test depth, and the risk sentence from the register. Do not re-score.
- Coverage-depth tokens only: Extensive / Standard / Cursory / None. Default: Critical → Extensive; High → Standard (Extensive if stopper); Medium → Standard; Low → Cursory.
- Test types: Functional, Security/authz, Integrity, Audit, API, Regression, UAT, Exploratory — **only where the strategy or intake supports that type**. Skip padding a type the product has no basis for; use `Not applicable: <reason>` rather than a decorative column of None.
- Test levels: Component, Integration, System, Acceptance/UAT.
- Technique tags only for failure modes the risk can actually hit. No orphan ROLE-MATRIX on a non-RBAC risk.
- Case IDs: from `case_pack_ref` / intake only. Otherwise `Planned`. Never mint `TC-`.
- Every Critical/High must have Standard or Extensive on at least one in-scope type and one level. Unexplained None on Critical is an immediate fail.
- Residual if untested: name the leftover the completion report would have to carry, or `N/A — allocated`.

## Fail-if-missing

`standards/rubrics/risk-based-test-matrix.md`. Immediate fail: invented TC/RSK IDs; numeric L×I scores; missing Stopper? or REQ on an allocation row; Critical with no allocation; dates/hours; presenting a draft register’s matrix as confirmed fact; mixing this file with a cycle RTM or role × screen matrix.

## Output path

`out/MTX-<PRODUCT>-001.md`

Optional CSV of §6: `out/MTX-<PRODUCT>-001.csv` with the Annex A header from the template.

## Worked pattern

`standards/risk-based-test-matrix-template.md` (blank structure + VaultGrid illustration rows). Treat illustration rows as layout only, not facts about the user’s product.

## After user corrections

Run `qa-scribe-improve`. Do not drop a Critical row or soften Extensive to Cursory to make the matrix look covered.
