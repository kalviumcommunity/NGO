import pandas as pd
import os

"""
MILESTONE: Pandas Data Selection & Indexing
Goal: Demonstrate accurate and intentional data extraction methods.

Methods demonstrated:
1. Column Selection (Single & Multiple)
2. Row Selection (.iloc & .loc)
3. Slicing (Positional)
4. Combined Row & Column Selection
"""

def demonstrate_selection(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # Load DataFrame
    df = pd.read_csv(file_path)
    
    print("-" * 60)
    print("--- PANDAS DATA SELECTION DEMONSTRATION ---")
    print("-" * 60)

    # 1. Selecting a single column by name
    # Using bracket notation - best for single-word column access.
    print("\n[1] SINGLE COLUMN SELECTION: 'ngo_name'")
    names = df['ngo_name']
    print(names.head(3))

    # 2. Selecting multiple columns
    # Using a list of names - returns a DataFrame.
    print("\n[2] MULTIPLE COLUMN SELECTION: ['ngo_name', 'cost', 'outcome_score']")
    metrics = df[['ngo_name', 'cost', 'outcome_score']]
    print(metrics.head(3))

    # 3. Selecting rows using positional indexing (.iloc)
    # Extracts the first row (index 0).
    print("\n[3] POSITIONAL ROW SELECTION (.iloc[0]): First NGO Record")
    first_row = df.iloc[0]
    print(first_row)

    # 4. Slicing a range of rows
    # Standard Python slicing [start:stop] - stop is exclusive.
    print("\n[4] SLICING ROWS (Index 1 to 3):")
    row_slice = df[1:4]
    print(row_slice)

    # 5. Selecting specific rows and columns together (.loc)
    # .loc[rows, columns] uses labels. 
    # Here we select rows 2 to 4 and specific columns.
    # Note: With .loc, the end index IS inclusive.
    print("\n[5] COMBINED SELECTION (.loc[2:4, ['program_type', 'location']]):")
    combined_selection = df.loc[2:4, ['program_type', 'location']]
    print(combined_selection)

    # 6. Selecting specific rows and columns together (.iloc)
    # .iloc[rows, columns] uses integer positions.
    # Selecting row at index 0 and column at index 4 (people_helped).
    print("\n[6] SPECIFIC CELL SELECTION (.iloc[0, 4]):")
    people_helped_first = df.iloc[0, 4]
    print(f"People helped by first NGO ({df.iloc[0, 0]}): {people_helped_first}")

    print("\n" + "-" * 60)
    print("Selection Demonstration Complete.")
    print("-" * 60)

if __name__ == "__main__":
    # Define path relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "dataset", "ngo_data.csv")
    
    demonstrate_selection(data_path)
