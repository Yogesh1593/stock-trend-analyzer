import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def fetch_stock_data(symbol):
    print(f"Fetching data for {symbol}...")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&outputsize=compact"
    
    response = requests.get(url)
    data = response.json()
    
    # Add this line to debug the response
    print(data)

    if "Time Series (Daily)" not in data:
        raise ValueError("Unexpected API response format")

    # Your parsing logic continues here...
