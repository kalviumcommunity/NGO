import pandas as pd
import os

"""
PROBLEM STATEMENT:
NGOs run large-scale welfare programs but lack evidence on which interventions 
create the most impact. How could data evaluation help them optimise resource allocation?

LOGICAL INTERPRETATION OF STRUCTURE:
To optimize resource allocation, we must first understand the variables we track.
This dataset links programs (categorical) to their financial inputs (cost) and 
social outputs (people_helped, outcome_score). By inspecting the shape and types, 
we ensure the data is structured for efficiency analysis—specifically calculating 
the 'Impact-to-Cost' ratio for different intervention types.
"""

def inspect_dataset(file_path):
    """
    Loads the NGO dataset and performs a structural inspection.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # Load the DataFrame
    df = pd.read_csv(file_path)

    print("-" * 50)
    print("--- NGO IMPACT DATASET: STRUCTURAL INSPECTION ---")
    print("-" * 50)

    # 1. Inspection of DataFrame shape
    print(f"\n[1] DATASET SHAPE:")
    shape = df.shape
    print(f"Total Rows: {shape[0]}")
    print(f"Total Columns: {shape[1]}")
    print(f"Shape (Rows, Columns): {shape}")

    # 2. Inspection of column data types
    print(f"\n[2] COLUMN DATA TYPES:")
    print(df.dtypes)

    # 3. Logical interpretation of the structure
    print("-" * 50)
    print("--- LOGICAL INTERPRETATION ---")
    print("-" * 50)
    
    # Mapping columns to their logical role in impact optimization
    interpretations = {
        'ngo_name': 'Identifier for the organization.',
        'program_type': 'Categorical variable for grouping interventions (e.g., Education vs. Health).',
        'location': 'Geographical context for resource distribution analysis.',
        'cost': 'Quantitative measure of financial input (Resource Allocation).',
        'people_helped': 'Quantitative measure of direct social output.',
        'outcome_score': 'Qualitative-to-quantitative metric of intervention effectiveness.'
    }

    for col, desc in interpretations.items():
        if col in df.columns:
            dtype = df[col].dtype
            print(f"- {col} ({dtype}): {desc}")

    print("\nCONCLUSION:")
    print("The dataset structure allows for 'Cost-Effectiveness Analysis'.")
    print("Specifically, we can calculate (Outcome Score / Cost) to rank intervention impact.")
    print("-" * 50)

if __name__ == "__main__":
    # Define path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "dataset", "ngo_data.csv")
    
    inspect_dataset(data_path)
