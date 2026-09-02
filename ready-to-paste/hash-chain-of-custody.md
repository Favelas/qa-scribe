# Document control

- Document type: Test Case Specification
- Standard(s) cited: IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification; ISO/IEC/IEEE 29119-4 / ISTQB (EP, BVA, ST, NEG, INTEGRITY)
- Product: VaultGrid
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Confluence; import integrity rows from `examples/cases/export.csv` into Xray.
2. Luis Ortega executes; Senior QA Analyst reviews hash oracles.
3. Delete this “How to use this file” block after paste.
4. Use only synthetic files; never real evidence hashes.
5. A Senior QA Analyst must verify this pack before it is used as a control of record.

# Case pack — hash, size, chain of custody

Priority mapping: Critical → 1; High → 2. Ordered risk-first.

Synthetic hash in fixtures: `sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` (fictional). Do not replace with production hashes.

---

### TC-INT-001 — Valid ingest stores server SHA-256 and size

| Field | Content |
| --- | --- |
| Identifier | TC-INT-001 |
| Objective / test condition | A valid file upload stores server-computed SHA-256 and byte length. |
| Requirement | REQ-INT-01 |
| Risk | RSK-INT-01 (control path) |
| Priority | 1 |
| Technique | INTEGRITY; EP |
| Preconditions / environment | Investigator `nw-inv`; case NW-1; file `sample-32.bin` exactly 32 bytes. |
| Inputs | Role=Investigator; tenant=NORTHWIND; optional client hash omitted |
| Dependencies | None |
| Postconditions | Evidence object `EV-NW-INT-1` exists; teardown after pack or leave for custody cases |

**Procedure**

1. Authenticate as `nw-inv`.
2. Upload `sample-32.bin` to NW-1 with correct Content-Length 32.
3. Read stored hash and size from metadata API.
4. Download bytes and hash locally (test tool).

**Expected outcomes**

- HTTP 201 on ingest.
- Stored size = 32.
- Stored SHA-256 equals hash of downloaded bytes.
- Object created in NORTHWIND only.

---

### TC-INT-002 — Client/server hash mismatch rejected (hash-mismatch)

| Field | Content |
| --- | --- |
| Identifier | TC-INT-002 |
| Objective / test condition | If the client sends a SHA-256 that does not match the server hash of received bytes, ingest is rejected and no evidence object is created. |
| Requirement | REQ-INT-03 |
| Risk | RSK-INT-01 |
| Priority | 1 |
| Technique | INTEGRITY; NEG |
| Preconditions / environment | Investigator `nw-inv`; case NW-1. File bytes are 32 × 0x01. Client header/field `X-Content-SHA256` (or API field `client_sha256`) set to `sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb` (does not match bytes). |
| Inputs | Role=Investigator; tenant=NORTHWIND; token=valid; mismatched client hash; Content-Length correct |
| Dependencies | None |
| Postconditions | No new object; any partial blob deleted |

**Procedure**

1. Authenticate as `nw-inv`.
2. POST ingest with file bytes and the mismatched client hash.
3. Record HTTP status and error body.
4. Search NW-1 for new evidence created in this minute.
5. As Admin, confirm no custody ingest event with the mismatched hash as accepted.

**Expected outcomes**

- HTTP 400 or 422 (reject). **201/200 with object id is a fail.**
- Evidence list for NW-1 unchanged.
- No stored object whose hash equals the client fake hash.
- Optional audit: ingest outcome=deny or equivalent.

---

### TC-INT-003 — Truncated body vs Content-Length rejected (BVA)

| Field | Content |
| --- | --- |
| Identifier | TC-INT-003 |
| Objective / test condition | Bytes received fewer than declared Content-Length are rejected; no object created. |
| Requirement | REQ-INT-02 |
| Risk | RSK-INT-01 |
| Priority | 1 |
| Technique | BVA; NEG; INTEGRITY |
| Preconditions / environment | API client that can send Content-Length: 100 and only 40 bytes. |
| Inputs | Role=Investigator; tenant=NORTHWIND; Content-Length=100; body length=40 |
| Dependencies | None |
| Postconditions | No partial object |

**Procedure**

1. Authenticate as `nw-inv`.
2. POST ingest with Content-Length 100 and 40 bytes, then close.
3. Record status.
4. List evidence created after T0.

**Expected outcomes**

- Connection may error; application must not return 201.
- Zero new evidence objects.
- Fail if a 40-byte object is stored as if complete.

---

### TC-INT-004 — Zero-byte upload policy

| Field | Content |
| --- | --- |
| Identifier | TC-INT-004 |
| Objective / test condition | 0-byte body with Content-Length 0 is rejected as not valid evidence (product rule this cycle). |
| Requirement | REQ-INT-01 |
| Risk | RSK-INT-01 |
| Priority | 1 |
| Technique | BVA; EP |
| Preconditions / environment | Investigator upload API. |
| Inputs | Empty file; Content-Length 0 |
| Dependencies | None |
| Postconditions | Not applicable |

**Procedure**

1. Upload empty file to NW-1.
2. Record status and list.

**Expected outcomes**

- Reject (400/422).
- No object. If product later allows 0-byte, this case must be amended by a human — do not silently change expected result.

---

### TC-INT-005 — Custody event on ingest, download, export

| Field | Content |
| --- | --- |
| Identifier | TC-INT-005 |
| Objective / test condition | Ingest, download, and Admin export each append a custody event with actor, hash, size, action, UTC. |
| Requirement | REQ-INT-04 |
| Risk | RSK-INT-02 |
| Priority | 2 |
| Technique | ST; INTEGRITY |
| Preconditions / environment | Object from TC-INT-001 still present (`EV-NW-INT-1`) or recreate via TC-INT-001. |
| Inputs | Investigator download; Admin bulk export including this object |
| Dependencies | TC-INT-001 |
| Postconditions | Export package retained as test artefact (synthetic) |

**Procedure**

1. Read custody chain after ingest (baseline).
2. Download original as `nw-inv`.
3. As Admin, export package including `EV-NW-INT-1`.
4. Read custody chain.

**Expected outcomes**

- Three event types: ingest, download, export (names per API).
- Hash on each event equals stored hash.
- Timestamps UTC, monotonic for this object.
- Fail if download does not append an event.

---

### TC-INT-006 — Evidence bytes immutable; replacement is new object

| Field | Content |
| --- | --- |
| Identifier | TC-INT-006 |
| Objective / test condition | Re-upload does not overwrite `EV-NW-INT-1` bytes. |
| Requirement | REQ-INT-05 |
| Risk | RSK-INT-02 |
| Priority | 2 |
| Technique | ST; INTEGRITY |
| Preconditions / environment | `EV-NW-INT-1` exists. |
| Inputs | Different 32-byte file to same case |
| Dependencies | TC-INT-001 |
| Postconditions | Two objects; do not delete unless teardown |

**Procedure**

1. Record hash of `EV-NW-INT-1`.
2. Upload a different file to NW-1.
3. GET `EV-NW-INT-1` bytes and hash.

**Expected outcomes**

- Original hash unchanged.
- New object id for the second file.
- Fail if original bytes changed.

**Human gate:** Luis Ortega executes; Amina Diallo consulted on any Severity 1. AI does not sign.
