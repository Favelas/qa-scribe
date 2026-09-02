# AGENTS.md — QA Scribe

Instructions for coding agents working in this repository.

## Load the matching skill

| User intent | Skill directory |
| --- | --- |
| Missing inputs, gather fields, incomplete YAML | `.cursor/skills/qa-scribe-intake/` |
| Test strategy, long-term approach | `.cursor/skills/qa-scribe-strategy/` |
| Test plan, cycle dates, hours, RTM | `.cursor/skills/qa-scribe-plan/` |
| Test cases, Xray, RBAC, hash mismatch | `.cursor/skills/qa-scribe-cases/` |
| Design prompts, generator contract | `.cursor/skills/qa-scribe-prompts/` |
| Status or completion report, go/no-go | `.cursor/skills/qa-scribe-report/` |
| Critique, rubric, improve the skill | `.cursor/skills/qa-scribe-improve/` |

Read `SKILL.md` first. Pull `reference.md`, `examples.md`, and `rubric.md` as needed. Keep `SKILL.md` under 500 lines; do not dump a CV into outputs.

## Cite and enforce the standard

`standards/standards-map.md` is the citation table. Copy the **exact** standard names into the document-control block. If a required heading has no data, keep the heading and write `Not applicable: <reason>`.

## Never mix strategy and plan

- Strategy: product-level approach. **No** cycle deadline, **no** named hours, **no** “Cycle 59”.
- Plan: IEEE 829 fifteen sections, dates, named allocation, RTM, approvals.

If the user asks for a hybrid, pick one document type and say so.

## Prefer editing templates and skills

Fix `standards/*-template.md` and `.cursor/skills/qa-scribe-*/` rather than one-off prose. Golden examples live in `examples/`. Generated drafts live in `out/` with `generator` + `skill_version`.

## After user corrections

Run **qa-scribe-improve**: score against that generator’s rubric, write `learnings/YYYY-MM-DD-<topic>.md`, patch the skill, append `learnings/CHANGELOG.md`, re-check goldens. Never lower the bar. Never store employer/client data in learnings.

## Promote goldens only when accepted

Do not copy `out/` into `examples/` or `ready-to-paste/` unless the user accepts the artefact as golden.

## Refuse confidential data

No real employer names, real tickets, real evidence hashes, real customer data, or work screenshots. Examples use **VaultGrid** only. VaultGrid and all sample records are **fake / fictional**. This repository is **QA Scribe**.

## Human gate

Every generated strategy, plan, case pack, prompt pack, and report remains **Draft — human sign-off required**. A QA Analyst, QA Manager, or the named approver in the plan must verify it before it is used as a control of record.
