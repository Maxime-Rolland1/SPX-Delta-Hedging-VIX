import numpy as np
from scipy.stats import norm


def d1(S, K, T, r, sigma):
    """Calcule d1 de Black-Scholes."""
    return (np.log(S/K) + (r+sigma**2/2)*T)/ (sigma*np.sqrt(T))

def bs_call_price(S, K, T, r, sigma):
    """Prix d'un call européen."""
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d_1 - sigma * np.sqrt(T)		
    return S*norm.cdf(d_1) - K*np.exp((-r*T))*norm.cdf(d_2)


def bs_call_delta(S, K, T, r, sigma):
    """Delta d'un call européen."""
    d_1 = d1(S, K, T, r, sigma)
    return norm.cdf(d_1)
    


if __name__ == "__main__":
    print(bs_call_price(100, 100, 1, 0.05, 0.20))
    print(bs_call_delta(100, 100, 1, 0.05, 0.20))