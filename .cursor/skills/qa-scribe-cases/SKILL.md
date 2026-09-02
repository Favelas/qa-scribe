---
name: qa-scribe-cases
description: Writes IEEE 829 / ISO 29119-3 test case packs with ISO 29119-4 and ISTQB techniques and Xray-oriented CSV. Use when the user asks for test cases, Xray cases, RBAC cases, isolation search, permission buttons, equivalence partitioning, decision tables, or a case pack to execute.
---

# QA Scribe — test cases

Version: **1.0.0**

Produce **what we will execute**. Risk-first. One behaviour per case. Markdown + CSV.

## When this skill applies

Trigger terms: test cases, test specifications, Xray, Jira cases, RBAC cases, isolation cases, hash, audit cases, 29119-4, EP, BVA, decision table.

## Human still signs

Cases remain Draft until a Senior QA Analyst (or named plan owner) reviews traces, expected results, and priority. You do not authorise execution.

## Standards cited (exact)

IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification. Techniques: ISO/IEC/IEEE 29119-4 and ISTQB — EP, BVA, DT, ST, use-case/scenario, negative testing, role × tenant permission matrix. Xray field names are a **tool schema**, not a standard; still required for usability.

## Intake schema

Required: product, cycle or product-level, REQ IDs, RSK IDs with levels, area, next ID, environment/precondition facts.

Optional: RBAC matrix path, Xray project key.

Do not invent REQ/RSK. Run `qa-scribe-intake`.

## Document control block

- Document type: Test Case Specification
- Standard(s) cited: (exact names above)
- Product: VaultGrid in examples
- Cycle / version: from intake
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required
- How to use this file: 5 lines (Markdown vs CSV, who imports to Xray, who signs)

Stamp: `generator: qa-scribe-cases`, `skill_version: 1.0.0`.

## Required fields on EVERY case

- Test case identifier (`TC-<AREA>-<nnn>`)
- Objective / test condition
- Trace to requirement ID and to risk ID
- Preconditions / environmental needs
- Inputs (test data, role, tenant, token/context)
- Procedure: ≤ 8 short independent steps
- Expected outcomes
- Dependencies
- Priority derived from risk (not preference)
- Postconditions if needed
- Technique tag(s): EP | BVA | DT | ST | NEG | ROLE-MATRIX | INTEGRITY

## Case design rules

- Crit/High risks before Low happy paths
- One behaviour per case; no “verify the page looks good”
- Include happy, negative, boundary, permission-bypass, and data-integrity paths when the feature can fail that way
- Provide markdown **and** CSV: Summary, Priority, Preconditions, Steps, Expected Result, Requirement Keys, Labels, Technique
- Steps numbered in CSV using `||` or newline as the user’s Xray convention; default: numbered lines separated by ` | `

## Fail-if-missing

`standards/rubrics/cases.md`. Immediate fail: missing REQ or RSK; no isolation search case when two companies are in scope; no role-button case when RBAC is in scope; >8 steps; mixed features.

## Output path

`out/TC-<AREA>-pack.md` and `out/TC-<AREA>-pack.csv`.

## VaultGrid worked examples

- `docs/cases.md` (UI isolation + role buttons)
- `docs/cases.csv`
- Intake: `inputs/examples/cases.rbac.yaml`

## After user corrections

Run `qa-scribe-improve`. Do not drop traces to make cases “cleaner”.
