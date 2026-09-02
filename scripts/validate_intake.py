#!/usr/bin/env python3
"""Validate QA Scribe intake YAML. Skills still work if the user pastes YAML into chat."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

STRATEGY_FORBIDDEN = {
    "cycle_deadline",
    "named_hours",
    "sprint_calendar",
    "tester_hours",
}

REQUIRED = {
    "strategy": [
        "product_name",
        "item_under_test",
        "objectives",
        "in_scope",
        "out_of_scope",
    ],
    "plan": [
        "product_name",
        "cycle_id",
        "strategy_id",
        "test_items",
        "features_in",
        "features_out",
        "people",
        "schedule",
        "risks_this_cycle",
        "requirements",
    ],
    "cases": ["product_name", "area", "requirements", "risks"],
    "prompts": ["product_name", "area"],
    "report": ["product_name", "cycle_id", "plan_id", "flavour", "counts_by_risk"],
}


def fail(msg: str) -> int:
    print(f"FAIL: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate QA Scribe intake YAML")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    if yaml is None:
        return fail("PyYAML is not installed. pip install pyyaml  — or paste YAML into chat; skills do not require this script.")
    if not args.path.is_file():
        return fail(f"not a file: {args.path}")
    data = yaml.safe_load(args.path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return fail("root must be a mapping")
    if data.get("confidential") is True:
        return fail("confidential: true — fictionalise before generating; do not store client data")
    doc = data.get("document")
    if doc not in REQUIRED:
        return fail("document must be one of: strategy, plan, cases, prompts, report")
    for key in REQUIRED[doc]:
        if key not in data or data[key] in (None, "", [], {}):
            return fail(f"missing required key for {doc}: {key}")
    if doc == "strategy":
        for bad in STRATEGY_FORBIDDEN:
            if bad in data:
                return fail(f"strategy intake must not include {bad}")
        sched = data.get("schedule") or {}
        if isinstance(sched, dict) and sched.get("cycle_deadline"):
            return fail("strategy intake must not include schedule.cycle_deadline")
    if doc == "plan":
        people = data["people"]
        if not isinstance(people, list) or not people:
            return fail("plan.people must be a non-empty list")
        for i, person in enumerate(people):
            for k in ("name", "role", "owns", "hours"):
                if k not in person:
                    return fail(f"people[{i}] missing {k}")
        sched = data["schedule"]
        if not isinstance(sched, dict) or "cycle_deadline" not in sched:
            return fail("plan.schedule.cycle_deadline is required")
        if data.get("regions") and not data.get("uat_windows"):
            return fail("regions present but uat_windows missing")
    if doc == "report":
        flavour = data["flavour"]
        if flavour not in ("status", "completion"):
            return fail("flavour must be status or completion")
        if flavour == "completion" and not data.get("recommendation"):
            print("WARN: completion without recommendation — generator will draft from residual risk rules", file=sys.stderr)
        if flavour == "status" and data.get("recommendation"):
            return fail("status flavour must not include a final recommendation")
    print(f"OK: {args.path} ({doc})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
