# Cloud migration test approach template

- Document type: Test Strategy overlay (cloud migration) — **not a cycle plan**
- Standard(s) cited: ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing)
- Product: (replace with intake product)
- Cycle / version: Program-level (not wave-bound)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Duplicate this file when a program is moving workloads to a cloud and you need a **high-level approach**, not a blank page. If intake claims **100% parity** with a legacy system, fill **§3 Parity contract** before the rest.
2. Fill only facts the program stated. Unknown stays `Unknown` or `Not applicable: <reason>`. Do not invent a vendor, RTO/RPO, or a cutover date.
3. Wave names, hours, and freeze dates belong later in `qa-scribe-plan`. This file must not become that plan.
4. Point at the risk register **and** the risk-based test matrix (`MTX-…`); copy **candidate lenses** from §12 into `qa-scribe-risks` only where the input gives a basis. §12 is **not** a substitute for `qa-scribe-matrix`.
5. Delete this block after paste into Confluence.

---

This is a **strategy overlay**. Identifier stays `STR-<PRODUCT>-<nnn>` when this file *is* the program strategy. It is not `PLN-…`.

When the user later asks Scribe to **generate** this kind of work: `qa-scribe-strategy` uses this overlay; `qa-scribe-risks` uses the migration lens in its reference. Do not start from a generic product strategy and omit dual-run / reconciliation.

## Document control

| Field | Value |
| --- | --- |
| Identifier | STR-\<PRODUCT\>-\<nnn\> |
| Document type | Test Strategy overlay (cloud migration) |
| Standard(s) cited | ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing) |
| Product | |
| Cycle / version | Program-level (not wave-bound) |
| Author role | Senior QA Analyst |
| Status | Draft — human sign-off required |
| Generator | (hand-filled from this template, or qa-scribe-strategy using this overlay) |
| Skill version | 1.1.0 |

## For the Software Testing Engineer (plain)

Keep this heading in every generated copy. Short sentences. No Scribe skill names here.

The old system is the answer key unless the program named something else.

1. Write down what “the same” means: which keys, which fields, usually **zero** difference unless they said otherwise.
2. If they also want to **clean** or **fix** old data, that is **not** 100% match — list those items separately (delta list).
3. Know the old system first (journeys, jobs, interfaces, known production defects).
4. Run the same inputs on old and new, then **diff**. If they claimed 100% of the data, compare **every in-scope row**, not a sample.
5. Then APIs and integrations. **Screens last.**
6. Practise going back **after** the new side has already written data.
7. An open **Critical** data, identity, isolation, or rollback problem means **do not cut over**.
8. In the risk table, skip rows this program never mentioned.

Dates, named people, and hours are a **later cycle plan**, not this file.

## What this file is not

Keep this heading. Do not delete it to look shorter.

- **Not a test plan.** No named people × hours, no wave calendar, no “cutover Saturday 22:00”.
- **Not a cloud architecture design.** Landing zone, account structure, and IaC stay with engineering unless intake made them a test objective.
- **Not a filled example.** No VaultGrid, no invented AWS/Azure/GCP.
- **Not a risk register or case pack.** Trace to `RSK-` / `REQ-` / later `TC-`; do not write procedures here.
- **Not a FinOps or billing review** unless intake named cost as a quality objective.
- **Not “click the new URL for a week.”** Exploratory on the target is last, after data and interface diffs.

## 1. Context (stated facts only)

| Prompt | Fill or `Unknown` / `Not applicable: <reason>` |
| --- | --- |
| What is moving (apps, data, identity, integrations) | |
| Source / **legacy** (on-prem, other cloud, mixed) | |
| Target (name the provider **only if stated**) | |
| Style if stated (rehost / replatform / refactor) | |
| Parity claim (e.g. 100% legacy = target) | Yes / No / Partial — quote intake |
| Multi-tenant / companies sharing the same site? | |

No sprint or wave dates in this section.

## 2. Test objectives (approach-level)

Measurable without a calendar. Typical prompts — keep, drop, or `Not applicable`:

1. Data: **in-scope rows** match legacy on the agreed contract (see §3). If the claim is 100% data parity, the check is **full reconciliation**, not a sample.
2. Behaviour: in-scope functions on the target match legacy (or the **named delta** list only).
3. Identity: login, roles, and tokens match the legacy contract as stated.
4. Connectivity: named integrations still exchange the same payloads/semantics.
5. Back-out: a rollback/back-out path is defined and **rehearsable as an approach** (including after the target has already written data).
6. Security / isolation: existing `RSK-ISO` / `RSK-RBAC` still hold after the move if those risks exist.

