"""Prime-aligned data center project reporting reference formulas.

Synthetic portfolio only; does not access or represent Prime Data Centers' systems.
Dates and dimensions must share a documented reporting cutoff and approved baselines.
"""
from decimal import Decimal
from datetime import date

def dec(v): return Decimal(str(v))

def guarded_ratio(num, denom):
    if dec(denom) <= 0:
        raise ValueError("Denominator must be positive")
    return dec(num) / dec(denom)

def portfolio_eac(project_rows):
    """Iterable of (approved_budget_usd, forecast_eac_usd, commissioned_it_mw)."""
    rows=list(project_rows)
    return sum((dec(r[1]) for r in rows), dec(0))

def variance_at_completion(approved_budget, forecast_eac):
    """Positive = favorable forecast underrun, negative = overrun."""
    return dec(approved_budget)-dec(forecast_eac)

def portfolio_cost_per_it_mw(project_rows):
    """Capacity-weighted cost per MW; never arithmetic mean of project ratios."""
    rows=list(project_rows)
    return guarded_ratio(sum((dec(r[1]) for r in rows),dec(0)),
                         sum((dec(r[2]) for r in rows),dec(0)))

def schedule_variance_days(baseline_finish:date, forecast_finish:date):
    """Positive = later than frozen approved baseline."""
    return (forecast_finish - baseline_finish).days

def milestone_on_time_rate(on_time_milestones, milestones_due):
    return guarded_ratio(on_time_milestones,milestones_due)

def milestone_completion_rate(completed_milestones, milestones_due):
    return guarded_ratio(completed_milestones,milestones_due)

def status_freshness_days(as_of:date,last_approved_status:date):
    lag=(as_of-last_approved_status).days
    if lag<0: raise ValueError("Status update in future relative to cutoff")
    return lag

def completeness_rate(populated_required_fields,expected_required_fields):
    return guarded_ratio(populated_required_fields,expected_required_fields)

def reporting_refresh_success(successful_runs, scheduled_runs):
    return guarded_ratio(successful_runs,scheduled_runs)

def intake_sla_rate(triaged_within_sla, requests_requiring_triage):
    return guarded_ratio(triaged_within_sla,requests_requiring_triage)

def forecast_variance_pct(total_budget,total_eac):
    return guarded_ratio(dec(total_budget)-dec(total_eac),total_budget)

def classify_project_risk(forecast_overrun_pct, delay_days, open_critical_overdue_risks,
                          overrun_threshold_pct=5, late_days_threshold=14):
    """Illustrative portfolio exception rules only, not Prime operating policy.

    input positive forecast_overrun_pct = adverse spending versus approved budget.
    """
    if (dec(forecast_overrun_pct)>=dec(overrun_threshold_pct)
        or delay_days>late_days_threshold or open_critical_overdue_risks>0):
        return "Escalate"
    return "Monitor"

def aggregate_milestone_rate(project_rows):
    """Iterable of (on_time_milestones, milestones_due); uses weighted totals."""
    rows=list(project_rows)
    return milestone_on_time_rate(sum(int(a) for a,b in rows),
                                  sum(int(b) for a,b in rows))
