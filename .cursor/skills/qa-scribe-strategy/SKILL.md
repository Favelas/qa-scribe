---
name: qa-scribe-strategy
description: Writes a product-level test strategy bound to ISO/IEC/IEEE 29119-3 and ISTQB (strategy vs plan, risk-based testing). Use when the user asks for a test strategy, QA approach, how we test this product, or long-term test design — not a cycle plan with dates and hours.
---

# QA Scribe — test strategy

Version: **1.0.0**

Produce a **test strategy**: how we test this product over months. Stable approach. Not this cycle’s calendar.

## When this skill applies

Trigger terms: test strategy, QA strategy, test approach, risk-based testing approach, 29119-3 strategy. If the user wants dates, named hours, or “Cycle 59”, **switch to `qa-scribe-plan`** (after intake). Do not mix.

## Human still signs

Status remains `Draft — human sign-off required`. QA Manager (and Product Owner for scope) sign. You do not.

## Standards cited (exact)

ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing). Optional overlay: ISO/IEC 25010 characteristics as a **checklist of what to evaluate**, not as the document type.

## Intake schema

Run `qa-scribe-intake` if required keys are missing. **Do not invent** product facts.

Required: `product_name`, `item_under_test`, `objectives`, `in_scope`, `out_of_scope`, `risk_register_ref` or pasted risks, `requirements_ref` or pasted REQ IDs.

Optional: tools, environment **classes**, automation intent, 25010 overlay, role titles (no hours).

Forbidden in this document: cycle deadline, named hour allocations, “Cycle 59”, sprint calendar, named testers’ hours.

## Document control block

Start every file with:

- Document type: Test Strategy
- Standard(s) cited: (exact names above)
- Product: from intake (VaultGrid in examples)
- Cycle / version: Product-level (not cycle-bound)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required
- How to use this file: 5 lines (where to paste, who signs, what to delete)

YAML stamp:

```yaml
generator: qa-scribe-strategy
skill_version: 1.0.0
```

## Required heading list (keep order)

Copy from `standards/strategy-template.md`:

1. Context / item under test
2. Test objectives
3. In scope
4. Out of scope
5. Test levels (component, integration, system, acceptance/UAT)
6. Test types
7. Test techniques to be used later (point to 29119-4; do not write every case)
8. Risk-based approach
9. Environments, test data strategy, tools
10. Independence and roles
11. Entry/exit criteria at **approach** level (no sprint Friday 17:00)
12. Incident / defect management model
13. Communication and catalogue of deliverables
14. Manual vs automated vs out of scope
15. ISO/IEC 25010 checklist or `Not applicable: 25010 overlay not requested in intake.`
16. Approvals

If a section has no data: keep the heading; write `Not applicable: <reason>`.

## Fail-if-missing

Use `standards/rubrics/strategy.md` and sibling `rubric.md`. Immediate fail: any named hours or cycle deadline; missing test levels; cases written in full in the strategy; no risk → depth rule.

## Output path

Write `out/STR-<PRODUCT>-001.md`. Do not promote to `examples/` or `ready-to-paste/` unless the user accepts it as golden.

## VaultGrid worked example

`examples/strategy/vaultgrid-strategy.md`  
Intake shape: `inputs/examples/strategy.vaultgrid.yaml`  
Reference: `reference.md`  
Style: `examples.md`

## After user corrections

Run `qa-scribe-improve` with this generator’s rubric. Do not weaken S17 (no hours in strategy).
