# Testing constitution — single-system internal / cross-system real integration

status: ACTIVE
Applies to: all tracks. Top-level law, peer to the ledgers.

## First principles

1. **Zero manual**: all verification is model-operated; no code change or deploy relies
   on a human clicking through first.
2. **Replayable**: tests densify into scripts, enter the gate, and can be re-run at will.
3. **Real user simulation**: frontend/entry verification must drive the real UI as a
   user would (log in → navigate → operate → assert rendering) — not API probes alone.
4. **Cross-system tests are kept**: any feature spanning systems or external
   dependencies keeps a "data-path correctness" test set, **retained long-term**, re-run
   before changes and deploys.
5. **Simulation is not integration**: mocks and simulators are single-system
   conveniences and **cannot substitute** for cross-system verification. Cross-system
   accounts settle only against the real system.

## The two tiers

### Tier 1: single-system internal (always-on; runs anytime; needs no external real system)

- Service / pure-function unit tests; API contract smoke; UI E2E (headless against the
  real UI, hitting a real backend + fixture DB).
- **Simulators/mocks**: speak the real protocol, so the real code path runs
  **unmodified** (the system under test believes it is talking to the real thing).
- **The self-certification trap (hard boundary)**: the simulator and the system under
  test read the same spec — if the spec is wrong, both are wrong together, and
  everything is green. **Simulator-green ≠ protocol correctly understood**; the first
  real integration is the spec's acceptance point and must be explicitly recorded as
  "protocol verified."

### Tier 2: cross-system real integration (final delivery + the deploy gate's source of truth)

- Full chain against the real {{external system / hardware}}; assertions must not rely
  only on what this side saw (a simulator can fake that too) — read real state back from
  the far side: **structured telemetry endpoints** as the mainstay (read-only, additive
  fields, assertable), plus **far-side probes** for the highest-risk flows (independently
  confirming state on the remote end).
- **Epistemic boundary**: backend telemetry only proves "the backend believes it read X
  from the far side"; closing the loop on "the data truly reached the far side" needs a
  far-side probe or a physical ground truth (loopback / known signal source). Test
  assertions label their coverage boundary accordingly.
- **One suite, two modes**: real mode (default; source of truth) / simulated mode
  (offline fallback), switched by a single config line.

## Gate semantics

- Deploy-readiness gate = Tier 1 all green + (when the real system is available) Tier 2
  **real mode** all green.
- When the real system is unavailable, Tier 2 runs simulated and is **explicitly labeled
  "not confirmed against the real system"** — simulated results **never count** toward
  the gate; the affected feature is either feature-flagged off or held at the gate until
  Tier 2 real mode has passed.
- **Kept-test enforcement**: any multi-system feature must add or update a data-path
  correctness case (Tier 2, dual-mode) before merge. Missing = no merge.

## Tool selection slots

- UI E2E: {{Playwright or similar — headless, model-scriptable, deterministic,
  traces/screenshots}}. Interactive browser tools are for ad-hoc debugging only and
  never become the test set.
- Simulator: {{a deterministic, parameterizable, model-start/stoppable standalone
  process}}.
- Far-side telemetry: read-only, properly guarded, additive-field assertable endpoints.
