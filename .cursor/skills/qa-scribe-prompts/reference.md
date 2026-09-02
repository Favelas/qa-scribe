# Prompts skill — reference

Use with `.cursor/skills/qa-scribe-prompts/SKILL.md`. Skill version 1.0.0.

## Contract test

A competent agent given **only** the prompt pack plus `product/requirements.md`, `product/risks.md`, and `product/rbac-matrix.md` should emit cases with the same field layout as `examples/cases/rbac-tenant-isolation.md`. If the prompt omits expected outcomes or traces, the contract is broken.

## Forbidden outputs (minimum list)

Always include: vague steps; mixed features; missing expected result; missing REQ or RSK trace; invented IDs; real customer data; strategy/plan prose; more than 8 steps.

## Golden regression

`examples/prompts/rbac-design-prompts.md` must still force ROLE-MATRIX, NEG, and the 404-not-403 cross-tenant rule.
