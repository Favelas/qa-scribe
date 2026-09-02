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

Actor in tenant A, object UUID of tenant B. Expected: **404**, empty body, audit deny in tenant A. Do not expect 403 for cross-tenant (existence oracle — RSK-ISO-02).

Home-tenant wrong role: **403**, audit deny.

## Integrity pattern (INTEGRITY / NEG / BVA)

- Hash mismatch: client SHA-256 ≠ server hash → reject, no object
- Truncated: bytes < Content-Length → reject
- Size boundaries: 0 bytes, 1 byte, max allowed size, max+1 if a limit exists in intake

## Procedure quality

Each step is an action the tester can do without reading the author’s mind. Expected results are in the **Expected outcomes** field, not hidden in steps. Maximum 8 steps.

## CSV

Header exactly:

```text
Summary,Priority,Preconditions,Steps,Expected Result,Requirement Keys,Labels,Technique
```

Requirement Keys: semicolon-separated REQ IDs. Labels: area, risk id, `qa-scribe`.

## Golden regression

RBAC pack must still contain a cross-tenant case. Hash pack must still contain mismatch. Both must trace REQ + RSK + technique.
