# Inception survey — lifecycle decisions up front

status: TEMPLATE (read once in the founding conversation, never injected again — outputs go into the charter and briefs; this file is not re-read)

**Why this exists**: feature requirements come find you; lifecycle requirements don't —
they only surface in incidents, which is always the most expensive moment to meet them.
This survey turns "decided whenever someone happens to think of it" into "asked at the
start, dispositioned in writing." Walking it takes about half an hour, **driven
proactively by the AI in the founding conversation** (the human doesn't need to remember
this survey exists; the source of truth for that behavior is the pack README, not any
single assistant's private memory).

**Companion-file design**: this file is the generic edition — no project-specific
details; each dimension's paid-for lessons are distilled into the questions themselves.
Keep an in-house **scar casebook** as the evidence layer (template:
`scar-casebook.template.md`): per dimension, log
"scar (one-line fact) → lesson (one transferable line) → source." The casebook is
**consulted during the founding conversation only — never copied into the new repo**
(another project's facts sitting in a fresh repo get read as this repo's facts:
contamination); each new project starts its own casebook and feeds it as lessons get
paid for. If the founding session cannot reach the origin workspace, copy only the
relevant rows, labeled "origin evidence, not this project's facts."

**Three-state disposition** (every item must land in exactly one; registry at the end):

- **Decide now** → written into the new project's charter (hard rules / layout);
- **Defer explicitly** → open a TODO brief with a **trigger condition** (it resurfaces on
  its own — not when someone happens to remember);
- **Not applicable** → one line on why, so nobody re-asks later.

**Scope**: lifecycle and operability only. Product-side day-one items (accounts,
permission model, i18n) are a separate conversation; test strategy isn't repeated here —
instantiate `TEST-CONSTITUTION.template.md`.

---

## 1. Delivery & deployment form

How does it reach users?

- Installer / scripted deploy / SaaS / images? Who performs installs, how often, any
  offline (air-gapped) sites?
- Does it need signing/notarization — and is that worth it for this distribution surface?
- Site-local config (ports/domains/paths): who owns it, how does it get rendered, and
  what happens when you **take over an already-installed site**?
- Must decide by: **before the first install for anyone**.

## 2. Upgrades & hotfixes

After v1 ships, how do changes arrive?

- Are full upgrades and hotfixes separate channels? Must hotfix branches fork from the
  **deployed commit**?
- Was the upgrade channel laid down and smoke-tested with the first install — or will you
  discover it was never wired the first time you actually need it?
- How do DB migrations coexist with upgrades (additive migrations / dual registry /
  checksum pinning)?
- What is the rollback artifact, where does it live, how long is it kept? **Version
  observability** — how does a deployed instance report what it is?
- Must decide by: version observability & rollback **before the first production deploy**;
  upgrade/hotfix channels **before the second release**.

## 3. Operations & site ground truth

Once production is running, who knows what it looks like?

- **Release baseline ledger**: which machine runs which commit right now — recorded where?
- Backups: who makes them, where do they go, **has restore ever been drilled**?
  Port/firewall closure checklist? Where do credentials live, how are they rotated, and
  does credential verification take an explicit "no default config" path?
- Who learns about problems first — monitoring, or a user report? Where does incident
  response accumulate (runbook/skill)?
- Has the deploy toolchain been smoke-tested against the target machine's
  **charset/locale**?
- Must decide by: **before the production cutover window**.

## 4. Instance topology & identity

How many of it will be running?

- Single site / multi-site / fleet? Where is the instance registry?
- How is instance identity established — self-registration / fingerprint / factory
  marking? Will heterogeneity appear (how do you prevent binary forks)?
- Must decide by: **before the second instance exists**.

## 5. Robustness budget

When it breaks, how is it supposed to break?

- For every long-lived connection or channel: reconnect semantics? How is state restored
  after reconnect (snapshot push-back)?
- What are the timeout/retry budgets — do individually reasonable per-layer timeouts
  stack into whole-system unavailability? Expected scale and concurrency? How does it
  degrade past its limits?
- **Failure must be visible**: no silent clamping, no swallowed errors — is an over-limit
  request refused in plain language, or quietly shrunk?
- Must decide by: **when each channel is first implemented** (a standing rule, not a
  one-time decision).

## 6. Environment ladder & fidelity

How many rungs sit between the dev box and production?

- Ladder inventory: local → dedicated sandbox → staging → production; what is allowed at
  each rung?
- **Are critical dependency versions pinned identical across rungs** (DB / runtime /
  drivers)? A staging conclusion under mismatched versions proves nothing.
- Can the network path produce **false connectivity** (VPN / proxy / port-forwarding
  making probes green while real traffic goes nowhere)?
- When several people or sessions share one machine, how does global state
  (DB/env/ports) avoid cross-trampling?
- Must decide by: **before the first time staging results are used as evidence**.

## 7. Data shape & backups

Which bytes are irreplaceable?

- Inventory of precious data (users / uploads / DB); each one's backup and **verified**
  restore path?
- Ingesting legacy data? Migration / adapter layers / compat columns — what are the
  hidden prerequisites?
- Any secrets or personal data inside? Do logs and backups carry them out the door?
- Must decide by: **before the first legacy ingestion or the first production cutover**.

## 8. External dependency health

Which things you didn't write can kill you?

- Inventory of toolchains / compilers / SDKs / vendor binaries (with a "confirmed
  working" column); license & certificate **expiry table**; paid services and cost
  ceilings.
- Does every critical dependency have a health probe? **Can its failure masquerade as
  success** (exit code 0 / silent degradation)?
- When a dependency is down, does the layer above say "dependency not running" — or does
  it just hang and time out?
- Must decide by: logged **the moment a dependency enters the critical path** (standing
  rule).

## 9. Agent reach (this survey's reason to exist; absent from industry readiness checklists)

What does the AI use to build and operate this? **Decide on day one** — every later day
pays wall-bumping tax for each missing channel.

- **Reachability**: at every tier (frontend / cloud / gateway / board / DB), what channel
  does the agent use to get there? How are keys managed? Channels must be able to
  **prove their own connectivity** (anti false-green).
- **Sandbox**: per tier, one standing instance the agent fully owns and can afford to
  break; the local dev environment starts with one command, dependency list on record;
  co-located sessions must not trample each other (contended state has a single owner).
- **Observability**: assertable version/health/telemetry endpoints per tier — tests and
  operations share the same touchpoints; endpoints must distinguish "no data" from
  "not registered / not configured."
- **Dedicated identity**: agent-only accounts and toggles — single-owner, no
  global-state flapping, transparent failure surface.
- **Boundaries**: allowlist by default + the exclusive-resource three-condition
  exception — design reach and guardrails **together**; boundaries retrofitted later =
  reach revoked later.
- Must decide by: **day one**.

---

## Registry (the survey's output; copy into the new project and fill per row)

| # | Dimension | Disposition | Landing (charter clause / brief id / N/A reason) | Trigger (required for deferred) |
|---|---|---|---|---|
| 1 | Delivery & deployment form | | | |
| 2 | Upgrades & hotfixes | | | |
| 3 | Operations & site ground truth | | | |
| 4 | Instance topology & identity | | | |
| 5 | Robustness budget | | | |
| 6 | Environment ladder & fidelity | | | |
| 7 | Data shape & backups | | | |
| 8 | External dependency health | | | |
| 9 | Agent reach | | | |
