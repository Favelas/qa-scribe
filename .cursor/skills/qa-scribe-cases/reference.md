# Cases skill — reference (829 / 29119-3 / 29119-4)

Use with `.cursor/skills/qa-scribe-cases/SKILL.md`. Skill version 1.0.0.

## Priority mapping

| Product risk level | Case priority (Xray) |
| --- | --- |
| Critical | 1 |
| High | 2 |
| Medium | 3 |
| Low | 4 |

State this mapping once at the top of the pack.

## Permission-bypass pattern (ROLE-MATRIX / NEG)

Actor in company A, search for company B’s case title. Expected: **zero rows** on screen.

Home-company wrong role: **button hidden** (Upload/Export/Manage users). Do not require HTTP codes unless intake says so.

## Integrity pattern (when intake has validation)

- Empty required field → error, no new record (BVA / NEG)
- Incomplete upload → file not listed as complete

## Procedure quality

Each step is an action the tester can do without reading the author’s mind. Expected results are in the **Expected outcomes** field, not hidden in steps. Maximum 8 steps.

## CSV

Header exactly:

```text
Summary,Priority,Preconditions,Steps,Expected Result,Requirement Keys,Labels,Technique
```

Requirement Keys: semicolon-separated REQ IDs. Labels: area, risk id, `qa-scribe`.

## Golden regression

`docs/cases.md` must still contain isolation search (A must not see B) and role-button cases with REQ + RSK + technique.
