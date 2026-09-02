# Learning — 2026-09-02 — bootstrap (updated 2026-09-02 UI simplify)

- Skill targeted: all `qa-scribe-*` (family v1.0.0)
- Artefact: repository design

## Failure

Not applicable for original bootstrap. Later: goldens were too API-heavy for a UI-first Senior QA walk.

## Root cause

HTTP 404 and hashing are real techniques but are the wrong memorisation load for this portfolio.

## Rule to add

Goldens live in **`docs/`**. Isolation oracle is **on-screen search**: Company A must not see Company B’s title. Cases stay IEEE 829 fields. Plan keeps 15 sections, hours, deadline, RTM. Completion names stopper vs not-a-stopper. Never lower the bar.

## Better excerpt

TC-ISO-001: search `GLOBEX-CASE-RED` as NORTHWIND → zero rows. Fail = DEF-STOP-01.

## Golden re-check

- [x] Strategy: no named hours, no cycle deadline (`docs/strategy.md`)
- [x] Plan: IEEE 829 15 sections, deadline, hours, RTM (`docs/plan.md`)
- [x] Isolation UI case + role buttons (`docs/cases.md`)
- [x] Status ≠ completion
- [x] Stopper vs not-a-stopper defects
