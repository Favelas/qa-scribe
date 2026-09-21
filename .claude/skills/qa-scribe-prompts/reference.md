# Prompts skill — reference

Use with `.cursor/skills/qa-scribe-prompts/SKILL.md`. Skill version 1.0.0.

## Contract test

A competent agent given **only** the prompt pack plus `docs/requirements.md`, `docs/risks.md`, and `docs/roles.md` should emit cases with the same field layout as `docs/cases.md`. If the prompt omits expected outcomes or traces, the contract is broken.

## Forbidden outputs (minimum list)

Always include: vague steps; mixed features; missing expected result; missing REQ or RSK trace; invented IDs; real customer data; strategy/plan prose; more than 8 steps.

## Golden regression

`docs/prompts.md` must still force ROLE-MATRIX, NEG, and UI isolation (Company A must not see Company B titles).
