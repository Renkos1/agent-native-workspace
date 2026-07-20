# {{PROJECT}} — workspace charter

This workspace is {{one line: what the project is + what this workspace does}}. This file
applies to sessions of any model (Claude / GPT / …; no proprietary tooling assumed).

**Session-start reading order: this file → active doctrines ({{doctrine list, ≤3-4
files}}) → the claimed brief.**
The kanban is one command: `grep -h "^status:" briefs/*.md` (backed by the status-header
validator; run it casually).
Document tiers & injection timing: `doc-map.md` — a new document passes through it before
landing; the session-start reading set only shrinks.

**Start-of-work protocol**: every brief carrying claimable work must embed a `## Start`
section — a self-contained start prompt (claim action, execution order, boundary
restatement, verify, status write-back). The human saying "**start <id>**" is the claim
instruction, equivalent to pasting that section: the session enters via the reading
order → opens the brief → executes its `## Start`. **"Start" unlocks no gates** —
anything the brief marks as requiring human authorization still needs it explicitly,
that time.

## Layout

- `{{code location}}` — code source of truth ({{worktree/branch/junction notes; where
  code vs docs each get committed}}).
- `briefs/` — active doctrines + live briefs + ledgers; closed campaigns in
  `briefs/archive/` (kept exactly as closed).
- `contracts/` — single source of truth for cross-tier contracts + test vectors.
- `docs/` — `conventions/` · {{domain-facts dir}} · `runbooks/` · `guides/`;
  `archive/` and `handoff/` are append-only.
- `scripts/` — `dev/` · `verify/` (one-command re-verification; one of the four delivery
  pieces) · `release/` · `audit/` (reconciliation).
- `MAP.md` — generated repo map (script-rendered; hand-editing forbidden).

## Canonical names (always these)

{{Name table: one canonical name per tier/system, synonyms banned repo-wide. Example:
client / cloud / gateway / … Split confusable concepts explicitly (e.g. "instrument
FPGA" vs "user FPGA" — never the bare word "FPGA").}}
Vocabulary authority: `{{glossary path}}`.

## Hard rules

1. **Quality gate**: {{the commands every commit must keep green, e.g. build + lint +
   typecheck}}. Not green, not merged.
2. **Boundaries**: {{which directories each track may touch; forbidden zones (read-only
   reference trees are never written)}}.
3. **Exclusive-resource safety**: see `ai-workflow.md` §safety — touch only
   {{allowlisted environments}} by default; {{production / exclusive resources}} are
   **exception-by-exception under the three conditions; pre-authorization does not
   exist**.
4. **git**: {{push rules: which branches the AI may push; branches never to touch;
   hotfix branches fork from the deployed commit}}.
5. **Ambiguity never stops work**: log to `briefs/AMBIGUITY-LEDGER.md`, keep moving.
6. **Documentation discipline**: state lives in brief headers and ledgers; no long
   conversational prose; archive is append-only.

## Frozen-tree table (anti-drift)

| Tree | Status |
|---|---|
| {{active dev line}} | **The only active dev line**; release source |
| {{legacy / frozen reference}} | Frozen archive, read-only; {{conditions under which merging back is allowed}} |
