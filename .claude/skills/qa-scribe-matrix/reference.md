# Matrix skill — reference (ISTQB risk-based testing)

Use with `.claude/skills/qa-scribe-matrix/SKILL.md`. Skill version 1.0.0.

## What this file is for

The register answers “what could go wrong?” This matrix answers “what testing, at what depth, against which of those risks?” Strategy § Risk-based approach stays narrative. Cases stay executable. The cycle RTM stays REQ → TC for one plan.

## Depth tokens (do not invent numbers)

| Register Level | Default token | Escalate to Extensive when |
| --- | --- | --- |
| Critical | Extensive | Always (do not drop) |
| High | Standard | Stopper? is Yes / Yes if the disallowed action succeeds |
| Medium | Standard | Register Test depth names bypass, isolation, or integrity |
| Low | Cursory | Never escalate just to look thorough |

None is allowed on Medium/Low with a §7 reason (e.g. “UAT not in strategy”). None on Critical is a fail.

## Column discipline

Delete or `Not applicable` a test-type column only when strategy/intake excludes that type. Do not invent an Integrity column because the template listed it if the register has no integrity risk and intake never mentioned files/hashes.

## Case ID discipline

| Situation | Cell |
| --- | --- |
| Intake or pack lists `TC-ISO-001` against `RSK-ISO-01` | `TC-ISO-001` |
| Cases not designed yet | `Planned` |
| User said “make up the case IDs” | Refuse. Leave Planned |

## Disambiguation (wrong artefact)

| User said | Actual artefact | Skill |
| --- | --- | --- |
| Risk register / what could go wrong | Product risk register | `qa-scribe-risks` |
| Traceability / RTM / REQ to cases this sprint | Plan Annex A | `qa-scribe-plan` |
| Who sees Upload / Export | Role × screen matrix | Cases + `docs/roles.md` |
| Allocate coverage to each RSK | **This matrix** | `qa-scribe-matrix` |
