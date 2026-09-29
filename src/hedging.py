import numpy as np
from pricing import bs_call_price, bs_call_delta


def simulate_gbm(S0, r, sigma, T, n_steps, seed=None):
    """Simule une trajectoire de prix (mouvement brownien géométrique).
    Renvoie un tableau de n_steps + 1 prix, de t=0 à t=T."""
    # TODO


def delta_hedge_pnl(path, K, T, r, sigma):
    """PnL final d'un vendeur de call couvert chaque jour en delta."""
    # TODO


if __name__ == "__main__":
    path = simulate_gbm(100, 0.05, 0.20, 1, 252, seed=42)
    print(delta_hedge_pnl(path, 100, 1, 0.05, 0.20))