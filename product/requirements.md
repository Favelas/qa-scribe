# VaultGrid requirements catalogue

- Document type: Requirements catalogue (intake source)
- Standard(s) cited: Traceability source for IEEE 829 / ISO/IEC/IEEE 29119-3 test documents; not itself a 29119-3 document
- Product: VaultGrid
- Cycle / version: Product-level (Cycle 59 tests a subset; see plan intake)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Trace every test case and RTM row to an ID in this catalogue (`REQ-…`).
2. Paste into Jira/Confluence as the fictional backlog only after Product confirms IDs are still the working set.
3. Do not invent `REQ-` IDs in generated output; if a behaviour has no ID, stop and run `qa-scribe-intake`.
4. Delete this “How to use this file” block after paste.
5. Never replace these IDs with real employer ticket keys.

---

IDs are stable. Priority here is **product** priority (business), not test-case priority. Test-case priority is derived from `product/risks.md`.

| ID | Statement | Area | Product priority |
| --- | --- | --- | --- |
| REQ-RBAC-01 | A principal acting in tenant T must not read, write, download, or export evidence objects that belong to tenant T′. | RBAC / isolation | Must |
| REQ-RBAC-02 | Each action in the RBAC matrix is allowed only for the roles marked Allow. All other role × action pairs are Deny. | RBAC | Must |
| REQ-RBAC-03 | A request that names an evidence UUID belonging to another tenant returns HTTP 404 and does not include object metadata in the body. | RBAC / API | Must |
| REQ-RBAC-04 | Only a tenant Admin may assign or change roles inside that tenant. A user cannot elevate their own role. | RBAC | Must |
| REQ-RBAC-05 | Read-only must not download original evidence bytes. | RBAC | Must |
| REQ-RBAC-06 | Reporter must not open or export a case to which they are not assigned. | RBAC | Must |
| REQ-RBAC-07 | Investigator must not call the bulk export endpoint. | RBAC | Must |
| REQ-RBAC-08 | After a role is revoked, subsequent API calls with a token that still carries the old role are rejected at the authorisation layer. | RBAC / session | Must |
| REQ-INT-01 | On successful ingest the server stores SHA-256 of the persisted bytes and the byte length. | Integrity | Must |
| REQ-INT-02 | If bytes received are fewer than the declared Content-Length, the upload is rejected and no evidence object is created. | Integrity | Must |
| REQ-INT-03 | If the client sends a SHA-256 and it does not match the server hash, the upload is rejected and no evidence object is created. | Integrity | Must |
| REQ-INT-04 | Ingest, download, and export each append a chain-of-custody event that records actor, hash, size, action, and UTC time. | Integrity | Must |
| REQ-INT-05 | Evidence bytes are immutable after a successful ingest. A replacement file is a new object, not an overwrite. | Integrity | Must |
| REQ-AUD-01 | Successful evidence access (view metadata, download, export) is written to the audit log. | Audit | Must |
| REQ-AUD-02 | Denied authorisation attempts (wrong role or wrong tenant) are written to the audit log with outcome = deny. | Audit | Must |
| REQ-AUD-03 | The audit log is append-only. Update and delete of audit events are not offered to any tenant role. | Audit | Must |
| REQ-AUD-04 | Each audit event includes actor, tenant, object (when applicable), action, outcome, and timestamp in UTC. | Audit | Must |
| REQ-EXP-01 | Only Admin may run tenant-wide bulk export. | Export | Must |
| REQ-EXP-02 | Reporter may export a report package only for assigned cases. | Export | Must |
| REQ-EXP-03 | Export packages contain only objects from the token’s tenant. | Export | Must |
| REQ-EXP-04 | Export packages include the SHA-256 of each included file as stored at export time. | Export | Must |
| REQ-API-01 | Tenant context is taken from the JWT `tenant_id`. A different tenant identifier in the body or query string is ignored. | API | Must |
| REQ-API-02 | The action requested must be allowed for the `role` claim in the token. | API | Must |
| REQ-API-03 | Missing, expired, or malformed Bearer tokens return HTTP 401 and do not return object bodies. | API | Must |
| REQ-UAT-01 | A tenant whose home region is US, UK, Brazil, or Australia can complete the assigned UAT scripts in that region. | UAT | Must |
| REQ-UAT-02 | Evidence uploaded in a home region remains stored in that region for the UAT window. | UAT | Must |

## Out of product scope for this catalogue

| Topic | Reason |
| --- | --- |
| Payment / billing | VaultGrid examples do not include a commercial storefront. |
| Mobile native clients | Web and API only in the current fictional backlog. |
| Physical chain-of-custody of devices | VaultGrid stores digital objects after ingest; device seizure process is out of scope. |
