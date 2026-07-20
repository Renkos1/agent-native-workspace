# {{ID}} — {{one-line title}}

status: TODO
who: —, when: —
origin: {{who/when/why this was opened; cite the ledger entry or decision}}

## 1. Goal & background

{{What to achieve; why now; upstream/downstream dependencies. Reference code as
path:symbol, not line numbers.}}

## 2. Work items

{{Waves/items, each independently acceptable; mark exclusive-resource items
[exclusive-resource] so they queue serially into windows.}}

## 3. Boundaries

{{Directories this block may touch (an explicit file allowlist is better); forbidden
list. Gates requiring human authorization listed explicitly — "start" does not unlock
them; they are granted per occasion.}}

## 4. Verify

{{Executable command list, written here verbatim; the all-green bar. Example:
- `{{build/lint/typecheck commands}}`
- `{{this block's test command}}`
- `{{this block's one-command re-verification script under scripts/verify/}}`}}

## Start (saying "start {{ID}}" executes this section)

1. Enter via the charter's reading order; re-read this brief in full; status header
   TODO → DOING (who/when).
2. {{Suggested execution order: what first, and why (undisputed bugs first / shared
   foundations first, etc.).}}
3. {{Boundary restatement: gated parts still need per-occasion authorization; how to
   request the exclusive-resource window.}}
4. On delivery, write the status header back; evidence = commit + Verify output.

## 5. Delivery

Four pieces: code + tests + verify script + a one-line doc index. Missing any = not done.
If this brief belongs to a campaign, move it to `briefs/archive/` at close (kept exactly
as closed).
