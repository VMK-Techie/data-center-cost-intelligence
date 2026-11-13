# How I Lead a Business Intelligence & Data Analytics Team

**Leadership portfolio | Senior Manager, Reporting & Data Analytics**

I lead with clear ownership, transparent prioritization, repeatable delivery standards, and accountability for business outcomes. My focus is not simply producing more dashboards: it is building a reporting function trusted by executives, project managers, Finance, and Operations.

> This page describes my management approach and a reusable example operating model. Targets, role assignments and routines shown below are illustrative guidance, not an assertion that every practice or quantitative outcome was deployed at a specific employer.

## 1. Team mission and leadership philosophy
- **Business-first delivery:** begin with the decision, intended audience, definition of success, and action owner—not the visualization.
- **One source of truth:** certified semantic models, owned KPI definitions, repeatable validation, version control, and controlled distribution.
- **Clear accountability without micromanagement:** each initiative has a delivery owner, business sponsor, acceptance criteria, dependencies and risk log.
- **People development:** coach BI developers and analytics engineers through regular one-on-ones, design reviews, pairing and cross-training.
- **Continuous improvement:** retrospectives focus on systemic causes such as missing requirements, fragmented sources, rework, delayed approvals and incident recurrence.

## 2. Roles and decision rights (illustrative team structure)

| Workstream | Accountable owner | Typical collaborators | Definition of done |
| --- | --- | --- | --- |
| BI roadmap / prioritization | Senior BI Manager | Business Operations, Director of Data, Finance, PMO | Sponsor and measurable decision/use case; approved priority |
| KPI and semantic modeling | BI Lead / Analytics Engineer | Finance, Data Architect, PMO | Approved metric definition; grain, denominator, RLS and reconciliation validated |
| Pipeline integration and monitoring | Data Engineering Lead | IT/Systems, source owners | Alerting, recoverability, data quality and lineage documented |
| Power BI design and development | BI Developer | KPI owner, UX/end users | Accessibility, performance, drill-through and UAT acceptance |
| Release and operational readiness | BI Manager / designated release owner | QA, Security, IT, Support | Peer review, refresh checks, permission review and rollback plan |
| Executive analytics adoption | BI Manager and sponsor | Leadership, Business Transformation | Executive interpretation and follow-up actions recorded |

Roles reflect **responsibilities**; do not infer number of direct reports or staff titles from this example.

## 3. Reporting delivery lifecycle

```mermaid
flowchart LR
  A[Business intake] --> B[Clarify decisions and KPI definitions]
  B --> C[Prioritize by impact and effort]
  C --> D[Assign owner and delivery plan]
  D --> E[Model and pipeline development]
  E --> F[Peer review and data reconciliation]
  F --> G[UAT and sign-off]
  G --> H[Controlled release]
  H --> I[Monitor adoption quality and incidents]
  I --> J[Measure outcome and improve backlog]
```

**Intake template:** requester, business sponsor, decision supported, required KPIs, data source and source owner, reporting grain, timeliness target, audience/RLS, target date, expected impact, acceptance criteria, dependencies, and expected ongoing support.

**Prioritization:** apply a transparent score combining (a) strategic/business value, (b) financial or operational risk, (c) regulatory/executive commitment, (d) data readiness, (e) technical effort, and (f) support burden. Do not treat an executive title as the sole criterion for bypassing governance.

**Change control:** scope change requests document delivery and capacity implications. A priority change requires an explicit tradeoff: what is delayed, de-scoped or stopped.

## 4. Operating cadence

| Cadence | Meeting / review | Purpose | Output |
| --- | --- | --- | --- |
| Daily or 2–3 times/week | 10–15 minute delivery sync | Surface blockers; coordinate BI, data engineering and QA | Blocker owner and resolution date |
| Weekly | Prioritized backlog and capacity review | Balance roadmap work against urgent operational requests | Approved priorities, WIP limits, delivery commitments |
| Weekly | Technical design and model review | Star schema, Power Query/DAX, Fabric/SQL, RLS, performance | Architecture decisions and peer-review actions |
| Biweekly | One-on-one and coaching | Career goals, feedback, workload sustainability and growth | Private development actions; no public personnel data |
| Biweekly or monthly | Stakeholder demos/UAT | Validate decisions and usefulness with sponsors | Acceptance or rework list |
| Monthly | Executive reporting governance review | KPI exceptions, trust issues, adoption, milestones, escalations | Executive action log and accountable owners |
| Monthly | Reliability and incident review | Refresh outages, reconciliation differences, repeated failures | Root causes and preventive actions |
| Quarterly | Roadmap and skills planning | Align operating priorities and technical capabilities | Roadmap, learning goals and succession/back-up coverage |

The actual cadence should be proportionate to team size and project load; meetings must produce decisions, not just status updates.

## 5. Practical examples of management behaviors

