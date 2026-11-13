# Enterprise Reporting Governance and Reliability

This reference operating standard demonstrates how I would align data center project reporting with enterprise-level BI, not Prime's actual internal policies.

## Standardized project-to-portfolio data contract
| Object | Required key / definition | Owner to approve |
| --- | --- | --- |
| Project | Durable ProjectID, site, phase, market, approved IT capacity | PMO / Development |
| Budget baseline | Effective-dated approved budget version and currency | Finance |
| Actuals | Posted ledger financial period and committed/paid treatment | Finance |
| Forecast EAC | Forecast version + project + as-of date; signed sponsor | PMO / Finance |
| Schedule | Approved baseline completion and current forecast milestone dates | PMO |
| Project risks | Open/closed state, severity, action owner, due date and last update | PMO / risk owner |
| Data quality | Freshness SLA, missing fields, reconciliation severity, source lineage | IT / Data team |
| Access | Workspace owner, report owner, approved RLS mapping | Security / BI |

### Recommended star schema
`DimProject`, `DimSite`, `DimDate`, `DimMilestone`, `DimMetric`, plus `FactBudgetVersion`, `FactActuals`, `FactCommitments`, `FactScheduleMilestone`, `FactRiskSnapshot`, and `FactReportRefresh`. Multiple baseline versions must not multiply amounts through accidental many-to-many joins. The reporting cutoff/approved version should be explicit.

### Monitoring and incident process
- Alert on broken pipeline, failed refresh, RLS misconfiguration, unusually stale project updates and incomplete or irreconcilable budget rollups.
- Distinguish a data-source failure from a dashboard modeling defect; record impact, owner and target recovery.
- For any financial mismatch, preserve source document IDs and cutoff dates, reconcile with Finance, and document the root cause before re-publishing.
- Report freshness and health in the executive report footer. A compelling visualization with outdated figures is not decision-grade reporting.

### Release governance checklist
1. Business purpose, approval owner and KPI definition version recorded.
2. Reconciliation and quality checks complete with documented exceptions.
3. Performance and capacity effect assessed.
4. RLS and workspace permissions validated.
5. Business UAT accepted.
6. Deployment, rollback, support owner and incident communication identified.
7. Post-release monitoring and stakeholder adoption reviewed.

### Suggested operational measures
Refresh SLA adherence, model ownership coverage, source reconciliation gap, report incident mean time to restore, unresolved critical KPI differences, certified model adoption, dashboard utilization and support burden by application. Interpret dashboards together with user feedback; raw view counts are not proof of business value.
