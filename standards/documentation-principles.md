# QA Scribe documentation principles

- Document type: Working standard for this repository
- Standard(s) cited: ISO/IEC/IEEE 29119-3; IEEE 829-2008; ISO/IEC/IEEE 29119-4; ISTQB; IEEE 1044 (defect classification overlay)
- Product: VaultGrid (examples); any product the user supplies in intake (generated work)
- Cycle / version: Skill family v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Read this before editing a skill, template, or golden example.
2. Use it as the conflict resolver when a model wants to “simplify” a heading.
3. Paste into a team wiki only if the QA Manager adopts QA Scribe as the house style.
4. Delete this “How to use this file” block after paste.
5. Do not lower these rules to make generation faster.

---

## 1. Five generators, five jobs

| Generator | Job | Not its job |
| --- | --- | --- |
| Test strategy | How we test **this product** over months | Cycle dates, named hours, “Cycle 59” |
| Test plan | How we get **this cycle** out the door | Replacing the strategy; inventing a new test approach from scratch |
| Test cases | What we will execute | Strategy narrative; resource calendar |
| Design prompts | Generator contracts for the next case pack | Executable cases (those belong in the case pack) |
| Metrics / report | Are we ready (status) or what remains (completion) | A vanity dashboard that hides High residual risk |

Mixing strategy and plan is a **fail**. If the user asks for “a test plan with our long-term approach only”, produce a strategy and say so.

## 2. AI drafts. Standards constrain. Humans sign.

- The model fills headings and fields. It does not own severity, residual risk, or go / no-go.
- Every generated file is **Draft — human sign-off required** until a named human changes Status.
- If a required heading has no data: keep the heading and write `Not applicable: <reason>`. Never delete the heading.

## 3. Risk-first coverage

- Product risk (Critical, High, Medium, Low) drives case order, case priority, and report slicing.
- Permission-bypass, isolation, integrity, and audit paths are designed before cosmetic happy paths.
- Reports slice by risk, not by “N cases passed”.

## 4. Traceability

- Cases trace to `REQ-` and `RSK-` IDs from intake (VaultGrid: `product/requirements.md`, `product/risks.md`).
- Plans include a requirements traceability matrix (RTM).
- Do not invent requirement IDs, dates, or people’s names. Collect them with `qa-scribe-intake`.

## 5. Immediate usability

- Standalone Markdown a manager can paste into Confluence.
- Cases also as CSV with Xray-oriented columns.
- Short sentences. Senior tone. No emoji, no badge walls, no hype.

## 6. Confidentiality

- Examples use VaultGrid only.
- Learnings never contain employer names, real tickets, real hashes, or customer data.
- Refuse to generate from confidential intake that looks like real evidence or real client names. Ask the user to fictionalise.

## 7. Human gate (mandatory)

Stamp every output with generator name and skill version. End with a sign-off reminder: a QA Analyst, QA Manager, or the named approver in the plan **must** verify the document before it is used as a control of record.

## 8. Quality overlay (optional)

ISO/IEC 25010 product-quality characteristics may appear as a **checklist of what to evaluate** (functional suitability, security, reliability, and so on). They are not a document type. Do not title a strategy “ISO 25010 report”.
