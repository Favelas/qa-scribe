# Rubric — test cases (`qa-scribe-cases`)

- Document type: Generator rubric
- Standard(s) cited: IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification; ISO/IEC/IEEE 29119-4 / ISTQB
- Product: VaultGrid (golden check)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Score each pack; spot-check every Critical/High case.
2. Packs that omit permission-bypass or hash-mismatch when those risks are in intake **fail**.
3. Use with `qa-scribe-improve`.
4. Delete this “How to use this file” block after wiki paste.
5. Do not accept “verify UI” as a case.

---

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| C01 | Document control + five-line how-to on the pack | Must | |
| C02 | Citations: IEEE 829 and 29119-3 case specification; 29119-4 / ISTQB techniques | Must | |
| C03 | Every case has TC-\<AREA\>-\<nnn\> | Must | |
| C04 | Every case has objective, REQ, RSK, preconditions, inputs, ≤8 steps, expected, dependencies, priority, technique | Must | |
| C05 | Priority derived from risk | Must | |
| C06 | Risk-first ordering in the pack | Must | |
| C07 | One behaviour per case | Must | |
| C08 | Markdown **and** CSV with Xray-oriented columns | Must | |
| C09 | Permission-bypass / cross-tenant case present when isolation/RBAC is in scope | Must | |
| C10 | Hash-mismatch or truncated-file case present when integrity is in scope | Must | |
| C11 | Technique tags from the allowed set only | Must | |
| C12 | No invented REQ/RSK; no real hashes or customer data | Must | |
| C13 | Human sign-off; generator + version | Must | |

Score: Must rows all Yes, or **rewrite**.
