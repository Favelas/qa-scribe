# Document control

- Document type: Test Case Specification
- Standard(s) cited: IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification; ISO/IEC/IEEE 29119-4 / ISTQB techniques (EP, DT, ST, NEG, ROLE-MATRIX)
- Product: VaultGrid
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Review in Confluence with this Markdown; import the matching rows from `examples/cases/export.csv` (RBAC rows) into Xray project VG.
2. Senior QA Analyst signs the pack before execution; Maya Chen owns execution.
3. Delete this “How to use this file” block after paste; keep Document control and every case field.
4. Do not execute against production or real evidence tenants.
5. A Senior QA Analyst must verify traces, expected HTTP codes, and priority before this pack is used as a control of record.

# Case pack — RBAC and tenant isolation

Priority mapping: Critical risk → 1; High → 2; Medium → 3; Low → 4. Cases are ordered risk-first.

Environment (all cases unless noted): Test class, build vaultgrid-2026.59.x, tenants NORTHWIND and GLOBEX, Chromium + API client.

---

### TC-RBAC-001 — Admin cannot read GLOBEX evidence via UI search

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-001 |
| Objective / test condition | A NORTHWIND Admin must not retrieve GLOBEX evidence metadata via tenant search. |
| Requirement | REQ-RBAC-01 |
| Risk | RSK-ISO-01 |
| Priority | 1 |
| Technique | ROLE-MATRIX; NEG |
| Preconditions / environment | Admin user `nw-admin` on NORTHWIND. GLOBEX has evidence `EV-GLOBEX-A` with a unique filename `globex-seal-A.bin`. |
| Inputs | Role=Admin; tenant=NORTHWIND; token=valid JWT for nw-admin; search string=`globex-seal-A.bin` |
| Dependencies | None |
| Postconditions | Not applicable: search is read-only |

**Procedure**

1. Authenticate as `nw-admin` (NORTHWIND Admin).
2. Open evidence search in the home tenant.
3. Submit search `globex-seal-A.bin`.
4. Capture the result list and any object IDs returned.

**Expected outcomes**

- Zero results for `globex-seal-A.bin`.
- No GLOBEX object IDs in the payload.
- HTTP 200 on search is acceptable if the list is empty; HTTP 200 with GLOBEX metadata is a fail.

---

### TC-RBAC-002 — Investigator download of assigned NORTHWIND original (happy path)

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-002 |
| Objective / test condition | Investigator assigned to case NW-1 can download original bytes for that case. |
| Requirement | REQ-RBAC-02 |
| Risk | RSK-ISO-01 (control: authorised path still works) |
| Priority | 1 |
| Technique | ROLE-MATRIX; EP |
| Preconditions / environment | Investigator `nw-inv` assigned to case NW-1; evidence `EV-NW-1` uploaded and healthy. |
| Inputs | Role=Investigator; tenant=NORTHWIND; token=valid; object=`EV-NW-1` |
| Dependencies | None |
| Postconditions | Download counted in custody; file bytes unchanged |

**Procedure**

1. Authenticate as `nw-inv`.
2. Open case NW-1.
3. Download original for `EV-NW-1`.
4. Record HTTP status and byte length.

**Expected outcomes**

- HTTP 200.
- Byte length matches ingest size.
- Object remains in NORTHWIND only.

---

### TC-RBAC-003 — Investigator API GET on GLOBEX UUID returns 404 (permission-bypass)

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-003 |
| Objective / test condition | An Investigator in NORTHWIND who presents a valid GLOBEX evidence UUID must receive HTTP 404 with no metadata (permission-bypass / IDOR). |
| Requirement | REQ-RBAC-03; REQ-RBAC-01; REQ-API-02 |
| Risk | RSK-ISO-01; RSK-API-01 |
| Priority | 1 |
| Technique | ROLE-MATRIX; NEG |
| Preconditions / environment | Valid GLOBEX UUID `11111111-aaaa-4bbb-8ccc-222222222222` exists. NORTHWIND Investigator `nw-inv` has a valid token. Tester knows the UUID by fixture sheet, not by UI. |
| Inputs | Role=Investigator; tenant=NORTHWIND; Authorization=Bearer nw-inv; path=`/api/v1/evidence/11111111-aaaa-4bbb-8ccc-222222222222` |
| Dependencies | None |
| Postconditions | Not applicable: no object created |

**Procedure**

1. Obtain Bearer token for `nw-inv` (NORTHWIND, Investigator).
2. Send GET `/api/v1/evidence/11111111-aaaa-4bbb-8ccc-222222222222` with that token.
3. Record status, body, and headers.
4. As NORTHWIND Admin, query audit for this request.

**Expected outcomes**

- HTTP **404**.
- Body contains no filename, hash, tenant id, or case id of the GLOBEX object.
- Audit event in **NORTHWIND**: action=read_evidence, outcome=deny, object id as requested.

---

### TC-RBAC-004 — Cross-tenant evidence UUID returns 404 (Read-only; ROLE-MATRIX / NEG)

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-004 |
| Objective / test condition | A Read-only user in tenant NORTHWIND, calling GET evidence with a UUID that belongs to tenant GLOBEX, receives HTTP 404, an empty body (no metadata), and a deny audit event on NORTHWIND. |
| Requirement | REQ-RBAC-03; REQ-RBAC-01 |
| Risk | RSK-ISO-01; RSK-ISO-02 |
| Priority | 1 |
| Technique | ROLE-MATRIX; NEG |
| Preconditions / environment | Read-only `nw-ro` on NORTHWIND. GLOBEX evidence UUID `11111111-aaaa-4bbb-8ccc-222222222222` exists. API base as Test class. |
| Inputs | Role=Read-only; tenant=NORTHWIND; token=Bearer for nw-ro; object UUID of GLOBEX; no tenant field in body |
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

