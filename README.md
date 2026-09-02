# QA Scribe

AI-assisted QA documentation accelerator: Cursor skills, ISO/IEEE/ISTQB templates, a short VaultGrid UI example, and a skill-rewrite loop — so a Senior QA Analyst spends time on risk, not on a blank page.

> **Fake product. Fake data.**  
> VaultGrid, companies NORTHWIND and GLOBEX, users, cases, hours, and dates are **invented**. Not a real investigation, customer, or employer system.

Goldens say **Draft — human sign-off required** on purpose. AI drafts; a named QA role signs.

**Fabian Velasquez** — Senior QA Analyst / Senior Functional QA Specialist / Senior Software Testing Engineer.  
Main work: **manual functional QA** on enterprise SaaS in the **browser** — who sees which buttons, two companies on one site (isolation), forms, activity log. Playwright and Postman are supporting skills, not this product.  
Thesis: AI drafts. Named standards shape headings. The tester owns risk and sign-off.

> **How a recruiter should walk it (60 seconds)**  
> Open **`docs/`** — that folder is the portfolio. Everything else supports it.
>
> 1. **[README.md](README.md)** — who you are and the five generators.  
> 2. **[docs/strategy.md](docs/strategy.md)** — strategy ≠ plan (no sprint dates).  
> 3. **[docs/plan.md](docs/plan.md)** — you can staff a cycle (names, hours, deadline, RTM).  
> 4. **[docs/cases.md](docs/cases.md)** — isolation = Company A must not see Company B in **search**.  
> 5. **[docs/report-completion.md](docs/report-completion.md)** — residual risk, not a fake green dashboard.
>
> One case: **TC-ISO-001**. Isolation in one line: two companies, same website; A must not see B’s case title.  
> Stopper vs not: **[docs/defect-stopper.md](docs/defect-stopper.md)** vs **[docs/defect-not-stopper.md](docs/defect-not-stopper.md)**.

| Intake | Output | Standard(s) |
| --- | --- | --- |
| Product, risks, REQ IDs (no dates, no hours) | Test **strategy** | ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB |
| Cycle, people × hours, dates, RTM | Test **plan** | IEEE 829-2008 (15 sections); 29119-3 Test Plan |
| REQ + RSK + UI steps | **Test cases** (Markdown + CSV) | IEEE 829 / 29119-3; 29119-4 / ISTQB |
| Same traces | **Design prompts** | Contract: still 829 / 29119-3 fields |
| Status or completion counts | **Report** | 29119-3 status **or** 29119-3 completion + IEEE 829 summary |

**Principle:** AI drafts. Standards shape fields. Humans own risk. High-priority risks first.

### Not this

- Not real customers or real evidence — **all sample data is fake**
- Not an autonomous tester, not TestRail/Xray as a product, not a hosted SaaS

---

## What you need (one folder)

**`docs/`** — product, requirements, roles, risks, strategy, plan, cases, RTM, both reports, two defects, prompt pack.

Ignore until you generate: `.cursor/skills/`, `standards/`, `inputs/`, `learnings/`, `out/`, `scripts/`.

## How to use immediately

1. Copy a file from `docs/` into Confluence, Jira, or Xray (`docs/cases.csv`).
2. For a new product, copy YAML from `inputs/examples/` — do not invent names, dates, hours, or REQ IDs. Optional: `python3 scripts/validate_intake.py inputs/examples/plan.cycle-59.yaml`.
3. In Cursor: *Use `qa-scribe-plan` with this YAML.* Drafts go to `out/`.

Human gate: Draft until a QA Analyst, QA Manager, or named approver verifies.

## Generate documentation for *your* project

VaultGrid is a **short UI example**. Replace it with your facts.

1. Pick one skill: `qa-scribe-strategy` | `qa-scribe-plan` | `qa-scribe-cases` | `qa-scribe-prompts` | `qa-scribe-report`.
2. Fill intake. Isolation in your words: “Customer A must not see Customer B’s records on screen.”
3. Review with `standards/rubrics/<type>.md`. Run `qa-scribe-improve` after a human critique.
4. Paste; a human signs. AI does not authorise release.

## Learning loop

`qa-scribe-improve` scores, writes `learnings/YYYY-MM-DD-<topic>.md`, patches the skill, updates `learnings/CHANGELOG.md`. Never lowers the bar. Bootstrap: `learnings/2026-09-02-bootstrap.md`.

## Sample plan YAML

```yaml
document: plan
confidential: false
product_name: VaultGrid
cycle_id: Cycle 59
strategy_id: STR-VAULTGRID-001
people:
  - name: Maya Chen
    role: QA Analyst
    owns: UI execution
    hours: 32
schedule:
  execution_start: 2026-09-15
  cycle_deadline: 2026-10-03T17:00:00Z
requirements: [REQ-ISO-01, REQ-RBAC-01]
risks_this_cycle:
  - id: RSK-ISO-01
    mitigation: Search isolation first; Severity 1 suspends
    test_refs: [TC-ISO-001]
```

Full file: `inputs/examples/plan.cycle-59.yaml`.

## Sample case — TC-ISO-001 (isolation)

**Isolation:** two companies on one site. NORTHWIND must not see GLOBEX’s case title in Search.

| Field | Content |
| --- | --- |
| Identifier | TC-ISO-001 |
| Objective | Search as NORTHWIND must not list `GLOBEX-CASE-RED`. |
| Requirement | REQ-ISO-01 |
| Risk | RSK-ISO-01 (stopper if it fails) |
| Priority | 1 |
| Technique | NEG; EP |
| Preconditions | GLOBEX has that case title. User `nw-ro`. |
| Inputs | Search string `GLOBEX-CASE-RED` |

**Procedure:** Log in as `nw-ro` → Search → type `GLOBEX-CASE-RED`.  
**Expected:** Zero rows. If the title appears, that is **DEF-STOP-01** — do not ship.

## Repo map

```text
docs/               ← read this (strategy, plan, cases, reports, defects)
inputs/examples/    YAML to generate more
.cursor/skills/     Cursor generators (agents)
standards/          Templates and rubrics
learnings/          Skill changelog
out/                New drafts (gitignored)
scripts/            Optional YAML check
```

## NDA and fake-data disclaimer

**All of it is fake.** Do not paste real evidence, customer names, or production URLs here.

## Author

Fabian Velasquez — [linkedin.com/in/fabianvelasqueza](https://linkedin.com/in/fabianvelasqueza)

MIT License. See [LICENSE](LICENSE).

**All generated documentation must be verified by a QA Analyst (or the QA Manager / Product Owner named in the plan) before it is used as a control of record.**
