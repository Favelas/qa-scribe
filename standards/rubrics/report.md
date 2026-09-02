# Rubric — metrics / report (`qa-scribe-report`)

- Document type: Generator rubric
- Standard(s) cited: IEEE 829-2008 Test Summary Report; ISO/IEC/IEEE 29119-3 Test Status Report and Test Completion Report; ISTQB progress and summary reporting
- Product: VaultGrid (golden check)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Confirm flavour A vs B matches intake (`status` vs `completion`).
2. Fail all-green completion reports that leave High residual risk unnamed.
3. Use with `qa-scribe-improve`.
4. Delete this “How to use this file” block after wiki paste.
5. Do not merge status and completion into one file.

---

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| R01 | Document control + five-line how-to | Must | |
| R02 | Flavour labelled: Test Status Report **or** Test Completion / Summary Report | Must | |
| R03 | Status (A): executed vs planned, blocked, not-run, defects opened, exit forecast — **not** a final go/no-go | Must if A | |
| R04 | Completion (B): IEEE 829 identifier, summary, variances, coverage assessment, results, evaluation, effort vs plan if hours exist, approvals + recommendation | Must if B | |
| R05 | Metrics sliced by **risk** | Must | |
| R06 | Open Crit/High listed (or explicit N/A) | Must | |
| R07 | Coverage gaps vs requirements | Must | |
| R08 | UAT remaining/completed by region/role if intake has regions | Must | |
| R09 | Completion recommendation is go / go-with-risks / no-go with owners | Must if B | |
| R10 | Not a fake 100% green dashboard if residual High remains | Must | |
| R11 | Status ≠ completion (no mixed document) | Must | |
| R12 | Human sign-off; generator + version; no real employer data | Must | |

Score: Must rows all Yes, or **rewrite**.
