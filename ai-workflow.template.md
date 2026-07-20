# The AI production process (ai-workflow)

Applies to: every AI session in this workspace (any model). Goal: convert AI parallel
capacity into throughput.
**Scarce resources = {{exclusive-resource windows}} · human adjudication bandwidth ·
context budget.** Code generation volume is not the bottleneck — do not schedule by
human-labor instincts. Document tiers & injection timing are defined once in `doc-map.md`
(not repeated here).

## Session protocol

1. **Start**: follow the charter's reading order; never re-excavate recorded facts;
   locate by index jumps (`MAP.md` + glossary) — a whole-repo scan is a smell worth
   reporting.
2. **Claim**: "start <id>" = execute that brief's `## Start` section; **"start" unlocks
   no gates**.
3. **Close**: brief header status + ledger rows + evidence (commit / quality-gate
   output); repeatable procedures get promoted to scripts or skills. Leaving facts only
   in the conversation is forbidden.
4. **Context discipline**: fan information-gathering out to subagents (structured
   returns; only conclusions enter the main context); near the context ceiling stop
   delegating — converge, write state back, hand off. **Brief + status line is the only
   handoff medium.**
5. **Assistant-side persistent memory** (model-private memory and the like) holds only
   pointers and conclusions; the source of truth stays in-repo; on conflict the repo
   wins — fix the memory in passing.

## Work-block protocol

- One block = one brief, self-contained and cold-startable, independent of chat history
  (template: `brief.template.md`).
- **Four-piece delivery: code + tests + verify script + a one-line doc index. Missing
  any = not done.**
- Acceptance = a demo + metrics (a reportable unit).

## Parallelism rules

- `contracts/` is the parallel boundary: two sessions each owning one side of a contract
  can work with zero coordination; changing a contract = changing its consumers in the
  same move (or a versioned transition).
- Blocks touching the same file never run in parallel; multi-session work uses git
  worktrees.
- `[exclusive-resource]` blocks queue serially; batch them into a single window when
  possible.

## Safety boundaries (hard rules — fill per project; instantiations may only be equal or stricter)

- Default allowlist: {{allowlisted environments/devices}} only; anything else needs an
  explicit brief allowlist or the human naming it this time.
- **{{Production / exclusive resources}} are untouchable by default** — an exception
  requires all three, **re-confirmed every single time (no standing pre-authorization)**:
  ① a rollback-capable backup of what is being replaced; ② a live check confirming no
  real usage is running right now; ③ the human explicitly approving **this specific
  operation, this time**.
- Destructive steps dry-run first; automatic backup before writes is the floor.
- {{Domain trap list: the environment traps that will be re-stepped-on unless written
  down, each pointing at its skill. Examples (origin workspace): after flashing you must
  reboot once more before trusting the link; a certain routine operation silently wipes
  remote firmware.}}

## Campaign session economics

- **One session = one brief.** At start, read only the reading-order files + the files
  the brief lists; whole-repo archaeology is forbidden.
- **Division of labor**: strong-model sessions do design / ambiguity judgment / review
  gates / {{exclusive-resource}} result interpretation; mechanical waves run on lighter
  models following the brief, with the strong model spot-checking each wave (≥1 block
  fully reviewed per wave).
- **Ambiguity never stops work**: fix-forward by default, log it, batch for human
  adjudication (ledger split: `ledgers/README.md`).

## Promotion candidates (executable beats prose)

{{"Procedure → skill" candidate list. Rule: only procedures that have actually run to
completion get promoted; fossilizing unverified steps is forbidden.}}
