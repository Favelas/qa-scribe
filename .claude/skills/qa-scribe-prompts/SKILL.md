---
name: qa-scribe-prompts
description: Writes generator-contract prompt packs so further test cases keep IEEE 829 / ISO 29119-3 fields and ISO 29119-4 / ISTQB techniques. Use when the user asks for design prompts, case-generator prompts, prompt pack, or contracts for the next Xray cases.
---

# QA Scribe — design prompts

Version: **1.0.0**

There is **no** ISO/IEEE standard for AI prompts. This file is a **generator contract**, not a test document. Output of any later generation MUST still look like senior Xray work.

## When this skill applies

Trigger terms: design prompts, prompt pack, generator contract, more cases like these, rewrite the case prompt.

## Human still signs

Prompt packs are not executed. Cases they produce still need a QA Analyst sign-off.

## Standards cited (exact sentence on the file)

Output MUST conform to IEEE 829 / ISO 29119-3 test case fields and ISO 29119-4 / ISTQB techniques. This file is a generator contract, not a test document.

## Intake schema

Required: product, area, REQ/RSK lists, last TC id, techniques to force.

Optional: known forbidden patterns from learnings.

## Document control block

- Document type: Design prompt pack (generator contract)
- Standard(s) cited: the sentence above
- Product: from intake
- Cycle / version: from intake
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required
- How to use this file: 5 lines

Stamp: `generator: qa-scribe-prompts`, `skill_version: 1.0.0`.

## Required heading list

From `standards/prompt-pack-template.md`:

1. Mission
2. Mandatory case fields (full list)
3. Techniques to apply
4. ID scheme
5. Risk-first ordering
6. Forbidden outputs
7. Layout (Markdown + CSV)
8. Human gate

Each pack **must force**: field list, risk-first order, named techniques, ID scheme, forbidden outputs (vague steps, mixed features, missing expected result, missing requirement trace).

## Fail-if-missing

`standards/rubrics/prompts.md`. Immediate fail: missing forbidden list; could not regenerate golden field layout.

## Output path

`out/PRM-<AREA>-001.md`

## VaultGrid worked example

`docs/prompts.md`  
`reference.md`, `examples.md`

## After user corrections

Run `qa-scribe-improve`.
