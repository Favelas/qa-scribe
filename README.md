# QA Scribe

AI-assisted QA documentation accelerator: Cursor project skills, named ISO/IEEE/ISTQB templates, VaultGrid golden examples, and a skill-rewrite learning loop — so a Senior QA Analyst spends time on permissions, isolation, integrity, audit, and UAT, not on blank-page writing.

> **Fake product. Fake data.**  
> **VaultGrid** is a fictional digital-evidence vault built only for this portfolio. Tenants (NORTHWIND, GLOBEX), users, roles, cases, files, hashes, UUIDs, defect IDs, hours, and dates are **invented examples**. Nothing here is a real investigation, a real customer, or a real employer system. Do not treat it as production evidence.

Goldens are stamped **Draft — human sign-off required** on purpose. AI drafts; a named QA role still signs. That mark is the control, not an unfinished repository.

**Fabian Velasquez** — Senior QA Analyst / Senior Functional QA Specialist / Senior Software Testing Engineer.  
Work is mainly **manual functional QA** on security-sensitive enterprise SaaS: multi-tenant RBAC, customer data isolation, integrity/hashing, audit logs, API authorisation, multi-region UAT.  
Playwright and Postman are supporting skills, not this product.  
Thesis: AI drafts; named standards constrain headings and fields; a human owns risk ranking, severity, and sign-off.

> **How a recruiter should walk it (60 seconds)**  
> These five files *are* the portfolio. Everything else in the repo supports them.
>
> 1. **[README.md](README.md)** — who you are and the five generators.  
> 2. **[examples/strategy/](examples/strategy/)** — you know strategy ≠ plan.  
> 3. **[examples/plan/](examples/plan/)** — you can staff a cycle.  
> 4. **[examples/cases/rbac-tenant-isolation.md](examples/cases/rbac-tenant-isolation.md)** — you design isolation / negative cases.  
> 5. **[examples/reports/cycle-59-completion.md](examples/reports/cycle-59-completion.md)** — you report residual risk, not a fake green dashboard.
>
> One case if you only open one: **TC-RBAC-004** (cross-tenant 404) in this README.
>
> Two more minutes (interview plus): **[defect write-up DEF-C59-004](examples/defects/def-c59-004-truncated-ingest.md)** (how a High integrity bug is reported) and **[US UAT script](examples/uat/us-uat-script.md)** (business-facing acceptance). Both use fake data only.

| Intake | Output | Standard(s) |
| --- | --- | --- |
| Product context, risks, REQ IDs (no dates, no hours) | Test **strategy** | ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (strategy vs plan; risk-based testing) |
| Cycle id, builds, named people × hours, dates, RTM keys | Test **plan** | IEEE 829-2008 Test Plan (15 sections); ISO/IEC/IEEE 29119-3 Test Plan; ISTQB staffing / entry-exit |
| REQ + RSK + area + environment | **Test cases** (Markdown + CSV) | IEEE 829 / ISO 29119-3 Test Case Specification; ISO/IEC/IEEE 29119-4 + ISTQB techniques |
| Same traces + techniques + last TC id | **Design prompts** (generator contract) | No ISO/IEEE prompt standard. Output MUST conform to IEEE 829 / ISO 29119-3 fields and 29119-4 / ISTQB techniques |
| Flavour status or completion + counts by risk | **Status** or **completion / summary** report | 29119-3 Test Status Report **or** 29119-3 Test Completion + IEEE 829-2008 Test Summary; ISTQB residual risk vs exit criteria |

**Principle:** AI drafts. Named standards shape headings and fields. The tester owns risk and sign-off. High-priority risks get depth first.

### Not this

- Not a real product, real investigation, or real customer dataset — **VaultGrid and all sample data are fake**
- Not employer assets, real tickets, real evidence hashes, or production URLs
- Not an autonomous tester and not TestRail/Xray as a product
- Not a hosted SaaS or a multi-tenant testing platform

---

