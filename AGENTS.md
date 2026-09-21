# AGENTS.md — QA Scribe

Load the matching skill: `.claude/skills/qa-scribe-*/` in Claude Code, `.cursor/skills/qa-scribe-*/` in Cursor. For "generate everything from these user stories" requests, use `qa-scribe-all`, which drafts a risk register (`qa-scribe-risks`) and confirms REQ/RSK IDs before delegating to the other generators.

## Canonical source vs mirror

`.claude/skills/` is canonical. `.cursor/skills/` is a **generated mirror** — same SKILL.md/reference.md/rubric.md format, no tool-specific content, so a byte-for-byte copy is both correct and sufficient. Never hand-edit `.cursor/skills/`; it will be overwritten by the next sync and a pre-commit hook blocks commits where the two trees disagree.

- Edit only `.claude/skills/<generator>/...`.
- Run `scripts/sync-skills.sh --apply` to regenerate `.cursor/skills/`.
- `scripts/sync-skills.sh --check` reports drift without writing anything; this is what `.githooks/pre-commit` runs on every commit.
- One-time setup after cloning this repo: `git config core.hooksPath .githooks`.

Goldens for humans: **`docs/`**. Do not mix strategy and plan. Cite `standards/standards-map.md`. Keep required headings; use `Not applicable: <reason>`.

Write new drafts to `out/` with `generator` and `skill_version`. Promote to `docs/` only when a human accepts them as golden.

After user corrections, run `qa-scribe-improve`. Never lower the bar. Never store real client data. VaultGrid and all sample records are **fake**.

UI oracles: buttons, lists, messages. Do not require HTTP codes unless intake says so.

Human gate: Draft until a QA Analyst or named approver verifies.
