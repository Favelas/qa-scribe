---
name: qa-scribe-strategy
description: Writes a product-level test strategy bound to ISO/IEC/IEEE 29119-3 and ISTQB (strategy vs plan, risk-based testing). Use when the user asks for a test strategy, QA approach, how we test this product, long-term test design, cloud migration approach, 100% parity with legacy, or dual-run/shadow testing — not a cycle plan with dates and hours.
---

# QA Scribe — test strategy

Version: **1.1.0**

Produce a **test strategy**: how we test this product over months. Stable approach. Not this cycle’s calendar.

## When this skill applies

Trigger terms: test strategy, QA strategy, test approach, risk-based testing approach, 29119-3 strategy, cloud migration approach/high-level (no dates), 100% parity, legacy vs cloud, dual-run, shadow testing, reconciliation. If the user wants dates, named hours, or “Cycle 59”, **switch to `qa-scribe-plan`** (after intake). Do not mix.

If the user wants a **cloud migration** high-level approach, “how would you test a migration”, or **100% parity** with a legacy system: copy headings from `standards/cloud-migration-approach-template.md` (read that file with the Read tool first). That file is a strategy overlay (`STR-…`), **not** a cycle plan.

Rules for that overlay:

- Legacy is the **oracle** unless intake named another. “Fix on the way” must be a **named delta list**, not silent.
- If intake says 100% **and** cleanse/fix data, split **parity set** vs **cleanse set** in §3; do not pretend both are 100% parity.
- How we test: baseline → freeze compare contract → dual-run/shadow → data diffs before API before UI → rollback rehearsal (after target writes) → cutover no-go on open Crit parity.
- Do not invent a cloud vendor, RTO/RPO, wave calendar, stores, or interfaces. Empty rows stay `Unknown` or `Not applicable: <reason>`.
- Do not start the strategy with exploratory UI on the new URL. Do not accept sampled-row reconciliation as 100% data parity.
- Candidate risks belong in `qa-scribe-risks` using §12 of the overlay as a **lens**, not pasted as a fake signed register inside the strategy.
- Always keep the heading **For the Software Testing Engineer (plain)** at the top of the generated overlay (after document control). Do not call that reader a “tester”. House role in the control block stays Senior QA Analyst unless intake named another title.

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
skill_version: 1.1.0
```

## Required heading list (keep order)

Copy from `standards/strategy-template.md`.

If the user asked for a **cloud migration** high-level approach, 100% parity, or dual-run (no dates): copy from `standards/cloud-migration-approach-template.md` instead (all of its numbered headings, including Parity contract, How we test, and Candidate risk lenses). Same fail-if-missing on hours/dates; extra fail: invented vendor, RTO/RPO, wave calendar, sampled-row “100%” data claim, or exploratory-UI-first sequence.

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

Use `standards/rubrics/strategy.md` and sibling `rubric.md`. Immediate fail: any named hours or cycle deadline; missing test levels; cases written in full in the strategy; no risk → depth rule. For the migration overlay: immediate fail if a 100% parity claim has no §3 contract, or if Crit data reconciliation is described as a sample.

## Output path

Write `out/STR-<PRODUCT>-001.md`. Do not promote to `docs/` unless the user accepts it as golden.

## VaultGrid worked example

`docs/strategy.md`  
Intake shape: `inputs/examples/strategy.vaultgrid.yaml`  
Reference: `reference.md`  
Style: `examples.md`

## After user corrections

Run `qa-scribe-improve` with this generator’s rubric. Do not weaken S17 (no hours in strategy).
