# Strategy skill — reference (29119-3 / ISTQB)

Use with `.cursor/skills/qa-scribe-strategy/SKILL.md`. Skill version 1.0.0.

## Strategy vs plan (do not mix)

| Strategy | Plan |
| --- | --- |
| Product, months | This cycle |
| Approach-level entry/exit | Dated gates and a deadline |
| Role titles and independence | Named people, hours, owns |
| Techniques to be used later | Which cases this cycle |
| Risk ranking method | This-cycle risks with mitigations and TC refs |

If the user says “strategy for Cycle 59 with 40 hours”, produce a plan **or** ask which document they want. Do not emit a hybrid.

## Risk → depth (default rule)

| Product risk | Coverage depth |
| --- | --- |
| Critical | Full: happy, negative, boundary, bypass, integrity as applicable; not deferred |
| High | Full functional + negative; sample only if hours are constrained **in the plan**, never by omitting from strategy |
| Medium | Representative EP/BVA; defer only via the plan’s “features not to be tested” |
| Low | Smoke / sample |

## Test levels — what to write

- **Component**: owned by development; QA audits that isolation-sensitive units (tenant filter, hash) have component tests. QA does not replace that layer in the strategy.
- **Integration**: identity token → authorisation → storage → audit pipeline.
- **System**: UI and API functional, RBAC, isolation, integrity, exports.
- **Acceptance/UAT**: regional business scripts; QA facilitates, business signs fitness.

## Defect model (strategy level)

Severity = impact on evidence integrity, isolation, or audit. Priority = when to fix relative to release **approach**, not a named sprint.

| Severity | Meaning |
| --- | --- |
| 1 Critical | Isolation break, accepted tampered evidence, audit off |
| 2 High | Authz bypass in home tenant, export over-share, custody gap |
| 3 Medium | Recoverable functional defect without data leak |
| 4 Low | Cosmetic, no security/integrity effect |

## Tools (supporting)

Jira/Xray for case repository, Confluence for signed docs, optional Postman/Playwright. QA Scribe is **documentation**, not those tools.

## Golden regression

After any skill patch, confirm `docs/strategy.md` still has **zero** named hours and **zero** cycle deadline (rubric S17).