## 3. Parity contract (legacy as oracle)

If intake does **not** claim parity with a legacy system: `Not applicable: no parity claim in intake.`

**100% parity is testable only if “same” is frozen.** Treat **legacy as the oracle**: for every in-scope record, rule, and journey, the target result must match legacy on an **agreed compare key**. Anything you “fix on the way” is a **delta**, not parity.

| Prompt | Fill or `Not applicable: <reason>` |
| --- | --- |
| Oracle | Legacy / other (state which) |
| Compare key(s) per store / interface | |
| Fields in compare | |
| Tolerance | Zero unless intake named a tolerance |
| Charset, timezone, null vs empty, collation, rounding | |
| Known legacy defects | Reproduce on target (true parity) / named as deltas |
| **Parity set** vs **cleanse set** | Split if Product also wants to “clean” data — those two requirements fight until listed separately |

**In the parity set:** UI “looks the same” is not an oracle. Data and interface diffs are.

**Do not treat as parity unless intake included them:** performance, pixel layout, log-line format, generated IDs that externals do not store, cloud-only telemetry.

## 4. How we test (approach sequence)

Not a calendar. If a step has no basis: `Not applicable: <reason>`.

| Step (class) | Intent |
| --- | --- |
| Baseline / characterisation | Inventory journeys, rules, jobs, interfaces, reports, identity, **known production defects** on legacy. You cannot prove parity against an uncharacterised source. |
| Freeze compare contract | §3 signed (or explicitly Draft). |
| Dual-run / shadow | Same inputs to legacy and target; automated diff; no user traffic on target until Crit diffs are empty or only **named** deltas. |
| Three oracles, this order | **(1) Data** — counts, hashes, field-level, referential integrity, BLOBs. **(2) Rules/API** — same request, same outcome (EP, DT, ST, NEG). **(3) UI** — only where the contract is the screen (ROLE-MATRIX, isolation). UI last. |
| Interface coverage | Every **in-scope** inbound/outbound path (file, queue, API, print, email) at least once with a known payload and a diff on the other side. |
| Rollback rehearsal | Failback **after** the target has written data, on a copy — not a document-only rollback. |
| Cutover (approach) | Go/no-go: any open **Critical** parity gap is **no-go**. Named Low UI leftover may be go-with-risks. |
| Hypercare (approach) | Same diffs keep running for a period named **later in a plan**, not here. |

Do **not** start with exploratory clicking on the new URL. Do **not** sample a handful of rows and call 100% data parity done.

## 5. In scope

Systems, data classes, identity, integrations, and quality characteristics testing will address **over the program**. Not “Wave 3 in June”.

## 6. Out of scope

Explicit exclusions with reason (e.g. performance: no NFR stated; DR numbers: not supplied; other business units not in this move).

## 7. Approach phases (classes, not a schedule)

These are **kinds of work**, not dates. When a phase has a real window, that belongs in a cycle plan.

| Phase (class) | Intent | Typical test focus | Ready for the next class when |
| --- | --- | --- | --- |
| Discover / baseline | Know source behaviour and data | Inventory, agreed oracles, known defects on source | §3 contract written; Crit risks ranked |
| Land / foundation | Target environments exist as a **class** | Connectivity smoke, identity path, data path dry-run | Target class is usable for test; no Crit env blocker |
| Migrate (waves as a class) | Move in-scope slices | Dual-run diffs, reconciliation, integrations, authz | Slice meets approach exit; leftovers named |
| Cutover (approach) | Switch traffic / system of record | Go/no-go, rollback rehearsal, smoke | Crit checks pass or no-go; rollback is executable |
| Hypercare (approach) | Watch after switch | Agreed monitors, same diffs, defect triage | Exit criteria for the program slice; duration only in a later plan |

If a phase is unused: keep the row and write `Not applicable: <reason>`.

## 8. What to consider

Mark each row. Do **not** add a row the input gives no basis for and then invent a risk.

