# Rubric — test plan (`qa-scribe-plan`)

- Document type: Generator rubric
- Standard(s) cited: IEEE 829-2008 Test Plan; ISO/IEC/IEEE 29119-3 Test Plan; ISTQB test plan / entry-exit / staffing
- Product: VaultGrid (golden check)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Score generated plans before they leave `out/`.
2. A plan without dates, named allocation, or RTM is not a plan — fail it.
3. Use with `qa-scribe-improve`.
4. Delete this “How to use this file” block after wiki paste.
5. Never drop an IEEE 829 section to shorten the file.

---

Fail if any **Must** row is No.

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| P01 | Document control + five-line how-to | Must | |
| P02 | Citations: IEEE 829-2008 Test Plan; ISO/IEC/IEEE 29119-3 Test Plan; ISTQB plan / entry-exit / staffing | Must | |
| P03 | Section 1 Test plan identifier | Must | |
| P04 | Section 2 Introduction | Must | |
| P05 | Section 3 Test items | Must | |
| P06 | Section 4 Features to be tested | Must | |
| P07 | Section 5 Features not to be tested | Must | |
| P08 | Section 6 Approach | Must | |
| P09 | Section 7 Item pass/fail criteria | Must | |
| P10 | Section 8 Suspension and resumption criteria | Must | |
| P11 | Section 9 Test deliverables | Must | |
| P12 | Section 10 Remaining test tasks | Must | |
| P13 | Section 11 Environmental needs | Must | |
| P14 | Section 12 Responsibilities / staffing and training — **named people vs hours vs owns** | Must | |
| P15 | Section 13 Schedule — **dates and cycle deadline** | Must | |
| P16 | Section 14 Risks and contingencies — this-cycle risks, mitigation, test refs | Must | |
| P17 | Section 15 Approvals | Must | |
| P18 | RTM present (table or CSV) with REQ → TC | Must | |
| P19 | UAT windows per region **if** intake has regions | Must | |
| P20 | No strategy/plan mix-up (approach points at strategy; does not omit dates) | Must | |
| P21 | No invented names, dates, or hours | Must | |
| P22 | Human sign-off; generator + version stamp | Must | |
| P23 | No real employer/client data | Must | |

Score: Must rows all Yes, or **rewrite**.
