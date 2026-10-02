# Matrix — fail-if-missing checklist

Canonical scored rubric: `standards/rubrics/risk-based-test-matrix.md`.

Human still signs. This generator is Draft-only until QA Manager confirms allocation depth and Product Owner acknowledges residual None/Planned on High.

Immediate fail:

- Invented `TC-` or `RSK-` IDs (Case IDs must be existing or Planned)
- Invented numeric probability/impact score
- Missing Stopper? or REQ IDs on an allocation row
- Critical/High ranked after Medium/Low
- Critical with None across types or no allocation row
- Named hours, cycle deadline, or sprint calendar
- Matrix presented as confirmed fact while the source register is still a candidate
- File used as a substitute for the risk register, cycle RTM, or role × screen matrix
- Required heading dropped instead of `Not applicable: <reason>`