| Consider | In this program? | Notes (or `Not applicable: <reason>`) |
| --- | --- | --- |
| Data reconciliation (100% of in-scope rows if parity claim is 100%) | Yes / No / Unknown | |
| Functional parity with source | | |
| Identity / IAM / SSO / roles | | |
| Network, DNS, firewall, private connectivity, TTL/split-brain | | |
| Secrets and config (never paste real secrets here) | | |
| Environment parity (non-prod class before prod class) | | |
| Rollback / back-out after target writes | | |
| Integrations, APIs, file transfers, message queues, idempotency | | |
| Batch / scheduler / timezone of jobs | | |
| Security, authorisation, tenant isolation | | |
| Audit / logging / observability | | |
| Reports as oracles (rounding, collation, PDF) | | |
| Performance or volume | Only if an NFR is stated | |
| Residency / compliance claim | Only if intake stated the obligation | |
| Automation of **diffs** (reconciliation, API compare) before UI automation | | |

## 9. What not to put in this file

| Topic | Where it belongs instead |
| --- | --- |
| Named people, hours, wave start/end, freeze, cutover clock time | Test plan (`PLN-…`) |
| Procedure steps and expected results | Test cases (`TC-…`) |
| Ranked `RSK-` table with Stopper? | Product risk register (`qa-scribe-risks`) |
| Risk × type × depth cells | Risk-based test matrix (`MTX-…`) |
| Cloud account IDs, real URLs, real customer data | Nowhere in this repo; fictionalise or keep off-repo |
| Invented RTO/RPO, invented provider, invented “99.9%” | Intake — ask once; do not guess |
| Full framework repo layout / pipeline YAML | Later automation approach, if asked; not this overlay |

## 10. Test levels and types

| Level | Intent for a migration | Typical owners |
| --- | --- | --- |
| Component | Units and services on the **target** in isolation | Development |
| Integration | Identity, data path, APIs, queues, network path | Dev + QA |
| System | Dual-run diffs, reconciliation, authz, rollback smoke | QA |
| Acceptance / UAT | Business fitness on the target | Business + QA support |

Test types to name as in/out: functional parity, data reconciliation, security/authorisation, connectivity, rollback rehearsal, regression of in-scope, UAT. Performance only if intake has an NFR.

Techniques later in cases (do not write cases here): EP, BVA, DT, ST, NEG, ROLE-MATRIX, INTEGRITY.

## 11. Risk-based approach

Use the register (`RSK-…`) and the **risk-based test matrix** (`MTX-…` / `qa-scribe-matrix`). Do not treat §12 as that matrix. Critical/High before Low happy-path UI. Open Critical parity gap = **no-go** at cutover (approach rule).

## 12. Candidate risk lenses (not a register)

This table is a **checklist for `qa-scribe-risks`**. It is not the signed register. **Skip a row** with `Not applicable: no basis in intake` — do not pad.

When generating risks, copy only the rows that the stories/requirements actually support. Basis must still be a REQ ID or quoted fragment. Typical levels are a starting rationale, not invented percentages.

