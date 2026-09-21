# Learnings changelog

Skill family starts at **v1.0.0**. Append only. No employer/client data.

| Date | Skill | Version | What | Why |
| --- | --- | --- | --- | --- |
| 2026-09-02 | qa-scribe-intake | 1.0.0 | Initial skill: required vs optional keys; refuse to invent dates, names, requirements | Bootstrap — generators must not fabricate staffing or REQ IDs |
| 2026-09-02 | qa-scribe-strategy | 1.0.0 | Initial skill: 29119-3 / ISTQB headings; forbid hours and cycle deadlines | Bootstrap — strategy vs plan separation |
| 2026-09-02 | qa-scribe-plan | 1.0.0 | Initial skill: IEEE 829 15 sections, RTM, named hours, dates | Bootstrap — a plan without allocation is not a plan |
| 2026-09-02 | qa-scribe-cases | 1.0.0 | Initial skill: 829 / 29119-3 fields, 29119-4 tags, Markdown+CSV | Bootstrap — risk-first executable cases |
| 2026-09-02 | qa-scribe-prompts | 1.0.0 | Initial skill: generator contract, not testware | Bootstrap — further cases stay on-standard |
| 2026-09-02 | qa-scribe-report | 1.0.0 | Initial skill: status vs completion; risk slice; no fake all-green | Bootstrap — residual High must remain visible |
| 2026-09-02 | qa-scribe-improve | 1.0.0 | Initial learning loop: score, dated note, patch, changelog, golden re-check | Bootstrap — skills improve without lowering the bar |
| 2026-09-02 | all generators | 1.0.0 | Goldens moved to `docs/`; UI isolation and role buttons; stopper vs not-a-stopper defects | Same standards, smaller human-facing set |
| 2026-09-17 | qa-scribe-risks | 1.0.0 | Initial skill: draft product risk register from requirements/user stories, Basis column, Draft-until-signed | Fills gap — no skill previously generated a risk register |
| 2026-09-21 | qa-scribe-cases | 1.1.0 | Added C14 (pack-wide EP+NEG+BVA coverage, not just conditional on isolation/RBAC) and C15 (every Critical/High risk in scope traces to a case) as Must rubric rows | Audit found a pack could pass every Must row with only happy-path cases and an uncovered Critical risk — see `learnings/2026-09-21-cases-risk-and-technique-coverage.md` |
| 2026-09-21 | tooling (all generators) | — | `.cursor/skills/` is now a generated mirror of canonical `.claude/skills/`, produced and verified by `scripts/sync-skills.sh`; a `.githooks/pre-commit` hook blocks commits where the two trees disagree | Manual dual-editing had already silently drifted (qa-scribe-improve's own patch instructions differed between the two copies, and Cursor was missing qa-scribe-risks/qa-scribe-all entirely) |
