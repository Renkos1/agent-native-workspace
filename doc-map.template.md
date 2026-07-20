# doc-map — document tiers × injection timing, the master contract

status: ACTIVE

This file answers two questions: ① where each kind of information lives (its single
source of truth) ② when each document enters AI session context. **Injection timing is a
first-class dimension**: the session-start reading set is a fixed context cost paid by
every session — it **may only shrink, never grow**. A new document that wants into the
start set must displace equal volume; otherwise it is injected on demand.

## The four tiers

| Tier | Contents | Injection timing | Change rules |
|---|---|---|---|
| L0 charter/doctrine | `AGENTS.md` · active doctrines (execution rules, aim ≤3-4 files) | **Read at every session start** (keep small) | Changes only follow human decisions; promoting or retiring a doctrine is a human call |
| L1 operating system | conventions `conventions/` · contracts `contracts/` · skills `skills/` · scripts `scripts/` · domain facts (device tables / glossary / environment tables) | **On demand** (trigger table below) | A change must update the affected rules/scripts in the same move |
| L2 live state | `briefs/` status headers & active briefs · ledgers · generated index `MAP.md` | On claim / on logging / on adjudication | Written back at every session close; moved to archive at campaign close |
| L3 history | `handoff/` · `archive/` · historical runbooks · `releases/` | **Never by default**; only explicit archaeology or audit reads it | Append-only |

## L1 on-demand trigger table (doing what → read what; fill per project)

| Trigger | Inject |
|---|---|
| Before writing {{tier/language}} code | `conventions/code-standards-{{tier}}.md` |
| Creating a new module / debugging keeps hitting walls | `retrieval-optimized-code.md` · `ai-debuggability.md` |
| Before touching any cross-tier seam | `contracts/<the contract>` + its test vectors |
| Before touching any exclusive resource (hardware / production DB / live env) | {{domain-facts doc}} + `ai-workflow.md` §safety |
| Running deploy / smoke / diagnosis | the matching skill (its trigger lives in the skill description) |
| When the matching incident occurs | `runbooks/<incident>` |
| Before release / push | {{git & release workflow doc}} |

## Information routing table (nothing written twice; cross-file references are path links)

| Information type | Its one home |
|---|---|
| Plans / decisions / boundaries | charter (workspace level) · doctrine (track level) · brief (block level) |
| Runtime facts (dated) | the owning brief or a ledger row; release facts go to `releases/` |
| Repeatable procedures | `skills/` or `scripts/` (**executable beats prose**) |
| Protocols / interfaces | `contracts/` |
| Hard domain facts (devices / environments / versions) | {{domain-facts directory}} |
| Work-block detail | `briefs/<id>.md` |

## Hygiene rules

- A document contradicts reality: **fix the document before doing the work**.
- Orphan documents (outside the tier table): either register into L1 with one clear
  responsibility, or archive.
- Two-mode reconciliation: a deterministic script (status headers / path existence; run
  casually) + a judgment-based multi-agent read-only audit (must run at campaign close);
  findings feed the next hygiene wave.
- State lives only in brief headers and ledgers; no long conversational prose;
  **brief + status line is the only handoff medium**.
