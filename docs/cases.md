---
generator: qa-scribe-cases
skill_version: 1.0.0
---

# Document control

- Document type: Test Case Specification
- Standard(s) cited: IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification; ISO/IEC/IEEE 29119-4 / ISTQB (EP, BVA, NEG, ROLE-MATRIX)
- Product: VaultGrid (**fake data**)
- Cycle / version: Cycle 59
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Paste into Confluence; import `docs/cases.csv` to Xray.
2. Maya Chen executes in the **browser**. Expected results are on screen.
3. Delete this block after paste.
4. Isolation in one line: log in as Company A; search must **not** list Company B’s case title.
5. A Senior QA Analyst verifies before this pack is a control of record.

# Case pack — UI (10 cases)

Priority: Critical risk → 1; High → 2; Medium → 3; Low → 4. Risk-first order.

**Isolation (plain English):** Two companies, same website. NORTHWIND must not see GLOBEX titles.

Environment: Test, vaultgrid-2026.59.x, Chromium. Fake users: `nw-ro`, `nw-inv`, `nw-admin`, GLOBEX case title **`GLOBEX-CASE-RED`**.

---

### TC-ISO-001 — Company A search does not show Company B

| Field | Content |
| --- | --- |
| Identifier | TC-ISO-001 |
| Objective | NORTHWIND search must not list the GLOBEX case title. |
| Requirement | REQ-ISO-01 |
| Risk | RSK-ISO-01 |
| Priority | 1 |
| Technique | NEG; EP |
| Preconditions | Logged out. GLOBEX has case titled `GLOBEX-CASE-RED`. NORTHWIND Read-only `nw-ro` exists. |
| Inputs | User=`nw-ro`; company=NORTHWIND; search=`GLOBEX-CASE-RED` |
| Dependencies | None |
| Postconditions | Not applicable: search is read-only |

**Procedure**

1. Log in as `nw-ro`.
2. Open Search.
3. Type `GLOBEX-CASE-RED` and search.
4. Look at the result list (and the main case list).

**Expected:** Zero rows with `GLOBEX-CASE-RED`. Fail if that title appears. This is a **stopper** if it fails.

---

### TC-RBAC-001 — Read-only does not see Upload

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-001 |
| Objective | Read-only must not see the Upload button. |
| Requirement | REQ-RBAC-01 |
| Risk | RSK-RBAC-01 |
| Priority | 2 |
| Technique | ROLE-MATRIX; NEG |
| Preconditions | `nw-ro` on an assigned NORTHWIND case. |
| Inputs | Role=Read-only |
| Dependencies | None |
| Postconditions | Not applicable |

**Procedure**

1. Log in as `nw-ro`.
2. Open an assigned case.
3. Look for **Upload**.

**Expected:** Upload is not on the screen.

---

### TC-RBAC-002 — Investigator can Upload

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-002 |
| Objective | Investigator sees Upload and can add a small synthetic file. |
| Requirement | REQ-RBAC-02 |
| Risk | RSK-RBAC-01 (happy path) |
| Priority | 2 |
| Technique | ROLE-MATRIX; EP |
| Preconditions | `nw-inv` assigned to case NW-1. File `sample.txt` (fake, tiny). |
| Inputs | Role=Investigator |
| Dependencies | None |
| Postconditions | File listed on NW-1 |

**Procedure**

1. Log in as `nw-inv`.
2. Open NW-1.
3. Click Upload; choose `sample.txt`.
4. Confirm the file name on the case.

**Expected:** Upload visible. File name shown. No GLOBEX data.

---

### TC-RBAC-003 — Investigator does not see Manage users

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-003 |
| Objective | Investigator must not see Manage users. |
| Requirement | REQ-RBAC-03 |
| Risk | RSK-RBAC-02 |
| Priority | 2 |
| Technique | ROLE-MATRIX; NEG |
| Preconditions | `nw-inv` logged in. |
| Inputs | Role=Investigator |
| Dependencies | None |
| Postconditions | Not applicable |

**Procedure**

1. Log in as `nw-inv`.
2. Open the main menu.
3. Look for **Manage users**.

**Expected:** Manage users not visible.

---

