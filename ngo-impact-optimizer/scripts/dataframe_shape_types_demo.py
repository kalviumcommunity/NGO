import pandas as pd

# Load the NGO programs dataset
# This file contains the standard NGO program records for analysis.
file_path = "data/raw/ngo_programs.csv"
ngo_df = pd.read_csv(file_path)

# ---------------------------------------------------------
# 1. Inspect Dataset Shape
# ---------------------------------------------------------
print("--- 1. Dataset Shape ---")
# .shape returns a tuple representing (number_of_rows, number_of_columns).
# First value (index 0) = total number of NGO records.
# Second value (index 1) = total number of features/attributes.
dataset_shape = ngo_df.shape
print(f"DataFrame Shape: {dataset_shape}")
print(f"Number of Records: {dataset_shape[0]}")
print(f"Number of Features: {dataset_shape[1]}")
print("-" * 50)

# ---------------------------------------------------------
# 2. Inspect Column Data Types
# ---------------------------------------------------------
print("\n--- 2. Column Data Types ---")
# .dtypes shows the data type for every column in the DataFrame.
# - Numeric columns are typically int64 (whole numbers) or float64 (decimals).
# - Categorical/Text columns are usually stored as 'object' types.
print(ngo_df.dtypes)
print("-" * 50)

# ---------------------------------------------------------
# 3. Data Interpretation
# ---------------------------------------------------------
print("\n--- 3. Interpretation Summary ---")
print("Rows represent individual NGO program entries in the database.")
print("Columns represent specific attributes like cost, location, and people_helped.")
print("\nData types provide critical info for analysis:")
print("- 'int64' and 'float64' means we can perform math (sums, averages) on these fields.")
print("- 'object' indicates text categories which we use for grouping and filtering.")

print("\nConclusion: DataFrame shape and data types inspection completed successfully.")
