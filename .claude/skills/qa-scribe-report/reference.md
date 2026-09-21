# Report skill — reference

Use with `.cursor/skills/qa-scribe-report/SKILL.md`. Skill version 1.0.0.

## Flavour selection

| Intake | Document |
| --- | --- |
| `flavour: status` or in-cycle / as-of date without cycle close | RPT-STS — no final recommendation |
| `flavour: completion` or end of cycle / go-no-go | RPT-SUM — recommendation required |

If the user asks for “a report” without flavour, ask once (intake). Do not emit both in one file.

## IEEE 1044 overlay (optional)

When listing defects: category (e.g. logic, interface, data) + severity. Do not invent categories not in intake.

## Residual risk language (completion)

Name the RSK ID, what was not closed, compensating control, owner, follow-up cycle. “Acceptable risk” without an ID is a fail.

## Golden regression

Status example must **not** contain a signed go/no-go. Completion example must recommend **go-with-risks** or **no-go** with at least one leftover High — not all-green.
