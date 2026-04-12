import pandas as pd
import os
import re

def standardize_data():
    # 1. Load the messy dataset
    dataset_path = os.path.join("dataset", "ngo_raw_messy.csv")
    
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found.")
        return

    df = pd.read_csv(dataset_path)
    
    print("=== BEFORE STANDARDIZATION ===")
    print("Column Names:", df.columns.tolist())
    print("\nDataFrame Info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    print("\n" + "="*30 + "\n")

    # 2. Clean and standardize column names
    # Requirement: lowercase, snake_case, no spaces, handle special characters
    def clean_column_name(name):
        # Remove special characters except spaces/alphanumerics
        name = re.sub(r'[^\w\s]', '', name)
        # Replace spaces or multiple underscores with a single underscore
        name = re.sub(r'[\s_]+', '_', name)
        # Convert to lowercase and strip
        return name.lower().strip('_')

    df.columns = [clean_column_name(col) for col in df.columns]

    # 3. Standardize Data Formats
    
    # Requirement: text normalization (e.g., Title Case for NGO names)
    if 'ngo_name' in df.columns:
        df['ngo_name'] = df['ngo_name'].str.strip().str.title()

    # Requirement: numeric cleanup (e.g., Budget removal of $ and ,)
    if 'budget' in df.columns:
        df['budget'] = df['budget'].replace(r'[\$,]', '', regex=True).astype(float)
        # Rename column for clarity
        df.rename(columns={'budget': 'budget_usd'}, inplace=True)

    # Bonus: Date formatting
    if 'start_date' in df.columns:
        df['start_date'] = pd.to_datetime(df['start_date'])

    print("=== AFTER STANDARDIZATION ===")
    print("Column Names:", df.columns.tolist())
    print("\nDataFrame Info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Compare value counts for normalized text
    print("\nNGO Name Value Counts (Normalized):")
    print(df['ngo_name'].value_counts())

    # Save the cleaned dataset
    output_path = os.path.join("dataset", "ngo_standardized.csv")
    df.to_csv(output_path, index=False)
    print(f"\nStandardized dataset saved to: {output_path}")

if __name__ == "__main__":
    standardize_data()
