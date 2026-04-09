import numpy as np

# ---------------------------------------------------------
# 1. Create Input Array
# ---------------------------------------------------------
# Representing the number of people helped by 3 NGO programs
people_helped_array = np.array([200, 150, 300])

print("Input Array (People Helped):")
print(f"  {people_helped_array}")
print("-" * 50)

# ---------------------------------------------------------
# 2. Loop-based Operation
# ---------------------------------------------------------
# Traditional approach: iterate over each element manually using a for loop.
# This works but becomes slow and verbose as data grows larger.
loop_result = []

for value in people_helped_array:
    loop_result.append(value * 2)

print("Loop-based Result (element * 2):")
print(f"  {np.array(loop_result)}")

# ---------------------------------------------------------
# 3. Vectorized Operation
# ---------------------------------------------------------
# NumPy applies the operation to every element simultaneously under the hood.
# No explicit loop is needed — NumPy uses optimized C-level routines internally.
# This means:
#   - Code is shorter and more readable
#   - Execution is significantly faster for large arrays
#   - No risk of off-by-one loop errors
vectorized_result = people_helped_array * 2

print("\nVectorized Result (array * 2):")
print(f"  {vectorized_result}")
print("-" * 50)

# ---------------------------------------------------------
# 4. Verification: Confirm Both Produce the Same Output
# ---------------------------------------------------------
# Convert the loop result to a NumPy array to compare with np.array_equal()
loop_result_array = np.array(loop_result)

if np.array_equal(loop_result_array, vectorized_result):
    print("Verification: PASSED — Both methods produce identical results.")
else:
    print("Verification: FAILED — Results differ.")

print("-" * 50)
print("Conclusion: Vectorization demo completed successfully.")
