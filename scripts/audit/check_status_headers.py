#!/usr/bin/env python3
"""Status-header validator -- the deterministic half of two-mode reconciliation.

Stdlib-only, run casually: `python scripts/audit/check_status_headers.py [repo-root]`
(default root: current directory). Exit 0 = all green; exit 1 = violations listed.

Checks (briefs/ tree; archive/ is append-only and exempt):
  - every .md file carries a `status:` header within the first HEADER_WINDOW lines;
  - the status value is legal for its class (brief / ledger / doctrine);
  - a DOING brief has who/when filled (no placeholder dash);
  - a TODO or DOING brief embeds a `## Start` section (the charter's claim protocol).

The judgment-based half (doc-vs-reality) is `doc-reality-audit.md` in this directory.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# ---- CONFIG (the only part meant to be edited per project) -------------------
BRIEFS_DIR = "briefs"
SKIP_DIRS = {"archive"}  # append-only, kept exactly as closed
LEDGER_SUFFIX = "-LEDGER.md"
DOCTRINE_FILES = {  # doctrines living in briefs/ per the charter layout
    "ai-workflow.md",
    "TEST-CONSTITUTION.md",
    "doc-map.md",
    "ai-debuggability.md",
    "retrieval-optimized-code.md",
}
BRIEF_STATUSES = {"TODO", "DOING", "DONE"}
LEDGER_STATUSES = {"ACTIVE"}
DOCTRINE_STATUSES = {"ACTIVE"}
HEADER_WINDOW = 6  # `status:` must appear within the first N lines
PLACEHOLDER = "—"  # the em-dash used by brief.template's `who: -, when: -` line
# ------------------------------------------------------------------------------

STATUS_RE = re.compile(r"^status:\s*([A-Z]+)")
WHO_RE = re.compile(r"^who:")


def check_file(path: Path, rel: str, violations: list[str]) -> None:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    head = lines[:HEADER_WINDOW]

    status = None
    for line in head:
        m = STATUS_RE.match(line)
        if m:
            status = m.group(1)
            break
    if status is None:
        violations.append(f"{rel}: no `status:` header in the first {HEADER_WINDOW} lines")
        return
    if status == "TEMPLATE":  # templates are not live state
        return

    if path.name.endswith(LEDGER_SUFFIX):
        allowed, kind = LEDGER_STATUSES, "ledger"
    elif path.name in DOCTRINE_FILES:
        allowed, kind = DOCTRINE_STATUSES, "doctrine"
    else:
        allowed, kind = BRIEF_STATUSES, "brief"
    if status not in allowed:
        violations.append(f"{rel}: {kind} status `{status}` not in {sorted(allowed)}")
        return
    if kind != "brief":
        return

    if status == "DOING":
        who = next((ln for ln in head if WHO_RE.match(ln)), None)
        if who is None or PLACEHOLDER in who:
            violations.append(f"{rel}: DOING but who/when unfilled (claim protocol)")
    if status in ("TODO", "DOING") and not any(ln.startswith("## Start") for ln in lines):
        violations.append(f"{rel}: claimable ({status}) but has no `## Start` section")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    briefs = root / BRIEFS_DIR
    if not briefs.is_dir():
        print(f"FAIL: `{briefs}` does not exist (run from the repo root, or pass it)")
        return 1

    violations: list[str] = []
    n = 0
    for path in sorted(briefs.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.relative_to(briefs).parts[:-1]):
            continue
        n += 1
        check_file(path, path.relative_to(root).as_posix(), violations)

    for v in violations:
        print(f"  {v}")
    print(f"{'FAIL' if violations else 'OK'}: {n} files checked, {len(violations)} violation(s)")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
