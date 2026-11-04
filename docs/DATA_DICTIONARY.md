# Data dictionary and governance

All repository input data are fabricated and designed for training, demonstration, and interviewing.

| Field | Grain | Meaning | Rule |
|---|---|---|---|
| project_id | project | Unique data center build/phase ID | Stable, non-null |
| commissioned_it_mw | project | Commissioned deliverable IT nameplate capacity | >0; do not substitute campus utility MW |
| approved_budget_usd | project | Current approved project budget baseline | Record baseline effective date |
| actual_cost_usd | posting | Posted costs in agreed accounting scope | Deduplicate ledger postings |
| po_total_usd | PO line | Approved purchase order amount | Excludes canceled lines |
| invoiced_usd | PO line | Invoice amount matched to PO | Must not exceed PO without reconciliation |
| open_commitments_usd | PO line | PO total less matched invoiced amount | Must not count in actuals again |
| uncommitted_etc_usd | work package | Forecast of not-yet-committed remaining work | Excludes open commitments |
| facility_kwh | site-month | Utility/facility energy within metering boundary | Same site and date as IT kWh |
| it_kwh | site-month | IT equipment electrical energy | >0; match period |
| unit_price_usd | PO line | Actual quoted/ordered equipment unit price | Normalize model/spec |
| baseline_unit_price_usd | PO line | Approved comparable price baseline | Store version and source |

## Quality tests for production
- Project ID must exist in project dimension and have one approved baseline per version.
- Line-level unique PO ID and invoice matching keys; no duplicated invoice postings.
- Valid currency conversion on transaction date; distinguish USD vs local currencies.
- Standardized equipment taxonomy and scope (equipment, installation, commissioning).
- No negative capacity or zero denominator; flag uncommissioned sites.
- Specify vintage of forecasts, tariffs, FX and duty rates.
- Restricted or commercially sensitive vendor bids must never enter public GitHub.
