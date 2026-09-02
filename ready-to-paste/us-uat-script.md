# Document control

- Document type: UAT script (acceptance / business fitness)
- Standard(s) cited: ISTQB acceptance testing; ISO/IEC/IEEE 29119-3 test levels (acceptance/UAT); traces REQ-UAT-01, REQ-UAT-02
- Product: VaultGrid (**fictional**; all data below is fake)
- Cycle / version: Cycle 59 — United States window
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Give this sheet to the regional coordinator (example: Jordan Hale). They execute; QA facilitates.
2. Sign the last table only if every step passed or a named residual is accepted.
3. Delete this “How to use this file” block after paste into Confluence.
4. Use **only synthetic files**. Never upload real evidence, real case names, or real customer data.
5. A business owner and a QA Analyst must verify a real UAT sheet before it is used as a control of record.

# US UAT — Investigator upload + Admin residency (fake tenant)

Window (example): 22–24 Sep 2026. Environment: US-uat. Tenant: **NORTHWIND-US** (fictional).

| Step | Role | Action | Expected | Pass? |
| --- | --- | --- | --- | --- |
| 1 | Investigator | Log in with synthetic US user | Home tenant is NORTHWIND-US; no GLOBEX data | |
| 2 | Investigator | Upload `uat-us-sample.bin` (synthetic, < 1 MB) to assigned case | Ingest succeeds; size and SHA-256 shown (fake file only) | |
| 3 | Admin | Open storage-region field for that object | Region = US | |
| 4 | Admin | Search for a GLOBEX filename from the fixture sheet | Zero results | |
| 5 | Coordinator | Confirm no production URL and no real evidence was used | Checklist signed | |

**Fail the window** if step 3 is not US or step 4 returns another tenant’s objects.

Sign-off (example names; fictional): Jordan Hale (coordinator), Fabian Velasquez (QA facilitation). Draft until humans sign.

**Human gate:** UAT fitness is a business signature. AI does not authorise go-live.
