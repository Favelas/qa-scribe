# QA Scribe

AI-assisted QA documentation accelerator: Cursor skills, ISO/IEEE/ISTQB templates, a short VaultGrid UI example, and a skill-rewrite loop — so a Senior QA Analyst spends time on risk, not on a blank page.

> **Fake product. Fake data.**  
> VaultGrid, companies NORTHWIND and GLOBEX, users, cases, hours, and dates are **invented**. Not a real investigation, customer, or employer system.

Goldens say **Draft — human sign-off required** on purpose. AI drafts; a named QA role signs.

## Folders — what to open

Most folders are **engine**, not **work**. Day to day you need three: **`standards/`** (create), **`docs/`** (filled example), **`out/`** (the draft the agent just wrote).

`.claude/skills/` and `.cursor/skills/` are the **same files twice**. Claude Code reads one path, Cursor reads the other.

| Folder | What is inside | You open it when… | You can ignore it when… |
| --- | --- | --- | --- |
| **[`standards/`](standards/README.md)** | Catalog, blank templates, rubrics, ID schemes, which standard each doc must cite | You want to **create** a document (copy a template or pick the skill) | Never, if you are the author |
| **[`docs/`](docs/)** | Filled **VaultGrid** examples (fake product): strategy, plan, cases, reports, defects | You want to **see** what a finished file looks like, or show a recruiter | You already know the shape and are writing for a real product |
| **[`out/`](out/)** | New AI drafts (`PLN-…`, `STR-…`, cases). Gitignored except the README | You just asked the agent to generate something | You are only browsing examples |
| **[`inputs/`](inputs/)** | Sample YAML of **facts** (names, hours, dates, REQ IDs) — not the document itself | You want a checklist of what a plan/strategy/report is allowed to use | You would rather paste facts in chat |
| **`.claude/skills/`** | Canonical generator instructions (`qa-scribe-plan`, `qa-scribe-cases`, …) | You are **changing how** Scribe writes (after a critique) | You are only producing a plan/cases for a project |
| **`.cursor/skills/`** | Byte-for-byte **mirror** of `.claude/skills/` | You should not. Sync overwrites it | Always, as an author |
| **[`learnings/`](learnings/)** | Dated notes + changelog when a human rejected a draft and the skill was patched | You want to know *why* a rule exists (e.g. Crit risks must have cases) | Everyday document creation |
| **`scripts/`** | `sync-skills.sh` (keep the two skill trees identical), optional YAML checker | After you edit `.claude/skills/` | Everyday document creation |
| **`.githooks/`** | Pre-commit: fail if Cursor skills drifted from Claude skills | One-time: `git config core.hooksPath .githooks` | After that is set |

Root files, not folders: this README, **`AGENTS.md`** (rules the agent must follow), **`LICENSE`**.

Document catalog (every artefact, template, skill, rubric, output path): **[`standards/README.md`](standards/README.md)**.

**Two ways to create a document:** (1) duplicate the template in `standards/` and fill your facts, or (2) in Cursor say the skill on that catalog row and paste your facts — draft lands in `out/`. **Suggested: (2).** Do not invent names, dates, hours, or REQ/RSK IDs.

## When and how to use Scribe

Scribe drafts IEEE/ISO/ISTQB-shaped QA paperwork from **your** facts. It does not log into the app, run tests, or sign go/no-go. You still own risk, hours, and sign-off. Never paste real customer data into this repo.

