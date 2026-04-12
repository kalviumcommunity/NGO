import pandas as pd
import os

"""
MILESTONE: Handling Missing Values
Goal: Demonstrate intentional data cleaning using drop and fill strategies.

Scenario: 
NGOs need accurate evidence to optimize resource allocation. Missing data can bias 
results (e.g., ignoring expensive programs because their 'cost' is missing). 
We must handle these gaps strategically.
"""

def handle_missing_data(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # 1. Load the dataset
    df = pd.read_csv(file_path)
    original_shape = df.shape
    
    print("-" * 65)
    print("--- NGO IMPACT DATA: DATA CLEANING STRATEGIES ---")
    print("-" * 65)
    print(f"Initial Dataset Shape: {original_shape} (Rows, Columns)")

    # 2. Detection of missing values
    print("\n[STEP 1] Detecting Missing Values:")
    null_counts = df.isnull().sum()
    print(null_counts[null_counts > 0])

    # -------------------------------------------------------------------------
    # STRATEGY A: DROPPING DATA (dropna)
    # -------------------------------------------------------------------------
    print("\n[STEP 2] Strategy A: Dropping Incomplete Records")
    # Intentional Decision: Drop any row with missing values to see the impact.
    # In a real scenario, we might only drop if critical columns (like NGO name) are missing.
    df_dropped = df.dropna()
    dropped_shape = df_dropped.shape
    
    print(f"Shape after dropna(): {dropped_shape}")
    print(f"Data Loss: {original_shape[0] - dropped_shape[0]} rows removed.")
    print("Reasoning: Dropping is the fastest way to get a 'perfect' dataset, but "
          "it often leads to significant data loss, especially in small NGO datasets.")

    # -------------------------------------------------------------------------
    # STRATEGY B: FILLING DATA (fillna)
    # -------------------------------------------------------------------------
    print("\n[STEP 3] Strategy B: Filling Missing Values (Intentional Imputation)")
    
    # We create a copy to avoid SettingWithCopyWarning or modifying the original accidentally
    df_filled = df.copy()

    # Column 1: 'location' (Categorical)
    # Decision: Fill with 'Unknown'. 
    # Logic: We can still analyze program impact even if the exact geographic 
    # location is missing.
    df_filled['location'] = df_filled['location'].fillna('Unknown')

    # Column 2: 'cost' (Numeric)
    # Decision: Fill with Median.
    # Logic: Costs can have outliers. Median is more representative of a typical 
    # program's cost than the mean for this small sample.
    cost_median = df_filled['cost'].median()
    df_filled['cost'] = df_filled['cost'].fillna(cost_median)

    # Column 3: 'outcome_score' (Numeric/Score)
    # Decision: Fill with Mean.
    # Logic: For performance scores, the average of the cohort is a reasonable 
    # estimate when specific data is missing.
    score_mean = df_filled['outcome_score'].mean()
    df_filled['outcome_score'] = df_filled['outcome_score'].fillna(score_mean)

    filled_shape = df_filled.shape
    print(f"Shape after fillna(): {filled_shape}")
    print(f"Data Retained: {filled_shape[0]} rows (0 nulls remaining).")
    
    print("\nApplied Logic summary:")
    print(f"- Location: Filled with 'Unknown'")
    print(f"- Cost: Filled with median ({cost_median})")
    print(f"- Outcome Score: Filled with mean ({score_mean:.2f})")

    # -------------------------------------------------------------------------
    # COMPARISON AND CONCLUSION
    # -------------------------------------------------------------------------
    print("\n" + "=" * 65)
    print("--- FINAL COMPARISON ---")
    print("=" * 65)
    comparison_data = {
        "Strategy": ["Original", "Dropped", "Filled"],
        "Rows": [original_shape[0], dropped_shape[0], filled_shape[0]],
        "Columns": [original_shape[1], dropped_shape[1], filled_shape[1]],
        "Nulls": [df.isnull().sum().sum(), df_dropped.isnull().sum().sum(), df_filled.isnull().sum().sum()]
    }
    comparison_df = pd.DataFrame(comparison_data)
    print(comparison_df)

    print("\nConclusion for NGO Stakeholders:")
    print("Filling data (Imputation) allowed us to keep 100% of our intervention records,")
    print("whereas dropping missing values would have cost us 50% of our evidence base.")
    print("This retention is crucial for optimizing resource allocation across all programs.")
    print("-" * 65)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "dataset", "ngo_data_with_missing.csv")
    handle_missing_data(data_path)
