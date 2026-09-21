---
name: qa-scribe-intake
description: Collects missing QA Scribe intake fields and refuses to invent requirements, dates, hours, or team names. Use when the user wants a test strategy, test plan, test cases, design prompts, or a test report but YAML/intake is incomplete, when they say gather inputs, missing fields, or start a QA Scribe run.
---

# QA Scribe — intake

Version: **1.0.0**

You collect facts. You do not generate the strategy, plan, cases, prompts, or report until required keys for that generator are present. You do not invent requirements, dates, people, hours, or risk rankings.

## When this skill applies

User asks to start QA documentation, provides partial YAML, or a generator skill is blocked on missing inputs. Trigger terms: intake, missing inputs, gather requirements, before you write the plan/strategy/cases/report.

## Human still signs

Intake YAML is not a signed test document. A Senior QA Analyst (or the role named in the plan) must confirm the facts before generators run for a control of record.

## Confidentiality

Refuse real employer names, real tickets, real evidence hashes, real customer data. Ask the user to fictionalise or use VaultGrid (`docs/product.md`).

## Workflow

1. Identify the **target generator**: strategy | plan | cases | prompts | report (status | completion).
2. Load the schema below. Compare to what the user pasted.
3. Ask **only** for missing **required** keys. Optional keys: mention once, do not block if unused (write `Not applicable` later).
4. If the user says “just make it up”: refuse. Point at `inputs/examples/`.
5. When complete, write YAML to `out/` only if they asked to save; otherwise keep it in chat. Then tell them which skill to run next.
6. Never run a generator that would mix strategy and plan.

## Shared keys (all generators)

| Key | Required | Notes |
| --- | --- | --- |
| `product_name` | Yes | Examples use VaultGrid |
| `author_role` | Yes | Default suggestion: Senior QA Analyst — still confirm |
| `confidential` | Yes | Must be `false` for this public workflow; if true, stop |

Do not invent `product_name`.

## Strategy — required vs optional

Required: `product_name`, `item_under_test`, `objectives`, `in_scope`, `out_of_scope`, `risk_register_ref` (path or pasted risks with IDs), `requirements_ref` (path or pasted REQ IDs).

Optional: `tools`, `environments_classes` (no cycle dates), `automation_intent`, `iso_25010_overlay` (boolean), `roles_who_tests_what` (role titles, **not** hours).

Forbidden in strategy intake: `cycle_deadline`, `named_hours`, `sprint_calendar`, tester hour tables.

## Plan — required vs optional

Required: `product_name`, `cycle_id`, `strategy_id`, `test_items` (builds/versions), `features_in`, `features_out`, `entry_exit_this_cycle`, `people` (name, role, owns, **hours**), `schedule` (dates including **deadline**), `risks_this_cycle` (id, mitigation, test refs if known), `requirements` (IDs for RTM).

Optional: `regions` (if present, UAT windows **per region** become required), `training`, `tools`, `defect_process_ref`.

If `regions` is non-empty: require `uat_windows[]` with region, dates, coordinator name from `people`.

## Cases — required vs optional

Required: `product_name`, `cycle_id` (or `product-level`), `requirements` with IDs, `risks` with IDs and levels, `area` (RBAC, INT, …), `id_next` (next TC number), `environments` for preconditions.

Optional: `rbac_matrix_ref`, `api_base`, `xray_project_key`.

## Prompts — required vs optional

Required: same traces as cases plus `techniques[]`, `forbidden_already_seen` (if any), `last_tc_id`.

Optional: `style_notes` from learnings.

## Report — required vs optional

Required: `product_name`, `cycle_id`, `plan_id`, `flavour` = `status` | `completion`, `as_of` (status) or `cycle_end` (completion), `counts_by_risk` (planned/executed/pass/fail/blocked/not_run), `open_crit_high[]`, `req_gaps[]`.

Optional: `hours_planned`, `hours_actual`, `defects[]` (IEEE 1044 category + severity), `regions_uat[]`, `recommendation` **only if flavour is completion and a human supplied it** — do not invent go/no-go.

## Fail if

- You filled dates, hours, or surnames that the user did not provide.
- You created REQ or RSK IDs not in intake or `docs/`.
- You proceeded to generate a plan without hours and deadline.

## Pointers

- Example YAML: `inputs/examples/`
- VaultGrid: `docs/product.md`
- Principles: `standards/documentation-principles.md`
- Validator (optional): `python3 scripts/validate_intake.py inputs/examples/plan.cycle-59.yaml`

## After intake is complete

| Target | Next skill |
| --- | --- |
| strategy | `qa-scribe-strategy` |
| plan | `qa-scribe-plan` |
| cases | `qa-scribe-cases` |
| prompts | `qa-scribe-prompts` |
| report | `qa-scribe-report` |
