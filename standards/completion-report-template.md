# Test completion / test summary report template (end of cycle)

- Document type: Test Completion Report / Test Summary Report template
- Standard(s) cited: ISO/IEC/IEEE 29119-3 Test Completion Report; IEEE 829-2008 Test Summary Report; ISTQB summary reporting; residual risk vs exit criteria
- Product: VaultGrid (replace with intake product)
- Cycle / version: From intake
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Use this flavour **after** planned execution (or on a formal stop). Not for mid-cycle status.
2. Paste into Confluence; send the recommendation section to Product and QA Manager.
3. Approvers sign go / go-with-risks / no-go. The generator does not.
4. Delete this “How to use this file” block after paste.
5. Keep IEEE 829 summary headings. Never publish all-green if High residual risk remains.

---

## Document control

| Field | Value |
| --- | --- |
| Identifier | RPT-SUM-\<PRODUCT\>-\<cycle\>-\<nnn\> |
| Document type | Test Completion Report (29119-3) / Test Summary Report (IEEE 829-2008) |
| Standard(s) cited | ISO/IEC/IEEE 29119-3 Test Completion Report; IEEE 829-2008 Test Summary Report; ISTQB summary reporting; residual risk vs exit criteria |
| Product | |
| Cycle / version | |
| Author role | Senior QA Analyst |
| Status | Draft — human sign-off required |
| Generator | qa-scribe-report |
| Skill version | 1.0.0 |

IEEE 829-2008 Test Summary content follows.

## 1. Identifier

Report ID, plan ID, strategy ID, cycle, build(s).

## 2. Summary of testing performed

Levels, types, regions, what was actually run.

## 3. Variances (plan vs actual)

Scope, schedule, hours, environment, skipped cases — with reasons.

## 4. Comprehensive assessment (coverage)

Coverage vs items, features, requirements, and **risks**. Gaps named by REQ and RSK.

## 5. Summary of results

Pass / fail / blocked / not-run, sliced by risk. Open Crit/High listed.

## 6. Evaluation

What passed, what failed, **remaining risk** against exit criteria. If a High remains, say so.

## 7. Summary of activities / effort vs plan

Hours from intake vs actual if hours exist. If no hours in intake: `Not applicable: plan intake contained no hours.`

## 8. Defect summary

Optional IEEE 1044: category + severity. Open vs closed.

## 9. UAT remaining or completed by region/role

If no regions: `Not applicable: intake has no regional UAT.`

## 10. Approvals and recommendation

| Recommendation | When to use |
| --- | --- |
| Go | Exit criteria met; no open Crit/High product risk in scope |
| Go-with-risks | Exit criteria mostly met; named High residual with owner and compensating control |
| No-go | Crit open, or High without accepted control, or coverage of Crit risks incomplete |

| Role | Name | Recommendation | Signature | Date |
| --- | --- | --- | --- | --- |
| Senior QA Analyst | | | | |
| QA Manager | | | | |
| Product Owner | | | | |

Human sign-off is mandatory.
