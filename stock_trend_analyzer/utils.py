import pandas as pd

def save_to_csv(dataframe, filename="output.csv"):
    """
    Save a pandas DataFrame to a CSV file.
    """
    dataframe.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

