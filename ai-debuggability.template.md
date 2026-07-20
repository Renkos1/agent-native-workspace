# AI-debuggability charter — keep the codebase cheap for agents to debug

status: ACTIVE (inject on demand: debugging keeps hitting walls / designing a new module)

This project is primarily built and maintained by AI agents. **Controlled divergence
from existing implementations is allowed and encouraged whenever it makes the system
easier for agents to run, observe, and reason about**; necessary logic stays, but
necessary logic must never block verification of real user paths.

## The single root cause of wall-bumping

Every recurring debugging wall has the same shape: **knowledge underivable from the
code, stored where an agent cannot act on it** — a previous session's chat log, or a
prose ledger. So every run rebuilds that knowledge by hitting the wall again.

{{List 3-5 project examples — the traps invisible in code that get rediscovered every
time. Examples (origin workspace): the runnable service lives in the neighboring
worktree, not this directory; the dev process runs --watch and dies on any file edit; a
certain operation silently wipes remote firmware; a global mutable toggle gets flipped
back and forth by concurrent sessions.}}

## Rule 1 — encode non-derivable knowledge where agents can act (priority high → low)

1. **Executable**: types, `assert` preconditions, preflights that name the exact missing
   condition, tests. Never stales; agents can *run* it.
2. **Structured runtime signals**: stage-named logs (`stage=...`), error messages naming
   the failed precondition, primary errors separated from cleanup errors. Turns "failed
   somewhere" into "failed *here*, because X."
3. **A one-line rationale comment at the site**: only the *why* that truly cannot be
   made executable.
4. **A ledger entry**: fallback and index — worst locality; the agent must first know to
   go read it.

This is not "comment everything" — descriptive *what* comments are low-value and rot.
Convert hidden preconditions into preflight assertions and stage logs; save prose for
the non-executable *why*.

## Rule 2 — the harness owns the environment, not the agent

Agent debugging should spend its turns on the problem itself, not on hand-starting
services or rediscovering "which tree runs." Every live verification has a single entry
point that either guarantees its own preconditions or fails fast naming what is missing.

## Rule 3 — "model-debuggability" is a hard acceptance criterion

Every block's acceptance includes: **a model can locate and reproduce any bug in this
domain with zero manual operation.** As executable constraints:

1. Stable test anchors (`data-testid` and the like — style changes must not break them).
2. No swallowed errors: everything reaches console/logs + visible state; bare silent
   `catch {}` banned; failures have deterministic copy.
3. Visible state: a unified state layer readable by tools and scripts; any single state
   reproducible without booting the whole machine.
4. Types as the floor: pull whole classes of error forward to build time (the failure
   surface models catch best).
5. Determinism: source maps / readable stacks pointing at sources; no implicit side
   effects (edit here, break there).
6. Isolatable: any single view or module can be mounted and debugged alone, without the
   whole machine.
