"""Reference metrics for a synthetic data-center analytics case study.

Uses Decimal for financial precision. Positive purchase-price variance is adverse.
Values use agreed scopes; do not treat these formulas as accounting policy.
"""
from decimal import Decimal

def D(x):
    return Decimal(str(x))

def ratio(numerator, denominator):
    n, d = D(numerator), D(denominator)
    if d == 0:
        raise ValueError("Denominator must not be zero")
    return n / d

def capex_per_mw(capex_usd, it_mw):
    return ratio(capex_usd, it_mw)

def capex_per_kw(capex_usd, it_mw):
    return ratio(capex_usd, D(it_mw) * 1000)

def landed_cost(base, freight=0, duties=0, tariffs=0, escalation=0, other=0):
    return sum(map(D, (base, freight, duties, tariffs, escalation, other)), D(0))

def price_variance(actual_unit_price, baseline_unit_price, quantity):
    return (D(actual_unit_price) - D(baseline_unit_price)) * D(quantity)

def open_commitment(po_total, invoiced_against_po):
    balance = D(po_total) - D(invoiced_against_po)
    if balance < 0:
        raise ValueError("Invoiced value exceeds PO value; reconcile before calculation")
    return balance

def estimate_at_completion(actuals, open_commitments, uncommitted_etc):
    return D(actuals) + D(open_commitments) + D(uncommitted_etc)

def forecast_variance_at_completion(approved_budget, eac):
    return D(approved_budget) - D(eac)

def cost_per_cooling_ton(cooling_cost, design_tons):
    return ratio(cooling_cost, design_tons)

def it_utilization(measured_it_kw, commissioned_it_kw):
    return ratio(measured_it_kw, commissioned_it_kw)

def pue(facility_kwh, it_kwh):
    return ratio(facility_kwh, it_kwh)

def wue(site_water_liters, it_kwh):
    return ratio(site_water_liters, it_kwh)

def supplier_on_time(on_time_deliveries, due_deliveries):
    return ratio(on_time_deliveries, due_deliveries)

def five_year_tco(initial_capex, annual_opex, refresh_cost=0, residual_value=0):
    return D(initial_capex) + sum(map(D, annual_opex)) + D(refresh_cost) - D(residual_value)

def npv_outflows(initial_capex, annual_cash_outflows, discount_rate):
    rate = D(discount_rate)
    if rate <= -1:
        raise ValueError("Discount rate must be greater than -100%")
    return D(initial_capex) + sum(D(cf) / (1 + rate)**year for year, cf in enumerate(annual_cash_outflows, 1))
