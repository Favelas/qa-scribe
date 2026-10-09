# QA Confluence space — placement process

- Document type: Process (wiki information architecture). Not a test strategy, not a test plan, not a generator output.
- Standard(s) cited: ISTQB (strategy vs plan; risk-based testing). House process for where QA pages live. Not an ISO/IEC/IEEE document type.
- Product: Any team that adopts this space shape
- Cycle / version: Works for weekly or two-week trains (page titles stay “this release”)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Use this when standing up or trimming a **QA Confluence space**. Do not rewrite Scribe templates from this file.
2. Answer **§ Fit questions** before copying the tree. This shape is not mandatory for every team.
3. Paste the tree onto the space Home if the QA Lead adopts it. Keep existing Scribe document-control blocks on generated pages — do **not** add an extra eight-question header on every wiki page.
4. Add pages only in the phase you are in. Measure use before growing the space.
5. Delete this “How to use this file” block after paste into the wiki Home if you want a cleaner Home; keep a link to this process.

---

Scribe **writes** artefacts (`STR-…`, `RSK-…`, `MTX-…`, `PLN-…`, cases, reports). This process says **where those artefacts sit** for a delivery team so information is one place, with a purpose and an audience, not sprawled.

Cases and execution counts stay in **Xray/Jira** unless a regulator forces them on the wiki.

## Document control (this process)

| Field | Value |
| --- | --- |
| Identifier | PROC-CONFLUENCE-QA-001 |
| Document type | Process — QA wiki placement |
| Audience | QA Lead, Software Testing Engineer, anyone creating a QA page |
| Owner | QA Lead of the space |
| Review | When the train cadence or tools change |
| Generator | (hand-filled; not a qa-scribe-* output) |

## 1. Fit questions (answer before adopting)

This structure fits a **product QA group** that releases on a train, owns go/no-go from a QA view, and already has (or will have) Jira/Xray. It may **not** fit a staff-aug squad with no wiki, a programme PMO space, or a team whose only SoT is a slide deck.

| # | Question | If you answer… | Then |
| --- | --- | --- | --- |
| F1 | Who is the **named owner** of the QA space? | No name | Do not start. Pages without an owner rot. |
| F2 | What is the release train? | Weekly / every 2 weeks / mixed | Use **This release** (not “Sprint N”). Only the dates on Readiness change. |
| F3 | Where do test **cases** live today? | Xray/Jira/TestRail | Keep them there. Confluence does not get the case library. |
| F4 | Where does go/no-go happen today? | Teams/Slack only | Adopt **Release readiness** as SoT; chat **links** that page. |
| F5 | Do you have a signed product **strategy**? | No | Create strategy first (Scribe `STR-…`). Do not start with a dashboard. |
| F6 | Is this team regulated / audit-heavy? | Yes | Keep case packs + RTM in the tool; wiki Traceability stays a **short** table. |
| F7 | Is this a **cloud migration** / 100% parity programme? | Yes | Add the migration overlay under How we work → Test strategy (child). Do not replace Risks or the matrix. |
| F8 | More than one product in one space? | Yes | Repeat **This release** per product (or one space per product). Do not mix two trains on one Readiness page. |
| F9 | Who may edit Readiness? | Unclear | Name STE (updates) and QA Lead (recommendation). |
| F10 | Will PO/Eng open Confluence, or only Teams? | Chat only | Still keep Readiness as record; the Teams message must include the URL or the process has failed. |

If F1 or F9 is empty, stop. Structure will not save an ownerless wiki.

## 2. What to consider when creating any team page

Do **not** put these eight prompts as a header on every page. Use them **once**, when someone asks for a new page. Existing Scribe control (type, standards, product, audience via Author role, Draft, owner in Approvals) stays as it is.

Create the page only if you can answer all of these. If not, **reject** or **add a section** on an existing SoT page.

| Consider | Rule |
| --- | --- |
| What problem does this page solve? | One problem. If you need “and also…”, you likely want two pages or a section. |
| Who will use it? | Named role (Software Testing Engineer, QA Lead, PO). “Everyone” is not an audience. |
| How often will it be used? | Process pages: rare. **This release** pages: every train. |
| What decision will it support? | Ready to ship? Test first? Accept leftover? Staff a wave? If none, do not create it. |
| Can this live somewhere else? | Xray, CI, Jira, git, Teams. **Link**. Do not copy. |
| What is the maintenance cost? | High + every train = it will die. Prefer one live page over many archives-in-place. |
| Is there already a document? | Strategy vs plan vs risks vs matrix vs RTM vs cases are **different jobs**. Do not merge them. Do not clone them. |
| What happens if it does not exist? | If nothing breaks, skip it. |

**Also consider:**

- **Process vs execution.** Strategy and “how we plan” change rarely. Readiness and current risks change every train.
- **One live page per concern.** Title `Current …` or `This release — …`. Never `Sprint 14 Readiness` as the live page.
- **Chat is the ping.** Teams/Slack announces; the wiki page is the record. “We’re good” without a URL is not a QA recommendation.
- **No vanity metrics** on the wiki. Pass rate without residual Crit/High is a fail.
- **Do not duplicate Scribe jobs.** Register ≠ matrix ≠ cycle RTM ≠ role × screen.
- **Language.** Address the **Software Testing Engineer**, not “tester,” unless the team’s HR title is different — then use **their** title in the audience line only.
- **Draft until a human signs** on generated paste-ins. Wiki Status must match.

