import numpy as np
from pricing import bs_call_price, bs_call_delta


def simulate_gbm(S0, r, sigma, T, n_steps, seed=None):
    """Simule une trajectoire de prix (mouvement brownien géométrique).
    Renvoie un tableau de n_steps + 1 prix, de t=0 à t=T."""
    dt = T / n_steps
    rng = np.random.default_rng(seed)
    Z=rng.standard_normal(n_steps)
    S = np.zeros(n_steps + 1)
    S[0] = S0
    for t in range(1, n_steps + 1):
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[t - 1])
    return S


def delta_hedge_pnl(path, K, T, r, sigma):
    """PnL final d'un vendeur de call couvert chaque jour en delta."""
    n_steps = len(path) - 1
    dt = T / n_steps
    cash_account = 0.0
    shares_held = 0.0

    for t in range(n_steps):
        if t==0:
            # Initial hedge: sell the call and buy delta shares
            time_to_maturity = T
            delta = bs_call_delta(path[t], K, time_to_maturity, r, sigma)
            shares_held = delta
            cash_account += bs_call_price(path[t], K, time_to_maturity, r, sigma) - shares_held * path[t]
        else:
            time_to_maturity = T - t * dt
            cash_account *= np.exp(r * dt)  # accrue interest on cash account
            delta = bs_call_delta(path[t], K, time_to_maturity, r, sigma)
            cash_account -= (delta - shares_held) * path[t]  # adjust cash for change in shares
            shares_held = delta
         
    cash_account *= np.exp(r * dt)  # accrue interest on cash account
    payoff = max(path[-1] - K, 0)
    return cash_account + shares_held * path[-1] - payoff            


if __name__ == "__main__":
    path = simulate_gbm(100, 0.05, 0.20, 1, 252, seed=42)
    print(delta_hedge_pnl(path, 100, 1, 0.05, 0.20))