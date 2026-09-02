# Rubric — intake (`qa-scribe-intake`)

- Document type: Generator rubric
- Standard(s) cited: Not a 29119 document; gates the others
- Product: Any (VaultGrid in examples)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Use before any generator when fields are missing.
2. Fail the intake skill if it invented dates, names, or requirements.
3. Delete this “How to use this file” block after wiki paste.
4. Prefer one question list over a long interview.
5. Never store real evidence or customer identifiers in the YAML you write back.

---

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| I01 | Asks only for missing required keys for the requested generator | Must | |
| I02 | Refuses to invent requirements, dates, team names, hours | Must | |
| I03 | Distinguishes required vs optional keys | Must | |
| I04 | Refuses confidential/real-client evidence content | Must | |
| I05 | Points to `inputs/examples/` for shape | Must | |
