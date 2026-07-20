# AMBIGUITY-LEDGER — the ambiguity ledger (fix-forward + batch adjudication)

status: ACTIVE (ledger)

Rule: ambiguity **never blocks** work. Default is fix-forward — judged wrong per
{{the doctrine holding the safety/correctness checklist}} → implement the correct
behavior, mark the site, log `FIXED (pending-review)`; externally observable behavior is
depended upon → preserve it, log `PRESERVED`. Unsure → log it and keep working; no
stalls, no questions. Batch entries for the human's "batch sign-off"; exclusions
(deploy-constrained / exclusive-resource / needs-individual-attribution items) are
listed explicitly and handled separately.

| id | where (path:symbol) | legacy behavior | disposition & reason | status |
|---|---|---|---|---|
| A-1 | {{path:symbol}} | {{one line}} | {{what changed / why preserved}} | FIXED (pending-review) |
