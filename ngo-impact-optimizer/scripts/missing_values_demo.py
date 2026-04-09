import pandas as pd

# ---------------------------------------------------------
# 1. Load Dataset
# ---------------------------------------------------------
# Loading the NGO programs CSV which now contains missing values (NaN)
file_path = "data/raw/ngo_programs.csv"
ngo_df = pd.read_csv(file_path)

# ---------------------------------------------------------
# 2. Detect Missing Values
# ---------------------------------------------------------
print("--- 1. Missing Value Detection (.isnull()) ---")
# isnull() returns a DataFrame of the same shape where each cell 
# is True if the value is missing (NaN), otherwise False.
print(ngo_df.isnull())
print("-" * 50)

# ---------------------------------------------------------
# 3. Count Missing Values per Column
# ---------------------------------------------------------
print("\n--- 2. Missing Value Count (.isnull().sum()) ---")
# sum() applied after isnull() counts the number of True values (missing) per column.
missing_counts = ngo_df.isnull().sum()
print(missing_counts)
print("-" * 50)

# ---------------------------------------------------------
# 4. Identify Columns with Missing Data
# ---------------------------------------------------------
print("\n--- 3. Columns with Missing Data ---")
# Filtering to find specifically which features are incomplete
cols_with_missing = missing_counts[missing_counts > 0].index.tolist()
print(f"Features requiring cleaning: {cols_with_missing}")
print("-" * 50)

# ---------------------------------------------------------
# 5. Inspect Rows with Missing Values
# ---------------------------------------------------------
print("\n--- 4. Rows with Missing Values ---")
# We use .any(axis=1) to find any row where at least one cell is missing data.
rows_with_missing = ngo_df[ngo_df.isnull().any(axis=1)]
print("Records requiring data entry or imputation:")
print(rows_with_missing)
print("-" * 50)

# ---------------------------------------------------------
# 6. Conclusion
# ---------------------------------------------------------
print("\nNote: Missing values (represented as NaN) can disrupt analysis and models.")
print("Identifying them is the critical first step of the data cleaning process.")
print("\nConclusion: Missing value detection demo completed successfully.")
