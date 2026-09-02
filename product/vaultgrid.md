# VaultGrid — fictional product brief

- Document type: Product brief (intake source, not a test document)
- Standard(s) cited: Not applicable: this file is NDA-safe product context for QA Scribe examples
- Product: VaultGrid
- Cycle / version: Product-level (not cycle-bound)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Treat this as the only product under test in golden examples and skill walkthroughs.
2. Copy requirement and risk IDs from `product/requirements.md` and `product/risks.md`; do not invent new IDs in examples.
3. Paste selected paragraphs into Confluence only after a Product Owner confirms they are still fictional.
4. Delete this “How to use this file” block after paste.
5. Never replace VaultGrid with a real employer product, real ticket IDs, or real evidence hashes.

---

## 1. What VaultGrid is

VaultGrid is a **fictional** multi-tenant digital-evidence vault (**fake product, fake data**). Investigation teams store files, hash records, chain-of-custody events, and case-scoped reports. Tenants are organisations (for example a municipal police force, a law firm, or a corporate incident-response unit). A tenant never shares evidence objects, users, or audit streams with another tenant.

This repository uses VaultGrid so QA documents can be public. It is not a real product, not a real investigation, and contains no real evidence.

## 2. Isolation model

- **Tenant ID** is the isolation boundary.
- Session and API tokens carry `tenant_id` and `role`. Object access is authorised from the token, not from a tenant field in the request body.
- Evidence object IDs are UUIDs. A valid UUID that belongs to another tenant must return **HTTP 404** (not 403) so the API does not become an existence oracle.
- Denied cross-tenant attempts are still written to the **acting tenant’s** audit stream as outcome = deny.

## 3. Roles

| Role | Intended use | Must not |
| --- | --- | --- |
| Admin | Manage users and roles inside the home tenant, set retention, export tenant-wide packages | Access another tenant; disable audit |
| Investigator | Upload evidence, search/view home-tenant evidence, add notes, download originals for assigned cases | Change roles; run bulk export; see other tenants |
| Reporter | Generate and export reports for **assigned** cases; read metadata | Upload evidence; open unassigned cases; download originals unless the report package explicitly includes a redacted copy |
| Read-only | View assigned case **metadata** and own audit of view actions | Download original files; export; upload; change roles |

The authoritative action grid is `product/rbac-matrix.md`.

## 4. Integrity and chain of custody

- On ingest the server computes **SHA-256** over the stored bytes and records size in bytes.
- If the client sends a pre-computed hash, it must match the server hash or the upload is rejected and no evidence object is created.
- Truncated transfers (bytes received < declared `Content-Length`) are rejected.
- Each ingest, download, and export appends a custody event linked to the current hash and actor.
- Evidence **bytes** are immutable after a successful ingest. Metadata corrections are new events, not in-place edits of the blob.

## 5. Audit

- Append-only log. No update or delete API for testers or tenant Admins.
- Every event records actor, tenant, object (if any), action, outcome (allow/deny), and UTC timestamp.
- Successful evidence access and **denied** authorisation attempts are both logged.
- Product policy: retain audit for 7 years. That policy is a test condition for retention jobs, not a promise about any real system.

## 6. Exports and reports

- Bulk export: Admin only, tenant-scoped.
- Case report export: Reporter, assigned cases only.
- Export packages include file hashes present at export time.
- Residual product risk (used in Cycle 59 reporting): Reporter export may still include investigator notes that a separate notes-ACL would have hidden. That is **RSK-EXP-01**.

## 7. API authorisation

- `Authorization: Bearer` JWT with `sub`, `tenant_id`, `role`, `exp`.
- Body or query `tenant_id` is ignored when it disagrees with the token.
- Role in the token is checked against `product/rbac-matrix.md` for the requested action.
- Expired or wrong-tenant tokens never return another tenant’s objects.

## 8. Regions and UAT

Home-region deployments used in examples: **US** (Virginia), **UK** (London), **Brazil** (São Paulo), **Australia** (Sydney). Evidence remains in the tenant’s home region. UAT is executed in all four regions when the cycle intake lists them.

## 9. What this brief is not

- Not a test strategy, test plan, or set of test cases.
- Not an employer system. Do not paste real hashes, customer names, or production URLs into this file.

## 10. Source files for generators

| Need | File |
| --- | --- |
| Shall statements | `product/requirements.md` |
| Role × action | `product/rbac-matrix.md` |
| Product risks | `product/risks.md` |
| Cycle 59 intake (plan/report) | `inputs/examples/plan.cycle-59.yaml` |
