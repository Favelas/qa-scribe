# Identifier schemes

- Document type: ID scheme
- Standard(s) cited: House scheme consistent with IEEE 829 identifiers; not a substitute for a standard
- Product: VaultGrid (examples)
- Cycle / version: Skill family v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Allocate IDs from this scheme in every generated file.
2. Do not reuse a case ID for a different behaviour.
3. Paste the table into the team wiki if the scheme is adopted.
4. Delete this “How to use this file” block after paste.
5. Never use real Jira keys as the primary test-case identifier; map them in RTM if the user supplies them.

---

| Artefact | Pattern | Example | Notes |
| --- | --- | --- | --- |
| Test strategy | `STR-<PRODUCT>-<nnn>` | `STR-VAULTGRID-001` | Product-level; increment when the approach changes, not every sprint |
| Test plan | `PLN-<PRODUCT>-<cycle>-<nnn>` | `PLN-VAULTGRID-C59-001` | One identifier per cycle plan |
| Test case | `TC-<AREA>-<nnn>` | `TC-RBAC-004` | Areas: RBAC, ISO, INT, AUD, EXP, API, UAT |
| Prompt pack | `PRM-<AREA>-<nnn>` | `PRM-RBAC-001` | Generator contract, not testware |
| Status report | `RPT-STS-<PRODUCT>-<cycle>-<nnn>` | `RPT-STS-VAULTGRID-C59-001` | In-cycle |
| Completion / summary report | `RPT-SUM-<PRODUCT>-<cycle>-<nnn>` | `RPT-SUM-VAULTGRID-C59-001` | End of cycle |
| Requirement | `REQ-<AREA>-<nnn>` | `REQ-ISO-01` | From intake / `docs/requirements.md` |
| Product risk | `RSK-<AREA>-<nnn>` | `RSK-ISO-01` | From intake / `docs/risks.md` |
| Defect (examples) | `DEF-<cycle>-<nnn>` | `DEF-C59-012` | Fictional; IEEE 1044 category + severity when listed |

## Area codes

| Code | Meaning |
| --- | --- |
| RBAC | Role-based access |
| ISO | Tenant isolation |
| INT | Integrity / hashing / custody |
| AUD | Audit log |
| EXP | Export / reports |
| API | API authorisation (when not covered by RBAC/ISO) |
| UAT | Acceptance in a region |
