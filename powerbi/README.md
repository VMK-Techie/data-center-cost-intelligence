# Data Center Cost & Procurement — Power BI Project

This is an editable **Power BI Project (PBIP)** using a source-controlled **Power BI report definition (PBIR)** and a **tabular model.bim** semantic model. Source data is embedded as *synthetic* Power Query M tables, so external credentials are not required.

## Open the report
1. Clone/download the parent GitHub repository.
2. Open `powerbi/DataCenterCostProcurement.pbip` in a recent release of **Power BI Desktop** on Windows with PBIP support.
3. Apply changes/refresh if prompted.
4. Check the five pages and measures. If your Desktop release flags a report definition schema compatibility issue, create a blank report and reuse the `model.bim` model and DAX measures, or use the CSV data files in the main repository. PBIR schemas evolve and the project has **not yet been opened and visually tested in Power BI Desktop** in this environment.
5. When working, save in Power BI Desktop, then commit the native generated project files back to the repository. Capture a screenshot from Desktop for the hiring-manager portfolio.

## Five pages (28 visual definitions)

| Page | KPIs and analysis |
| --- | --- |
| Executive Overview | Approved CAPEX, EAC, forecast overrun, cost per IT MW, project budget vs EAC, OFCI vs CFCI equipment |
| CAPEX & Cost per MW | Actuals, open commitments, uncommitted ETC, VAC, project comparison, site cost per MW |
| OFCI-CFCI Equipment | Baseline vs proposed landed equipment costs by item and by procurement ownership |
| Supplier Comparison | Total landed vendor bid by package, supplier lead time and quality score |
| Cash Flow Forecast | Monthly forecast vs actual cash, annual totals, remaining forecast |

**No real employer data, client documents, supplier bids or project claims are included.**

## Data model
Four imported model tables are embedded in the semantic model: `Projects`, `Equipment`, `VendorBids`, `CashFlow`. These are intentionally **separate small illustrative subject areas**, not a fake shared fact grain. The main warehouse architecture in a production implementation would use conformed DimProject, DimVendor, DimEquipment, DimDate and separate actuals, commitments, purchase-order, billing, metering and forecast facts.

### Key financial definitions
- **EAC = posted actuals + PO open commitments net of invoicing + uncommitted ETC.** This assumes invoiced PO costs are already included in actuals.
- **Variance at completion = approved budget − EAC**; negative means an overrun.
- **Cost per MW** is forecast project CAPEX divided by commissioned IT MW, not gross facility electrical supply MW.
- **Equipment cost avoidance** is modeled baseline landed amount less proposed landed amount; it is *potential*, not realized or booked savings.
- **Vendor landed bid** is quantity × (base + freight + duties + tariffs + escalation). Compare vendors within the *same* bid package; different packages are not comparable.
- **Cash flow** represents paid or projected USD cash movements, distinct from posted accounting actuals. The synthetic monthly dataset intentionally sets future-month actuals to zero. Display zero as “not yet recorded,” not “under budget.”

### Portfolio caveats
The Vendor Comparison page's global total and average across multiple bid packages are illustrative **screening** indicators, not an award decision. In a production report, bind a slicer to bid package and show per-package rankings based on executable landed costs, service level, quality, warranty and schedule impact.

## Technical files
- [Open the PBIP project](DataCenterCostProcurement.pbip)
- [Semantic model](DataCenterCostProcurement.SemanticModel/model.bim)
- [Report definition](DataCenterCostProcurement.Report/definition/report.json)
- [Page configuration](DataCenterCostProcurement.Report/definition/pages/pages.json)
- [Financial Python test suite](../tests/test_metrics.py)
- [Synthetic source CSV](../data/projects_synthetic.csv)

## Follow-on enhancements
Replace embedded tables with Fabric Warehouse or CSV-backed Power Query, add proper date/calendar dimension, scenario parameters, vendor package slicer and multi-period variance bridge, then publish from Power BI Desktop to an authorized Power BI workspace. GitHub does **not** host an interactive Power BI report: it hosts the **editable source project**. Publishing a live interactive report requires a Power BI workspace and appropriate access permissions.
