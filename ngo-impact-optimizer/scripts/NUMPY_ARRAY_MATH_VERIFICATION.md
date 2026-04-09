# NumPy Array Math Verification

## Script Details

- **File Name**: `numpy_array_math_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates the use of NumPy for performing numerical computations on arrays, covering both element-wise binary operations and scalar transformations, using NGO program data as the context.

## Array Creation

Two NumPy arrays are created from Python lists:
- `cost_array` — representing the total budget for each NGO program.
- `people_helped_array` — representing the number of individuals reached per program.

## Element-wise Operations

NumPy applies mathematical operators independently to each matching pair of elements:

| Operation | Description |
|---|---|
| Addition | Combines cost and reach per program |
| Subtraction | Finds difference between cost and reach |
| Multiplication | Scales cost by reach for each program |
| Division | Calculates reach per unit cost (efficiency) |

Operations occur **element by element** — `result[i] = array1[i] op array2[i]`.

## Scalar Operations

A scalar value is broadcast across every element in an array:
- **Multiplication by constant**: `cost_array * 2` doubles each cost value.
- **Addition of constant**: `people_helped_array + 10` increments each reach value.

No second array is needed — NumPy automatically applies the scalar to all positions.

## Shape Compatibility

For element-wise binary operations, both arrays **must have the same shape**. A shape mismatch (e.g., arrays of different lengths) raises a `ValueError` at runtime. Scalar operations bypass this requirement since the constant is broadcast uniformly.

## Execution

Run the script to see all operations in action:
```bash
python scripts/numpy_array_math_demo.py
```

## Conclusion

The script successfully demonstrates that NumPy's vectorized computation model allows efficient, readable, and concise numerical operations across entire arrays without requiring explicit loops.
