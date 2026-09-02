---
generator: qa-scribe-cases
skill_version: 1.0.0
---

# Document control

- Document type: Defect report (IEEE 1044-style classification overlay)
- Standard(s) cited: IEEE 1044 (category + severity); ISTQB incident/defect reporting; traces to ISO/IEC/IEEE 29119-3 incident model in the strategy
- Product: VaultGrid (**fictional**; all data below is fake)
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Jira as the defect description (summary line = title). This is a **portfolio example**, not a live ticket.
2. Engineering and QA Manager use severity vs priority as written; do not inflate.
3. Delete this “How to use this file” block after paste.
4. Never replace the fictional hash, tenants, or IDs with real evidence or real customer data.
5. A Senior QA Analyst must verify a real defect write-up before it is used as a control of record.

# DEF-C59-004 — Truncated ingest can persist a partial object

**Fictional defect. Fake product, fake tenants, fake files, fake hashes.**

| Field | Value |
| --- | --- |
| Identifier | DEF-C59-004 |
| Detected in | vaultgrid-2026.59.1 (Test class) |
| Found by | Luis Ortega (QA Analyst) executing TC-INT-003 |
| Date found | 21 Sep 2026 (example timeline) |
| Requirement | REQ-INT-02 |
| Risk | RSK-INT-01 (Critical product risk: tampered or truncated file stored as evidence) |
| IEEE 1044 category | Data |
| Severity | 2 High (not 1 Critical: UI path still rejected; API path stored 40 bytes as complete) |
| Priority | 1 (fix before UAT and before exit) |
| Status at writing | Closed on vaultgrid-2026.59.2 (see completion report) |

## Summary

POST ingest with `Content-Length: 100` and a body of **40 bytes** sometimes created an evidence object of size 40 with a SHA-256 of those 40 bytes. REQ-INT-02 requires reject and **no object**.

## Environment

- Test class, tenants NORTHWIND / GLOBEX (**fake organisations**)
- Role: Investigator `nw-inv` (synthetic user)
- API: `POST /api/v1/cases/NW-1/evidence` (fictional path)
- File: 40 bytes of `0x01` (synthetic; not real evidence)

## Preconditions

Investigator assigned to case NW-1. Case exists. No object `EV-NW-TRUNC` before the call.

## Steps to reproduce

1. Authenticate as `nw-inv`; capture Bearer token.
2. Send POST ingest with header `Content-Length: 100` and a body exactly 40 bytes, then close the connection.
3. Record HTTP status.
4. List evidence on NW-1 created after T0.
5. If an object exists, GET metadata: size and SHA-256.

## Expected

- No HTTP 201.
- Zero new evidence objects.
- Optional: 400/422 and audit ingest outcome = deny.

## Actual (59.1)

- HTTP 201 on two of five API attempts (intermittent).
- Object size = 40.
- Stored hash = SHA-256 of the 40-byte body (`sha256:aaaaaaaa…` **fictional placeholder**, not a real evidence hash).
- UI upload of a truncated file still rejected (control path).

## Impact

A receiving agency could treat a **partial** file as the authentic original. Isolation is not broken. Audit still showed an ingest allow. That is why severity is **High**, not Critical isolation.

## Isolation / not

- Not reproduced on UI multipart upload (same build).
- Not reproduced when Content-Length equals body length.
- Reproduced only on API with Content-Length > bytes received.

## Suggested cause (for triage, not a root-cause sign-off)

Ingest handler committed the blob on stream end without comparing `bytes_received` to `Content-Length`.

## Fix verification (59.2)

Retest TC-INT-003: five truncated API attempts, zero objects, no 201. See Cycle 59 completion report.

**Human gate:** This ticket is an example. A QA Analyst must verify real defects against real builds before they are used as a control of record.
