# Improve skill — reference

Use with `.cursor/skills/qa-scribe-improve/SKILL.md`. Skill version 1.0.0.

## Learning file template

```markdown
# Learning — YYYY-MM-DD — <topic>

- Skill targeted: qa-scribe-<generator>
- Artefact: (path or “chat output”)
- Scorer: human + agent

## Failure

## Root cause

## Rule to add

## Better excerpt

## Golden re-check

- [ ] Strategy hours/deadline still absent
- [ ] Plan still has 15 sections, dates, hours, RTM
- [ ] Cases still have isolation search + role buttons
- [ ] Status ≠ completion
```

## Semver

| Change | Bump |
| --- | --- |
| New Must rule, new required heading | MINOR (1.1.0) |
| Clarification, extra example, tighter forbidden list | PATCH (1.0.1) |
| Breaking heading rename | MINOR or MAJOR; do not do this lightly — templates and goldens must move together |

## What not to patch

Do not add “if the user is in a hurry, skip RTM”. That is lowering the bar.

## Confidentiality strip

Replace any real name with a role. Replace hashes with `sha256:deadbeef…` fictional. Replace ticket IDs with `DEF-C59-…`.
