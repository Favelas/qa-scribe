# Test case specification template

- Document type: Test Case Specification template
- Standard(s) cited: IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification; techniques ISO/IEC/IEEE 29119-4 and ISTQB
- Product: VaultGrid (replace with intake product)
- Cycle / version: From intake
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. One behaviour per case. Copy the field list below for every `TC-`.
2. Export CSV with columns: Summary, Priority, Preconditions, Steps, Expected Result, Requirement Keys, Labels, Technique.
3. Import CSV to Xray/Jira; paste Markdown into Confluence for review.
4. Delete this “How to use this file” block after paste.
5. Keep fields even when unused: `Not applicable: <reason>`.

---

## Document control (pack)

| Field | Value |
| --- | --- |
| Identifier | Case pack: area + cycle |
| Document type | Test Case Specification |
| Standard(s) cited | IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification; ISO/IEC/IEEE 29119-4 / ISTQB techniques |
| Product | |
| Cycle / version | |
| Author role | Senior QA Analyst |
| Status | Draft — human sign-off required |
| Generator | qa-scribe-cases |
| Skill version | 1.0.0 |

Xray is a **tool schema**, not a standard. Columns exist so the pack is paste-ready.

## Fields on every case (IEEE 829 / 29119-3)

| Field | Rule |
| --- | --- |
| Test case identifier | `TC-<AREA>-<nnn>` |
| Objective / test condition | One behaviour |
| Trace to requirement ID | At least one `REQ-` |
| Trace to risk ID | At least one `RSK-` |
| Preconditions / environmental needs | Role, tenant, build, region if relevant |
| Inputs | Test data, role, tenant, token/context |
| Procedure | ≤ 8 short independent steps |
| Expected outcomes | Observable; include HTTP code when API |
| Dependencies | Other TCs or `None` |
| Priority | Derived from risk level (Crit/High/Med/Low), not preference |
| Postconditions | Cleanup or `Not applicable: no durable state` |
| Technique tag(s) | EP \| BVA \| DT \| ST \| NEG \| ROLE-MATRIX \| INTEGRITY |

## Case design rules

- Risk-first: Critical/High risks before Low happy paths in the pack order.
- Happy, negative, boundary, permission-bypass, and data-integrity paths when the feature can fail that way.
- No “verify the page looks good”.
- Priority maps: Critical risk → Priority 1; High → 2; Medium → 3; Low → 4 (state the mapping in the pack).

## Skeleton

### TC-\<AREA\>-\<nnn\> — \<title\>

| Field | Content |
| --- | --- |
| Identifier | TC-\<AREA\>-\<nnn\> |
| Objective / test condition | |
| Requirement | REQ-… |
| Risk | RSK-… |
| Priority | |
| Technique | |
| Preconditions / environment | |
| Inputs | |
| Dependencies | |
| Postconditions | |

**Procedure**

1.
2.

**Expected outcomes**

-

## CSV header (Xray-oriented)

```text
Summary,Priority,Preconditions,Steps,Expected Result,Requirement Keys,Labels,Technique
```

`Summary` should start with the identifier, e.g. `TC-ISO-001 Company A search does not show Company B`.
