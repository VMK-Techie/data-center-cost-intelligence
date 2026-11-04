"""Synthetic portfolio reference formulas for OFCI sourcing and supplier reporting.

Decimal arithmetic is used for cost/ratio precision; dates are date objects.
Scores/thresholds are portfolio assumptions, NOT Nscale policy. No actual company data.
"""
from decimal import Decimal
from datetime import date

def d(v): return Decimal(str(v))
def divide(n, denom):
    if d(denom) <= 0: raise ValueError("Denominator must be positive")
    return d(n)/d(denom)
def pct(n, denom): return divide(n,denom)*100

def weighted_unit_price(rows):
    """rows: (quantity, unit_price). Like-for-like scope and currency required."""
    rows=list(rows)
    return divide(sum((d(q)*d(p) for q,p in rows), d(0)),
                  sum((d(q) for q,_ in rows),d(0)))

def unit_price_change_pct(prior_rows, current_rows):
    baseline=weighted_unit_price(prior_rows)
    return (divide(weighted_unit_price(current_rows),baseline)-1)*100

def supplier_otd_pct(on_time_accepted_deliveries, due_accepted_deliveries):
    return pct(on_time_accepted_deliveries,due_accepted_deliveries)

def lead_time_variance_days(actual_receipt:date, promised_receipt:date):
    """Positive = late; use frozen original promise for commitment adherence."""
    return (actual_receipt-promised_receipt).days

def lead_time_trend_days(current_period_avg, previous_period_avg):
    """Positive = deterioration in mean actual PO-to-receipt lead time."""
    return d(current_period_avg)-d(previous_period_avg)

def nonconformance_rate_pct(ncr_units, inspected_units):
    return pct(ncr_units,inspected_units)

def responsiveness_sla_pct(responses_within_sla, responses_due):
    return pct(responses_within_sla,responses_due)

def commitment_adherence_pct(deliveries_on_original_promise, due_deliveries):
    return pct(deliveries_on_original_promise,due_deliveries)

def rfp_bid_coverage_pct(compliant_bids_received, qualified_suppliers_invited):
    return pct(compliant_bids_received,qualified_suppliers_invited)

def sourcing_cycle_days(rfp_release:date, award_approval:date):
    days=(award_approval-rfp_release).days
    if days < 0: raise ValueError("Award before RFP release")
    return days

def milestone_on_time_pct(milestones_met, milestones_due):
    return pct(milestones_met,milestones_due)

def contract_days_until_expiration(as_of:date, expiration:date):
    return (expiration-as_of).days

def supply_gap_units(forecast_required_units, confirmed_available_units):
    return max(d(0),d(forecast_required_units)-d(confirmed_available_units))

def supply_coverage_pct(confirmed_available_units, forecast_required_units):
    return pct(confirmed_available_units, forecast_required_units)

def demand_forecast_wape_pct(actual_units, forecast_units):
    """Aggregate rows: denominator SUM(abs(actual)); avoid misleading averaging."""
    a=list(map(d,actual_units)); f=list(map(d,forecast_units))
    if len(a)!=len(f): raise ValueError("Actual/forecast series must align")
    return divide(sum((abs(x-y) for x,y in zip(a,f)),d(0)),
                  sum((abs(x) for x in a),d(0)))*100

def projected_late_units(required_units, committed_units_before_need_by):
    return supply_gap_units(required_units,committed_units_before_need_by)

def escalation_adjusted_cost(baseline_commodity_component, baseline_index, current_index, fixed_component=0, cap_pct=None):
    """Commodity-index escalation only on eligible cost component; floor/cap by contract."""
    change=divide(current_index,baseline_index)-1
    if cap_pct is not None: change=min(change,d(cap_pct)/100)
    return d(fixed_component)+d(baseline_commodity_component)*(1+change)

def reporting_freshness_hours(as_of, last_refresh):
    """Naive timestamps assumed same timezone; use timezone-aware in production."""
    seconds=(as_of-last_refresh).total_seconds()
    if seconds<0: raise ValueError("Refresh timestamp in the future")
    return d(seconds)/3600

def reconciliation_gap(finance_actuals, procurement_posted_actuals):
    """Nonzero = unresolved definition/timing/FX/interface difference."""
    return d(procurement_posted_actuals)-d(finance_actuals)

def normalized_weighted_score(score_by_dimension, weights):
    """0-100 higher-is-better scores, weights sum to 1; missing dimensions rejected."""
    if set(score_by_dimension)!=set(weights): raise ValueError("Scores and weights mismatch")
    if sum(map(d,weights.values()),d(0))!=1: raise ValueError("Weights must total 1")
    if any(not 0<=d(v)<=100 for v in score_by_dimension.values()):
        raise ValueError("Scores must lie in [0,100]")
    return sum((d(score_by_dimension[k])*d(weights[k]) for k in weights),d(0))