| Pattern | Risk (plain English) | Typical level | Stopper? | Test depth | Use when input mentions… |
| --- | --- | --- | --- | --- | --- |
| RSK-REC-* | Row counts or hashes differ; silent drop/duplicate | Critical | Yes — stopper | Full reconciliation, not sample | 100% parity, ETL, CDC, migrate data |
| RSK-INT-* | Field mutation (trim, encoding, decimal, date, timezone, DST, null vs empty) | Critical | Yes if money, dates, or keys | BVA on money/dates/null/charset; golden rows | Data types, money, dates, charset |
| RSK-INT-* | Attachments/BLOBs missing or hash-mismatch | High / Crit if custody | Yes if documents in scope | Hash + open sample | Files, documents, evidence |
| RSK-INT-* | IDs change and **external** refs break | Critical | Yes | Trace a foreign key end-to-end | Identity columns, UUID, downstream keys |
| RSK-INT-* | Referential orphans; soft-delete vs hard-delete mismatch | High | Yes if integrity is a ship gate | Integrity queries both sides | FK, cascade, soft delete |
| RSK-REC-* | History matches but **in-flight** work does not | Critical | Yes | Dual-run across a job boundary | Open cases, batches, freeze |
| RSK-RBAC-* | SSO/roles/tokens not 1:1; extra privilege **works** | High / Crit | Yes if disallowed action succeeds | ROLE-MATRIX + try the forbidden action | IAM, SSO, roles |
| RSK-ISO-* | Tenant isolation weaker on target | Critical | Yes — stopper | A must not see B on search **and** API **and** export | Multi-tenant, companies, shared search |
| RSK-INT-* | Integration accepted but semantics/duplicates differ | High | Yes if money/orders | Idempotency + replay NEG | Queues, retries, files, APIs |
| RSK-NET-* | DNS/TTL/allowlist split-brain (legacy and target both live) | Critical | Yes | Cutover rehearsal, both URLs, cache | DNS, cutover, IP allowlist |
| RSK-NET-* | Timeouts/retries change outcomes (double post) | High | Yes if duplicates money | NEG + duplicate detection | Latency vs old LAN |
| RSK-BAT-* | Job runs twice, never, or in the wrong timezone | High | Yes if that job is the business | One full batch cycle both sides | Cron, scheduler, night batch |
| RSK-CFG-* | Config/secrets/flags differ by environment | High | Yes if prod-class behaviour wrong | Config diff as a test; no real secrets in docs | Feature flags, parameter store |
| RSK-RBL-* | Rollback untested; target already wrote data | Critical | Yes until rehearsal succeeds | Restore/failback on a copy | Rollback, failback, back-out |
| RSK-CUT-* | Dual-write window: legacy and target diverge | Critical | Yes | Dual-write reconciliation during the window | Phased go-live, dual-write |
| RSK-EXP-* | Reports/PDF/rounding/sort differ (report is an ops/legal oracle) | High / Med | Yes if the report is the oracle | Golden reports or hash | Reports, PDF, statements |
| RSK-AUD-* | Audit incomplete or clock-skewed | Med / High | If compliance is stated | Denied action + timestamp compare | Audit, trail, timestamps |
| RSK-NFR-* | Throttling/quotas make the function fail | High | Yes if an NFR/SLA is in REQ | Volume only on the **stated** NFR | Limits, SLA, batch window |
| RSK-AUD-* | Cannot see failure (no logs/traces) | High | Yes if cutover cannot be diagnosed | Monitoring as entry | Observability, logging |
| RSK-INT-* | Backup/restore untested on target | High | Yes if restore is a ship gate | Restore drill | Backup, DR (only if stated) |
| RSK-AUD-* | Residency/PII path changed | High | If a stated obligation | Only if intake named the duty | Residency, GDPR, region |
| RSK-UX-* | UI copy/layout differs; data is equal | Low | No | One visual pass; not go/no-go | Skin, labels |
| RSK-VAL-* | Cloud **fixed** a legacy bug and the engineer fails it as a mismatch (or ships a bug because “legacy did that”) | High (process) | Until deltas are named | Delta register: must-match-bug vs must-differ | “100% parity” **and** “clean data” / “fix bugs” together |

Area codes: `REC`, `MIG`, `NET`, `BAT`, `RBL`, `CUT`, `CFG` plus existing `INT`, `RBAC`, `ISO`, `AUD`, `EXP`, `VAL`. See `standards/id-schemes.md`.

## 13. Environments, data, tools

Classes only (legacy-like test, target non-prod, target prod **as a class**). Data: synthetic or agreed anonymised copies — never production dumps in this file. Tools: only names intake supplied. Prefer automating **diffs** over UI scripts first.

## 14. Entry and exit (approach, not a weekday)

**Entry (program):** identifiable legacy and target; REQ IDs; §3 contract if parity is claimed; risks ranked; a target environment **class** is available.  
**Exit (program slice):** Critical data/identity/connectivity/rollback risks in scope have been executed; Crit diffs empty or only named deltas; rollback rehearsed; residual High named for the Product Owner.  
**Cutover rule:** open Critical parity gap → **no-go**.  
Not applicable: “testing ends Friday 17:00” or “Wave 2 is the 12th”.

## 15. Manual vs automated vs out of scope

| Stay manual (typical) | Candidate to automate **first** | Out of scope for QA authorship |
| --- | --- | --- |
| UAT, exploratory, cutover war-room judgement | Reconciliation, API/payload compare, repeatable smoke connectivity | Vendor/cloud console as a product; unit tests (dev-owned); UI automation before diffs are green |

Do not write cases or a framework design here.

## 16. Catalogue of deliverables

This overlay, risk register, **risk-based test matrix**, later case packs, later **wave** plans, status and completion reports. Prompt packs if more cases will be generated. Never drop the matrix because this overlay exists.

## 17. Approvals

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| Senior QA Analyst (author) | From intake or Not applicable: name not supplied | | |
| QA Manager | | Approach | |
| Product Owner | | Scope / residual / delta list | |

Human sign-off is mandatory. The generator does not approve. Product Owner must accept the **parity set vs cleanse/delta set** when both were requested.
