import pandas as pd
import os

def handle_duplicates():
    # 1. Load the dataset
    dataset_path = os.path.join("dataset", "ngo_impact_duplicates.csv")
    
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found.")
        return

    df = pd.read_csv(dataset_path)
    print("--- Initial Dataset Statistics ---")
    print(f"Total records: {len(df)}")
    print(df.head(10))
    print("\n")

    # 2. Detect duplicate rows
    # df.duplicated() returns a boolean Series indicating whether a row is a duplicate.
    duplicates = df[df.duplicated(keep=False)] # keep=False shows all occurrences of duplicates
    
    print("--- Detected Duplicate Rows ---")
    if not duplicates.empty:
        print(f"Found {len(df[df.duplicated()])} duplicate entries (total rows involved: {len(duplicates)})")
        print(duplicates.sort_values(by="ngo_name"))
    else:
        print("No duplicate rows detected.")
    print("\n")

    # 3. Inspect duplicate entries intentionally
    # We can also check duplicates based on specific subsets if needed
    # e.g., df.duplicated(subset=['ngo_name', 'location'])

    # 4. Remove duplicates
    # keep='first' is the default; it keeps the first occurrence and removes subsequent ones.
    print("--- Removing Duplicates ---")
    df_cleaned = df.drop_duplicates(keep='first')
    
    # 5. Verify that duplicates have been handled correctly
    print("--- Verification ---")
    print(f"Dataset shape before: {df.shape}")
    print(f"Dataset shape after:  {df_cleaned.shape}")
    
    remaining_duplicates = df_cleaned.duplicated().sum()
    print(f"Remaining duplicates: {remaining_duplicates}")
    
    if remaining_duplicates == 0:
        print("SUCCESS: All duplicate records have been removed.")
    else:
        print("WARNING: Some duplicates might still remain.")

    # Save the cleaned dataset
    output_path = os.path.join("dataset", "ngo_impact_cleaned.csv")
    df_cleaned.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved to: {output_path}")

if __name__ == "__main__":
    handle_duplicates()
