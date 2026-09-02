# Intake YAML

- Document type: Intake instructions
- Standard(s) cited: Not a 29119 document; feeds the generators
- Product: VaultGrid (examples)
- Cycle / version: Skill family v1.0.0
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Copy an example in `inputs/examples/` and replace values. Do not invent people, dates, hours, or REQ/RSK IDs.
2. Paste the YAML into Cursor and name the skill (`qa-scribe-plan`, and so on).
3. If keys are missing, `qa-scribe-intake` will ask only for those keys.
4. Delete this “How to use this file” block if you paste these notes into a wiki.
5. Set `confidential: false`. If the material is real-client, stop and fictionalise.

---

Skills work if you paste YAML into chat. Saving a file is optional.

Optional validator:

```bash
python3 scripts/validate_intake.py inputs/examples/plan.cycle-59.yaml
```

| File | Generator |
| --- | --- |
| `examples/strategy.vaultgrid.yaml` | `qa-scribe-strategy` |
| `examples/plan.cycle-59.yaml` | `qa-scribe-plan` |
| `examples/cases.rbac.yaml` | `qa-scribe-cases` |
| `examples/report.cycle-59.yaml` | `qa-scribe-report` (completion flavour in file; set `flavour: status` for in-cycle) |

Never commit real evidence hashes, customer names, or employer ticket keys.
