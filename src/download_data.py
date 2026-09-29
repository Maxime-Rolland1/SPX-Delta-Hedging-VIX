import yfinance as yf
import pandas as pd

START = "2005-01-01"

def download_close(ticker):
    """Télécharge les cours de clôture journaliers d'un ticker Yahoo Finance."""
    df = yf.Ticker(ticker).history(start=START)
    df.index = df.index.tz_localize(None)  # enlève le fuseau horaire pour aligner les dates
    return df["Close"]

spx = download_close("^GSPC")
vix = download_close("^VIX")

data = pd.concat([spx, vix], axis=1, keys=["SPX", "VIX"]).dropna()
data.to_csv("data/spx_vix.csv")

print(data.head())
print(data.tail())
print("Nombre de jours :", len(data))