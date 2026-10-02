# Risk-based test matrix template

- Document type: Risk-based test matrix template
- Standard(s) cited: ISTQB risk-based testing (product risk → test depth / priority / allocation). There is no ISO/IEC/IEEE document number for this artefact — do not invent one. Technique tags: ISO/IEC/IEEE 29119-4 / ISTQB.
- Product: VaultGrid (replace with intake product)
- Cycle / version: Product-level (not cycle-bound)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Duplicate this file or let `qa-scribe-matrix` fill it from a signed (or still-draft) risk register and REQ list.
2. Paste into Confluence as the working allocation table the strategy’s risk-based approach points at.
3. QA Manager signs allocation depth; Product Owner acknowledges residual “None” / Planned gaps on Critical/High.
4. Delete this “How to use this file” block after paste.
5. If a section has no data, keep the heading and write `Not applicable: <reason>`.

---

This file is **not** the product risk register (`RSK-…` identification), **not** the cycle requirements traceability matrix (plan Annex A), and **not** the role × screen oracle (`ROLE-MATRIX`). It allocates already-identified risks to test levels, types, techniques, and coverage depth.

Required headings (keep this order).

## Document control

| Field | Value |
| --- | --- |
| Identifier | MTX-\<PRODUCT\>-\<nnn\> |
| Document type | Risk-based test matrix |
| Standard(s) cited | ISTQB risk-based testing (product risk → test depth / priority / allocation); ISO/IEC/IEEE 29119-4 / ISTQB technique tags |
| Product | |
| Cycle / version | Product-level (not cycle-bound) |
| Author role | Senior QA Analyst |
| Status | Draft — human sign-off required |
| Generator | qa-scribe-matrix |
| Skill version | 1.0.0 |
| Risk register ref | RSK-… / path |
| Requirements ref | REQ-… / path |
| Strategy ref | STR-… or `Not applicable: strategy not yet written` |
| Case pack ref | TC-… / path or `Not applicable: cases not yet designed — Case IDs stay Planned` |

## 1. Purpose and relationship

| Artefact | Job | This matrix does not |
| --- | --- | --- |
| Product risk register | Identify, rank, stopper call, named test depth | Re-score likelihood × impact |
| **This matrix** | Allocate each `RSK-` to levels, types, techniques, coverage depth, and later `TC-` IDs | Invent risks, REQ IDs, case IDs, dates, or hours |
| Test strategy § Risk-based approach | Narrative of the rule (Crit/High first) | Hold the working table |
| Cycle RTM (plan annex) | `REQ-` → `TC-` for **this cycle** | Replace product-level risk allocation |
| Role × screen matrix | Button/menu Show/Hide oracle | Allocate product risk |

## 2. Inputs

List the register, requirements, and (if present) strategy test types/levels actually used. Do not invent IDs.

- Risk register:
- Requirements:
- Strategy test types/levels in force: copy from `STR-…` or use the default set below.
- Case pack: path or `Not applicable: cases not yet designed.`

If the register is still Draft, this matrix stays Draft. Do not treat allocation as a signed control of record until the register’s levels and stopper calls are confirmed.

## 3. Coverage-depth legend

Do **not** invent numeric probability or impact scores. Copy **Level** and **Stopper?** from the register. Translate the register’s Test depth into one of these tokens:

| Token | Meaning | Typical for |
| --- | --- | --- |
| Extensive | Happy + negative + bypass/isolation (or integrity) + the extra technique the register named | Critical; High that is a stopper if it fires |
| Standard | Happy + negative (or the register’s named depth) | High / Medium |
| Cursory | One confirming or sample case | Low |
| None | Not allocated — **must** appear in §7 with a reason | Medium/Low only, with reason. Never an unexplained None on Critical |

Default mapping when the register’s Test depth is a sentence rather than a token: Critical → Extensive; High → Standard (Extensive if Stopper? is Yes); Medium → Standard; Low → Cursory.

