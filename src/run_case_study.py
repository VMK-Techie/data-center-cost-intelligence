"""Run the self-contained, synthetic decision case."""
try:
    from .metrics import *
except ImportError:
    from metrics import *

def main():
    budget = D(250_000_000)
    actuals = D(140_000_000)
    remaining_open_pos = D(81_000_000)
    uncommitted_etc = D(36_000_000)
    eac = estimate_at_completion(actuals, remaining_open_pos, uncommitted_etc)
    baseline = landed_cost(3_900_000, 120_000, 50_000, 100_000, 35_000)
    bid = landed_cost(3_650_000, 130_000, 50_000, 155_000, 25_000)
    print('SYNTHETIC CASE — 24 MW IT data center (USD)')
    print(f'Approved CAPEX: ${budget:,.0f}')
    print(f'Estimate at completion: ${eac:,.0f}')
    print(f'Forecast budget overrun: ${-forecast_variance_at_completion(budget, eac):,.0f}')
    print(f'Forecast cost per IT MW: ${capex_per_mw(eac, 24):,.0f}')
    print(f'Baseline vendor landed unit cost: ${baseline:,.0f}')
    print(f'Alternative vendor landed unit cost: ${bid:,.0f}')
    print(f'Illustrative cost avoidance for 4 identical units: ${(baseline-bid)*4:,.0f}')
    print(f'Annual PUE: {pue(168_000_000, 120_000_000):.2f}')
    print('RECOMMENDATION: reconcile overrun by cost package; validate equivalent vendor specs,')
    print('delivery dates, warranty and redundancy before counting forecast cost avoidance.')
if __name__ == '__main__':
    main()
