# Founding kickoffs — product planning & architecture

status: TEMPLATE (each used once, in its founding conversation; outputs land per doc-map; never injected afterwards)

Founding a project is three conversations, in a fixed order — the survey owns lifecycle,
Prompt A owns *what to build*, Prompt B owns *how to build it*:

| # | Conversation | Input | Output (landing) |
|---|---|---|---|
| 1 | Inception survey (`inception-survey`) | your product idea, roughly told | lifecycle registry → charter clauses + deferred briefs |
| 2 | Product planning (Prompt A) | idea + survey registry | product brief → v1 scope → campaign briefs |
| 3 | Architecture & stack (Prompt B) | product brief + survey registry | charter tech sections + contracts skeletons + ADR list |

Running all three in one session is best; when splitting sessions, paste the matching
opener to any model. Converse in any language — artifacts land in the workspace language.

## Prompt A — product-planning opener

> Read `<this directory>/kickoff-prompts.md`, section "Prompt A contract", and execute
> it: you drive a product-planning interview; I adjudicate. Deliverables: a product
> brief + the first batch of campaign briefs, landed per doc-map.

### Prompt A contract (the AI executes this)

1. **Roles**: you interview and draft; the human only adjudicates. Lead everywhere with
   a default proposal to veto — any question you could answer with a sensible default
   must not be thrown at the human.
2. **Batch the interview**: ≤{{7}} questions per round, grouped by theme; two rounds
   should usually converge. No one-question-at-a-time grinding.
3. **Cover** (skip whatever the human already made clear):
   - Users & jobs: who uses it, for what job, how often; who pays (if not the same
     person).
   - Problem & bet: what pain, why now, the one-sentence bet (the core assumption that
     makes this worth building).
   - v1 scope: walking-skeleton cut — the smallest end-to-end slice that proves the
     bet; MoSCoW the rest.
   - **Non-goals**: an explicit list, one line of reasoning each (prevents re-litigating
     scope later).
   - Success metrics: how v1's success is judged (numbers, not vibes) + the review date.
   - Product-side day-one items the survey excluded: accounts/roles, permissions, i18n,
     pricing/licensing, brand constraints.
   - Hard constraints: deadline, budget, compliance, systems it must integrate with.
   - Riskiest assumptions → each gets the cheapest possible validation (spike /
     prototype / fake door), scheduled before the work that depends on it.
4. **Deliverables** (summarize for the human first; write after sign-off):
   - `{{product brief path, e.g. docs/product-brief.md}}`: positioning line, users &
     jobs, bet, v1 scope, non-goals, metrics, constraints — **hard cap: one page**.
   - Campaign briefs: v1 scope cut into claimable briefs (template:
     `brief.template.md`), each with acceptance = demo + metric; riskiest-assumption
     spikes first.
   - Deferred/rejected items: one ledger line each, with reason + trigger.
5. **Ambiguity**: the human contradicts themselves or leaves a fork open → log to the
   ambiguity ledger, proceed on the recommended default; never stall the conversation.

## Prompt B — architecture & stack opener

> Read `<this directory>/kickoff-prompts.md`, section "Prompt B contract", and execute
> it: you drive architecture and stack selection; I adjudicate. Inputs: the product
> brief + the survey registry. Deliverables: charter tech sections + contracts
> skeletons + the ADR list.

### Prompt B contract (the AI executes this)

1. **Roles**: you propose with reasons and a recommendation; the human picks. Every
   decision gets one ADR line: decision / reason / revisit trigger. A decision not
   logged does not exist.
2. **Inputs first**: read the product brief and the survey registry before proposing;
   the survey's "decide now" items (delivery form / instance topology / robustness
   budget / environment ladder / agent reach) are binding constraints, not suggestions.
3. **Selection criterion — model-legibility is first-class**: the workforce is AI
   sessions, so prefer boring, mainstream, strongly-typed, convention-heavy stacks
   (where model knowledge runs deepest); deterministic tooling; one command for
   everything. A niche stack must pay for its niche-ness in a written ADR.
4. **Cover**:
   - Stack per tier ({{frontend/backend/DB/infra}}), each with its model-legibility
     argument.
   - System decomposition: tiers/modules and the **seams — every seam gets a
     `contracts/` skeleton** (the precondition for multi-session parallelism later).
   - Data-model first cut + storage; which bytes are irreplaceable (feeds survey
     dimension 7).
   - Environment ladder made concrete: local / sandbox / staging / production — what
     exists on day one, versions pinned.
   - Quality gate made concrete: exact build/lint/typecheck/test commands — into the
     charter's hard rules; must run on day one.
   - Test foundation: instantiate the testing constitution's tool slots (E2E runner /
     simulator strategy / telemetry endpoints).
   - Agent reach made real: the sandbox instance, dedicated identities, assertable
     health/version endpoints — scheduled as day-one briefs, never "later".
   - Repo skeleton: layout per the charter, MAP generator seed, glossary seed
     (canonical names for every tier — the addressability foundation).
5. **Deliverables**:
   - Charter (`AGENTS.md`) tech sections filled: layout / canonical names / quality
     gate / boundaries.
   - A `contracts/` skeleton per seam; glossary seeded.
   - ADR list at `{{docs/adr path}}` (one line each is fine).
   - Scaffold + day-one agent-reach briefs, claimable via "start <id>".
6. **Ambiguity**: same as Prompt A — log, default, proceed.
