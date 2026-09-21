---
name: qa-scribe-all
description: Takes pasted requirements or user stories and drives the full QA Scribe set in one pass — risk register, strategy, and test cases automatically, plan and report when the extra facts exist. Use when the user pastes user stories/requirements and wants QA documentation generated, asks to "generate everything", "create all the docs", "run qa scribe on this", or wants a plan/test-case/risk/strategy bundle from one input instead of running each generator by hand.
---

# QA Scribe — generate everything

Version: **1.0.0**

Single entry point: paste requirements/user stories once, get as much of the QA Scribe document set as the input actually supports — instead of running `qa-scribe-intake` and five generators by hand. This skill does not duplicate any generator's rules; for every document it produces, it **reads** that generator's own `SKILL.md` (+ `reference.md` + `rubric.md`) with the Read tool and follows those rules exactly. This file is the coordinator, not a second copy of the rulebook.

## When this skill applies

Trigger terms: generate everything, create all the docs, run qa scribe on this, give me strategy/plan/cases/risks from these stories, full QA Scribe bundle.

## Human still signs

Nothing this skill writes is signed testware. Every output keeps the Draft status and generator/skill_version stamp its own skill defines. This skill's own extra step — proposing REQ/RSK IDs from freeform text — is risk/requirement **analysis**, allowed under `qa-scribe-risks`' rules; it is never allowed to invent hours, dates, named people, or execution counts. Those stay gated exactly as `qa-scribe-intake` defines them.

## Step 1 — Take the input as given

Accept whatever the user pasted: user stories, a requirements list, a feature description, a ticket dump. Do not ask them to reformat it into YAML first.

## Step 2 — Propose IDs, don't invent facts

1. Derive a candidate `product_name` from the input (ask in one line if genuinely absent).
2. Split the input into distinct requirements and assign each a candidate `REQ-<AREA>-nn` (area codes: `standards/id-schemes.md`; invent a new short area code only if none fits).
3. Apply `.claude/skills/qa-scribe-risks/SKILL.md`'s inference rules to draft candidate `RSK-<AREA>-nn` risks from those requirements.
4. Show the user a single short list — product name, REQ list, RSK list with level + one-line basis — and ask them to confirm or correct it **in one message**, not a form. Proceed with their edits; do not re-derive from scratch after confirmation.

This list becomes the shared intake (`requirements_ref` / `risk_register_ref` equivalent) every downstream generator in this run will use — mint no further REQ/RSK IDs later in the same run without going back through this confirmed list.

## Step 3 — Ask exactly one scope question

Ask once, via AskUserQuestion (or equivalent), before generating anything:

- **All applicable now (recommended)** — Risk Register + Strategy + Test Cases generate immediately from the confirmed IDs; Plan and Report are attempted too but will report as pending if their required facts (below) aren't supplied.
- **Let me pick specific ones** — offer Risk Register / Strategy / Test Cases / Plan / Report / Prompts as a multi-select.

Do not ask this question more than once per run. If the user's original message already said which ones they want (or said "just cases" etc.), skip the question and honor that.

## Step 4 — What "all" actually produces

| Doc | Needs beyond the confirmed REQ/RSK list | Runs in "all" without extra asking? |
| --- | --- | --- |
| Risk register | Nothing else | Yes |
| Strategy | Scope/objectives (in/out of scope) — ask one follow-up if not inferable from the input | Yes |
| Test cases | `area`, next TC id (default `001` if this is a fresh area), environment/precondition facts — ask one follow-up if missing | Yes |
| Plan | Named people + hours, a real schedule/deadline | Only if the user supplies these when asked; otherwise reported as pending, never fabricated |
| Report | `plan_id` from an already-generated plan, plus real execution counts | Only if the user has execution results; otherwise reported as pending |
| Prompts pack | Same traces as cases, plus techniques to force | Opt-in only — not part of "all" by default, since it is a generator-contract for future cases, not a paperwork deliverable |

When Plan or Report is in scope but its extra facts are missing, ask for them once, plainly: "Plan needs named people+hours and a deadline — do you have those, or should I skip Plan for now?" Never invent a placeholder person, hour count, or date to unblock it.

## Step 5 — Generate, one generator at a time, by reading its own rules

For each doc type in scope, in this order — Risk register → Strategy → Test cases → Plan → Report → Prompts (skip any not in scope or missing required facts):

1. Read `.claude/skills/qa-scribe-<type>/SKILL.md`, its `reference.md`, and its `rubric.md`.
2. Follow those files' required headings, fail-if-missing conditions, and output path exactly, using the confirmed IDs from Step 2 and any facts gathered in Step 4.
3. Write the result to the exact `out/` path that skill's own SKILL.md specifies (e.g. `out/RSK-<PRODUCT>-register.md`, `out/STR-<PRODUCT>-001.md`, `out/TC-<AREA>-pack.md` + `.csv`, `out/PLN-<PRODUCT>-<cycle>-001.md` + `out/<cycle>-rtm.csv`, `out/RPT-STS-...md` or `out/RPT-SUM-...md`).
4. Self-check against that generator's own `rubric.md` before moving to the next doc; fix Must-fails before writing the file, don't hand the user a known-failing draft.

## Step 6 — Status summary

End every run with:

- A table of what was written and to which `out/` path.
- What was skipped and exactly what fact is blocking it (e.g. "Plan — skipped, needs named people+hours and a deadline").
- The standing reminder: everything in `out/` is a draft; nothing is promoted to `docs/` without explicit human acceptance (`out/README.md`).

## Fail-if-missing

Immediate fail for this skill specifically: generating a doc type without reading its own SKILL.md/rubric first; asking the scope question more than once; fabricating any Plan/Report fact instead of reporting it pending; padding the risk register or cases with content the confirmed ID list doesn't support.

## After user corrections

Route the correction to the specific generator that produced the flawed doc, then run `qa-scribe-improve` against that generator — this skill itself has no rubric of its own to patch beyond the "Fail-if-missing" list above.
