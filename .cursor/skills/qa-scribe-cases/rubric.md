# Cases — fail-if-missing checklist

Canonical scored rubric: `standards/rubrics/cases.md`.

Human still signs. Goldens under `examples/cases/`.

Immediate fail:

- Missing IEEE 829 / 29119-3 field on any case
- Priority not derived from risk
- No CSV
- Isolation in scope but no permission-bypass / cross-tenant case
- Integrity in scope but no hash-mismatch or truncated-file case
- Invented REQ/RSK or real hashes
