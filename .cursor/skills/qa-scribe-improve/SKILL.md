---
name: qa-scribe-improve
description: Scores generated QA Scribe output against the matching rubric, writes a dated learning note, patches the generator skill with a concrete rule, and re-checks golden examples. Use when the user critiques a strategy, plan, cases, prompts, or report, fills a rubric, provides a corrected document, or asks to improve, learn, or rewrite the skill.
---

# QA Scribe — learning loop

Version: **1.0.0**

Take generated output + human critique and/or filled rubric + optional corrected document. Raise the bar. Never lower it.

## When this skill applies

Trigger terms: improve the skill, learning loop, rubric score, rewrite the generator, we rejected this plan/strategy/cases/report, add a rule.

## Human still signs

Learnings are engineering notes for the skills. They are not signed testware. Golden promotion to `examples/` still needs explicit human acceptance.

## Workflow

1. Identify the **target generator** (strategy | plan | cases | prompts | report). Load that skill’s `rubric.md` and `standards/rubrics/<generator>.md`.
2. Score the artefact. Record Must fails.
3. Write dated learning: `learnings/YYYY-MM-DD-<topic>.md` with:
   - Failure (what the human saw)
   - Root cause (skill gap vs user error vs missing intake)
   - Rule to add (one concrete sentence the skill can enforce)
   - Better excerpt (NDA-safe, VaultGrid or fictional)
4. **PATCH** the relevant skill (`SKILL.md` and/or `reference.md`) with that rule. Bump patch or minor version in the skill header (semver). Start family was **v1.0.0**.
5. Append `learnings/CHANGELOG.md`: skill, semver bump, what, why.
6. Re-check golden examples so the rewrite did not destroy the standard (see checklist below).
7. Stamp future outputs with generator name + new skill version.

## Golden re-check (mandatory)

| Generator | Must still be true after the patch |
| --- | --- |
| strategy | `examples/strategy/vaultgrid-strategy.md` — zero named hours, zero cycle deadline |
| plan | `examples/plan/cycle-59-plan.md` — IEEE 829 15 sections, deadline, named allocation, RTM, approvals |
| cases | Permission-bypass and hash-mismatch still present with REQ + RSK + technique |
| prompts | Field layout still forced |
| report | Status ≠ completion; completion is go-with-risks or no-go with leftover High |

## Rules that never change

- Never lower the bar to make generation easier
- Never store employer/client data in learnings (no real tickets, hashes, customer names)
- Never mix strategy and plan to “fix” a critique
- Prefer editing templates/skills over one-off prose in `out/`

## Fail-if-missing

`standards/rubrics/improve.md`. Immediate fail: critique filed with no skill patch; changelog skipped; goldens not re-read.

## Pointers

Bootstrap: `learnings/2026-09-02-bootstrap.md`  
Changelog: `learnings/CHANGELOG.md`  
Reference: `reference.md`
