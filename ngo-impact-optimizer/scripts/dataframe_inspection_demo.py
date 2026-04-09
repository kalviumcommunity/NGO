import pandas as pd

# Load the NGO programs dataset
# This file was created in a previous step and contains realistic NGO data points.
file_path = "data/raw/ngo_programs.csv"
ngo_df = pd.read_csv(file_path)

# ---------------------------------------------------------
# 1. Preview Data using head()
# ---------------------------------------------------------
print("--- 1. Data Preview (.head()) ---")
# head() displays the first few rows (default is 5) for quick visual understanding 
# of the dataset's structure and initial values.
print(ngo_df.head())
print("-" * 50)

# ---------------------------------------------------------
# 2. Inspect Structure using info()
# ---------------------------------------------------------
print("\n--- 2. Structural Inspection (.info()) ---")
# info() provides a concise summary of the DataFrame:
# - Total number of entries (rows)
# - Column names and order
# - Number of non-null values (helps identify missing data)
# - Column data types (Dtype)
# - Memory usage
ngo_df.info()
print("-" * 50)

# ---------------------------------------------------------
# 3. Summary Statistics using describe()
# ---------------------------------------------------------
print("\n--- 3. Summary Statistics (.describe()) ---")
# describe() generates descriptive statistics for all numeric columns.
# - count: number of non-empty values
# - mean: the average value
# - std: standard deviation (variance in data)
# - min/max: range of the data
# - percentiles: distribution of the values (25%, 50%, 75%)
print(ngo_df.describe())
print("-" * 50)

print("\nConclusion: DataFrame inspection demonstration completed successfully.")
