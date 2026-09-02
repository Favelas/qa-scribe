# Learning — 2026-09-02 — bootstrap

- Skill targeted: all `qa-scribe-*` (family v1.0.0)
- Artefact: repository design, not a rejected generation
- Scorer: Senior QA Analyst (author)

## Failure

Not applicable: this note records **initial design decisions** before the first improve cycle. There is no failed generation yet.

## Root cause

Blank-page QA documentation is slow. Models draft quickly but mix test strategy with test plan, omit IEEE 829 sections, skip traces, and paint all-green reports. Hiring-manager portfolios often show outlines instead of signable documents.

## Rule to add

These rules are already in the v1.0.0 skills (not a later patch):

1. Five generators; never mix jobs. Strategy has zero named hours and zero cycle deadline. Plan has IEEE 829 fifteen sections, deadline, named allocation, RTM, approvals.
2. Document control + five-line how-to on every golden and generated file. Keep required headings; use `Not applicable: <reason>`.
3. Cases: IEEE 829 / 29119-3 fields, risk-first, REQ + RSK traces, technique tags, Markdown + CSV. Isolation in scope ⇒ permission-bypass. Integrity in scope ⇒ hash-mismatch or truncate.
4. Reports: flavour A status ≠ flavour B completion. Completion recommendation is go / go-with-risks / no-go. Residual High must be named; no fake 100% green.
5. Intake refuses to invent requirements, dates, or team names.
6. Improve loop writes dated learnings, patches the skill, changelogs semver, re-checks goldens, never lowers the bar, never stores client data.
7. Fictional product is **VaultGrid** only. Repository name is **QA Scribe**.

## Better excerpt

From the golden completion report: recommendation **go-with-risks** because RSK-EXP-01 remains High (Reporter export includes investigator notes; notes ACL deferred). Isolation and ingest integrity met on vaultgrid-2026.59.2.

## Golden re-check

- [x] Strategy hours/deadline still absent (`examples/strategy/vaultgrid-strategy.md`)
- [x] Plan still has 15 sections, dates, hours, RTM (`examples/plan/cycle-59-plan.md`)
- [x] Cases still have bypass + hash mismatch (`examples/cases/rbac-tenant-isolation.md`, `hash-chain-of-custody.md`)
- [x] Status ≠ completion (`examples/reports/`)
- [x] Prompt pack forces field layout (`examples/prompts/rbac-design-prompts.md`)

## Human gate

Skills draft. Named standards constrain headings. A QA Analyst (or QA Manager / Product Owner as named in the plan) still owns risk ranking, severity, and sign-off.
