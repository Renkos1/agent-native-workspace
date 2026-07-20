---
name: {{kebab-name}}
description: {{One line: what it does + when to use it. Put the trigger into the description — it decides when the skill gets injected; "use when X" beats a feature list.}}
---

{{Goal in one line. Skills exist for "repeatable procedures with traps" — anyone can
list the steps; the traps are the actual content.}}

1. **{{step name}}**: `{{exact command}}` → expect {{output/state; concrete values,
   e.g. "200 with lane:\"nest\""}}.
2. **{{step name}}**: `{{command}}` → expect {{...}}.
3. … (each step independently PASS/FAIL; report per-layer results)

## Traps (the reason this skill exists — the pits that get re-stepped-in unless written down)

- {{Trap 1: symptom → root cause → correct action. Example (origin workspace): degraded
  link status after flashing = the mandatory second reboot was skipped, not a flash
  failure.}}
- {{Trap 2: environment quirk. Example: this host has no RTC — log wall-clock times lie;
  use offsets from boot. Services briefly report inactive right after boot; wait ~60s
  before concluding.}}
- {{Trap 3: destructive side effect. Example: a certain routine operation silently
  resets the remote end / wipes its firmware — forbidden mid-test.}}

## Fault bisection table

{{Step N fails → dig in which layer; one line each. Makes diagnosis O(layers), not
O(chain). Example: 1-2 fail → web tier · 3 fails → local dependencies · 4-5 fail →
gateway · 6-7 fail → board}}
