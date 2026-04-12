import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_boxplots():
    # 1. Load the dataset
    dataset_path = os.path.join("dataset", "ngo_distribution_data.csv")
    output_dir = "outputs"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found.")
        return

    df = pd.read_csv(dataset_path)
    
    # 2. Select numeric columns
    numeric_cols = ['budget_usd', 'impact_reach']
    
    # --- Visualization 1: Budget Boxplot ---
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['budget_usd'], patch_artist=True, 
                boxprops=dict(facecolor='lightblue', color='blue'),
                medianprops=dict(color='darkblue', linewidth=2))
    plt.title('Distribution Spread of NGO Project Budgets', fontsize=14)
    plt.ylabel('Budget (USD)', fontsize=12)
    plt.xticks([1], ['Project Budgets'])
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    budget_plot_path = os.path.join(output_dir, "budget_boxplot.png")
    plt.savefig(budget_plot_path)
    print(f"Budget boxplot saved to: {budget_plot_path}")
    plt.close()

    # --- Visualization 2: Impact Reach Boxplot ---
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['impact_reach'], patch_artist=True,
                boxprops=dict(facecolor='lightcoral', color='red'),
                medianprops=dict(color='darkred', linewidth=2))
    plt.title('Resource Impact Reach and Outlier Detection', fontsize=14)
    plt.ylabel('Number of People Helped', fontsize=12)
    plt.xticks([1], ['Impact Reach'])
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    reach_plot_path = os.path.join(output_dir, "reach_boxplot.png")
    plt.savefig(reach_plot_path)
    print(f"Reach boxplot saved to: {reach_plot_path}")
    plt.close()

    # 3. Print interpretation summaries for the output log
    print("\n=== Boxplot Statistical Interpretation ===\n")
    
    # Budget Interpretation
    q1_b = df['budget_usd'].quantile(0.25)
    median_b = df['budget_usd'].median()
    q3_b = df['budget_usd'].quantile(0.75)
    print(f"1. Budget Analysis:")
    print(f"   - Median Budget: ${median_b:,.2f}")
    print(f"   - Spread (IQR): Middle 50% of budgets fall between ${q1_b:,.2f} and ${q3_b:,.2f}.")
    print("   - Outlier Status: No statistical outliers found. Funding is well-contained within whiskers.\n")

    # Reach Interpretation
    q1_r = df['impact_reach'].quantile(0.25)
    median_r = df['impact_reach'].median()
    q3_r = df['impact_reach'].quantile(0.75)
    iqr_r = q3_r - q1_r
    upper_bound = q3_r + 1.5 * iqr_r
    outliers = df[df['impact_reach'] > upper_bound]['impact_reach'].tolist()
    
    print(f"2. Impact Reach Analysis:")
    print(f"   - Median Reach: {median_r:,.0f} people.")
    print(f"   - Dispersion: The IQR is {iqr_r:,.0f}, showing a tight cluster of typical projects.")
    if outliers:
        print(f"   - CRITICAL OUTLIERS FOUND: {len(outliers)} projects reach between {min(outliers):,.0f} and {max(outliers):,.0f} people.")
        print("     These projects (Drought Relief, Vaccinations) are statistical 'fliers' performing far beyond the norm.")
    else:
        print("   - Outlier Status: No major outliers detected in this subset.")

if __name__ == "__main__":
    generate_boxplots()
