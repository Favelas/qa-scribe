# Test status report template (in-cycle)

- Document type: Test Status Report template
- Standard(s) cited: ISO/IEC/IEEE 29119-3 Test Status Report; ISTQB progress reporting
- Product: VaultGrid (replace with intake product)
- Cycle / version: From intake
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Use this flavour **during** the cycle. Do not use it as the exit summary.
2. Paste into the daily/weekly QA channel or Confluence status page.
3. QA Analyst owns the numbers; QA Manager reads residual Crit/High.
4. Delete this “How to use this file” block after paste.
5. Keep headings. `Not applicable: <reason>` if a slice has no data.

---

## Document control

| Field | Value |
| --- | --- |
| Identifier | RPT-STS-\<PRODUCT\>-\<cycle\>-\<nnn\> |
| Document type | Test Status Report (ISO/IEC/IEEE 29119-3) |
| Standard(s) cited | ISO/IEC/IEEE 29119-3 Test Status Report; ISTQB progress reporting |
| Product | |
| Cycle / version | |
| Author role | Senior QA Analyst |
| Status | Draft — human sign-off required |
| Generator | qa-scribe-report |
| Skill version | 1.0.0 |
| Report as-of | Date/time UTC from intake |

## 1. Period and scope

Reporting period, build under test, plan identifier.

## 2. Executed vs planned (by risk)

| Risk level | Planned cases | Executed | Passed | Failed | Blocked | Not run |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | | | | | | |
| High | | | | | | |
| Medium | | | | | | |
| Low | | | | | | |

Vanity totals without this slice are not sufficient.

## 3. Blocked and not-run

IDs, reason, owner, since when.

## 4. Defects opened this period

| ID | Summary | Severity | Priority | IEEE 1044 category (optional) | Status | Related RSK/REQ |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## 5. Open Critical / High

List even if “in progress”. If none: `Not applicable: no open Crit/High as of this status cut.`

## 6. Coverage gaps vs requirements

REQ IDs with no executed case this cycle, or blocked coverage.

## 7. UAT remaining by region/role

If intake has no regions: `Not applicable: intake has no regional UAT.`

## 8. Exit criteria forecast

Which approach/plan exit criteria are met, at risk, or red. This is a **forecast**, not a go/no-go.

## 9. Issues for management

Staffing, environment, data, scope change — facts, not slogans.

## 10. Human gate

Status numbers are not a ship decision. Completion report is a separate document.
