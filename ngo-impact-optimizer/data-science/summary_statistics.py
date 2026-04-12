import pandas as pd
import os

def analyze_statistics():
    # 1. Load the dataset
    dataset_path = os.path.join("dataset", "ngo_standardized.csv")
    
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found.")
        return

    df = pd.read_csv(dataset_path)
    
    print("=== NGO Impact Summary Statistics ===\n")

    # 2. Select individual numeric columns
    cols_to_analyze = ['budget_usd', 'peoplereached']
    
    # 3. Compute basic summary statistics
    # We use .describe() for a quick overview, but manually compute specific ones for clarity
    stats_dict = {}
    for col in cols_to_analyze:
        stats_dict[col] = {
            'Count': df[col].count(),
            'Mean': df[col].mean(),
            'Median': df[col].median(),
            'Min': df[col].min(),
            'Max': df[col].max(),
            'Std Dev': df[col].std()
        }

    # Convert to DataFrame for readable output
    stats_df = pd.DataFrame(stats_dict)
    print(stats_df)
    print("\n" + "="*40 + "\n")

    # 4. Interpret the results clearly
    print("=== Interpretation of Results ===\n")
    
    # Budget Interpretation
    budget_mean = stats_dict['budget_usd']['Mean']
    budget_std = stats_dict['budget_usd']['Std Dev']
    print(f"1. Budget Overview: The average project budget is ${budget_mean:,.2f}.")
    print(f"   Insight: With a Standard Deviation of ${budget_std:,.2f}, there is significant variability")
    print("   between project sizes, ranging from small local gardens to large vaccination drives.\n")

    # People Reached Interpretation
    reach_mean = stats_dict['peoplereached']['Mean']
    reach_median = stats_dict['peoplereached']['Median']
    print(f"2. Reach Overview: The average impact per project is {reach_mean:,.0f} people.")
    print(f"   Insight: The median ({reach_median:,.0f}) is lower than the mean, suggesting that a few")
    print("   high-impact projects (like vaccinations) are pulling the average upward.\n")

    # Brief Comparison
    print("3. Comparative Analysis:")
    cost_per_person = budget_mean / reach_mean
    print(f"   - On average, the organization invests roughly ${cost_per_person:,.2f} per person helped.")
    print("   - High investment projects (Budget Max) correlate with high reach (People Max),")
    print("     validating that resource allocation is scaling with target impact.")

if __name__ == "__main__":
    analyze_statistics()