### TC-RBAC-004 — Admin sees Manage users

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-004 |
| Objective | Admin can open Manage users for NORTHWIND only. |
| Requirement | REQ-RBAC-04 |
| Risk | RSK-RBAC-02 (control path) |
| Priority | 2 |
| Technique | ROLE-MATRIX; EP |
| Preconditions | `nw-admin`. |
| Inputs | Role=Admin |
| Dependencies | None |
| Postconditions | Not applicable |

**Procedure**

1. Log in as `nw-admin`.
2. Open **Manage users**.
3. Scan the user list for GLOBEX names.

**Expected:** Page opens. Only NORTHWIND users. No GLOBEX users.

---

### TC-AUTH-001 — Valid login

| Field | Content |
| --- | --- |
| Identifier | TC-AUTH-001 |
| Objective | Valid NORTHWIND user reaches the case list. |
| Requirement | REQ-AUTH-01 |
| Risk | RSK-ISO-01 (control: own list only) |
| Priority | 1 |
| Technique | EP |
| Preconditions | `nw-inv` password known (synthetic). |
| Inputs | Valid credentials |
| Dependencies | None |
| Postconditions | Session open |

**Procedure**

1. Open the login page.
2. Enter `nw-inv` and password.
3. Submit.

**Expected:** Case list for NORTHWIND. No GLOBEX titles.

---

### TC-AUTH-002 — Wrong password

| Field | Content |
| --- | --- |
| Identifier | TC-AUTH-002 |
| Objective | Wrong password does not open the case list. |
| Requirement | REQ-AUTH-02 |
| Risk | RSK-RBAC-01 |
| Priority | 2 |
| Technique | NEG; EP |
| Preconditions | Login page. |
| Inputs | `nw-inv` + wrong password |
| Dependencies | None |
| Postconditions | Still on login |

**Procedure**

1. Enter `nw-inv` and a wrong password.
2. Submit.

**Expected:** Error message. Case list not shown.

---

### TC-VAL-001 — Empty Case title does not save

| Field | Content |
| --- | --- |
| Identifier | TC-VAL-001 |
| Objective | Save with blank title must not create a case. |
| Requirement | REQ-VAL-01 |
| Risk | RSK-VAL-01 |
| Priority | 3 |
| Technique | BVA; NEG |
| Preconditions | `nw-inv` on New case. |
| Inputs | Title empty; other fields optional |
| Dependencies | None |
| Postconditions | No extra case |

**Procedure**

1. Log in as `nw-inv`.
2. Open New case.
3. Leave title empty; click Save.

**Expected:** Error on title. Case list count unchanged.

---

### TC-RBAC-005 — Read-only does not see Export

| Field | Content |
| --- | --- |
| Identifier | TC-RBAC-005 |
| Objective | Read-only must not see Export. |
| Requirement | REQ-RBAC-05 |
| Risk | RSK-RBAC-03 |
| Priority | 2 |
| Technique | ROLE-MATRIX; NEG |
| Preconditions | `nw-ro` on assigned case. |
| Inputs | Role=Read-only |
| Dependencies | None |
| Postconditions | Not applicable |

**Procedure**

1. Log in as `nw-ro`.
2. Open the assigned case.
3. Look for **Export**.

**Expected:** Export not visible. If visible but click produces no file, record DEF leftover (not a stopper if no file). Fail as High leftover for go-with-risks.

---

### TC-AUD-001 — Denied try in Activity log

| Field | Content |
| --- | --- |
| Identifier | TC-AUD-001 |
| Objective | After Read-only has no Upload, Admin log shows the session; if they had a hidden action attempt, log shows deny. |
| Requirement | REQ-AUD-01 |
| Risk | RSK-AUD-01 |
| Priority | 3 |
| Technique | NEG; EP |
| Preconditions | Complete TC-RBAC-001. Admin `nw-admin`. |
| Inputs | Actor=`nw-ro` |
| Dependencies | TC-RBAC-001 |
| Postconditions | Not applicable |

**Procedure**

1. As `nw-ro`, stay on the case with no Upload (already true).
2. Log in as `nw-admin`.
3. Open Activity log; filter user `nw-ro` for today.

**Expected:** View (or deny) rows for `nw-ro`. Fail if the log is empty for that user today.

**Human gate:** Maya executes; Fabian confirms TC-ISO-001 before UAT. AI does not sign.
