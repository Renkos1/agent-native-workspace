# agent-native-workspace — a workspace template pack for AI-led engineering

Project-agnostic mechanism templates extracted from a real production project (an FPGA
remote-lab platform, 2026-07). For any software or hardware project where AI sessions are
the primary workforce and humans adjudicate. **Scope: greenfield founding** — the
instantiation steps assume a brand-new project whose code is written under the glossary
from day one; retrofitting an existing codebase is not covered (yet).

`{{...}}` marks fill-in variables; replace "Example:" passages with your project's facts.

> **The one-line bootstrap (paste to any model — the only thing a human needs to remember):**
> "Read `<this directory>/README.md`, follow the instantiation steps; you proactively
> drive the founding conversations in steps 2-3 (survey → product → architecture)."
> The source of truth for behavioral protocols like that is **this README** — never any
> single assistant's private memory. Swap models and nothing is lost.

## Design principles (why it looks like this)

1. **Scarce-resource economics**: the bottleneck of an AI-led project is not code
   generation — it is **exclusive-resource windows (real hardware / production), human
   adjudication bandwidth, and context budget**. Every mechanism here economizes those three.
2. **Injection timing is a first-class dimension**: having many documents is not the
   problem — injecting them all is. Every document class declares when it enters session
   context (see `doc-map.template.md`); the session-start reading set is a fixed overhead
   that may only shrink, never grow.
3. **Executable beats prose**: repeatable procedures become scripts and skills, not
   paragraphs; non-executable knowledge is encoded where an agent can act on it, following
   the four-level priority in ai-debuggability.
4. **Ambiguity never stops work**: log judgment calls to a ledger and keep moving; batch
   them for human adjudication — never trade adjudication bandwidth for progress.
5. **Any model can cold-start**: charter, doctrines, and briefs are self-contained — no
   dependence on chat history or proprietary tooling.
6. **Lifecycle decisions up front**: feature requirements come find you; lifecycle
   requirements (deployment, upgrades, operations, robustness, agent reach…) only show up
   in incidents — at the most expensive possible moment. Run the `inception-survey` at
   project start and give every dimension one of three dispositions (decide now / defer
   explicitly with a trigger / not applicable), driven proactively by the AI.

## Contents and dependencies

| File | What it is | Depends on |
|---|---|---|
| `inception-survey.template.md` | Inception survey (nine lifecycle dimensions + three-state disposition; **the first thing in the founding conversation**, read once and never injected again; hard-won lessons are distilled into the questions themselves) | outputs land in AGENTS + briefs |
| `kickoff-prompts.template.md` | Founding kickoffs — product planning (Prompt A) & architecture/stack (Prompt B): the founding conversations that follow the survey; read once, never injected again | inception-survey, brief |
| `doc-map.template.md` | Document tiers × injection timing, the master contract (**read this first; filled at step 4**) | — |
| `AGENTS.template.md` | Workspace charter (reading order / layout / hard rules / start-of-work protocol) | doc-map |
| `ai-workflow.template.md` | Session protocol / work-block protocol / parallelism rules / economics / safety boundaries | AGENTS, doc-map |
| `TEST-CONSTITUTION.template.md` | Testing constitution (two-tier testing + the simulator self-certification trap + gate semantics) | — |
| `retrieval-optimized-code.template.md` | Addressability rules (the anti-vector-index ruling) | — |
| `ai-debuggability.template.md` | Priority encoding for non-derivable knowledge + harness-owns-environment | — |
| `ledgers/` | The three ledgers + the split-by-adjudication principle | ai-workflow |
| `brief.template.md` | Work-block brief template (with its `## Start` section) | AGENTS start protocol |
| `skill.template.md` | Skill template (the fossilized-trap form) | — |
| `scar-casebook.template.md` | Scar casebook (the survey's evidence layer; lives in your org's private workspace, **never** inside a project repo) | inception-survey |
| `scripts/` | Reference implementations: status-header validator + doc-vs-reality audit prompt (`audit/`) · MAP generator seed (`dev/`) | doc-map, AGENTS |

## Instantiation steps

1. Copy this directory into the new project; drop the `.template` suffixes.
2. **Run the inception survey**: in the founding conversation, the AI proactively walks
   `inception-survey` (nine lifecycle dimensions), giving each item a three-state
   disposition — "decide now" conclusions feed step 5's charter; deferred items become
   TODO briefs with explicit triggers. (If your organization keeps a scar casebook, the
   AI consults it during this conversation as evidence — it is **never copied into the
   new repo**; the new project starts a casebook of its own.)
3. **Run the two kickoffs**: from `kickoff-prompts`, Prompt A (product planning →
   product brief + campaign briefs), then Prompt B (architecture & stack → charter tech
   sections + contracts skeletons + ADR list).
4. **Fill doc-map**: decide this project's document tiers, each tier's injection timing,
   and the session-start reading set (aim for ≤4 files; the pack's own default is two —
   `AGENTS.md` + `ai-workflow.md` — everything else injects on demand; keep the headroom
   for your project's doctrines).
5. Fill `AGENTS.md`: layout / canonical-name table / quality-gate commands / safety
   allowlist (replace every `{{...}}`, including the survey's "decide now" outcomes and
   Prompt B's ADR rulings).
6. Trim to fit: no hardware → delete the real-hardware safety sections but keep the
   "exclusive-resource three-condition exception" skeleton (production databases and live
   environments need it just the same); no dual-track parallelism → delete the contracts
   parallel-boundary section, keep the contract-first principle.
7. Create `briefs/` `contracts/` `scripts/verify/` `scripts/audit/`; briefs come from
   the survey's deferred items and Prompt A's campaign cut (template: brief.template).
8. Wire the two reconciliation checks — reference implementations ship in `scripts/`:
   `audit/check_status_headers.py` (deterministic, stdlib-only, run casually; edit its
   CONFIG block to your layout) + `audit/doc-reality-audit.md` (judgment-based
   multi-agent read-only audit prompt, run at campaign close). Then seed the index:
   `dev/gen_map.py` renders `MAP.md` from its SEED table — this is the generator the
   charter's "hand-editing forbidden" rule presumes.

## Provenance and maintenance

Extracted from a private production workspace (an FPGA remote-lab platform; DOCOPS-1,
2026-07-19); **this repo is its public distribution mirror**, English edition. Mechanisms
keep evolving in the origin workspace; this repo does not auto-track — major upgrades are
synced as manual snapshots. The origin project's own scar casebook (its itemized paid-for
lessons) is internal and not published — its transferable lessons are already distilled
into the survey's questions, so nothing is missing here.

License: MIT (see `LICENSE`).
