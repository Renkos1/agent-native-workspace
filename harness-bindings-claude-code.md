# Harness bindings — Claude Code edition

status: TEMPLATE (read once at instantiation step 9; bindings are wiring, not law — the
mechanism semantics live in the pack files, and on any conflict the pack wins)

**The principle**: a binding is a pointer and a switch, never a mechanism. This page maps
each pack mechanism onto the harness feature that executes it natively; it redefines
nothing. When the harness updates, this page changes and the core does not. Portability
is preserved because the degradation column **is** the pack itself — a session on a
harness without these features follows the pack files as written and loses only
convenience, never semantics.

## The mapping (pack mechanism → Claude Code native)

| Pack mechanism (source of truth) | Claude Code binding | Degradation (no such feature) |
|---|---|---|
| Charter session-start injection (`AGENTS.md`; doc-map L0) | `CLAUDE.md` / `AGENTS.md` is read natively at session start — the manual reading order shrinks to doctrines + brief | paste the charter path as the session's first message |
| doc-map L1 trigger table | each on-demand doc wraps into a skill whose `description` carries its trigger row ("use when X") — injection becomes automatic | the trigger table stays manual; sessions consult it per protocol |
| Skill format (`skill.template.md`) | **already native** — the frontmatter (name / description-as-trigger) is the harness's own skill format, unchanged | skills stay markdown procedures, read on trigger |
| "start <id>" claim protocol (charter start-of-work) | a slash command (e.g. `/start <id>`) that opens the brief and executes its `## Start` | the human types "start <id>"; the session follows the charter protocol |
| Subagent fan-out, conclusions-only returns (ai-workflow §context discipline) | Agent tool / Explore agents with structured returns | single-session: gather serially, write state back to the brief between phases |
| Status-header validator, run casually | a Stop / session-close hook running `scripts/audit/check_status_headers.py` | run it by hand at session close (the protocol already says to) |
| Directory boundaries (charter hard rules §2) | a PreToolUse hook denying writes outside the brief's allowlist — discipline becomes enforcement | boundaries stay protocol; the doc-reality audit catches breaches after the fact |
| Quality gate before merge | pre-commit / PostToolUse hooks running the gate commands | the brief's Verify section, run manually |
| Exclusive-resource three-condition exception (**no standing pre-authorization**) | the relevant commands are **never** added to the permission allowlist — every touch prompts the human, which is exactly the required semantics | unchanged: the rule is already human-in-the-loop |
| Assistant-side memory holds pointers only; repo wins (ai-workflow §5) | the harness memory directory, constrained per that clause | no memory: everything already lives in-repo (the pack's default posture) |

## What must NOT be bound

- **Gate semantics** (TEST-CONSTITUTION): simulated-mode results never count toward the
  gate, regardless of what any hook reports green. A binding can *run* the gate; it can
  never redefine what green *means*.
- **Adjudication** (ledgers): batch sign-offs, polish sweeps, and the three-condition
  exception are human acts. No harness feature automates them away.
- **The session-start budget** (doc-map L0): native charter injection does not make the
  budget free — `CLAUDE.md` is still a fixed overhead every session pays; the
  only-shrinks ratchet applies to it identically.

## Adding a page for another harness

Copy this file; keep column 1 verbatim (it names the pack mechanisms — that column is
the contract); refill column 2 with the target harness's features. Column 3 needs no
edits — degradation is harness-independent, because it is the pack itself. A harness
with no matching feature gets "—" in column 2, not a workaround invented in prose.
