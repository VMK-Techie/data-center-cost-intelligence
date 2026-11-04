# Data Center Cost Intelligence & FP&A | Analytics Engineering Portfolio

## 📊 Power BI Data Center Cost & Procurement Dashboard

**Five-page editable Power BI Project (PBIP) published:** [Open dashboard source](powerbi/DataCenterCostProcurement.pbip) · [Read setup and modeling notes](powerbi/README.md).

Includes CAPEX tracking, forecast CAPEX per IT MW, OFCI/CFCI procurement cost, multi-vendor total landed cost, and cash-flow forecasting using synthetic data. The project source is versioned in GitHub; an interactive published Power BI report is not hosted here. **Power BI Desktop open/render validation remains pending.**


**Focus:** data center CAPEX, OFCI/CFCI sourcing, power/cooling cost normalization, procurement variance, vendor performance, financial forecasting and executive decisions.

> **Portfolio demonstration, not employer work product.** All datasets, bids, assumptions and outcomes are synthetic. These are not claims of actual savings at Vantage Data Centers or any other company.

## Why this matters
The lowest quoted equipment price may not be the lowest total project cost once tariffs, freight, escalation, delivery lead times, warranties and commissioning are included. This project connects purchasing decisions to cost per MW, estimate at completion (EAC), cash flow and TCO.

## Repository guide
- [KPI catalog](docs/METRIC_CATALOG.csv): definitions, formulas, units and caveats
- [Python metrics](src/metrics.py): reusable Decimal-based calculations and input guards
- [Runnable case study](src/run_case_study.py): synthetic 24 MW project analysis
- [SQL models](sql/kpi_models.sql): EAC, purchase price variance and project exposure
- [Power BI DAX](docs/POWER_BI_DAX.md): semantic model and measure patterns
- [Decision story](docs/DECISION_STORY.md): executive implications and risk controls
- [Data dictionary](docs/DATA_DICTIONARY.md): KPI definitions and validation
- [Synthetic data](data/): projects and equipment bids
- [Tests](tests/test_metrics.py): Python unit tests

## Run
Python 3.9+; no external dependencies.

```bash
python -m src.run_case_study
python -m unittest discover -s tests -v
```

## Core calculations
| KPI | Calculation | Interpretation |
| --- | --- | --- |
| Forecast CAPEX / IT MW | EAC / commissioned IT MW | Normalized project cost |
| EAC | Actuals + open commitments + uncommitted ETC | Forecast at completion |
| Variance at completion | Approved budget − EAC | Negative = overrun |
| Total landed cost | Unit cost + freight + duties + tariffs + escalation + other | Compare equivalent supplier bids |
| PPV | (Actual unit price − approved baseline price) × quantity | Positive = adverse |
| PUE | Total facility energy / IT equipment energy | Annual energy overhead |

## Synthetic case study
A **24 MW IT** project has **$250M approved budget**, **$140M actuals**, **$81M open commitments** and **$36M remaining uncommitted ETC**. Result: **$257M EAC**, **$7M forecast overrun**, and **$10.708M forecast CAPEX per IT MW**. A separately evaluated four-unit alternative vendor bid indicates **$780K possible cost avoidance**, before specification, schedule and commercial risk checks.

These are illustrative scenarios and are not a claim of realized business results. Do not subtract potential savings from EAC without validating the baseline and reconciling procurement assumptions.

## Proposed Microsoft Fabric architecture
ERP / PO / vendor contracts / metering → Bronze ingestion → Silver quality & normalization → Gold Warehouse dimensional models → certified Power BI semantic model → executive scorecards.

Data governance must define the IT capacity denominator, approved budget baseline, currency and FX date, invoice treatment, PO change orders, supplier-bid comparability and report security.

## Next improvements
1. Dated cash-flow forecast and monthly forecast error.
2. Weighted vendor bid scorecards with lead-time, warranty and reliability factors.
3. A portable Power BI project (`.pbip`) and dashboard screenshots using synthetic data.
4. Automated data-quality validations.

**Contact:** Replace this section with your LinkedIn and professional email before sharing.

## References
- [US Department of Energy: Data Center Design Best Practices](https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf)
- [GitHub profile README documentation](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
