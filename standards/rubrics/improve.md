# Rubric — improve / learning loop (`qa-scribe-improve`)

- Document type: Generator rubric
- Standard(s) cited: Applies the target generator’s rubric; does not replace it
- Product: VaultGrid (golden regression)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Run after a human critique of generated output.
2. Fail the improve run if it lowered a Must rule or skipped golden re-check.
3. Delete this “How to use this file” block after wiki paste.
4. Learnings files stay NDA-safe.
5. Semver bump is recorded in `learnings/CHANGELOG.md`.

---

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| M01 | Scores against the **target** generator rubric | Must | |
| M02 | Writes `learnings/YYYY-MM-DD-<topic>.md` with failure, root cause, rule, better excerpt | Must | |
| M03 | Patches the relevant skill with a **concrete** new rule | Must | |
| M04 | Appends `learnings/CHANGELOG.md` (skill, semver, what, why) | Must | |
| M05 | Re-checks golden examples still match standards | Must | |
| M06 | Does not lower the bar | Must | |
| M07 | No employer/client data in learnings | Must | |