## How to use immediately (VaultGrid examples)

1. **Copy** a cleaned example from [`ready-to-paste/`](ready-to-paste/) into Confluence, Jira, or an email to Product.
2. **Fill intake** from [`inputs/examples/`](inputs/examples/) (or paste YAML into chat). Do not invent names, dates, hours, or requirement IDs. Optional: `python3 scripts/validate_intake.py inputs/examples/plan.cycle-59.yaml`.
3. **Ask Cursor** to use the named skill, for example: *Use `qa-scribe-plan` with this YAML* (skills live under [`.cursor/skills/`](.cursor/skills/)). Write drafts to `out/` with generator name and skill version.

Human gate: every generated file is **Draft — human sign-off required** until a QA Analyst, QA Manager, or named approver verifies it.

## Generate documentation for *your* project

VaultGrid is a **fictional worked example with fake data**. Do not ship VaultGrid names, REQ IDs, or people as if they were yours. Replace them with your product’s facts.

1. **Pick the document you need** (one at a time — never mix strategy and plan):

   | You need | Skill to name in Cursor |
   | --- | --- |
   | How we test this product over months | `qa-scribe-strategy` |
   | How *this cycle* gets out the door | `qa-scribe-plan` |
   | Cases to execute / import to Xray | `qa-scribe-cases` |
   | A contract so later cases stay on-standard | `qa-scribe-prompts` |
   | In-cycle status or end-of-cycle summary | `qa-scribe-report` |

2. **Collect intake. Do not invent.** Copy the matching file under `inputs/examples/`, then replace values with *your* product name, requirements (`REQ-…`), risks (`RSK-…`), environments, and — for a plan — **real** names, hours, and dates. If a field is unknown, leave it blank and say so. `qa-scribe-intake` must ask for missing keys rather than fabricate them. Optional check: `python3 scripts/validate_intake.py path/to/your.yaml`.

3. **Open this repo in Cursor** (clone or add the skills). Paste the YAML and ask: *Use `qa-scribe-<type>` with this intake. Write the draft under `out/`.* If the YAML is incomplete, the intake skill runs first.

4. **Review like a sign-off, not like a spellcheck.** Use `standards/rubrics/<type>.md`. Confirm traces, risk order, and that strategy still has no cycle calendar. Edit the draft. When a generation is wrong, run `qa-scribe-improve` with your critique so the skill gains a rule — never lower the rubric to make drafting easier.

5. **Paste, then a human signs.** Copy from `out/` (or a cleaned Markdown) into Confluence, Jira, or Xray. Change Status from Draft only after a QA Analyst, QA Manager, or the named approver in the plan has verified the document. AI does not authorise execution or release.

Confidentiality: fictionalise or omit real customer names, evidence hashes, and ticket keys before they enter this repo or a chat. Learnings files stay NDA-safe.

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
examples/           Golden strategy, plan, cases, prompts, reports, RTM, defect, UAT
ready-to-paste/     Confluence-cleaned copies of the best goldens
learnings/          Bootstrap note, changelog, future improve notes
out/                Generated drafts (gitignored except README)
scripts/            Optional intake YAML validator
AGENTS.md           Rules for future agents
```

## NDA and fake-data disclaimer

**All of it is fake.** VaultGrid is not a real system. NORTHWIND, GLOBEX, every person name in the examples, every hash, UUID, case id, defect id, timestamp, and hour figure is **synthetic portfolio data**. This repository is not connected to a live investigation, a live customer, or an employer’s confidential programme.

Do not paste real evidence, real customer names, real tickets, or production URLs into this repository. If your own intake looks confidential, stop and fictionalise before you generate.

## Author

Fabian Velasquez — [linkedin.com/in/fabianvelasqueza](https://linkedin.com/in/fabianvelasqueza)

MIT License. See [LICENSE](LICENSE).

**All generated documentation must be verified by a QA Analyst (or the QA Manager / Product Owner named in the plan) before it is used as a control of record.**
