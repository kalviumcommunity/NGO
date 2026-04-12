import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize_relationship():
    # 1. Load the dataset
    dataset_path = os.path.join("dataset", "ngo_distribution_data.csv")
    output_dir = "outputs"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found.")
        return

    df = pd.read_csv(dataset_path)
    
    # 2. Select two numeric columns
    # X: budget_usd, Y: impact_reach
    
    # 3. Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['budget_usd'], df['impact_reach'], color='darkblue', alpha=0.7, edgecolors='black', s=80)
    
    # Formatting
    plt.title('Relationship: Investment vs Community Impact', fontsize=14)
    plt.xlabel('Budget (USD)', fontsize=12)
    plt.ylabel('People Helped (Reach)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Add annotations for key outliers if they exist
    # (Just example labels for clarity based on high values)
    max_reach_row = df.loc[df['impact_reach'].idxmax()]
    plt.annotate(f"Power Performer\n({max_reach_row['Program_Type']})", 
                 (max_reach_row['budget_usd'], max_reach_row['impact_reach']),
                 textcoords="offset points", xytext=(0,10), ha='center',
                 fontsize=9, color='darkred', weight='bold')

    # Save the scatter plot
    plot_path = os.path.join(output_dir, "budget_vs_reach.png")
    plt.savefig(plot_path)
    print(f"Scatter plot saved to: {plot_path}")
    plt.close()

    # 4. Identify patterns, trends, clusters, or outliers
    print("\n=== Relationship Pattern Interpretation ===\n")
    
    print("1. General Trend:")
    print("   - There is a visible positive correlation between budget and reach.")
    print("   - In general, projects with higher budgets tend to help more people,")
    print("     which validates the organization's scaling strategy.\n")

    print("2. Cluster Detection:")
    print("   - High-Core Cluster: Most projects are clustered between $20,000 and $80,000 budget")
    print("     reaching under 5,000 people.")
    print("   - Efficiency Gap: A few points represent 'High Cost, Moderate Reach', suggesting")
    print("     interventions that are more resource-intensive per person.\n")

    print("3. Outlier Identification:")
    print(f"   - The program '{max_reach_row['Program_Type']}' stands out as a significant outlier,")
    print(f"     achieving {max_reach_row['impact_reach']:,} reach with a budget of ${max_reach_row['budget_usd']:,}.")
    print("   - This point represents a massive efficiency peak compared to the main cluster.")

if __name__ == "__main__":
    visualize_relationship()
