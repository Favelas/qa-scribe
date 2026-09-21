---
name: qa-scribe-plan
description: Writes a cycle test plan bound to IEEE 829-2008 (15 sections), ISO/IEC/IEEE 29119-3 Test Plan, and ISTQB staffing/entry-exit. Use when the user asks for a test plan, cycle plan, RTM, named hours, schedule, UAT windows, or how we get this release out the door.
---

# QA Scribe — test plan

Version: **1.0.0**

Produce a **test plan**: how we get **this cycle** out the door. Dates, names, hours, RTM. Not a substitute for the product strategy.

## When this skill applies

Trigger terms: test plan, IEEE 829, cycle plan, staffing, schedule, RTM, UAT windows, entry/exit this sprint/cycle. If they want a long-term approach with no dates, use `qa-scribe-strategy`.

## Human still signs

Approvals section is unsigned until QA Manager, Product Owner, and Engineering Lead (from intake) sign. You do not approve.

## Standards cited (exact)

IEEE 829-2008 Test Plan; ISO/IEC/IEEE 29119-3 Test Plan; ISTQB test plan / entry-exit / staffing.

## Intake schema

Required: `product_name`, `cycle_id`, `strategy_id`, `test_items`, `features_in`, `features_out`, `people` (name, role, owns, hours), `schedule` including **deadline**, `risks_this_cycle`, `requirements` for RTM.

If `regions` present: `uat_windows` per region required.

**Do not invent** people, hours, or dates. Run `qa-scribe-intake`.

## Document control block

- Document type: Test Plan
- Standard(s) cited: (exact names above)
- Product: from intake (VaultGrid in examples)
- Cycle / version: from intake
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required
- How to use this file: 5 lines

Stamp: `generator: qa-scribe-plan`, `skill_version: 1.0.0`.

## Required heading list (IEEE 829 order)

Do not drop sections. Wording may be slightly modernised.

1. Test plan identifier
2. Introduction
3. Test items
4. Features to be tested
5. Features not to be tested
6. Approach
7. Item pass/fail criteria
8. Suspension and resumption criteria
9. Test deliverables
10. Remaining test tasks
11. Environmental needs
12. Responsibilities / staffing and training
13. Schedule
14. Risks and contingencies
15. Approvals

Also required: **RTM** (CSV and/or annex table); named people vs hours vs owns; this-cycle risks with mitigation and test refs; UAT windows per region if intake has regions.

## Fail-if-missing

`standards/rubrics/plan.md`. Immediate fail: no deadline, no hours table, no RTM, skipped IEEE section, strategy-only prose.

## Output path

`out/PLN-<PRODUCT>-<cycle>-001.md` and `out/<cycle>-rtm.csv`.

## VaultGrid worked example

`docs/plan.md`  
`docs/rtm.csv`  
`inputs/examples/plan.cycle-59.yaml`  
`reference.md`, `examples.md`

## After user corrections

Run `qa-scribe-improve`. Do not remove staffing hours to “match strategy purity”.