## 3. Sources of truth (do not sprawl)

| Need | SoT page (Confluence) | Not SoT |
| --- | --- | --- |
| How we test this product | **Test strategy** | Planning, chat, slide deck |
| Who / hours / dates for a **named wave** | **Planning** | Strategy |
| Ship **this** train? (QA view) | **Release readiness** | Teams without a link |
| What can still go wrong? | **Risks** (current register) | Spreadsheet of the week |
| How deep / which type per risk | **Matrix** (child of Risks) | A second register |
| Journey/REQ covered this train? | **Traceability** (thin) or a section on Readiness | Pasting all `TC-` into wiki |
| Executable steps | **Xray** (Scribe CSV import) | Confluence case dumps |
| Paths that must never break | **Critical journeys** | Random smoke |
| Build even testable? | **Smoke checklist** (linked from Readiness) | A second smoke on Readiness |
| What we accepted last train | **Archive / [release-id]** | History piled on live Readiness |

Scribe drafts → human edits → **paste onto the matching SoT page**. Git `docs/` is the portfolio example, not the live team wiki.

## 4. Structure to put in Confluence

Four parents plus Archive. Strategy and planning are **siblings** under How we work (never one page). Risks and traceability are **siblings** under This release (never mixed with strategy).

```text
QA  (space)
├── Home
│     Purpose: Where SoT lives; Xray vs wiki vs Teams; link this process.
│     Audience: Anyone in the team who needs a QA page.
│
├── 1. How we work                    (process — rare change)
│     ├── Test strategy               STR-…  Audience: STE, QA Lead, PO (scope)
│     ├── Planning                    PLN-… only when a named wave has people × hours
│     └── Defects (optional, short)   Stopper vs leftover; not a defect database
│
├── 2. This release                   (always current train — weekly or 2-week)
│     ├── Release readiness           ★ QA go / go-with-risks / no-go
│     ├── Risks                       ★ Current register (RSK-…)
│     │     └── Matrix                MTX-… allocation; not the register; not the RTM
│     └── Traceability                Thin RTM this train; full REQ→TC in Xray
│
├── 3. What we protect                (slow change)
│     ├── Critical journeys
│     └── Smoke checklist
│
└── 4. Archive
      └── [release-id]                Frozen copy of readiness + risks used
```

**Release readiness (QA only)** — the page that must exist for a ship decision. Update it, **then** inform the team in Teams with this URL.

Keep short: train id/dates; smoke result; regression **by risk**; open defects (stopper vs leftover); leftover Crit/High with owner; recommendation; who was informed; QA Lead (and PO if leftover High).

Blocked if smoke has no result or risks were not reviewed. Do not invent green.

After the train: copy to Archive; reset This release for the next train.

**Planning** is empty or stub for a normal train. Fill it when there is a UAT window, migration cutover, or named hours. Do not write an IEEE plan every Tuesday.

## 5. Cadence (weekly now, two weeks later)

Do not fork the tree. Change **dates on Readiness** and the review line in document control. Archive by **release id**, not by “weekly folder” vs “biweekly folder.”

## 6. Build in phases (assess use before adding)

| Phase | Create in Confluence | Do not create yet | You are ready to grow when |
| --- | --- | --- | --- |
| **1 Foundation** | Home, Test strategy, Release readiness, Risks, Critical journeys, Smoke, Archive | Dashboards, automation doctrine, formal plan every train, extra checklists | Readiness is updated **before** the Teams ping; Risks touched the same day; last train is in Archive |
| **2 Control** | Planning (when a wave needs it), Matrix child, Traceability as own page if the Readiness table grew, short Defects, Environments | KPI framework, exec pack | People other than the author open Readiness; leftover High has a PO name |
| **3 Later** | Link to Xray/CI; migration overlay under strategy if that programme exists | New “methodology” or “risk framework” pages | A named person asked for a trend, not a guess |

Phase 1 is enough to release weekly with a straight face. Adding pages before that evidence is how unread spaces start.

## 7. Placement map (Scribe → wiki)

| Scribe artefact | Confluence place |
| --- | --- |
| `STR-…` strategy (or cloud overlay) | 1. How we work → Test strategy |
| `PLN-…` + cycle RTM CSV | 1. How we work → Planning (only if that wave exists) |
| `RSK-…` register | 2. This release → Risks |
| `MTX-…` matrix | Child of Risks |
| `TC-…` pack + CSV | **Xray**; wiki only if audit forces a snapshot (link, don’t maintain two) |
| Status report | Fold into **Release readiness** while the train is open |
| Completion / summary | **Archive / [release-id]** (or paste as the snapshot) |
| Role × screen, product, REQ list | What we protect, or linked from strategy — not a fourth SoT for risk |

Do not delete or merge these Scribe types. This process only **places** them.

## 8. What not to add to the wiki

- A page per sprint  
- Test methodology, risk framework, or playbook that repeats strategy  
- Regression status + release checklist **next to** readiness (put sections **on** readiness)  
- Copied CI dashboards  
- Numeric risk scores with no stated basis  
- Full case text in Confluence when Xray exists  

## 9. Approvals (this process)

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| QA Lead (space owner) | | Adopt / adapt / reject this tree | |
| Software Testing Engineer (author of live pages) | | Can update Readiness and Risks | |

Human sign-off is mandatory before this becomes the team’s wiki law. The generator does not approve.
