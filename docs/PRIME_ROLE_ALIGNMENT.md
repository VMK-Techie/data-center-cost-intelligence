# Prime Data Centers — Sr. Manager, Reporting & Data Analytics

**Portfolio role alignment | Independent demonstration, not a claim of employment at Prime.**

**Source job:** [Prime Data Centers LinkedIn posting 4489051665](https://www.linkedin.com/jobs/view/4489051665/) (reviewed 2026-11-13). The posting emphasizes executive BI reporting, enterprise KPI standards, project-level budget/schedule/milestone rollups, collaboration with Operations Excellence, PMO, Business Transformation and IT/Systems, plus identification/escalation of trends and risks.

## What this repository demonstrates

| Prime responsibility | Demonstration in this repository | Business outcome |
| --- | --- | --- |
| Executive dashboards and reporting packages | [Five-page financial dashboard](../powerbi/README.md) and [project portfolio metrics](PRIME_PORTFOLIO_KPIS.csv) | Consistent business-operations briefings |
| Project-to-enterprise reporting | [Synthetic project status dataset](../data/prime_projects_synthetic.csv), [Python metrics](../src/prime_portfolio_metrics.py) | Cross-project budget and milestone aggregation |
| Standardized reporting definitions | [Metric definitions and governance](PRIME_PORTFOLIO_KPIS.csv) | Comparable KPIs across projects |
| Identify trends, risks and opportunities | Risk-tier and schedule-slippage calculations; actionable management scenarios below | Decision escalation with owner and due date |
| Cross-functional PMO/Operations Excellence work | [Operating model](TEAM_LEADERSHIP_AND_OPERATING_MODEL.md) | Prioritized backlog, stakeholder alignment and change control |
| BI platform administration and infrastructure partnership | [Governance and reliability controls](PRIME_REPORTING_GOVERNANCE.md) | Trusted data, access and refresh assurance |
| Lead reporting teams professionally | [Separate leadership page](TEAM_LEADERSHIP_AND_OPERATING_MODEL.md) | Accountable delivery, coaching and predictable execution |

## Decision example: project schedule and budget rollup

The fictional project records identify four data-center programs with approved capital budgets, current EAC, baseline and forecast completion dates, milestone counts and the age of the latest status update. A portfolio leader can:

1. Compare **EAC to budget**, calculate forecast overrun, and isolate projects exceeding an agreed exception threshold.
2. Compare forecast finish with **baseline project finish**, using positive delay days to flag schedule exposure.
3. Calculate on-time milestone adherence **only over milestones due by the reporting cutoff**.
4. Evaluate stale project updates and unresolved critical risks before presenting a consolidated executive dashboard.
5. Assign the appropriate PMO, Finance, Engineering or Operations owner to each exception.

**Important aggregation rules:** portfolio EAC = sum of project EAC in a single reporting currency and scope; portfolio cost/MW = sum of EAC / sum of commissioned IT MW. Do *not* average project cost/MW values without capacity weighting. Portfolio on-time milestones = total on-time milestones divided by total milestones due, not the unweighted average of project percentages.

## Metrics worth demonstrating specifically for this job

- Budget-to-EAC variance and portfolio cost / commissioned IT MW
- Schedule variance in days and on-time project milestone adherence
- Project status update freshness and overdue critical risk counts
- Data completeness, reconciliation exceptions and definition coverage
- Report refresh success, BI incident response and dashboard adoption
- Delivery cycle time, intake SLA, throughput and work-in-progress
- Executive actions closed on time

These are suggested metrics, **not declared internal Prime KPIs or official Prime target thresholds**.

## Job interview narrative

> My work connects a strong BI and Microsoft data-platform foundation with the realities of data center capital programs. I build consistent financial and operational definitions, establish reliable semantic models, translate project reporting into enterprise decision tools, and lead teams through a disciplined intake, prioritization, quality assurance and stakeholder-feedback process. This portfolio uses fictional data to demonstrate those methods.

The portfolio does not assert actual savings, team headcount, percentage productivity improvement, or other outcomes without verified supporting evidence.

## Gaps / next steps

The editable PBIP project in this repository currently shows financial and procurement pages. The Prime-specific project reporting metrics below are coded and documented separately; **they are not yet deployed as additional Power BI visual pages**. A production-style reporting page would incorporate project baseline vs forecast completion dates, milestones, risks, and reporting freshness, using project and date dimensions.
