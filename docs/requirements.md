# Requirements (short catalogue)

- Document type: Requirements catalogue
- Standard(s) cited: Traceability source for IEEE 829 / 29119-3; not itself a 29119 document
- Product: VaultGrid (**fake data**)
- Cycle / version: Product-level / Cycle 59 tests this set
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Every test case traces to a `REQ-` ID here. Do not invent IDs.
2. These are **UI** shall-statements (buttons, lists, messages).
3. Delete this “How to use this file” block after wiki paste.
4. Fake companies and users only.
5. A Product Owner confirms the list before a real project uses a copy.

| ID | What the product must do (you can see it in the UI) | Priority |
| --- | --- | --- |
| REQ-AUTH-01 | Valid user can log in and land on the case list for their company. | Must |
| REQ-AUTH-02 | Wrong password shows an error and does not open the case list. | Must |
| REQ-ISO-01 | Logged-in NORTHWIND user must not see GLOBEX case titles in Search or in the case list. | Must |
| REQ-RBAC-01 | Read-only must not see the **Upload** button. | Must |
| REQ-RBAC-02 | Investigator must see **Upload** and can add a file to an assigned case. | Must |
| REQ-RBAC-03 | Investigator must not see **Manage users**. | Must |
| REQ-RBAC-04 | Admin must see **Manage users** and can open that page. | Must |
| REQ-VAL-01 | Save with an empty Case title must show an error and must **not** create a case. | Must |
| REQ-RBAC-05 | Read-only must not see the **Export** button. | Must |
| REQ-AUD-01 | If a user tries an action they cannot do, Activity log (Admin) shows that attempt. | Must |
