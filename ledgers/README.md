# ledgers/ — ledger templates (split by adjudication mode)

Ledgers are where "ambiguity never stops work" lands. **The split principle: divide by
who adjudicates and when — never by topic.** That way each ledger carries exactly one
execution rule, and a session holding an entry knows immediately whether it may act.

| Ledger | Adjudication | Collects |
|---|---|---|
| `AMBIGUITY-LEDGER` | fix-forward by default + **batched** human sign-off | behavioral ambiguity: is the legacy behavior a bug or a contract — correct it or preserve it |
| `QUICKFIX-LEDGER` | the user naming it **is the approval**; log, then fix directly | small fixes the user points out (semantics / copy / default-value scale) |
| `POLISH-LEDGER` | **item-by-item** discussion; approved before execution | pure polish/consistency (no behavioral change) |

Optional fourth (dual-track / migration periods): `PORT-LEDGER`, the porting ledger —
every **behavioral** change on the legacy track logs one row; the new track clears rows
as it claims each domain; closing requires a zeroed table. Pure styling / comments /
build-script changes don't log.

Common rules:

- One row per entry; state machine `LOGGED → DOING → DONE (evidence: commit + quality
  gate) | DEFERRED (reason)`.
- Hard constraints live in the **ledger header** (contract freeze / quality gate /
  directory boundaries), unbreakable per entry — an executing session reads the header
  and has every constraint, no doctrine re-read needed.
- Ledgers carry their own `status:` header (ACTIVE) and are covered by the status-header
  validator together with the briefs.
- After a batch sign-off, append a "batch sign-off record" (date + scope + exclusions)
  instead of editing rows — avoids write conflicts with concurrent sessions on the same
  table.
