# \# SPX Delta Hedging with VIX

# 

# Backtest of the delta hedging of an S\&P 500 call, priced with the VIX

# as implied volatility, on real historical data (2005 to today).

# 

# \## Objective

# Measure how effective daily delta hedging is on real data, and relate the

# final PnL to the gap between implied volatility (VIX) and realized volatility.

# 

# \## Progress

# \- \[x] Data download (SPX and VIX from Yahoo Finance) -> data/spx\_vix.csv

# \- \[x] Black-Scholes call pricer and delta (src/pricing.py)

# \- \[ ] Hedging on a simulated path (src/hedging.py)

# \- \[ ] Hedging on one real 30-day window

# \- \[ ] Backtest over all windows

# \- \[ ] Analysis: PnL vs (VIX - realized volatility)

# \- \[ ] Extensions: transaction costs, rebalancing frequency, crises

# 

# \## Limits and assumptions (to complete)

# \- The VIX is a proxy for the implied volatility of a 30-day at-the-money call.

# \- Overlapping windows are not independent.

# \- The option is theoretical, not a real traded contract.

