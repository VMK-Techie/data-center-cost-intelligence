

## Business questions hiring managers care about
1. Which power and cooling suppliers are likely to miss project installation dates?
2. Where is equipment demand greater than confirmed, specification-compliant supply?
3. What is the normalized landed-cost and price-escalation exposure by site, vendor, and equipment family?
4. How competitive and timely are our RFPs, awards, and supplier agreements?
5. Can executives trust the metrics: reconciliation, source freshness, and consistent definitions?

## New metrics and calculation logic
See [30 additions](KPI_ADDITIONS.csv) and [Python reference formulas](../src/procurement_metrics.py).
The KPI catalog is intentionally **separate from the original 51-metric catalog** to make the job-specific additions auditable.

| Domain | Metrics introduced | Management action |
|---|---|---|
| Supplier performance | on-time accepted deliveries, original commitment adherence, NCR rate, NCR closure, response SLA, supplier score and corrective action closure | escalate suppliers before site schedule impact |
| Supply and demand | confirmed supply vs forecast required units, shortfall, at-risk equipment, forecast WAPE and bias | trigger alternate sourcing or adjust PO timing |
| Sourcing execution | RFP bid coverage, sourcing cycle, milestone adherence, award completion, expiration risk, bid price spread, bid-tab readiness | manage procurement pipeline and contract renewals |
| Commodity and cost | commodity-index escalation, forecast landed-cost exposure | stress-test copper/steel/aluminum escalation and tariffs |
| Data controls | dataset refresh age, Finance-vs-procurement reconciliation, refresh success and metric lineage | strengthen management's confidence in scorecards |

### Configurable weighted supplier scorecard

**Illustrative dimensions and weights — not Nscale policy.**

- On-time delivery: 30%
- Quality / nonconformance: 30%
- Response SLA compliance: 15%
- Original promise adherence: 15%
- Landed-cost competitiveness: 10%

For all inputs, convert each metric to a comparable **0–100, higher-is-better score** first. Scores for lead time, price, and nonconformance require a documented scoring band or benchmark. Never add unnormalized dollars, days and percentages. If a dimension is missing, flag the supplier *Not Scorable*, rather than automatically assigning zero.

**Example:** delivery 90, quality 80, responsiveness 100, adherence 80, cost 70 → score = **85/100**.

The score is a decision-support input; sourcing should also consider disqualifying requirements such as equipment certification, 2N redundancy, approved technical specifications and contractual terms.

### Example DAX for future Power BI extension

The existing five-page PBIP report remains a financial portfolio foundation. To show the following metrics in Power BI, add the synthetic supplier and sourcing CSVs as tables first, and create the measures below. These DAX measures are **not yet wired into the PBIP report pages**.

```dax
Supplier On-Time Delivery % =
DIVIDE(SUM(SupplierEvents[on_time_deliveries]),
       SUM(SupplierEvents[due_deliveries]))

Supplier Original Promise Adherence % =
DIVIDE(SUM(SupplierEvents[original_promise_met]),
       SUM(SupplierEvents[due_deliveries]))

Nonconformance % =
DIVIDE(SUM(SupplierEvents[ncr_units]),
       SUM(SupplierEvents[inspected_units]))

Supplier Response SLA % =
DIVIDE(SUM(SupplierEvents[responses_within_sla]),
       SUM(SupplierEvents[responses_due]))

Confirmed Supply Coverage % =
DIVIDE(SUM(SourcingEvents[confirmed_available_before_need]),
       SUM(SourcingEvents[required_units]))

Supply Shortfall Units =
SUMX(SourcingEvents,
    MAX(0, SourcingEvents[required_units] -
           SourcingEvents[confirmed_available_before_need]))

RFP Bid Coverage % =
DIVIDE(SUM(SourcingEvents[compliant_bids]),
       SUM(SourcingEvents[qualified_invited]))
```

**Denominator controls:** use BLANK for empty populations, audit dates with original committed vs revised date, and interpret RFP coverage as bid participation (not supplier award quality).

## Synthetic data and executable examples
- [Supplier quarterly event samples](../data/supplier_events_synthetic.csv)
- [Sourcing and award samples](../data/sourcing_events_synthetic.csv)
- [Python metrics](../src/nscale_procurement_metrics.py)
- [Unit tests](../tests/test_nscale_procurement_metrics.py)

Run from repository root:
```bash
python -m unittest discover -s tests -v
```

## Executive presentation outline
**Slide 1:** Power/cooling OFCI cost per MW by campus with budget, actuals, commitments and EAC.
**Slide 2:** Supplier on-time and original-promise compliance; top late critical components and lead-time trends.
**Slide 3:** Supply-demand gap by equipment and required-by project milestone; at-risk units and remediation owners.
**Slide 4:** RFP pipeline, qualified bid coverage, bid normalization and sourcing cycle time.
**Slide 5:** Landed-cost exposure (freight/duties/tariff/commodity escalation) and Finance reconciliation exceptions.

## Data governance
Use unique keys for PO lines, supplier sites, procurement packages, original and revised promised receipt dates, quality inspection lots, RFP and award records, and baseline versions. Supplier delivery history should be matched to accepted goods receipt dates, not PO issue dates. Commodity indexes require correct base date, contract-specific applicable portion, and cap/floor terms.

**Limitations:** sample project scale, supplier performance, financial values, and thresholds are invented. Actual reporting would require controlled ERP/procurement data, supplier confirmations, engineering approved Bill of Materials, and data-quality ownership.
