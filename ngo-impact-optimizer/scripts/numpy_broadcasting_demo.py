import numpy as np

# ---------------------------------------------------------
# 1. Scalar Broadcasting
# ---------------------------------------------------------
# Creating a 1D array representing people helped by 3 programs
people_helped_array = np.array([200, 150, 300])

print("--- 1. Scalar Broadcasting ---")
print(f"Original Array: {people_helped_array}")
print(f"Array Shape:    {people_helped_array.shape}")

# Scalar broadcasting: Adding a single value (10) to the entire array.
# NumPy "broadcasts" the scalar 10 into an array of the same shape [10, 10, 10]
# and performs element-wise addition.
scalar_addition_result = people_helped_array + 10

print(f"After adding 10: {scalar_addition_result}")
print("-" * 50)

# ---------------------------------------------------------
# 2. 1D to 2D Broadcasting
# ---------------------------------------------------------
# Creating a 2D array representing NGO metrics: [cost, people_helped]
ngo_data_matrix = np.array([
    [5000, 200],
    [8000, 150],
    [3000, 300]
])

# Creating a 1D adjustment array: [cost_adjustment, reach_adjustment]
adjustment_array = np.array([1000, 10])

print("\n--- 2. 1D to 2D Broadcasting ---")
print(f"2D Matrix (cost, reach):\n{ngo_data_matrix}")
print(f"Matrix Shape: {ngo_data_matrix.shape}")

print(f"\n1D Adjustment Array: {adjustment_array}")
print(f"Adjustment Shape: {adjustment_array.shape}")

# 1D to 2D broadcasting:
# The 1D array has shape (2,). The 2D matrix has shape (3, 2).
# Since the trailing dimensions match (the '2'), NumPy broadcasts the 1D array 
# across all rows of the 2D matrix.
# This is much cleaner than using a loop to add values to each row.
broadcast_sum_result = ngo_data_matrix + adjustment_array

print(f"\nResulting Matrix (after adding adjustment to each row):\n{broadcast_sum_result}")
print("-" * 50)

# ---------------------------------------------------------
# 3. Shape Inspection Summary
# ---------------------------------------------------------
# Broadcasting works based on two rules:
# 1. Dimensions are compared from right to left.
# 2. Dimensions are compatible if they are equal, or one of them is 1.

print("\nShape compatibility check:")
print(f"Matrix shape (3, 2) + Adjustment shape (2,) -> Compatible")
print("NumPy expands (2,) to (3, 2) internally by replicating the row.")

print("\nConclusion: NumPy broadcasting demo completed successfully.")
