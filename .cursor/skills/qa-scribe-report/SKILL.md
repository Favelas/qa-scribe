---
name: qa-scribe-report
description: Writes an in-cycle Test Status Report or an end-of-cycle Test Completion / IEEE 829 Test Summary Report, sliced by risk vs exit criteria. Use when the user asks for a test report, QA status, test summary, completion report, residual risk, go/no-go, or metrics dashboard for a test cycle.
---

# QA Scribe — metrics / report

Version: **1.0.0**

Choose flavour from intake. **Never** mix them in one file.

- **A) Test Status Report** (ISO/IEC/IEEE 29119-3) — in-cycle: executed vs planned, blocked, not-run, defects opened, exit criteria **forecast**
- **B) Test Completion / Test Summary Report** (29119-3 + IEEE 829-2008) — end of cycle: variances, coverage, evaluation, **go / go-with-risks / no-go**

## When this skill applies

Trigger terms: test report, status report, completion report, test summary, residual risk, exit criteria, go-no-go, QA metrics.

## Human still signs

Recommendation on completion reports is a **draft** until QA Manager and Product Owner sign. Do not invent go/no-go if the user did not supply a recommendation **and** residual risks; if residual High exists, default draft recommendation is **go-with-risks** or **no-go** per the rule below — still labelled Draft.

Rule: if any in-scope Critical is open or untested → draft **no-go**. If Critical is clear but High remains with a named compensating control from intake → draft **go-with-risks**. If the user insists on all-green while High remains → **refuse** (rubric R10).

## Standards cited (exact)

IEEE 829-2008 Test Summary Report; ISO/IEC/IEEE 29119-3 Test Status Report and Test Completion Report; ISTQB progress reporting, summary reporting, residual risk vs exit criteria. Optional: IEEE 1044-style defect classification (category + severity) when listing defects.

## Intake schema

Required: product, cycle, plan_id, `flavour` (`status`|`completion`), counts by risk, open Crit/High, requirement gaps.

Status also needs `as_of`. Completion also needs cycle end and, if hours were in the plan, planned vs actual hours.

Optional: defects with 1044 category, regions UAT, human recommendation.

Do not invent defect IDs or counts. Run `qa-scribe-intake`.

## Document control block

- Document type: flavour A or B labelled clearly
- Standard(s) cited: matching flavour
- Product, cycle, author role, Draft status
- How to use this file: 5 lines

Stamp: `generator: qa-scribe-report`, `skill_version: 1.0.0`.

## Required headings

**Flavour A** — copy `standards/status-report-template.md` (period, executed vs planned by risk, blocked, defects, open Crit/High, REQ gaps, UAT remaining, exit forecast, issues, human gate).

**Flavour B** — IEEE 829 Test Summary content in order from `standards/completion-report-template.md`:

1. Identifier
2. Summary of testing performed
3. Variances (plan vs actual)
4. Comprehensive assessment (coverage vs items/features/requirements/risks)
5. Summary of results (pass/fail/blocked/not-run)
6. Evaluation (remaining risk)
7. Summary of activities / effort vs plan if hours exist
8. Approvals and recommendation: go / go-with-risks / no-go + owners

Plus defect summary and UAT by region when data exists.

## Metrics rules

- Slice by **RISK**, not vanity “420 cases passed”
- Open Crit/High listed
- Coverage gaps vs requirements
- UAT remaining by region/role if intake has it
- Never a fake 100% green dashboard if residual High risk remains

## Fail-if-missing

`standards/rubrics/report.md`. Immediate fail: mixed A+B; completion all-green with unnamed High; no risk slice.

## Output path

`out/RPT-STS-…md` or `out/RPT-SUM-…md`.

## VaultGrid worked examples

- `examples/reports/cycle-59-status.md`
- `examples/reports/cycle-59-completion.md` (go-with-risks, leftover High RSK-EXP-01)
- Intake: `inputs/examples/report.cycle-59.yaml`

## After user corrections

Run `qa-scribe-improve`.
