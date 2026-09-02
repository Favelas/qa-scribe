#!/usr/bin/env python3
"""Copy golden examples into ready-to-paste/ without YAML generator frontmatter."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ready-to-paste"

COPIES = {
    "examples/strategy/vaultgrid-strategy.md": "vaultgrid-strategy.md",
    "examples/plan/cycle-59-plan.md": "cycle-59-plan.md",
    "examples/cases/rbac-tenant-isolation.md": "rbac-tenant-isolation.md",
    "examples/cases/hash-chain-of-custody.md": "hash-chain-of-custody.md",
    "examples/prompts/rbac-design-prompts.md": "rbac-design-prompts.md",
    "examples/reports/cycle-59-status.md": "cycle-59-status.md",
    "examples/reports/cycle-59-completion.md": "cycle-59-completion.md",
    "examples/rtm/cycle-59-rtm.csv": "cycle-59-rtm.csv",
    "examples/cases/export.csv": "xray-cases.csv",
}


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5 :].lstrip("\n")
    return text


def main() -> None:
    OUT.mkdir(exist_ok=True)
    readme = """# Ready to paste

- Document type: Confluence/Jira-cleaned goldens
- Standard(s) cited: Same as the source example in `examples/`
- Product: VaultGrid
- Cycle / version: Cycle 59 (except product-level strategy)
- Author role: Senior QA Analyst
- Status: Draft — human sign-off required

## How to use this file

1. Open the matching `.md` or `.csv` and paste into Confluence, Jira, or Xray.
2. Keep Document control. Delete the five-line how-to after paste if your wiki template already explains process.
3. Do not paste into a real evidence system.
4. These files are cleaned of Cursor YAML stamps only; content matches `examples/`.
5. A QA Analyst must verify before use as a control of record.

| File | Source |
| --- | --- |
| `vaultgrid-strategy.md` | `examples/strategy/vaultgrid-strategy.md` |
| `cycle-59-plan.md` | `examples/plan/cycle-59-plan.md` |
| `rbac-tenant-isolation.md` | `examples/cases/rbac-tenant-isolation.md` |
| `hash-chain-of-custody.md` | `examples/cases/hash-chain-of-custody.md` |
| `rbac-design-prompts.md` | `examples/prompts/rbac-design-prompts.md` |
| `cycle-59-status.md` | `examples/reports/cycle-59-status.md` |
| `cycle-59-completion.md` | `examples/reports/cycle-59-completion.md` |
| `cycle-59-rtm.csv` | `examples/rtm/cycle-59-rtm.csv` |
| `xray-cases.csv` | `examples/cases/export.csv` |
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")
    for src_rel, dest_name in COPIES.items():
        src = ROOT / src_rel
        raw = src.read_text(encoding="utf-8")
        if dest_name.endswith(".md"):
            raw = strip_frontmatter(raw)
        (OUT / dest_name).write_text(raw, encoding="utf-8")
        print(dest_name)


if __name__ == "__main__":
    main()
