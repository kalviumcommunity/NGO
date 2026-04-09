import pandas as pd

# Load the NGO programs dataset
file_path = "data/raw/ngo_programs.csv"
ngo_df = pd.read_csv(file_path)

# ---------------------------------------------------------
# 1. Column Selection
# ---------------------------------------------------------
print("--- 1. Column Selection ---")

# Selecting a single column returns a Series
cost_column = ngo_df["cost"]
print(f"Single Column (cost):\n{cost_column}")

# Selecting multiple columns returns a DataFrame
# Note the double brackets: [[ "col1", "col2" ]]
basic_info = ngo_df[["ngo_name", "program_type"]]
print(f"\nMultiple Columns (name, type):\n{basic_info}")
print("-" * 50)

# ---------------------------------------------------------
# 2. Row Selection using Slicing
# ---------------------------------------------------------
print("\n--- 2. Row Selection using Slicing ---")

# Selecting first two rows (index 0 and 1)
first_two_rows = ngo_df[0:2]
print(f"Slicing (0:2):\n{first_two_rows}")
print("-" * 50)

# ---------------------------------------------------------
# 3. loc and iloc Selection
# ---------------------------------------------------------
print("\n--- 3. loc vs iloc Selection ---")

# .loc is LABEL-BASED selection.
# Syntax: ngo_df.loc[row_labels, column_labels]
# Here we select rows 0 through 2 (inclusive in loc) and specific column names.
loc_selection = ngo_df.loc[0:2, ["ngo_name", "cost"]]
print(f".loc Selection (Rows 0-2, name and cost):\n{loc_selection}")

# .iloc is INTEGER POSITION-BASED selection.
# Syntax: ngo_df.iloc[row_positions, column_positions]
# Here we select rows at positions 0 and 1 (2 is exclusive in iloc) 
# and columns at positions 0, 1, and 2.
iloc_selection = ngo_df.iloc[0:2, 0:3]
print(f"\n.iloc Selection (Positions [0:2], [0:3]):\n{iloc_selection}")

print("\nNote: .loc handles label names, while .iloc handles numerical positions.")
print("-" * 50)

print("\nConclusion: DataFrame selection demo completed successfully.")
