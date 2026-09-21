# Risks skill — reference (ISTQB risk-based testing)

Use with `.claude/skills/qa-scribe-risks/SKILL.md`. Skill version 1.0.0.

## Category lens (apply only where the input gives a basis)

| Input mentions... | Consider this risk category | Typical level driver |
| --- | --- | --- |
| Multiple tenants/companies/orgs sharing a search, list, or export | Tenant isolation (RSK-ISO-*) | Critical if data can cross the boundary on screen |
| Roles, permissions, "admin only", "read-only" | RBAC / permission leakage (RSK-RBAC-*) | High if the disallowed action actually succeeds; lower if only a button is visible |
| Uploads, files, hashes, custody, "must not corrupt" | Data integrity (RSK-INT-*) | High/Medium depending on whether corruption is silent |
| "Required field", limits, min/max, empty input | Validation / negative (RSK-VAL-*) | Medium unless it lets bad data persist silently |
| "Log", "trail", "who did what", compliance | Audit / traceability (RSK-AUD-*) | Medium, escalate if it's the only evidence for a compliance claim |
| Export, download, report generation | Export / availability (RSK-EXP-*) | Low/Medium unless the export itself leaks cross-tenant data (then Critical, folds into ISO) |
| Named regions, UAT windows | Regional acceptance (RSK-UAT-*) | Depends on what's being accepted per region |

## Level rationale phrasing

One clause, tied to what happens if the risk fires — not a bare adjective:

- "Critical — data crosses a tenant boundary that a customer can see."
- "High — disallowed action succeeds, not just a visible button."
- "Medium — bad data persists but stays inside one tenant/role."
- "Low — cosmetic or logging-only gap."

## Stopper wording

Match the existing convention exactly: `Yes — stopper`, `Yes if <condition>`, `No — but named leftover` (go-with-risks), or `No`. Never write a bare "No" for a Critical risk without saying why it isn't a stopper.

## Golden pattern

`docs/risks.md` — table shape and the ranking rule ("A report that looks all green while a Critical is open is a fail of the report, not a pass of the product") to preserve in every draft.
