import pandas as pd

# ---------------------------------------------------------
# 1. Create DataFrame from Dictionary
# ---------------------------------------------------------
# A dictionary where keys represent column names (features)
# and values represent the data for each column.
ngo_data_dict = {
    "ngo_name": ["NGO_A", "NGO_B", "NGO_C"],
    "program_type": ["Education", "Healthcare", "Food"],
    "cost": [5000, 8000, 3000],
    "people_helped": [200, 150, 300]
}

# Converting the dictionary into a Pandas DataFrame
# Rows represent individual NGO records.
# Columns represent attributes or features.
ngo_df_dict = pd.DataFrame(ngo_data_dict)

print("--- 1. DataFrame from Dictionary ---")
print(ngo_df_dict)
print("-" * 50)

# ---------------------------------------------------------
# 2. Load DataFrame from CSV
# ---------------------------------------------------------
# Loading external data from a CSV file into a DataFrame
csv_file_path = "data/raw/ngo_sample_data.csv"
ngo_df_csv = pd.read_csv(csv_file_path)

print("\n--- 2. DataFrame from CSV File ---")
print(ngo_df_csv)
print("-" * 50)

# ---------------------------------------------------------
# 3. Inspect DataFrame Structure
# ---------------------------------------------------------
print("\n--- 3. Structural Inspection ---")

# Accessing column names
print(f"Column Names: {ngo_df_csv.columns.tolist()}")

# Previewing the first few rows (defaults to 5)
print("\nFirst 2 rows using .head(2):")
print(ngo_df_csv.head(2))

# Checking the size of the DataFrame (Rows, Columns)
print(f"\nDataFrame Shape (Rows, Columns): {ngo_df_csv.shape}")

print("\nNote: Each row is an NGO program instance, and each column is a metadata field.")
print("-" * 50)

print("\nConclusion: Pandas DataFrame creation and inspection demo completed successfully.")
