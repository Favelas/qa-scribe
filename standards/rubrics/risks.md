# Rubric — risk register (`qa-scribe-risks`)

- Document type: Generator rubric
- Standard(s) cited: ISTQB risk-based testing
- Product: from intake (golden check: `docs/risks.md` shape)
- Cycle / version: Skill v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Score each register; spot-check every Critical/High risk's Basis column.
2. A register with a risk that has no Basis, or that pads in generic filler categories the input never supported, **fails**.
3. Use with `qa-scribe-improve`.
4. Delete this "How to use this file" block after wiki paste.
5. Do not accept a bare adjective ("High") with no one-clause rationale as a Level.

---

| ID | Check | Must? | Pass? |
| --- | --- | --- | --- |
| R01 | Document control + five-line how-to on the register | Must | |
| R02 | Citation: ISTQB risk-based testing (no invented ISO/IEEE number) | Must | |
| R03 | Every risk has `RSK-<AREA>-<nnn>` | Must | |
| R04 | Every risk has Basis (REQ ID or quoted/paraphrased input fragment) | Must | |
| R05 | Every risk has Level with a one-clause rationale, not a bare adjective | Must | |
| R06 | Every risk has Stopper? using the exact convention (`Yes — stopper` / `Yes if <condition>` / `No — but named leftover` / `No`) | Must | |
| R07 | Every risk has Test depth | Must | |
| R08 | Critical/High ranked before Medium/Low | Must | |
| R09 | No invented probability/impact number with no stated basis | Must | |
| R10 | No generic filler risk for a category the input gave no basis for | Must | |
| R11 | Register marked Draft / candidate, not presented as confirmed fact | Must | |
| R12 | Human sign-off note present; generator + version stamped | Must | |

Score: Must rows all Yes, or **rewrite**.
