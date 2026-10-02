# Rubric — risk-based test matrix (`qa-scribe-matrix`)

- Document type: Generator rubric
- Standard(s) cited: ISTQB risk-based testing; ISO/IEC/IEEE 29119-4 / ISTQB technique tags
- Product: from intake (layout check: `standards/risk-based-test-matrix-template.md`)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Score each matrix before it leaves `out/`.
2. A matrix that invents `TC-` IDs, probability numbers, or a new `RSK-` not on the register **fails**.
3. Use with `qa-scribe-improve`.
4. Delete this "How to use this file" block after wiki paste.
5. Never drop a required heading to make the table look complete.

---

Fail the document if any **Must** row is No.

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| M01 | Document control + five-line how-to | Must | |
| M02 | Citation: ISTQB risk-based testing; no invented ISO/IEEE number for this artefact; 29119-4 / ISTQB technique tags named | Must | |
| M03 | Identifier `MTX-<PRODUCT>-<nnn>` | Must | |
| M04 | Purpose section distinguishes register vs this matrix vs cycle RTM vs role × screen matrix | Must | |
| M05 | Inputs name the risk register and requirements; Draft if the register is still Draft | Must | |
| M06 | Coverage-depth legend present; tokens only Extensive / Standard / Cursory / None | Must | |
| M07 | No invented numeric probability/impact score | Must | |
| M08 | Risk × test type matrix: every in-scope RSK; Critical/High before Medium/Low | Must | |
| M09 | Risk × test level matrix: component, integration, system, acceptance/UAT (or `Not applicable: <reason>` per unused level) | Must | |
| M10 | Allocation table: every risk has Level, Stopper?, REQ IDs, techniques, coverage depth, Case IDs or Planned | Must | |
| M11 | Case IDs are from an existing pack/intake or the cell says Planned — no minted `TC-` | Must | |
| M12 | Every Critical/High has Standard or Extensive allocation (not None across types) | Must | |
| M13 | Coverage gaps section present; unexplained None on Critical is a fail | Must | |
| M14 | Ordering rule: Critical/High before Medium/Low | Must | |
| M15 | Approvals table; generator + skill version stamped | Must | |
| M16 | Product-level: **zero** named hours, **zero** cycle deadline, **zero** sprint calendar | Must | |
| M17 | Empty sections use `Not applicable: <reason>` | Must | |
| M18 | No real employer/client data | Must | |
| M19 | Not a substitute for the risk register, cycle RTM, or role × screen matrix | Must | |

Score: Must rows all Yes, or **rewrite**.