---

### TC-RBAC-005 — Foreign UUID vs unknown UUID same 404 shape

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-005 |
| Objective / test condition | Response code and body schema for another-tenant UUID versus a never-issued UUID are not distinguishable. |
| Requirement | REQ-RBAC-03 |
| Risk | RSK-ISO-02 |
| Priority | 2 |
| Technique | EP; NEG |
| Preconditions / environment | Same as TC-RBAC-004; compare captured bodies. |
| Inputs | Role=Investigator; tenant=NORTHWIND; two UUIDs: GLOBEX real vs random |
| Dependencies | TC-RBAC-003 (fixture UUID) |
| Postconditions | Not applicable |

**Procedure**

1. GET foreign existing UUID as `nw-inv`.
2. GET random UUID as `nw-inv`.
3. Diff status codes and JSON schema (keys only).

**Expected outcomes**

- Both 404.
- Same key set in body (or both empty).
- No `exists: true` or tenant field.

---

### TC-RBAC-006 — Read-only denied original download (home tenant)

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-006 |
| Objective / test condition | Read-only assigned to NW-1 cannot download original bytes. |
| Requirement | REQ-RBAC-05 |
| Risk | RSK-RBAC-01 |
| Priority | 2 |
| Technique | ROLE-MATRIX; DT; NEG |
| Preconditions / environment | `nw-ro` assigned to NW-1; `EV-NW-1` exists. |
| Inputs | Role=Read-only; tenant=NORTHWIND; action=download original |
| Dependencies | None |
| Postconditions | Not applicable |

**Procedure**

1. Authenticate as `nw-ro`.
2. Open NW-1 and request original download for `EV-NW-1`.
3. Record HTTP status.
4. Check NORTHWIND audit for deny.

**Expected outcomes**

- HTTP **403** (home tenant, wrong role).
- Bytes not returned.
- Audit outcome=deny.

---

### TC-RBAC-007 — Investigator cannot self-assign Admin

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-007 |
| Objective / test condition | Investigator cannot change their own role to Admin. |
| Requirement | REQ-RBAC-04 |
| Risk | RSK-RBAC-01 |
| Priority | 2 |
| Technique | DT; NEG |
| Preconditions / environment | `nw-inv` valid; role-admin API known. |
| Inputs | Role=Investigator; body role=Admin; target user=self |
| Dependencies | None |
| Postconditions | Role of `nw-inv` still Investigator |

**Procedure**

1. Authenticate as `nw-inv`.
2. PUT/PATCH own role to Admin.
3. Re-read token or `/me` role.
4. Confirm audit deny.

**Expected outcomes**

- HTTP 403.
- Role remains Investigator.
- Audit deny on role_change.

---

### TC-RBAC-008 — Revoked Investigator token cannot download

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-008 |
| Objective / test condition | After Admin revokes Investigator, a previously issued token must not download originals. |
| Requirement | REQ-RBAC-08 |
| Risk | RSK-RBAC-02 |
| Priority | 2 |
| Technique | ST; NEG |
| Preconditions / environment | `nw-inv` assigned; token captured **before** revoke. |
| Inputs | Old Bearer token; object=`EV-NW-1` |
| Dependencies | TC-RBAC-002 (happy path baseline) |
| Postconditions | User remains Read-only or disabled per fixture; do not leave an extra Admin |

**Procedure**

1. Capture Bearer token for `nw-inv`.
2. As `nw-admin`, revoke Investigator (set Read-only or disable).
3. GET download with the **old** token.
4. Record status.

**Expected outcomes**

- HTTP 401 or 403 (either is acceptable if bytes are not returned; 200 is a fail).
- No original bytes.
- Audit deny or unauthenticated, as designed.

---

### TC-RBAC-009 — Body tenant_id GLOBEX ignored for NORTHWIND token

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-009 |
| Objective / test condition | JSON body `tenant_id=GLOBEX` does not switch context for a NORTHWIND token. |
| Requirement | REQ-API-01 |
| Risk | RSK-API-01 |
| Priority | 2 |
| Technique | NEG; EP |
| Preconditions / environment | API search or list endpoint that historically accepted tenant in body. |
| Inputs | Bearer NORTHWIND; body `{"tenant_id":"GLOBEX"}` |
| Dependencies | None |
| Postconditions | Not applicable |

**Procedure**

1. Authenticate as `nw-inv`.
2. POST/GET list with body tenant GLOBEX.
3. Inspect returned objects’ tenant.

**Expected outcomes**

- Only NORTHWIND objects or empty list.
- No GLOBEX objects.
- No 500.

---

### TC-RBAC-010 — Reporter cannot open unassigned case

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-010 |
| Objective / test condition | Reporter assigned to NW-1 cannot open NW-2. |
| Requirement | REQ-RBAC-06 |
| Risk | RSK-EXP-01 |
| Priority | 2 |
| Technique | ROLE-MATRIX; NEG |
| Preconditions / environment | `nw-rep` assigned only to NW-1; NW-2 exists in NORTHWIND. |
| Inputs | Role=Reporter; case=NW-2 |
| Dependencies | None |
| Postconditions | Not applicable |

**Procedure**

1. Authenticate as `nw-rep`.
2. GET case NW-2 (UI or API).
3. Record status and body.

**Expected outcomes**

- HTTP 403 or 404 per product rule for **home-tenant** unassigned (document actual; Cycle 59 oracle: **403**).
- No investigator notes from NW-2.
- Audit deny.

**Human gate:** Maya Chen executes; Fabian Velasquez confirms 404-not-403 on cross-tenant before UAT. AI does not sign.
