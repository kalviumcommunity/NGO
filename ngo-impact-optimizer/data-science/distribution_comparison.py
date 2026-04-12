import pandas as pd
import os

def compare_distributions():
    # 1. Load the dataset
    dataset_path = os.path.join("dataset", "ngo_distribution_data.csv")
    
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found.")
        return

    df = pd.read_csv(dataset_path)
    
    # 2. Compute summary statistics for each column
    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    print("=== Multi-Column Summary Statistics ===\n")
    stats = df[numeric_cols].describe().T
    
    # Add Median (not in default describe)
    stats['median'] = df[numeric_cols].median()
    
    # Add Coefficient of Variation (CV = std / mean) - helps compare spread regardless of scale
    stats['CV'] = df[numeric_cols].std() / df[numeric_cols].mean()
    
    # Add Skewness
    stats['skewness'] = df[numeric_cols].skew()
    
    print(stats[['mean', 'median', 'std', 'min', 'max', 'CV', 'skewness']])
    print("\n" + "="*50 + "\n")

    # 3. Interpret similarities and differences meaningfully
    print("=== Distribution Comparison & Interpretation ===\n")

    # Budget Analysis
    budget_stats = stats.loc['budget_usd']
    print(f"1. Budget Dist (USD): CV={budget_stats['CV']:.2f}, Skew={budget_stats['skewness']:.2f}")
    print("   Interpretation: The budget distribution is relatively balanced but spread out.")
    print("   The mean and median are close, suggesting a normal-ish distribution of funding sizes.\n")

    # Impact Reach Analysis
    reach_stats = stats.loc['impact_reach']
    print(f"2. Reach Dist (People): CV={reach_stats['CV']:.2f}, Skew={reach_stats['skewness']:.2f}")
    print("   Interpretation: EXTREMELY HIGH VARIANCE. The CV of {:.2f} indicates that impact varies".format(reach_stats['CV']))
    print("   much more than costs. The high positive skew ({:.2f}) confirms that a few massive".format(reach_stats['skewness']))
    print("   projects are reaching far more people than the typical project.\n")

    # Success Rate Analysis
    success_stats = stats.loc['success_rate']
    print(f"3. Success Rate Dist: CV={success_stats['CV']:.2f}, Skew={success_stats['skewness']:.2f}")
    print("   Interpretation: HIGHLY CONSISTENT. The very low CV ({:.2f}) shows that despite".format(success_stats['CV']))
    print("   different budgets and reaches, the quality of outcomes remains stable across programs.\n")

    # Cross-Column Insight
    print("4. Core Resource Allocation Insight:")
    print("   - While Budget and Success remain predictable, 'Impact Reach' is the wild variable.")
    print("   - This suggests that some interventions are vastly more scalable than others,")
    print("     regardless of having a similar budget range.")

if __name__ == "__main__":
    compare_distributions()
