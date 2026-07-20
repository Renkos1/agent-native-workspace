# doc-vs-reality audit — the judgment half of two-mode reconciliation

status: TEMPLATE (a prompt, not a script — paste it to a session at campaign close; the
deterministic half is `check_status_headers.py`, run casually anytime)

When: **mandatory at campaign close**; optional before a major refactor. Read-only — the
audit files findings; it never fixes in place. Findings feed the next hygiene wave under
doc-map's rule: fix the document before doing the work.

## The prompt (paste to the auditing session)

> Run a read-only doc-vs-reality audit of this workspace. Fan out one subagent per
> document class below (subagents unavailable → run the classes serially yourself; the
> classes are the unit of coverage, not the parallelism). Each returns **findings only**
> — structured rows, no prose. You merge, dedup, and file the result.

## Classes × checks (one subagent each)

1. **Charter & doctrines**: every referenced path exists; every quoted command exists
   (probe `--help`, never execute for effect); canonical-name table vs actual
   identifiers/filenames (sample, don't exhaust).
2. **Contracts**: each contract's consumers still match its signatures and test vectors;
   orphan contracts (nothing names them); consumers renamed away from their contract.
3. **Briefs & ledgers**: status headers vs content (a DONE brief whose Verify output is
   absent; a DOING brief nobody owns); ledger rows stuck in LOGGED/DOING past their
   batch point; ledger hard-constraint headers still true.
4. **Skills & runbooks**: steps reference live commands and paths; trap entries still
   match the environment (static check only — destructive steps are never executed).
5. **doc-map itself**: orphan documents (files outside the tier table); L1 trigger rows
   pointing at dead paths; the session-start set matching the charter's reading order.

## Findings format (one row each)

`file · claim · reality · severity (BROKEN / DRIFT / ORPHAN) · suggested fix`

- **BROKEN** — a doc asserts something false enough to misdirect a session; blocks
  campaign close until fixed.
- **DRIFT** — stale but survivable; schedule into the hygiene wave.
- **ORPHAN** — outside the tier table; register into L1 or archive (doc-map hygiene).
