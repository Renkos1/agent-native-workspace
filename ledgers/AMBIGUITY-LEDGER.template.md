# AMBIGUITY-LEDGER — 歧义账（fix-forward + 批量裁决）

status: ACTIVE（账本）

规则: 歧义**不阻塞**工作。默认 fix-forward——按 {{安全/正确性清单所在法典}} 判断旧行为
是错 → 实现正确行为并标记代码现场, 记 `FIXED (pending-review)`; 外部可观察面依赖旧行为
→ 保真, 记 `PRESERVED`。拿不准 → 记账 + 继续干活, 不停工不提问。攒批供用户「批量签收」,
排除项（部署约束/独占资源项/需单独归属的）显式列出另行处置。

| id | where (path:symbol) | 旧行为 | 处置与理由 | status |
|---|---|---|---|---|
| A-1 | {{path:symbol}} | {{legacy 行为一句话}} | {{改成了什么/为何保真}} | FIXED (pending-review) |
