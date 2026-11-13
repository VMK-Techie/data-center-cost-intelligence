import unittest
from datetime import date
from decimal import Decimal
from src.prime_portfolio_metrics import (
    portfolio_eac,variance_at_completion,portfolio_cost_per_it_mw,
    schedule_variance_days,milestone_on_time_rate,status_freshness_days,
    classify_project_risk,aggregate_milestone_rate,reporting_refresh_success,
    guarded_ratio
)
class PrimePortfolioMetricTests(unittest.TestCase):
    def setUp(self):
        self.rows=[(250,257,24),(126,123,12),(183,190,18),(312,320,30)]
    def test_portfolio_eac(self):
        self.assertEqual(portfolio_eac(self.rows),Decimal(890))
    def test_variance_convention(self):
        self.assertEqual(variance_at_completion(250,257),Decimal(-7))
    def test_weighted_cost_per_mw(self):
        self.assertEqual(portfolio_cost_per_it_mw(self.rows),Decimal(890)/Decimal(84))
    def test_schedule_variance(self):
        self.assertEqual(schedule_variance_days(date(2027,3,31),date(2027,4,15)),15)
    def test_on_time_weighted(self):
        self.assertEqual(aggregate_milestone_rate([(17,20),(12,12),(11,15),(7,9)]),Decimal(47)/Decimal(56))
    def test_update_age(self):
        self.assertEqual(status_freshness_days(date(2026,11,13),date(2026,11,3)),10)
    def test_escalation(self):
        self.assertEqual(classify_project_risk(2,15,0),"Escalate")
        self.assertEqual(classify_project_risk(1,2,0),"Monitor")
    def test_refresh(self):
        self.assertEqual(reporting_refresh_success(19,20),Decimal("0.95"))
    def test_zero_denominator(self):
        with self.assertRaises(ValueError): guarded_ratio(1,0)
    def test_future_status(self):
        with self.assertRaises(ValueError):status_freshness_days(date(2026,11,13),date(2026,11,14))
if __name__=="__main__":unittest.main()
