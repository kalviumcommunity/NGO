import numpy as np

# ---------------------------------------------------------
# 1. Create Arrays from Python Lists
# ---------------------------------------------------------
# Representing cost and reach data for 3 NGO programs
cost_list = [5000, 8000, 3000]
people_helped_list = [200, 150, 300]

# Converting to NumPy arrays enables vectorized (element-wise) math operations
cost_array = np.array(cost_list)
people_helped_array = np.array(people_helped_list)

print("Input Arrays:")
print(f"  Cost Array:          {cost_array}")
print(f"  People Helped Array: {people_helped_array}")
print("-" * 50)

# ---------------------------------------------------------
# 2. Element-wise Operations
# ---------------------------------------------------------
# NumPy applies each operation independently to matching index pairs.
# e.g., result[0] = cost_array[0] + people_helped_array[0], and so on.
# Both arrays MUST have the same shape for element-wise ops to work.
# Mismatched shapes will raise a "broadcast" or ValueError.

addition_result = cost_array + people_helped_array
subtraction_result = cost_array - people_helped_array
multiplication_result = cost_array * people_helped_array
division_result = people_helped_array / cost_array  # people helped per dollar

print("Element-wise Operations:")
print(f"  Addition       (cost + people): {addition_result}")
print(f"  Subtraction    (cost - people): {subtraction_result}")
print(f"  Multiplication (cost * people): {multiplication_result}")
print(f"  Division   (people / cost):     {division_result}")
print("-" * 50)

# ---------------------------------------------------------
# 3. Scalar Operations
# ---------------------------------------------------------
# A scalar is applied uniformly to every element in the array
# without needing a second array of matching size.

double_cost = cost_array * 2
boosted_reach = people_helped_array + 10

print("Scalar Operations:")
print(f"  Double cost (cost_array * 2):          {double_cost}")
print(f"  Boosted reach (people_helped + 10):    {boosted_reach}")
print("-" * 50)

print("Conclusion: NumPy array math operations completed successfully.")
