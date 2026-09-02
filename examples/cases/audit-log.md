---
generator: qa-scribe-cases
skill_version: 1.0.0
---

# Document control

- Document type: Test Case Specification
- Standard(s) cited: IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification; ISO/IEC/IEEE 29119-4 / ISTQB (NEG, DT, ROLE-MATRIX)
- Product: VaultGrid
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Confluence; import audit rows from `examples/cases/export.csv` into Xray.
2. Luis Ortega executes after isolation cases exist so deny events are generated.
3. Delete this “How to use this file” block after paste.
4. Do not attempt to delete audit rows in production-like UAT.
5. A Senior QA Analyst must verify this pack before it is used as a control of record.

# Case pack — audit log

---

### TC-AUD-001 — Successful download is audited (allow)

| Field | Content |
| --- | --- |
| Identifier | TC-AUD-001 |
| Objective / test condition | Investigator download of assigned original writes audit outcome=allow with required fields. |
| Requirement | REQ-AUD-01; REQ-AUD-04 |
| Risk | RSK-AUD-01 (control path) |
| Priority | 2 |
| Technique | EP |
| Preconditions / environment | After a successful TC-RBAC-002-style download on `EV-NW-1`. |
| Inputs | Actor=`nw-inv`; tenant=NORTHWIND; action=download |
| Dependencies | TC-RBAC-002 or equivalent download |
| Postconditions | Not applicable: audit append-only |

**Procedure**

1. Perform an authorised download as `nw-inv`.
2. As `nw-admin`, query audit by object `EV-NW-1` and time window.
3. Open the newest download event.

**Expected outcomes**

- Event present with actor, tenant NORTHWIND, object, action, outcome=allow, timestamp UTC.
- Fail if the download succeeded and no event exists.

---

### TC-AUD-002 — Denied cross-tenant GET is audited

| Field | Content |
| --- | --- |
| Identifier | TC-AUD-002 |
| Objective / test condition | HTTP 404 cross-tenant read still writes outcome=deny on the **acting** tenant. |
| Requirement | REQ-AUD-02; REQ-RBAC-03 |
| Risk | RSK-AUD-01 |
| Priority | 2 |
| Technique | NEG; ROLE-MATRIX |
| Preconditions / environment | Execute immediately after TC-RBAC-004 or repeat that GET. |
| Inputs | Actor=`nw-ro`; GLOBEX UUID |
| Dependencies | TC-RBAC-004 |
| Postconditions | Not applicable |

**Procedure**

1. Repeat GET of GLOBEX UUID as `nw-ro` if needed.
2. As NORTHWIND Admin, filter audit by actor and object id.
3. Confirm GLOBEX Admin audit does **not** contain the NORTHWIND actor’s successful read.

**Expected outcomes**

- NORTHWIND audit: outcome=deny.
- GLOBEX audit: no allow for this actor.
- Fail if deny is missing.

---

### TC-AUD-003 — Home-tenant wrong-role 403 is audited

| Field | Content |
| --- | --- |
| Identifier | TC-AUD-003 |
| Objective / test condition | Read-only download deny is logged. |
| Requirement | REQ-AUD-02 |
| Risk | RSK-AUD-01 |
| Priority | 2 |
| Technique | NEG; DT |
| Preconditions / environment | Pair with TC-RBAC-006. |
| Inputs | Actor=`nw-ro`; action=download |
| Dependencies | TC-RBAC-006 |
| Postconditions | Not applicable |

**Procedure**

1. Trigger 403 download as `nw-ro`.
2. Admin query audit.

**Expected outcomes**

- outcome=deny, action=download (or equivalent).
- Fail if only allow events exist for this attempt.

---

### TC-AUD-004 — Admin cannot delete an audit event

| Field | Content |
| --- | --- |
| Identifier | TC-AUD-004 |
| Objective / test condition | No tenant role can update or delete audit events. |
| Requirement | REQ-AUD-03 |
| Risk | RSK-AUD-02 |
| Priority | 3 |
| Technique | NEG |
| Preconditions / environment | Known audit event id from TC-AUD-001. |
| Inputs | Role=Admin; method=DELETE or PATCH on audit event |
| Dependencies | TC-AUD-001 |
| Postconditions | Event still present |

**Procedure**

1. As `nw-admin`, DELETE (and PATCH) the audit event URL.
2. Re-GET the event.

**Expected outcomes**

- HTTP 403, 404, or 405.
- Event body unchanged.
- Fail on 204/200 delete.

**Human gate:** Luis Ortega executes. AI does not sign.
