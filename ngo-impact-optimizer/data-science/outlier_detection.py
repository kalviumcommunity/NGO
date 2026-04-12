import pandas as pd
import matplotlib.pyplot as plt
import os

def detect_outliers():
    # 1. Load the dataset
    dataset_path = os.path.join("dataset", "ngo_distribution_data.csv")
    output_dir = "outputs"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found.")
        return

    df = pd.read_csv(dataset_path)
    
    # --- Step 1: Visual Inspection ---
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['impact_reach'], patch_artist=True, 
                boxprops=dict(facecolor='lightyellow', color='orange'),
                flierprops=dict(marker='o', markerfacecolor='red', markersize=10))
    plt.title('Visual Inspection for Outliers (Impact Reach)', fontsize=14)
    plt.ylabel('Number of People Helped', fontsize=12)
    plt.xticks([1], ['Impact Reach'])
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Save diagnostic plot
    plot_path = os.path.join(output_dir, "outlier_detection_plot.png")
    plt.savefig(plot_path)
    print(f"Diagnostic boxplot saved to: {plot_path}")
    plt.close()

    # --- Step 2: Apply Simple Rule (IQR Method) ---
    Q1 = df['impact_reach'].quantile(0.25)
    Q3 = df['impact_reach'].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_whisker = Q1 - 1.5 * IQR
    upper_whisker = Q3 + 1.5 * IQR
    
    # Flag outliers
    outliers_df = df[(df['impact_reach'] < lower_whisker) | (df['impact_reach'] > upper_whisker)]
    
    print("\n" + "="*50)
    print("=== Outlier Detection Logic (IQR Method) ===")
    print(f"Q1 (25th Percentile): {Q1:,.0f}")
    print(f"Q3 (75th Percentile): {Q3:,.0f}")
    print(f"IQR: {IQR:,.0f}")
    print(f"Upper Bound/Whisker: {upper_whisker:,.0f}")
    print("="*50 + "\n")

    # --- Step 3: Clear Output Showing Flagged Values ---
    print("--- Flagged Outliers ---")
    if not outliers_df.empty:
        print(outliers_df[['NGO_Name', 'Program_Type', 'impact_reach']])
    else:
        print("No statistical outliers detected based on the 1.5*IQR rule.")

    # --- Step 4: Interpret and Explain Findings ---
    print("\n=== Interpretation & Reasoning ===\n")
    if not outliers_df.empty:
        for idx, row in outliers_df.iterrows():
            print(f"Outlier: {row['NGO_Name']} ({row['Program_Type']})")
            print(f"   Value: {row['impact_reach']:,} reach.")
            print("   Reason: This project significantly exceeds the upper statistical bound.")
            if row['impact_reach'] > 20000:
                print("   Interpretation: These represent 'Scalability Superstars'—interventions capable of")
                print("   nationwide impact (e.g., Drought Relief) compared to local programs.\n")
            else:
                print("   Interpretation: This intervention (e.g., Vaccination) achieves high efficiency")
                print("   by utilizing mass-delivery mechanics.\n")
    else:
        print("Insight: The project portfolio is highly uniform, with no programs deviating")
        print("from the standard operational scale.")

if __name__ == "__main__":
    detect_outliers()
