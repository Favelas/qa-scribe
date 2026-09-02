# Plan skill — reference (IEEE 829 / 29119-3)

Use with `.cursor/skills/qa-scribe-plan/SKILL.md`. Skill version 1.0.0.

## What makes it a plan

Dates, named allocation, RTM. If any of the three is missing, it is not finished.

## Approach section

One to three pages that **apply** `STR-…` to this cycle: which levels run, which Critical/High risks are in, which techniques the case packs will use. Do not paste the full strategy.

## RTM columns (minimum)

`requirement_key,risk_keys,feature,test_case_ids,owner,result`

Result may be `planned` until execution. Do not mark pass in the plan.

## UAT windows

When intake lists US, UK, Brazil, Australia (or any regions), section 13 includes a row per region: start, end, coordinator, tenant/environment. Missing window = fail rubric P19.

## Suspension examples (cycle level)

- Severity 1 isolation or integrity defect in the build under test
- UAT region unavailable for the booked window with no fallback
- Loss of synthetic data set that invalidates in-flight execution

Resumption: new build number, defect verified, environment health check signed by the environment owner named in section 12.

## Golden regression

`docs/plan.md` must retain all 15 IEEE sections, a deadline, named hours, RTM, and approvals. After skill edits, re-read those headings.
