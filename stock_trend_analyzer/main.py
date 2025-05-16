from stock_trend_analyzer.fetch_data import fetch_stock_data
from stock_trend_analyzer.analyze_data import add_indicators
from stock_trend_analyzer.visualize import plot_stock
from stock_trend_analyzer.utils import save_to_csv

def main():
    symbol = "AAPL"
    print(f"Fetching data for {symbol}...")
    df = fetch_stock_data(symbol)
    df = add_indicators(df)
    save_to_csv(df, symbol)
    plot_stock(df, symbol)

if __name__ == "__main__":
    main()
