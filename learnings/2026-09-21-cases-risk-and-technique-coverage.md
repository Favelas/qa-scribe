# Learning — cases pack could pass rubric with an uncovered Critical risk

- Date: 2026-09-21
- Generator: `qa-scribe-cases`
- Reviewer: Fabian Velasquez (via audit request, not a rejected artefact)

## Failure (what was found)

`standards/rubrics/cases.md` and both `qa-scribe-cases/rubric.md` fail-if-missing
checklists only required happy/negative/boundary/permission-bypass coverage
**conditionally** — the Must rows only fired for isolation search and RBAC
button scenarios named in intake. A case pack for a feature with no
isolation/RBAC facts could satisfy every Must row while shipping only
happy-path (EP) cases, with no NEG or BVA case anywhere in the pack.

Separately, cases trace **to** a REQ/RSK (C04), but nothing checked the
reverse direction: a Critical or High risk sitting in the risk register with
zero cases pointing back at it would not fail any rubric row. Spot-checking
the golden risk register (`docs/risks.md`) against the golden pack
(`docs/cases.md`) confirmed every Critical/High risk *is* covered there — but
that was incidental (the worked example happens to be thorough), not
something the rubric enforced.

## Root cause

Skill gap. The design rule ("Include happy, negative, boundary,
permission-bypass, and data-integrity paths when the feature can fail that
way") existed as prose in `SKILL.md` but had no corresponding scored rubric
row, so `qa-scribe-improve`'s scoring pass had nothing to check it against.
Risk coverage was designed as case→risk traceability only, never as
register→pack completeness.

## Rule to add

1. Pack-wide Must: at least one EP, one NEG, and one BVA case somewhere in
   the pack, or an explicit `Not applicable: <reason>` — enforced
   independently of whether isolation/RBAC is in scope.
2. Pack-wide Must: every Critical/High risk in scope from the risk register
   has at least one case tracing to it. Medium/Low may go uncovered without
   a note (risk-based depth, not padding).

## Better excerpt (fictional / VaultGrid-safe)

Before: a case pack for a plain "user updates profile" feature with only
`TC-PROF-001 — user saves new display name` (EP), no negative or boundary
case, would score all Must rows Yes under the old rubric.

After: same pack now also needs e.g. `TC-PROF-002 — empty display name is
rejected` (NEG/BVA) before it can score all Must rows Yes, and if
`RSK-PROF-01 (High)` — "profile update silently fails and old name is lost" —
is in the register, a case must trace to it or the pack fails C15.

## Status

Patched `standards/rubrics/cases.md` (C14, C15), `standards/case-template.md`,
`.claude/skills/qa-scribe-cases/{SKILL.md,rubric.md,reference.md}`, and the
`.cursor/skills/qa-scribe-cases/` mirror. Bumped skill to **1.1.0**. Golden
re-check: `docs/cases.md` already satisfies both new rows (EP/NEG/BVA all
present; every Critical/High risk in `docs/risks.md` — ISO-01, RBAC-01,
RBAC-02, VAL-01, RBAC-03, AUD-01 — traces to a case; only the Low
`RSK-UX-01` is uncovered, which the new rule permits). No golden edit needed.

Also fixed while auditing: `standards/id-schemes.md` was missing the `VAL`
area code already used by the golden examples and `qa-scribe-risks`
reference; `README.md` didn't mention `.claude/skills/` anywhere even though
`AGENTS.md` already documents the Claude Code port.
