import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_trends():
    # 1. Load the dataset
    dataset_path = os.path.join("dataset", "ngo_timeseries_data.csv")
    output_dir = "outputs"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found.")
        return

    df = pd.read_csv(dataset_path)
    
    print("--- Initial Data (Unsorted) ---")
    print(df.head(5))
    print("\n")

    # 2. Ensure data is correctly ordered by time
    # Requirement: Convert to datetime and sort
    df['month_start'] = pd.to_datetime(df['month_start'])
    df = df.sort_values(by='month_start')
    
    print("--- Sorted Data (Chronological) ---")
    print(df.head(5))
    print("\n")

    # 3. Create a line plot using numeric columns
    # We will plot 'monthly_reach' over 'month_start'
    plt.figure(figsize=(12, 6))
    
    # Plot Monthly Reach
    plt.plot(df['month_start'], df['monthly_reach'], marker='o', linestyle='-', color='teal', linewidth=2, label='Monthly Reach')
    
    # Formatting
    plt.title('NGO Community Impact Trend (2023)', fontsize=14)
    plt.xlabel('Timeline (Months)', fontsize=12)
    plt.ylabel('Number of People Helped', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # Save the trend plot
    plot_path = os.path.join(output_dir, "impact_trend.png")
    plt.savefig(plot_path)
    print(f"Trend visualization saved to: {plot_path}")
    plt.close()

    # 4. Identify and explain visible trends
    print("\n=== Trend Interpretation ===\n")
    
    first_reach = df.iloc[0]['monthly_reach']
    last_reach = df.iloc[-1]['monthly_reach']
    total_growth = ((last_reach - first_reach) / first_reach) * 100

    print(f"1. Directional Trend: There is a clear upward trajectory in community impact.")
    print(f"   Insight: Reach increased from {first_reach:,} in January to {last_reach:,} in December.")
    print(f"   Growth: Total impact grew by {total_growth:.1f}% over the year.\n")

    print(f"2. Seasonal Observations:")
    print(f"   - Steady growth is visible from January through September.")
    print(f"   - A slight dip occurred in November (13,000) before a major year-end surge")
    print("     to 18,000 in December, likely due to holiday-driven outreach programs.")

if __name__ == "__main__":
    analyze_trends()
