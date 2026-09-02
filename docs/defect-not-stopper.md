---
generator: qa-scribe-report
skill_version: 1.0.0
---

# Document control

- Document type: Defect report (not a stopper)
- Standard(s) cited: IEEE 1044-style (category + severity); ISTQB incident reporting
- Product: VaultGrid (**fake data**)
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. This is the **not-a-stopper** example. Interview line: “We can ship; I still log it.”
2. Contrast with `docs/defect-stopper.md`.
3. Delete this block after paste.
4. Fake export only.
5. A QA Analyst verifies real defects on a real build.

# DEF-NS-01 — Export file name has no date (NOT A STOPPER)

| Field | Value |
| --- | --- |
| Severity | **4 — Low** |
| Priority | 3 |
| IEEE 1044 category | Documentation / interface (file name) |
| REQ / RSK | RSK-UX-01 (no Must REQ for file name) |
| Found | Exploratory export as Admin on 59.2 |
| Final | **Open** at exit — accepted leftover |

**What went wrong:** Admin Export downloaded `export.zip`. Product wanted a date in the name (e.g. `export-2026-09-24.zip`).

**Expected:** Date in the file name (if Product asks). **Actual:** `export.zip`.

**Why it is not a stopper:** Nobody saw another company’s cases. Nobody downloaded extra files. Workaround: rename the file after download.

**Interview contrast**

| | Stopper (DEF-STOP-01) | This (DEF-NS-01) |
| --- | --- | --- |
| Data leak? | Yes | No |
| Suspend cycle? | Yes | No |
| Sign go? | No until fixed | Yes, or go-with-risks for other High leftovers |

Human gate: naming bugs still get a ticket. They do not get Sev 1.
