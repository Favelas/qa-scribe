---
name: qa-scribe-risks
description: Drafts a candidate product risk register (ID, plain-English risk, level, stopper?, test depth) from requirements or plain user stories, bound to ISTQB risk-based testing. Use when the user asks for a risk register, product risks, what could go wrong, risk-based test depth, or wants risks derived from user stories before running strategy, plan, or cases.
---

# QA Scribe — risk register

Version: **1.0.0**

Turn stated features into a ranked list of **what could go wrong**. Every downstream generator (`qa-scribe-strategy`, `qa-scribe-plan`, `qa-scribe-cases`) treats this file's output as the `risk_register_ref` input — so it must be honest about being a draft, not settled fact.

## When this skill applies

Trigger terms: risk register, product risks, what could go wrong, risk-based testing, stopper risks, risk levels, before we write the strategy/plan/cases.

## Human still signs

This is the one generator explicitly allowed to **infer** from stated input — that is risk analysis, not invention. It may never assert a fact the input didn't state (no PII claim if none was mentioned, no numeric probability with no basis). Every risk stays **Draft** until the QA Manager or Product Owner confirms level and stopper status. Strategy/plan/cases must not silently promote an unconfirmed risk to fact.

## Standards cited (exact)

ISTQB risk-based testing (product risk identification, likelihood × impact, risk-based test depth). There is no ISO/IEC/IEEE document number for a product risk register itself — do not cite one.

## Intake schema

Required: `product_name`, and **either** existing `REQ-<AREA>-nn` requirement IDs **or** plain-English requirements/user stories to analyze.

Optional: known constraints that widen the risk lens — multi-tenant?, RBAC/permission tiers?, handles files/uploads?, audit/compliance needs?, integrations/APIs?, regions/UAT?

Inference is allowed (e.g. "search across tenants" → tenant-isolation risk). Invention is not: do not assign a probability/impact number, name a specific data type, or claim a compliance obligation that nothing in the input implies. If the input is too thin to support even inference, say so and ask one clarifying question rather than filling the table with generic filler risks.

## Document control block

- Document type: Product risk register (candidate/draft)
- Standard(s) cited: ISTQB risk-based testing
- Product: from intake
- Cycle / version: product-level unless intake names a cycle
- Author role: Senior QA Analyst (AI-drafted, pending sign-off)
- Status: **Draft — human sign-off required before strategy/plan/cases treat this as fact**

Stamp: `generator: qa-scribe-risks`, `skill_version: 1.0.0`.

## Required fields on EVERY risk

| Field | Rule |
| --- | --- |
| Identifier | `RSK-<AREA>-<nnn>` (area codes: `standards/id-schemes.md`) |
| Risk (plain English) | One sentence, one failure mode |
| Basis | The REQ ID or the specific stated feature/phrase this risk was inferred from — never blank |
| Level | Critical \| High \| Medium \| Low, with a one-clause rationale |
| Stopper? | Yes — stopper / Yes if \<condition\> / No — but named leftover / No |
| Test depth | What must run to close or accept this risk |

## Risk design rules

- Rank Critical/High before Medium/Low — same convention as every other QA Scribe pack.
- Use a category lens only where the input actually supports it: tenant isolation, RBAC/permission leakage, data integrity (upload/hash/custody), negative/validation (empty/boundary input), audit/traceability, export/availability, regional/UAT acceptance. Skip categories the input gives no basis for — do not pad the table to look thorough.
- Every risk traces to a REQ ID or a quoted/paraphrased fragment of the input in the Basis column. No orphan risks.
- If the same failure mode could be split into a Critical version (data crosses a real boundary) and a lesser version (button visible but action blocked), write both — that distinction is what makes "go-with-risks" vs "no-go" decisions later actually mean something.

## Fail-if-missing

`standards/rubrics/risks.md`. Immediate fail: a risk with no Basis; missing Stopper column; not ranked Critical/High first; a numeric probability/impact score invented with no stated basis; risks presented as confirmed rather than draft.

## Output path

`out/RSK-<PRODUCT>-register.md`

## Worked pattern

`docs/risks.md` shows the target shape (ID / Risk / Level / Stopper? / Test depth table, ranking note at the bottom) — treat it as a layout reference only, not as facts about your product.

## After user corrections

Run `qa-scribe-improve`. Do not soften a Critical to Medium just to make the register shorter.
