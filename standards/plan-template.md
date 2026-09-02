# Test plan template

- Document type: Test Plan template
- Standard(s) cited: IEEE 829-2008 Test Plan; ISO/IEC/IEEE 29119-3 Test Plan; ISTQB test plan / entry-exit / staffing
- Product: VaultGrid (replace with intake product)
- Cycle / version: From intake (required)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Duplicate this file or let `qa-scribe-plan` fill it. IEEE 829 section order is mandatory.
2. Paste into Confluence; attach the RTM CSV.
3. Named approvers sign section 15.
4. Delete this “How to use this file” block after paste.
5. Keep every numbered section. Use `Not applicable: <reason>` rather than deleting.

---

## Document control

| Field | Value |
| --- | --- |
| Identifier | PLN-\<PRODUCT\>-\<cycle\>-\<nnn\> |
| Document type | Test Plan |
| Standard(s) cited | IEEE 829-2008 Test Plan; ISO/IEC/IEEE 29119-3 Test Plan; ISTQB test plan / entry-exit / staffing |
| Product | |
| Cycle / version | |
| Author role | Senior QA Analyst |
| Status | Draft — human sign-off required |
| Generator | qa-scribe-plan |
| Skill version | 1.0.0 |

IEEE 829-2008 headings follow in this order (wording may be slightly modernised; do not drop sections).

## 1. Test plan identifier

Full identifier, cycle name, and related strategy identifier (`STR-…`).

## 2. Introduction

Why this cycle exists, references (strategy, requirements, risks), glossary pointers. This is **this cycle**, not the multi-month approach.

## 3. Test items

Builds, services, APIs, clients, and configuration items in **this** cycle, with versions from intake.

## 4. Features to be tested

Requirements and features in scope this cycle, with REQ IDs.

## 5. Features not to be tested

Explicit deferrals with reason and residual risk IDs.

## 6. Approach

How this cycle applies the strategy: levels, types, techniques, risk order, UAT windows **if intake has regions**. Point to the strategy; do not rewrite it.

## 7. Item pass/fail criteria

When an item (build, feature, requirement) is considered passed or failed this cycle.

## 8. Suspension and resumption criteria

What stops the cycle (environment down, Crit blocker, data integrity incident in test) and what resumes it.

## 9. Test deliverables

Plan, cases, RTM, logs, status reports, completion report, defect list.

## 10. Remaining test tasks

Design remaining, data setup, environment bookings, UAT facilitation — with owners.

## 11. Environmental needs

Test and UAT environments, regions, tools, accounts, synthetic data rules.

## 12. Responsibilities / staffing and training

**Named people vs hours vs owns.** Training if a new tool or region is in play. This section makes the document a plan.

## 13. Schedule

Dates: design, execution, UAT windows per region, exit review, cycle deadline. No vague “when ready”.

## 14. Risks and contingencies

This-cycle risks: mitigation, trigger, test refs (`TC-…` / `RSK-…`).

## 15. Approvals

| Role | Name | Hours (if the person tests) | Signature | Date |
| --- | --- | --- | --- | --- |
| Senior QA Analyst (author) | | | | |
| QA Manager | | | | |
| Product Owner | | | | |
| Engineering Lead | | | | |

## Annex A — Requirements traceability matrix

Mandatory. Either embed a table or link `docs/rtm.csv` / `out/…-rtm.csv`. Columns: REQ ID, risk IDs, feature, test case IDs, owner, cycle result placeholder.

## Annex B — Named allocation table

| Name | Role | Owns | Hours this cycle | Dates |
| --- | --- | --- | --- | --- |
| | | | | |

If intake omits hours: **stop** and run `qa-scribe-intake`. Do not invent hours.
