# VaultGrid (fictional) — what it is

- Document type: Product brief
- Standard(s) cited: Not applicable: intake context, not a 29119-3 document
- Product: VaultGrid
- Cycle / version: Product-level
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. This is the only product in the goldens. **Fake product, fake data.**
2. Testers use the **web UI** (browser). Expected results are what you see on screen, not API codes.
3. Paste into Confluence only after Product agrees it is still fictional.
4. Delete this “How to use this file” block after paste.
5. Never put real customer cases or real files here.

---

VaultGrid is a **made-up** website where two companies keep their own investigation cases. Think: two customers on the same login page.

**Tenant isolation (plain English):** Company A and Company B both use VaultGrid. When you log in as Company A, you must **not** see Company B’s case names in search or in the case list. That is the whole idea.

**Roles (what you see on screen):**

| Role | What you use the site for |
| --- | --- |
| Admin | Manage users, Export, see Activity log |
| Investigator | Create cases, Upload files, search own company |
| Reporter | Export for assigned cases only |
| Read-only | View assigned cases. No Upload, no Export, no Manage users |

Two fake companies in examples: **NORTHWIND** (Company A) and **GLOBEX** (Company B).

Out of scope for this brief: mobile app, billing, real evidence, API status codes as the main oracle.
