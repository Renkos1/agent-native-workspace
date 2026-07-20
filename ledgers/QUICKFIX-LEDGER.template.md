# QUICKFIX-LEDGER — the quickfix ledger (logged = approved)

status: ACTIVE (ledger)

Rule: small problems the user names in passing — logging one row **is the approval**;
execute directly; deliver with evidence (commit + quality gate). Split with the other
ledgers: behavioral ambiguity needing adjudication → `AMBIGUITY-LEDGER`; pure polish →
`POLISH-LEDGER`. This ledger takes small behavioral fixes at semantics / copy /
default-value scale.
Hard constraints as in the doctrines (unbreakable per entry): {{contract freeze /
quality-gate commands / directory boundaries}}.

## State machine

LOGGED → DOING → DONE (evidence: commit + quality gate) | DEFERRED (reason)

## Entries

| id | domain | problem | fix | status |
|---|---|---|---|---|
| QF-1 | | | | |

## Start (saying "fix QF-<n>" — or describing a new small fix — executes this section)

- New problem: log one row first (take the next id), then fix.
- Existing entry: execute per its "fix" column; for DEFERRED entries, first check
  whether the deferral reason has cleared.
- On delivery, set the row to DONE + evidence (commit + quality-gate output).
