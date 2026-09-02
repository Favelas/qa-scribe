# Standards map

- Document type: Citation map
- Standard(s) cited: See table (this file **is** the map)
- Product: VaultGrid (examples)
- Cycle / version: Skill family v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Copy the **Standard(s) cited** cell into the document-control block of the matching generator output.
2. Use the forbidden column as a review checklist.
3. Link this file from pull requests that change a template.
4. Delete this “How to use this file” block after paste into a wiki.
5. Do not cite a standard you did not follow in the body.

---

QA Scribe binds each generator to named standards so headings and fields are not a matter of taste.

| Document | QA Scribe skill | Standard(s) cited (mandatory) | Optional overlay | Forbidden in that document |
| --- | --- | --- | --- | --- |
| Test strategy | `qa-scribe-strategy` | ISO/IEC/IEEE 29119-3 Test Strategy; ISTQB (test strategy vs test plan; risk-based testing) | ISO/IEC 25010 characteristics as an evaluation checklist only | Cycle deadline, named hour allocations, “Cycle 59”, sprint calendar, named testers’ hours |
| Test plan | `qa-scribe-plan` | IEEE 829-2008 Test Plan (15 sections in order); ISO/IEC/IEEE 29119-3 Test Plan; ISTQB test plan / entry-exit / staffing | — | Strategy-only prose with no dates, no named allocation, no RTM |
| Test cases | `qa-scribe-cases` | IEEE 829 Test Case Specification; ISO/IEC/IEEE 29119-3 Test Case Specification; techniques from ISO/IEC/IEEE 29119-4 and ISTQB | Xray field names (tool schema, not a standard) | Vague UI “looks good” cases; mixed features in one case; missing REQ/RSK trace |
| Design prompts | `qa-scribe-prompts` | No ISO/IEEE standard for AI prompts. File must state: output MUST conform to IEEE 829 / ISO 29119-3 test case fields and ISO 29119-4 / ISTQB techniques. This file is a generator contract, not a test document. | — | Executable case packs presented as signed testware; missing forbidden-output list |
| Test status report | `qa-scribe-report` (flavour A) | ISO/IEC/IEEE 29119-3 Test Status Report; ISTQB progress reporting | IEEE 1044-style defect classification when listing defects | End-of-cycle go/no-go presented as if the cycle were closed |
| Test completion / summary report | `qa-scribe-report` (flavour B) | ISO/IEC/IEEE 29119-3 Test Completion Report; IEEE 829-2008 Test Summary Report; ISTQB summary reporting; residual risk vs exit criteria | IEEE 1044-style defect classification when listing defects | Fake 100% green when Crit/High residual risk remains |

## Technique tags (cases)

| Tag | Technique | Primary citations |
| --- | --- | --- |
| EP | Equivalence partitioning | ISO/IEC/IEEE 29119-4; ISTQB |
| BVA | Boundary value analysis | ISO/IEC/IEEE 29119-4; ISTQB |
| DT | Decision table | ISO/IEC/IEEE 29119-4; ISTQB |
| ST | State transition | ISO/IEC/IEEE 29119-4; ISTQB |
| NEG | Negative testing | ISTQB; used with 29119-4 invalid partitions |
| ROLE-MATRIX | Role × tenant permission matrix | Decision table applied to RBAC; ISTQB experience-based overlay on 29119-4 |
| INTEGRITY | Hash / size / custody checks | Domain application of EP/BVA/NEG to integrity requirements |

## Identifiers

See `standards/id-schemes.md`.
