# POLISH-LEDGER — the polish ledger (batch veto; unswept = expired)

status: ACTIVE (ledger)

Rule: logging is free — polish never blocks work, so nothing here ever interrupts a
session. Execution is gated on a **batch sweep**: at each natural adjudication point
(campaign close, or whenever the human opens a sweep — the same sitting as the
ambiguity batch sign-off), the human veto-scans the LOGGED rows and approves the few
worth doing; **every row not approved in that sweep is EXPIRED** — struck, never
carried as debt. Re-logging an expired item costs nothing, and recurrence is itself
the evidence it matters: the queue self-cleans, noise dies, real irritants come back.
Exception: `restructure? = yes` rows (layout/interaction reorganization) still take
item-by-item approval. Deliver approved items with evidence (commit + quality gate).
This ledger owns "looks/consistency" only — never behavioral semantics. The design
source of truth is {{the design guidance doc}}; this ledger does not redefine style —
where the guidance has no coverage, propose here first; rulings (approved or rejected)
fold back into the guidance so the question never re-opens. No freestyling.

## Hard constraints (unbreakable per entry)

1. {{Contract freeze: no changes to backend-facing field names / status-code branches /
   envelope reads}}
2. {{Debuggability floor: existing test anchors never removed or renamed; new elements
   add them as needed}}
3. {{Stack boundary: no new UI libraries or frameworks}}
4. {{Quality-gate commands}}
5. Items that reorganize layout or interaction structure set the "restructure?" column
   to **yes** and get item-by-item human approval; "no" = purely visual / token-level.

## State machine

LOGGED → APPROVED (named in a sweep record) → DOING → DONE (evidence)

- **EXPIRED** needs no row edit: a LOGGED row older than the latest batch-sweep record
  and not named in it is expired by definition — the sweep record (append-only, per the
  common rules) is the authority, so there are no write conflicts. Expired rows are
  cleared when the ledger archives at campaign close.
- **REJECTED** (explicit, with reason) is different from expiry: it records a ruling
  that folds back into the design guidance, so the whole class never gets re-proposed.

| id | domain | item | restructure? | status |
|---|---|---|---|---|
| PL-1 | | | no | LOGGED |
