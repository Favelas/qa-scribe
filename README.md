# QA Scribe

AI-assisted QA documentation accelerator: Cursor project skills, named ISO/IEEE/ISTQB templates, VaultGrid golden examples, and a skill-rewrite learning loop — so a Senior QA Analyst spends time on permissions, isolation, integrity, audit, and UAT, not on blank-page writing.

**Fabian Velasquez** — Senior QA Analyst / Senior Functional QA Specialist / Senior Software Testing Engineer.  
Work is mainly **manual functional QA** on security-sensitive enterprise SaaS: multi-tenant RBAC, customer data isolation, integrity/hashing, audit logs, API authorisation, multi-region UAT.  
Playwright and Postman are supporting skills, not this product.  
Thesis: AI drafts; named standards constrain headings and fields; a human owns risk ranking, severity, and sign-off.

| Intake | Output | Standard(s) |
| --- | --- | --- |
| Product context, risks, REQ IDs (no dates, no hours) | Test **strategy** | ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (strategy vs plan; risk-based testing) |
| Cycle id, builds, named people × hours, dates, RTM keys | Test **plan** | IEEE 829-2008 Test Plan (15 sections); ISO/IEC/IEEE 29119-3 Test Plan; ISTQB staffing / entry-exit |
| REQ + RSK + area + environment | **Test cases** (Markdown + CSV) | IEEE 829 / ISO 29119-3 Test Case Specification; ISO/IEC/IEEE 29119-4 + ISTQB techniques |
| Same traces + techniques + last TC id | **Design prompts** (generator contract) | No ISO/IEEE prompt standard. Output MUST conform to IEEE 829 / ISO 29119-3 fields and 29119-4 / ISTQB techniques |
| Flavour status or completion + counts by risk | **Status** or **completion / summary** report | 29119-3 Test Status Report **or** 29119-3 Test Completion + IEEE 829-2008 Test Summary; ISTQB residual risk vs exit criteria |

**Principle:** AI drafts. Named standards shape headings and fields. The tester owns risk and sign-off. High-priority risks get depth first.

### Read these first (no install)

- [VaultGrid test strategy](examples/strategy/vaultgrid-strategy.md)
- [Cycle 59 test plan](examples/plan/cycle-59-plan.md)
- [RBAC / tenant isolation cases](examples/cases/rbac-tenant-isolation.md)
- [Cycle 59 completion report](examples/reports/cycle-59-completion.md)

### Not this

- Not employer assets, real tickets, real evidence hashes, or customer data
- Not an autonomous tester and not TestRail/Xray as a product
- Not CoreCheck (a different project) and not a hosted SaaS tenant
- Not a multi-tenant testing platform

---

## How to use immediately

1. **Copy** a cleaned example from [`ready-to-paste/`](ready-to-paste/) into Confluence, Jira, or an email to Product.
2. **Fill intake** from [`inputs/examples/`](inputs/examples/) (or paste YAML into chat). Do not invent names, dates, hours, or requirement IDs. Optional: `python3 scripts/validate_intake.py inputs/examples/plan.cycle-59.yaml`.
3. **Ask Cursor** to use the named skill, for example: *Use `qa-scribe-plan` with this YAML* (skills live under [`.cursor/skills/`](.cursor/skills/)). Write drafts to `out/` with generator name and skill version.

Human gate: every generated file is **Draft — human sign-off required** until a QA Analyst, QA Manager, or named approver verifies it.

## Learning loop

`qa-scribe-improve` scores output against that generator’s rubric, writes `learnings/YYYY-MM-DD-<topic>.md`, patches the skill with a concrete rule, appends [`learnings/CHANGELOG.md`](learnings/CHANGELOG.md), and re-checks goldens. It never lowers the bar and never stores client data. Bootstrap: [`learnings/2026-09-02-bootstrap.md`](learnings/2026-09-02-bootstrap.md).

## Standards map (summary)

Full table: [`standards/standards-map.md`](standards/standards-map.md).

- **Strategy** — how we test the product over months. Forbidden: cycle deadline, named hours, “Cycle 59”.
- **Plan** — how this cycle ships. Required: IEEE 829 sections 1–15, dates, named allocation, RTM.
- **Cases** — one behaviour, REQ + RSK, ≤8 steps, technique tags (EP, BVA, DT, ST, NEG, ROLE-MATRIX, INTEGRITY).
- **Prompts** — contracts so the next cases still look like senior Xray work.
- **Reports** — slice by **risk**. Status ≠ completion. No fake 100% green if High residual risk remains.