## 4. Risk × test type matrix

Rows: every in-scope `RSK-`, Critical/High before Medium/Low. Columns: only types the strategy (or intake) actually uses — delete a column only if you write `Not applicable: <type> not in strategy/intake` in §7, not to hide a gap.

Cell: Extensive / Standard / Cursory / None.

| Risk ID | Level | Functional | Security / authz | Integrity | Audit | API | Regression | UAT | Exploratory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RSK-\<AREA\>-\<nnn\> | | | | | | | | | |

If a type is out of scope for the product: keep the column and put `None` plus a §7 reason, or replace the whole column with `Not applicable: <type> not in strategy/intake.`

## 5. Risk × test level matrix

Same rows. Levels match the strategy: component, integration, system, acceptance/UAT.

| Risk ID | Level | Component | Integration | System | Acceptance / UAT |
| --- | --- | --- | --- | --- | --- |
| RSK-\<AREA\>-\<nnn\> | | | | | |

## 6. Allocation table

One row per risk. Rank Critical/High first. Technique tags: EP \| BVA \| DT \| ST \| NEG \| ROLE-MATRIX \| INTEGRITY — only tags the risk can actually fail by.

| Risk ID | Risk (short) | Level | Stopper? | REQ IDs | Test depth (from register) | Test level(s) | Test type(s) | Technique tag(s) | Coverage depth | Case IDs or Planned | Residual if untested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RSK-\<AREA\>-\<nnn\> | | | | | | | | | | | |

Rules:

- Case IDs only from an existing pack or intake. If none: write `Planned`. Never mint a `TC-` here.
- Every Critical/High row must have at least one type **and** one level that is not None, and coverage depth Extensive or Standard.
- Residual if untested: what leftover the completion report would have to name (or `N/A — allocated`).

## 7. Coverage gaps

List every Critical/High that is Planned-only, None on a type the strategy said was in, or missing a technique the register’s Test depth required. If none: `Not applicable: every in-scope Critical/High has an allocation of Standard or Extensive.`

| Risk ID | Gap | Why it is still open | Owner to close (role, not a fabricated name) |
| --- | --- | --- | --- |
| | | | |

Immediate fail: a Critical with None across types, or no allocation row.

## 8. Ordering rule

Design and later execution follow this matrix, not UI flow: Critical/High before Medium/Low. A case pack that leads with a Low happy path while a Critical row is Planned is a fail of the pack, not a pass of coverage.

## 9. Approvals

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| Senior QA Analyst (author) | From intake or Not applicable: name not supplied | | |
| QA Manager | | Allocation depth | |
| Product Owner | | Residual None / Planned on High | |

Human sign-off is mandatory. The generator does not approve.

## Annex A — Allocation CSV (optional)

Same columns as §6, for Excel or a wiki table. If unused: `Not applicable: Markdown table in §6 is the control copy.`

```text
risk_id,risk,level,stopper,req_ids,test_depth,test_levels,test_types,techniques,coverage_depth,case_ids,residual_if_untested
```

## Worked pattern (VaultGrid, fake — delete after paste)

Illustration only. Replace with the product’s register. Do not copy these rows into a real client matrix.

| Risk ID | Risk (short) | Level | Stopper? | REQ IDs | Coverage depth | Case IDs or Planned |
| --- | --- | --- | --- | --- | --- | --- |
| RSK-ISO-01 | Company A sees Company B’s case title in search or list | Critical | Yes — stopper | REQ-ISO-01 | Extensive | TC-ISO-001 (or Planned) |
| RSK-RBAC-01 | Read-only can Upload (button shown and upload works) | High | Yes if upload succeeds | REQ-RBAC-01 | Standard | TC-RBAC-001 (or Planned) |
| RSK-UX-01 | Export file name has no date | Low | No — not a stopper | (export naming REQ if present) | Cursory | Planned |
