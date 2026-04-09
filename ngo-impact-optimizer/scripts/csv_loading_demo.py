import pandas as pd

# ---------------------------------------------------------
# 1. Load CSV Data
# ---------------------------------------------------------
# Loading the primary NGO program dataset into a DataFrame
file_path = "data/raw/ngo_programs.csv"
ngo_df = pd.read_csv(file_path)

print("--- 1. Data Preview (.head()) ---")
# Rows represent individual NGO program entries
# Columns represent attributes like cost, people helped, and outcome scores
print(ngo_df.head())
print("-" * 50)

# ---------------------------------------------------------
# 2. Verify Loading and Structure
# ---------------------------------------------------------
print("\n--- 2. Structural Verification ---")

# Accessing column names
print(f"Column Names: {ngo_df.columns.tolist()}")

# Checking dimensions (rows, columns)
print(f"DataFrame Shape: {ngo_df.shape}")

# Verifying basic data structure and types
print("\nDataFrame Info:")
ngo_df.info()
print("-" * 50)

# ---------------------------------------------------------
# 3. Structural Integrity Check
# ---------------------------------------------------------
print("\n--- 3. Structural Integrity Check ---")

# Verification: Are column names correct?
expected_columns = ["ngo_name", "program_type", "location", "cost", "people_helped", "outcome_score"]
actual_columns = ngo_df.columns.tolist()

if actual_columns == expected_columns:
    print("[SUCCESS] Column names match the expected structure.")
else:
    print("[WARNING] Column names differ from expectations.")

# Verification: Are there 6 columns as expected?
if ngo_df.shape[1] == 6:
    print("[SUCCESS] Column count is correct (6 features).")
else:
    print(f"[ERROR] Expected 6 columns, but found {ngo_df.shape[1]}.")

print("-" * 50)

print("\nConclusion: CSV loading and verification demo completed successfully.")
