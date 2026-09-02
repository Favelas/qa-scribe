# Cases — fail-if-missing checklist

Canonical scored rubric: `standards/rubrics/cases.md`.

Human still signs. Goldens under `docs/`.

Immediate fail:

- Missing IEEE 829 / 29119-3 field on any case
- Priority not derived from risk
- No CSV
- Isolation in scope but no permission-bypass / cross-tenant case
- Isolation in scope but no “A must not see B in search” case
- Integrity in scope (only if intake has it) but no fail-to-save / incomplete upload case
- Invented REQ/RSK or real hashes
