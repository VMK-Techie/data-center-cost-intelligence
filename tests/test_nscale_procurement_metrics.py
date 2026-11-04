import unittest
from datetime import date,datetime,timedelta
from decimal import Decimal
from src.nscale_procurement_metrics import *

class ProcurementMetricTests(unittest.TestCase):
    def test_wavg_price(self):
        self.assertEqual(weighted_unit_price([(2,100),(3,110)]),Decimal("106"))
    def test_price_trend(self):
        self.assertEqual(unit_price_change_pct([(2,100)],[(2,105)]),Decimal("5.00"))
    def test_otd_and_nonconformance(self):
        self.assertEqual(supplier_otd_pct(18,20),Decimal("90"))
        self.assertEqual(nonconformance_rate_pct(2,50),Decimal("4"))
    def test_response_adherence(self):
        self.assertEqual(responsiveness_sla_pct(16,20),Decimal("80"))
        self.assertEqual(commitment_adherence_pct(9,10),Decimal("90"))
    def test_variance(self):
        self.assertEqual(lead_time_variance_days(date(2026,6,12),date(2026,6,10)),2)
    def test_sourcing(self):
        self.assertEqual(rfp_bid_coverage_pct(3,5),Decimal("60.0"))
        self.assertEqual(sourcing_cycle_days(date(2026,1,2),date(2026,2,1)),30)
        self.assertEqual(contract_days_until_expiration(date(2026,1,1),date(2026,2,1)),31)
    def test_supply(self):
        self.assertEqual(supply_gap_units(12,9),Decimal("3"))
        self.assertEqual(supply_coverage_pct(9,12),Decimal("75.00"))
        self.assertEqual(projected_late_units(12,9),Decimal("3"))
    def test_wape(self):
        self.assertEqual(demand_forecast_wape_pct([10,20],[12,18]),Decimal("13.33333333333333333333333333"))
    def test_index_escalation(self):
        self.assertEqual(escalation_adjusted_cost(100,200,220,50),Decimal("160.0"))
        self.assertEqual(escalation_adjusted_cost(100,200,260,50,cap_pct=10),Decimal("160.0"))
    def test_scoring(self):
        weights={"delivery":".30","quality":".30","responsiveness":".15","adherence":".15","cost":".10"}
        scores={"delivery":90,"quality":80,"responsiveness":100,"adherence":80,"cost":70}
        self.assertEqual(normalized_weighted_score(scores,weights),Decimal("85.00"))
    def test_bad_weights(self):
        with self.assertRaises(ValueError):
            normalized_weighted_score({"x":80},{"x":".5"})
    def test_reconciliation(self):
        self.assertEqual(reconciliation_gap(500,505),Decimal("5"))
    def test_freshness(self):
        self.assertEqual(reporting_freshness_hours(datetime(2026,1,2),datetime(2026,1,1,12)),Decimal("12"))
    def test_invalid_denominator(self):
        with self.assertRaises(ValueError): supplier_otd_pct(1,0)

if __name__=="__main__":unittest.main()
