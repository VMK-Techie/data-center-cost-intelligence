# Power BI semantic-model measures (illustrative)

Use dimension tables `DimProject`, `DimDate`, `DimVendor`, `DimEquipment`, with fact tables `FactActual`, `FactPO`, `FactETC`, `FactFacilityEnergy`.

```dax
Actual Spend USD = SUM(FactActual[ActualUSD])
Approved Budget USD = SUM(DimProject[ApprovedBudgetUSD])
Open Commitments USD = SUMX(FactPO, FactPO[POValueUSD] - FactPO[InvoicedUSD])
Uncommitted ETC USD = SUM(FactETC[UncommittedETCUSD])
EAC USD = [Actual Spend USD] + [Open Commitments USD] + [Uncommitted ETC USD]
Variance At Completion USD = [Approved Budget USD] - [EAC USD]
EAC Per IT MW USD = DIVIDE([EAC USD], SUM(DimProject[CommissionedITMW]))
Purchase Price Variance USD = SUMX(FactPO, (FactPO[ActualUnitPriceUSD] - FactPO[BaselineUnitPriceUSD]) * FactPO[Quantity])
Total Facility kWh = SUM(FactFacilityEnergy[FacilityKWh])
IT Equipment kWh = SUM(FactFacilityEnergy[ITKWh])
PUE = DIVIDE([Total Facility kWh], [IT Equipment kWh])
```

**Power BI modeling caution:** For a portfolio-wide per-MW value, `SUM(cost) / SUM(MW)` is the capacity-weighted ratio. Ensure project budget is stored once per project, and avoid duplicating approved budgets in a fact table with multiple rows per project. Energy readings must be additive across projects but not accidentally duplicated by equipment joins. Model PO partial invoice and actual postings with consistent keys to avoid double counting.