| Situation | What you do |
| --- | --- |
| New product, you have user stories, you want the pack | *Use `qa-scribe-all`.* Confirm the REQ/RSK list it proposes. It writes register + matrix + strategy + cases to `out/`. Plan/report wait until you have people, hours, a deadline, or execution counts. |
| You only need **this cycle’s plan** | Bring product, cycle name, `STR-…` if you have it, named people × hours, deadline, in/out features, `RSK-` list. *Use `qa-scribe-plan`.* Draft: `out/PLN-…` + RTM CSV. Without named people, hours, and a deadline it will refuse — that would be a strategy, not a plan. |
| Isolation / RBAC / “who sees which button” | Need `REQ-` + `RSK-` + roles. *Use `qa-scribe-cases`.* Paste Markdown to Confluence; import CSV to Xray. |
| “How we test this product” with **no** sprint dates | *Use `qa-scribe-strategy`.* If you also give dates and hours, that is a **plan**, not a strategy. |
| Mid-cycle “are we on track?” | Real pass/fail/blocked counts by risk. *Use `qa-scribe-report` (status).* |
| End of cycle go / go-with-risks / no-go | Same counts plus leftover Crit/High. *Use `qa-scribe-report` (completion).* You (or QA Manager / PO) choose the recommendation — the agent does not. |
| You have stories but not hours or a deadline yet | Do **not** start with a plan. Register → matrix → strategy → cases first. |
| Facts are incomplete and you do not want invented names | *Use `qa-scribe-intake`.* It asks only for missing keys, then tells you which skill to run. |
| A human said the draft is wrong | *Use `qa-scribe-improve`.* It scores the rubric, patches the **canonical** skill, syncs Cursor. Next run is stricter, not looser. |
| You want to type it yourself | [`standards/README.md`](standards/README.md) → duplicate the template → fill your product. Same headings; no agent. |
| Recruiter / portfolio (60 seconds) | Open **`docs/`** only — walk below. |

**Principle:** AI drafts. Standards shape fields. Humans own risk. High-priority risks first.

### Not this

- Not real customers or real evidence — **all sample data is fake**
- Not an autonomous tester, not TestRail/Xray as a product, not a hosted SaaS

---

**Fabian Velasquez** — Senior QA Analyst / Senior Functional QA Specialist / Senior Software Testing Engineer.  
Main work: **manual functional QA** on enterprise SaaS in the **browser** — who sees which buttons, two companies on one site (isolation), forms, activity log. Playwright and Postman are supporting skills, not this product.  
Thesis: AI drafts. Named standards shape headings. The tester owns risk and sign-off.

> **How a recruiter should walk it (60 seconds)**  
> Open **`docs/`** — that folder is the portfolio. Everything else supports it.
>
> 1. **[README.md](README.md)** — who you are and which folder to open. **[`standards/README.md`](standards/README.md)** — what the tool can create.  
> 2. **[docs/strategy.md](docs/strategy.md)** — strategy ≠ plan (no sprint dates).  
> 3. **[docs/plan.md](docs/plan.md)** — you can staff a cycle (names, hours, deadline, RTM).  
> 4. **[docs/cases.md](docs/cases.md)** — isolation = Company A must not see Company B in **search**.  
> 5. **[docs/report-completion.md](docs/report-completion.md)** — residual risk, not a fake green dashboard.
>
> One case: **TC-ISO-001**. Isolation in one line: two companies, same website; A must not see B’s case title.  
> Stopper vs not: **[docs/defect-stopper.md](docs/defect-stopper.md)** vs **[docs/defect-not-stopper.md](docs/defect-not-stopper.md)**.

## How to use immediately

1. Copy a template from [`standards/README.md`](standards/README.md), or copy a filled file from `docs/` into Confluence, Jira, or Xray (`docs/cases.csv`).
2. For a new product, copy YAML from `inputs/examples/` — do not invent names, dates, hours, or REQ IDs. Optional: `python3 scripts/validate_intake.py inputs/examples/plan.cycle-59.yaml`.
3. In Cursor: *Use `qa-scribe-plan` with this YAML* (or the skill on the catalog row). Drafts go to `out/`.

Human gate: Draft until a QA Analyst, QA Manager, or named approver verifies.

## Generate documentation for *your* project

VaultGrid is a **short UI example**. Replace it with your facts.

1. Open [`standards/README.md`](standards/README.md) and pick the document (or say `qa-scribe-all` for the full set).
2. Duplicate its template, or in Cursor: *Use `qa-scribe-plan` with this YAML* (swap the skill for the row you picked). Drafts go to `out/`.
3. Isolation in your words: “Customer A must not see Customer B’s records on screen.” Do not invent names, dates, hours, or REQ IDs — use `qa-scribe-intake` if those are missing.
4. Review with the rubric linked on that row. Run `qa-scribe-improve` after a human critique.
5. Paste; a human signs. AI does not authorise release.

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

## NDA and fake-data disclaimer

**All of it is fake.** Do not paste real evidence, customer names, or production URLs here.

## Author

Fabian Velasquez — [linkedin.com/in/fabianvelasqueza](https://linkedin.com/in/fabianvelasqueza)

MIT License. See [LICENSE](LICENSE).

**All generated documentation must be verified by a QA Analyst (or the QA Manager / Product Owner named in the plan) before it is used as a control of record.**
