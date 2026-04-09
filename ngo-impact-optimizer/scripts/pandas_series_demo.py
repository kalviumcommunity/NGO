import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. Create Series from Python List
# ---------------------------------------------------------
# A list representing people helped by 3 different NGO programs
people_helped_list = [200, 150, 300]

# Converting the list into a Pandas Series
people_helped_series = pd.Series(people_helped_list)

print("--- 1. Series from Python List (People Helped) ---")
print(people_helped_series)
print("-" * 50)

# ---------------------------------------------------------
# 2. Create Series from NumPy Array
# ---------------------------------------------------------
# A NumPy array representing cost values for programs
cost_values_array = np.array([5000, 8000, 3000])

# Converting the NumPy array into a Pandas Series
cost_series = pd.Series(cost_values_array)

print("\n--- 2. Series from NumPy Array (Cost Values) ---")
print(cost_series)
print("-" * 50)

# ---------------------------------------------------------
# 3. Inspect Series Structure
# ---------------------------------------------------------
# Every Pandas Series consists of 'values' (the data) and an 'index' (the labels).

print("\n--- 3. Structural Inspection ---")

# Inspecting People Helped Series
print("People Helped Series:")
print(f"  Values: {people_helped_series.values}")
print(f"  Index:  {people_helped_series.index}")

# Inspecting Cost Series
print("\nCost Series:")
print(f"  Values: {cost_series.values}")
print(f"  Index:  {cost_series.index}")

# Notice index behavior: 
# Since we didn't specify custom labels, Pandas automatically 
# assigned an integer index starting from 0 (RangeIndex).
print("\nNote: Pandas automatically assigned a 0-based integer index.")
print("-" * 50)

print("\nConclusion: Pandas Series creation and inspection demo completed successfully.")