### Conflicting project priorities
A PMO leader needs a schedule milestone dashboard while Finance requests a monthly CAPEX reconciliation. I document value, deadline, risk and effort for both. I agree the business-critical delivery sequence with stakeholders, allocate work by capability, and communicate which lower-priority request moves. The team is not expected to deliver two first priorities with unchanged capacity.

### Ambiguous requirements
If a stakeholder requests a "cost per MW" metric without defining what counts as cost or capacity, I do not allow separate reports to invent definitions. I facilitate an agreement on IT MW versus facility MW, committed versus actual CAPEX, and how in-flight project phases are treated; then I publish one governed definition.

### Data engineer disagreement
If a quick visual-layer transformation conflicts with a maintainable enterprise model, I compare options on correctness, refresh performance, reuse, ownership, testing effort and deadlines. The team documents the decision and revisits assumptions when evidence changes.

### Underperforming delivery
I first inspect constraints: unclear acceptance criteria, too much work-in-progress, dependency failures, absent reviews, or skill gaps. I give specific feedback and coaching with measurable next checkpoints. If problems persist I manage them through fair, documented expectations, not public blame.

### Executive risk escalation
An executive report should answer: **what changed, why it matters, what actions are available, who owns each action, and by when**. I escalate high-impact reporting failures and unresolved contradictory KPIs promptly instead of presenting questionable numbers as established facts.

## 6. Delivery and team health scorecard

| Measure | Calculation / governance | Leadership use |
| --- | --- | --- |
| Accepted release throughput | Count of deliverables accepted in time window | Capacity planning, not individual performance ranking |
| Delivery cycle time | Accepted release date minus active-start date | Surface system bottlenecks |
| Backlog aging | Days since intake for open requests, grouped by status | Identify neglected work |
| Intake response SLA | Requests triaged within SLA / eligible requests | Improve requester experience |
| Defect escape rate | Production defects / releases in period | Test quality and operational readiness |
| Dashboard refresh reliability | Successful scheduled refreshes / expected runs | Trust and platform health |
| Reconciliation issue count | Finance/PMO mismatches awaiting root cause | Data credibility |
| Metric ownership coverage | Approved published KPIs with named owner / all KPIs | Governance maturity |
| Stakeholder acceptance | Deliverables approved in first review / all reviewed | Requirement quality |
| Action closure adherence | Due actions completed on time / actions due | Accountability |
| Coaching / growth coverage | Team members with active development plans / eligible team members | Development, private by design |
| Sustainable load | Planned team capacity by initiative and support burden | Avoid chronic overload |

**Do not use story points, commit count, or dashboard count as simplistic rankings of individual developers.** Track value, reliability, maintainability and feedback alongside throughput.

## 7. Quality, governance and release gates
- Semantic models use star schemas where appropriate, consistent conformed dimensions and clear metric owners.
- Every project reporting measure has a definition, data owner, refresh date, denominator, grain, known limitations and reconciliation method.
- Peer reviews check SQL query plans, DAX correctness, semantic model shape, incremental refresh/capacity impacts and RLS boundaries.
- Production releases require source reconciliation, sponsor UAT, approved access roles, regression checks, fallback/rollback, support owner and runbook.
- Operational incidents use severity, business impact, owner, escalation route, recovery validation and retrospective actions.

## 8. First 30/60/90 days as an incoming reporting manager

**Days 1–30 — Learn and baseline:** meet Business Operations, PMO, Finance, Operations Excellence and IT; inventory BI assets and ownership; document pain points; baseline refresh reliability, definition conflicts, stakeholder needs, project reporting gaps and team workload.

**Days 31–60 — Stabilize and standardize:** establish KPI ownership and review process; implement visible intake prioritization; identify and fix a small number of high-impact trust/performance problems; define a project portfolio executive template and release process.

**Days 61–90 — Scale and prove value:** launch approved project-to-portfolio reporting pilots; publish recurring executive exceptions and action logs; measure adoption and reporting reliability; create a roadmap for governed semantic models, platform consolidation and sustainable team staffing.

## 9. How I describe my leadership in interviews

> My management style is collaborative and outcome-driven. I clarify the business decisions before assigning technical work, establish transparent priorities and ownership, and give developers and engineers autonomy with consistent design and quality standards. I partner with Finance, PMO, Operations and IT on governed definitions, coach team members through regular feedback, and communicate meaningful delivery and reporting risks early. I measure success by trusted executive decisions and reliable adoption—not by the number of dashboards produced.

For validated experience examples, I can discuss BI leadership, enterprise Power BI reporting, semantic model standardization, Microsoft Fabric modernization, change control, and data-center financial/operational analytics. Any specific headcount, savings amount, cycle-time reduction or adoption improvement should be included only if supported by actual records.

## Related
- [Prime role gap and KPI alignment](PRIME_ROLE_ALIGNMENT.md)
- [Governed project and BI delivery KPIs](PRIME_PORTFOLIO_KPIS.csv)
- [Prime synthetic project data](../data/prime_projects_synthetic.csv)
- [Prime portfolio metric code](../src/prime_portfolio_metrics.py)