## Sample plan YAML

Shape of [`inputs/examples/plan.cycle-59.yaml`](inputs/examples/plan.cycle-59.yaml) (abbreviated):

```yaml
document: plan
confidential: false
product_name: VaultGrid
cycle_id: Cycle 59
strategy_id: STR-VAULTGRID-001
people:
  - name: Maya Chen
    role: QA Analyst
    owns: RBAC and isolation execution
    hours: 40
schedule:
  execution_start: 2026-09-15
  cycle_deadline: 2026-10-03T17:00:00Z
regions: [US, UK, Brazil, Australia]
uat_windows:
  - region: US
    start: 2026-09-22
    end: 2026-09-24
    coordinator: Jordan Hale
requirements: [REQ-RBAC-01, REQ-RBAC-03, REQ-INT-03]
risks_this_cycle:
  - id: RSK-ISO-01
    mitigation: Cross-tenant cases before UAT; Severity 1 suspends
    test_refs: [TC-RBAC-003, TC-RBAC-004]
```

## Sample case — cross-tenant Read-only (ROLE-MATRIX / NEG)

Full pack: [`examples/cases/rbac-tenant-isolation.md`](examples/cases/rbac-tenant-isolation.md). Identifier **TC-RBAC-004**.

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-004 |
| Objective / test condition | A Read-only user in tenant NORTHWIND, calling GET evidence with a UUID that belongs to tenant GLOBEX, receives HTTP 404, an empty body (no metadata), and a deny audit event on NORTHWIND. |
| Requirement | REQ-RBAC-03; REQ-RBAC-01 |
| Risk | RSK-ISO-01; RSK-ISO-02 |
| Priority | 1 (Critical isolation) |
| Technique | ROLE-MATRIX; NEG |
| Preconditions | Read-only `nw-ro` on NORTHWIND. GLOBEX evidence UUID `11111111-aaaa-4bbb-8ccc-222222222222` exists. |
| Inputs | Role=Read-only; tenant=NORTHWIND; Bearer for nw-ro; GLOBEX object UUID |
| Dependencies | TC-RBAC-003 uses the same UUID (independent otherwise) |
| Postconditions | Not applicable: no durable write |

**Procedure**

1. Authenticate as `nw-ro` and capture the JWT. Confirm claim `tenant_id` is NORTHWIND and `role` is Read-only.
2. Send GET `/api/v1/evidence/11111111-aaaa-4bbb-8ccc-222222222222` with that Bearer token. Do not send a body tenant override.
3. Record HTTP status and raw body.
4. Repeat GET with a well-formed UUID that does not exist in any tenant (`99999999-ffff-4aaa-8bbb-000000000000`).
5. As NORTHWIND Admin, open audit and filter by actor `nw-ro` and the two object IDs.

**Expected outcomes**

- Both GETs return HTTP **404**.
- Bodies do not include hashes, filenames, or tenant names; they do not distinguish “exists elsewhere” from “does not exist”.
- Two audit rows on NORTHWIND with outcome=deny.
- Fail if either call returns 403, 200, or 404-with-GLOBEX metadata (existence oracle).

## Repo map

```text
.cursor/skills/     Cursor project skills (qa-scribe-intake … qa-scribe-improve)
standards/          Principles, citation map, templates, rubrics, ID schemes
product/            VaultGrid brief, requirements, RBAC matrix, risks
inputs/examples/    YAML intake for each generator
examples/           Golden strategy, plan, cases, prompts, reports, RTM
ready-to-paste/     Confluence-cleaned copies of the best goldens
learnings/          Bootstrap note, changelog, future improve notes
out/                Generated drafts (gitignored except README)
scripts/            Optional intake YAML validator
AGENTS.md           Rules for future agents
```

## NDA disclaimer

VaultGrid, NORTHWIND, GLOBEX, all hashes, UUIDs, defect IDs, and people in examples are **fictional**. Do not paste real investigation data, real customer names, or employer artefacts into this repository. If intake looks confidential, stop and fictionalise.

## Author

Fabian Velasquez — [linkedin.com/in/fabianvelasqueza](https://linkedin.com/in/fabianvelasqueza)

MIT License. See [LICENSE](LICENSE).

**All generated documentation must be verified by a QA Analyst (or the QA Manager / Product Owner named in the plan) before it is used as a control of record.**
