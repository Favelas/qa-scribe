# Rubric — test strategy (`qa-scribe-strategy`)

- Document type: Generator rubric
- Standard(s) cited: ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing)
- Product: VaultGrid (golden check)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Score generated strategies before they leave `out/`.
2. `qa-scribe-improve` uses this rubric; do not silently skip failed rows.
3. Paste scores into the learning note if the output is rejected.
4. Delete this “How to use this file” block after wiki paste.
5. Never lower a row to make generation easier.

---

Fail the document if any **Must** row is No.

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| S01 | Document control present: type, standards, product, cycle/version, author role, Draft status | Must | |
| S02 | Five-line “How to use this file” present | Must | |
| S03 | Citations: ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB strategy vs plan and risk-based testing | Must | |
| S04 | Context / item under test | Must | |
| S05 | Test objectives | Must | |
| S06 | In scope and out of scope | Must | |
| S07 | Test levels: component, integration, system, acceptance/UAT | Must | |
| S08 | Test types named (functional, security/authorisation, regression, API, UAT, others as relevant) | Must | |
| S09 | Techniques pointed to 29119-4 / ISTQB; cases not written in full | Must | |
| S10 | Risk-based approach: product risk → depth and priority | Must | |
| S11 | Environments, test data strategy, tools | Must | |
| S12 | Independence and roles | Must | |
| S13 | Entry/exit at **approach** level (no sprint Friday deadline) | Must | |
| S14 | Incident/defect model (severity/priority) | Must | |
| S15 | Communication and catalogue of deliverables | Must | |
| S16 | Manual vs automated vs out of scope | Must | |
| S17 | **Zero** named hours, **zero** cycle deadline, **zero** “Cycle 59”, **zero** named testers’ hours | Must | |
| S18 | Required empty sections use `Not applicable: <reason>` | Must | |
| S19 | Human sign-off note; generator + skill version stamped | Must | |
| S20 | No real employer/client data | Must | |

Score: Must rows all Yes, or **rewrite**.
