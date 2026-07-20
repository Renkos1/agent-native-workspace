# POLISH-LEDGER — the polish ledger (item-by-item approval)

status: ACTIVE (ledger)

Rule: each polish item logs one row and executes only **after discussion and approval
(APPROVED)**; deliver with evidence (commit + quality gate). This ledger owns
"looks/consistency" only — never behavioral semantics. The design source of truth is
{{the design guidance doc}}; this ledger does not redefine style — where the guidance
has no coverage, propose here first, and after approval fold the ruling back into the
guidance. No freestyling.

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

LOGGED → APPROVED → DOING → DONE (evidence) | REJECTED (reason)

| id | domain | item | restructure? | status |
|---|---|---|---|---|
| PL-1 | | | no | LOGGED |
