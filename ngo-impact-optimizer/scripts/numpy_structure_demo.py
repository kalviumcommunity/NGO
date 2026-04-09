import numpy as np

# ---------------------------------------------------------
# 1. 1D Array Creation
# ---------------------------------------------------------
# A list representing the number of people helped by various NGO programs
people_helped_list = [100, 250, 180, 400]
ngo_people_array = np.array(people_helped_list)

print("1D NGO People Array:")
print(ngo_people_array)

# ---------------------------------------------------------
# 2. 2D Array Creation
# ---------------------------------------------------------
# A nested list representing NGO records: [[cost_usd, people_reached], ...]
ngo_data_records = [
    [1000, 150],
    [5000, 800],
    [2500, 300],
    [4200, 600]
]
ngo_data_matrix = np.array(ngo_data_records)

print("\n2D NGO Data Matrix (Cost vs. Reach):")
print(ngo_data_matrix)

# ---------------------------------------------------------
# 3. Inspecting Structure (Shape and Dimensions)
# ---------------------------------------------------------
# .shape returns a tuple representing the size of each dimension (rows, columns).
# .ndim returns the total number of dimensions (e.g., 1 for vector, 2 for matrix).

print("\n--- Structural Inspection ---")
print(f"1D Array Shape:     {ngo_people_array.shape} (Number of elements)")
print(f"1D Array Dimensions: {ngo_people_array.ndim}D")

print(f"\n2D Array Shape:     {ngo_data_matrix.shape} (Rows, Columns)")
print(f"2D Array Dimensions: {ngo_data_matrix.ndim}D")

# ---------------------------------------------------------
# 4. Indexing (Accessing Data)
# ---------------------------------------------------------
# Indexing in NumPy starts at 0.
# For 1D: array[index]
# For 2D: array[row_index, column_index]

print("\n--- Indexing Demonstration ---")

# Accessing the 3rd element in the 1D array (index 2)
third_element = ngo_people_array[2]
print(f"1D Indexing: 3rd program helped {third_element} people.")

# Accessing specific metrics from the 2D matrix
# Example: Cost of the 2nd program (Row index 1, Col index 0)
second_prog_cost = ngo_data_matrix[1, 0]

# Example: Reach of the 4th program (Row index 3, Col index 1)
fourth_prog_reach = ngo_data_matrix[3, 1]

print(f"2D Indexing: 2nd program cost ${second_prog_cost}.")
print(f"2D Indexing: 4th program reach: {fourth_prog_reach} people.")

print("\nConclusion: NumPy structure inspection and indexing demonstrated successfully.")
