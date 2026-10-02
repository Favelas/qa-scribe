# standards/ — what this tool can create

Open **this file** when you want to produce QA documentation. This folder is the catalog. `docs/` is filled VaultGrid examples. Your new drafts go to `out/`.

## How to create a document

1. Pick a row in **Documents you can create** below.
2. Either **duplicate the template** (blank structure) or in Cursor say **Use `qa-scribe-<skill>`** with your facts.
3. Drafts land in `out/` with `generator` and `skill_version`. Do not invent names, dates, hours, or REQ/RSK IDs — run `qa-scribe-intake` if those are missing.
4. Score against the **rubric** before you paste to Confluence/Xray.
5. A human signs. Nothing here is a control of record while Status is Draft.

Need the whole set from one paste of user stories? Use `qa-scribe-all` instead of running each skill by hand.

## Documents you can create

Suggested order for a new product: 1 → 2 → 3 → 4, then 6 when you have people and dates, then 7/8 during and after the cycle. 5 is optional.

| # | Document | What it is | Duplicate this template | Say this in Cursor | Filled example | Rubric | Draft lands in |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Product risk register | What could go wrong; level; stopper?; test depth | [risk-template.md](risk-template.md) | `qa-scribe-risks` | [docs/risks.md](../docs/risks.md) | [rubrics/risks.md](rubrics/risks.md) | `out/RSK-<PRODUCT>-register.md` |
| 2 | Risk-based test matrix | Allocate each `RSK-` to level, type, technique, coverage depth | [risk-based-test-matrix-template.md](risk-based-test-matrix-template.md) | `qa-scribe-matrix` | None yet — use the template | [rubrics/risk-based-test-matrix.md](rubrics/risk-based-test-matrix.md) | `out/MTX-<PRODUCT>-001.md` |
| 3 | Test strategy | How we test **this product** over months (no sprint dates) | [strategy-template.md](strategy-template.md) | `qa-scribe-strategy` | [docs/strategy.md](../docs/strategy.md) | [rubrics/strategy.md](rubrics/strategy.md) | `out/STR-<PRODUCT>-001.md` |
| 4 | Test cases | What we will execute (Markdown + Xray CSV) | [case-template.md](case-template.md) | `qa-scribe-cases` | [docs/cases.md](../docs/cases.md) | [rubrics/cases.md](rubrics/cases.md) | `out/TC-<AREA>-pack.md` + `.csv` |
| 5 | Design prompt pack | Contract for **more** cases later (not testware) | [prompt-pack-template.md](prompt-pack-template.md) | `qa-scribe-prompts` | [docs/prompts.md](../docs/prompts.md) | [rubrics/prompts.md](rubrics/prompts.md) | `out/PRM-<AREA>-001.md` |
| 6 | Test plan | How we get **this cycle** out the door (names, hours, deadline, RTM) | [plan-template.md](plan-template.md) | `qa-scribe-plan` | [docs/plan.md](../docs/plan.md) | [rubrics/plan.md](rubrics/plan.md) | `out/PLN-<PRODUCT>-<cycle>-001.md` + RTM CSV |
| 7 | Test status report | In-cycle progress, sliced by risk | [status-report-template.md](status-report-template.md) | `qa-scribe-report` (status) | [docs/report-status.md](../docs/report-status.md) | [rubrics/report.md](rubrics/report.md) | `out/RPT-STS-…md` |
| 8 | Test completion / summary report | End of cycle; residual risk; go / go-with-risks / no-go | [completion-report-template.md](completion-report-template.md) | `qa-scribe-report` (completion) | [docs/report-completion.md](../docs/report-completion.md) | [rubrics/report.md](rubrics/report.md) | `out/RPT-SUM-…md` |

Do not mix strategy and plan. Do not use the risk-based test matrix as a substitute for the risk register, the cycle RTM, or the role × screen table.

## Overlays (not a ninth generator)

Use these **in addition to** documents 1–8 when the program is a special shape. They do **not** replace the risk register, the **risk-based test matrix**, cases, or a later cycle plan. They are still `STR-…` (approach), never `PLN-…`. No filled golden until a human asks for one.

A cloud migration still needs: register (`RSK-…`) → **matrix (`MTX-…`)** → this overlay as the strategy body → cases.

| Overlay | What it is | Duplicate this template | Say this in Cursor |
| --- | --- | --- | --- |
| Cloud migration test approach | High-level what to consider when moving workloads to a cloud, including **100% parity** with legacy (oracle, dual-run, full reconciliation, candidate risk lenses). Phases are **classes**, not dates. **Addition** to register + matrix + cases — not a replacement. | [cloud-migration-approach-template.md](cloud-migration-approach-template.md) | `qa-scribe-strategy` (overlay) **and** `qa-scribe-risks` **and** `qa-scribe-matrix`. Do **not** ask for a test plan unless you have people, hours, and a deadline. |

## Helpers (not documents)

| Skill | When to use |
| --- | --- |
| `qa-scribe-intake` | Facts are missing. Collects keys; refuses to invent dates, hours, names, REQ IDs. |
| `qa-scribe-all` | One paste of user stories → as many of the documents above as the facts support. |
| `qa-scribe-improve` | A human rejected a draft. Scores the rubric, patches the skill, never lowers the bar. |

Sample intake YAML: [`inputs/examples/`](../inputs/examples/).

## You supply these (not generated as a primary document)

Keep them next to the generated set. VaultGrid copies live in `docs/`.

| File | What it is | VaultGrid example |
| --- | --- | --- |
| Requirements list | `REQ-` IDs the generators may trace to | [docs/requirements.md](../docs/requirements.md) |
| Role × screen matrix | Button/menu Show/Hide oracle for ROLE-MATRIX cases | [docs/roles.md](../docs/roles.md) |
| Product description | What the system is, in one page | [docs/product.md](../docs/product.md) |

## House rules (this folder)

| File | What it is |
| --- | --- |
| [standards-map.md](standards-map.md) | Which standard each document must cite (and what is forbidden) |
| [id-schemes.md](id-schemes.md) | `STR-` `MTX-` `PLN-` `TC-` `RSK-` `REQ-` `RPT-` patterns |
| [documentation-principles.md](documentation-principles.md) | Strategy ≠ plan; risk-first; human gate |
| [rubrics/](rubrics/) | Fail-if-missing checklists per document |

Citations for pull requests that change a template: [standards-map.md](standards-map.md).
