import unittest
from decimal import Decimal
from src.metrics import (capex_per_mw,capex_per_kw,landed_cost,price_variance,
    open_commitment,estimate_at_completion,forecast_variance_at_completion,pue,ratio,npv_outflows)
class MetricsTests(unittest.TestCase):
    def test_capex(self):
        self.assertEqual(capex_per_mw(240_000_000,24),Decimal('10000000'))
        self.assertEqual(capex_per_kw(240_000_000,24),Decimal('10000'))
    def test_landed(self):
        self.assertEqual(landed_cost(100,5,3,2,1),Decimal('111'))
    def test_ppv_adverse(self):
        self.assertEqual(price_variance(120,100,4),Decimal('80'))
    def test_commitment_no_double_count(self):
        self.assertEqual(open_commitment(100,40),Decimal('60'))
        self.assertEqual(estimate_at_completion(40,60,20),Decimal('120'))
    def test_eac(self):
        self.assertEqual(forecast_variance_at_completion(100,120),Decimal('-20'))
    def test_pue(self):
        self.assertEqual(pue(140,100),Decimal('1.4'))
    def test_zero_guard(self):
        with self.assertRaises(ValueError): ratio(4,0)
    def test_bad_po(self):
        with self.assertRaises(ValueError): open_commitment(10,11)
    def test_npv(self):
        self.assertEqual(npv_outflows(100,[110],Decimal('0.1')),Decimal('200'))
if __name__ == '__main__': unittest.main()
