import numpy as np

# ---------------------------------------------------------
# 1. 1D Array Creation
# ---------------------------------------------------------
# Defining a Python list of people helped by different NGO programs
ngo_people_helped_list = [200, 150, 300, 180, 220, 250]

# Converting the list into a 1D NumPy array
ngo_people_helped_array = np.array(ngo_people_helped_list)

print("1D Array (People Helped):")
print(ngo_people_helped_array)

# ---------------------------------------------------------
# 2. 2D Array Creation
# ---------------------------------------------------------
# Defining a nested list representing NGO metrics: [cost, people_helped]
ngo_metric_data = [
    [5000, 200],
    [8000, 150],
    [3000, 300],
    [7000, 180]
]

# Converting the nested list into a 2D NumPy array
ngo_data_array = np.array(ngo_metric_data)

print("\n2D Array (Cost and People Helped):")
print(ngo_data_array)

# ---------------------------------------------------------
# 3. Inspect Array Properties
# ---------------------------------------------------------
print("\nArray Properties:")
print(f"1D Array - Shape: {ngo_people_helped_array.shape}, Data Type: {ngo_people_helped_array.dtype}")
print(f"2D Array - Shape: {ngo_data_array.shape}, Data Type: {ngo_data_array.dtype}")

# ---------------------------------------------------------
# 4. Simple Array Operation
# ---------------------------------------------------------
# Let's say we want to calculate the data for next year assuming a 10% increase in reach
# We multiply the 1D array by 1.1
projected_reach = ngo_people_helped_array * 1.1

print("\nSimple Operation (10% Reach Increase):")
print(projected_reach)

# Verification of calculation results
print("\nConclusion: NumPy arrays created and operations performed successfully.")
