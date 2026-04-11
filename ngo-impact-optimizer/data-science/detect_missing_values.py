import pandas as pd
import os

"""
MILESTONE: Missing Value Detection
Goal: Identify and summarize missing data in the NGO dataset.

Detection logic:
1. Detect any null values in the DataFrame.
2. Summarize null counts by column.
3. Isolate and inspect specific rows with missing information.
"""

def analyze_missing_data(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # Load the dataset
    df = pd.read_csv(file_path)
    
    print("-" * 60)
    print("--- NGO DATASET: MISSING VALUE ANALYSIS ---")
    print("-" * 60)

    # 1. Detection of missing values
    # .isnull() creates a boolean mask. 
    # .values.any() tells us if AT LEAST one null exists in the entire DF.
    has_nulls = df.isnull().values.any()
    print(f"\n[1] DATASET INTEGRITY CHECK:")
    print(f"Does the dataset contain missing values? {'YES' if has_nulls else 'NO'}")

    # 2. Identification of columns with missing data
    # .isnull().sum() provides a count per column.
    print(f"\n[2] MISSING VALUES PER COLUMN:")
    null_counts = df.isnull().sum()
    print(null_counts[null_counts > 0] if has_nulls else "All columns are complete.")
    
    # Detailed count for all columns
    print("\nDetailed Summary:")
    print(null_counts)

    # 3. Inspection of rows containing missing values
    # We filter the DataFrame using .isnull().any(axis=1) to find rows 
    # where ANY column contains a null value.
    print(f"\n[3] INSPECTION OF INCOMPLETE RECORDS:")
    if has_nulls:
        incomplete_rows = df[df.isnull().any(axis=1)]
        print(f"Found {len(incomplete_rows)} rows with missing data:")
        print(incomplete_rows)
        
        print("\nInterpretation of Impact:")
        for idx, row in incomplete_rows.iterrows():
            missing_cols = row[row.isnull()].index.tolist()
            print(f"- Row {idx} ({row['ngo_name']}): Missing {missing_cols}. "
                  f"This prevents calculation of '{'Efficiency' if 'cost' in missing_cols or 'outcome_score' in missing_cols else 'Location-based analytics'}'.")
    else:
        print("No incomplete records found.")

    print("\n" + "-" * 60)
    print("Missing Value Detection Complete.")
    print("-" * 60)

if __name__ == "__main__":
    # Define path relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "dataset", "ngo_data_with_missing.csv")
    
    analyze_missing_data(data_path)
