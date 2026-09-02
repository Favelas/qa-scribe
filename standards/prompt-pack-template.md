# Design prompt pack template

- Document type: Generator contract (not a test document)
- Standard(s) cited: Output MUST conform to IEEE 829 / ISO 29119-3 test case fields and ISO 29119-4 / ISTQB techniques. This file is a generator contract, not a test document.
- Product: VaultGrid (replace with intake product)
- Cycle / version: From intake
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste a prompt block into Cursor (or another agent) when generating **additional** cases for the same area.
2. Do not send this file to Xray as testware.
3. A Senior QA Analyst reviews generated cases against the case rubric before import.
4. Delete this “How to use this file” block after paste into a team prompt library.
5. Keep every constraint section. If a constraint does not apply: `Not applicable: <reason>`.

---

## Document control

| Field | Value |
| --- | --- |
| Identifier | PRM-\<AREA\>-\<nnn\> |
| Document type | Design prompt pack (generator contract) |
| Standard(s) cited | Output MUST conform to IEEE 829 / ISO 29119-3 test case fields and ISO 29119-4 / ISTQB techniques. This file is a generator contract, not a test document. |
| Product | |
| Cycle / version | |
| Author role | Senior QA Analyst |
| Status | Draft — human sign-off required |
| Generator | qa-scribe-prompts |
| Skill version | 1.0.0 |

## 1. Mission

Generate test cases for: \<area / requirements\>. Order by product risk, not by UI flow.

## 2. Mandatory case fields

Every case must include: identifier `TC-<AREA>-<nnn>`; objective; REQ trace; RSK trace; preconditions; inputs (role, tenant, token/context, data); procedure ≤ 8 steps; expected outcomes; dependencies; priority from risk; postconditions; technique tags.

## 3. Techniques to apply

Name the 29119-4 / ISTQB techniques that **must** appear in the pack (EP, BVA, DT, ST, NEG, ROLE-MATRIX, INTEGRITY).

## 4. ID scheme

Next ID after: \<last TC\>. Area code: \<AREA\>. Do not reuse IDs.

## 5. Risk-first ordering

List RSK IDs in the order cases must be produced. Critical and High before Low.

## 6. Forbidden outputs

- Vague steps (“click around”, “verify it looks good”)
- Mixed features in one case
- Missing expected result
- Missing requirement or risk trace
- Invented REQ/RSK IDs, dates, or people
- Strategy or plan prose inside the case pack
- Real customer data, real hashes, real ticket keys

## 7. Layout

Markdown tables plus CSV with: Summary, Priority, Preconditions, Steps, Expected Result, Requirement Keys, Labels, Technique.

## 8. Human gate

Generated cases remain Draft until a named QA Analyst or QA Manager signs. The prompt does not authorise execution.
