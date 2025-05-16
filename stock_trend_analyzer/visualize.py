import matplotlib.pyplot as plt
import pandas as pd

def plot_stock(df: pd.DataFrame, symbol: str):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price', linewidth=2)
    plt.plot(df['SMA_10'], label='10-Day SMA', linestyle='--')
    plt.plot(df['SMA_30'], label='30-Day SMA', linestyle='--')
    
    plt.title(f"{symbol} Stock Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend
