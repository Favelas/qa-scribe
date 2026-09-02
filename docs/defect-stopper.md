---
generator: qa-scribe-report
skill_version: 1.0.0
---

# Document control

- Document type: Defect report (stopper)
- Standard(s) cited: IEEE 1044-style (category + severity); ISTQB incident reporting
- Product: VaultGrid (**fake data**)
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. This is the **stopper** example. Interview line: “I do not sign go while this is open.”
2. Paste into Jira as description if you demo the format.
3. Delete this block after paste.
4. Fake title `GLOBEX-CASE-RED` only.
5. A QA Analyst verifies real defects on a real build.

# DEF-STOP-01 — Company A search shows Company B’s case (STOPPER)

| Field | Value |
| --- | --- |
| Severity | **1 — Stopper** |
| Priority | 1 |
| IEEE 1044 category | Data |
| REQ / RSK | REQ-ISO-01 / RSK-ISO-01 |
| Found | TC-ISO-001 on 2026.59.1 |
| Final | **Closed** on 2026.59.2 |

**What went wrong (plain English):** I logged in as NORTHWIND. I searched `GLOBEX-CASE-RED`. The list showed that title. Company A saw Company B’s case name.

**Expected:** Zero results.

**Actual:** One row with `GLOBEX-CASE-RED`.

**Why it is a stopper:** Another customer’s data is visible. We **suspend** the cycle. We do **not** start UAT. We do **not** sign go.

**Steps:** Log in `nw-ro` → Search → type `GLOBEX-CASE-RED` → see a row.

**Fix check:** Same steps on 59.2 → zero rows.
