import pandas as pd
import numpy as np
import os

# Path to the dataset
data_path = os.path.join("..", "dataset", "ngo_data.csv")

def load_data(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        print("Dataset loaded successfully.")
        print(df.head())
        return df
    else:
        print(f"File not found: {path}")
        return None

if __name__ == "__main__":
    df = load_data(data_path)
    if df is not None:
        # Example: Calculate average cost
        avg_cost = df['cost'].mean()
        print(f"\nAverage Program Cost: ${avg_cost:,.2f}")
