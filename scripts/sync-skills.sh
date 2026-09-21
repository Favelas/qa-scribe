#!/usr/bin/env bash
# Keep .cursor/skills/ as an exact mirror of .claude/skills/ (canonical).
#
# Cursor and Claude Code read the same SKILL.md/reference.md/rubric.md
# format from their own dot-folder; there is no tool-specific content.
# Edit .claude/skills/ only, then run this script with --apply so the two
# trees never drift apart. --check (default) fails loudly and writes
# nothing -- this is what .githooks/pre-commit runs.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
canonical="$repo_root/.claude/skills"
mirror="$repo_root/.cursor/skills"
mode="${1:---check}"

case "$mode" in
  --check)
    if diff_output=$(diff -rq "$canonical" "$mirror" 2>&1); then
      echo "OK: $mirror matches $canonical"
      exit 0
    fi
    echo "$diff_output" >&2
    echo "FAIL: .cursor/skills/ is out of sync with .claude/skills/. Run: scripts/sync-skills.sh --apply" >&2
    exit 1
    ;;
  --apply)
    rm -rf "$mirror"
    cp -a "$canonical" "$mirror"
    echo "OK: $mirror now matches $canonical"
    ;;
  *)
    echo "usage: $0 [--check|--apply]" >&2
    exit 2
    ;;
esac
