# Rubric — design prompts (`qa-scribe-prompts`)

- Document type: Generator rubric
- Standard(s) cited: Generator contract — IEEE 829 / ISO 29119-3 fields and ISO 29119-4 / ISTQB techniques
- Product: VaultGrid (golden check)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Score prompt packs before they are reused to generate cases.
2. A prompt pack that could not regenerate the golden field layout **fails**.
3. Use with `qa-scribe-improve`.
4. Delete this “How to use this file” block after wiki paste.
5. Do not treat the prompt file as signed testware.

---

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| D01 | Document control states this is a generator contract, not a test document | Must | |
| D02 | Citation sentence: output MUST conform to IEEE 829 / ISO 29119-3 fields and 29119-4 / ISTQB techniques | Must | |
| D03 | Full case field list forced | Must | |
| D04 | Risk-first ordering forced | Must | |
| D05 | Named techniques to apply | Must | |
| D06 | ID scheme specified | Must | |
| D07 | Forbidden outputs listed (vague steps, mixed features, missing expected, missing traces) | Must | |
| D08 | Five-line how-to; human still signs generated cases | Must | |
| D09 | No real employer data | Must | |

Score: Must rows all Yes, or **rewrite**.
