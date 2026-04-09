# NumPy Array Verification

## Script Details

- **File Name**: `numpy_array_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates the fundamental usage of NumPy for scientific computing, specifically focusing on array creation and basic mathematical operations within an NGO data context.

## NumPy Usage

- **Importing**: Standard convention is used to import the library: `import numpy as np`.
- **Conversion**: Demonstrates the seamless conversion of standard Python sequential types (lists and nested lists) into high-performance NumPy arrays.

## Array Creation

- **1D Array**: Created from a simple list representing the number of people reached by various programs.
- **2D Array**: Created from a nested list (matrix) where rows represent different programs and columns represent metrics like `[cost, people_helped]`.

## Array Inspection

The script verifies array dimensions and data storage types using built-in properties:
- **`shape`**: Returns a tuple representing the dimensions of the array.
- **`dtype`**: Shows the numeric type of elements stored in the array (e.g., `int32`, `float64`).

## Array Operations

- **Element-wise Multiplication**: Demonstrates NumPy's ability to perform mathematical operations across an entire array simultaneously (vectorization). 
- **Example**: In the script, we calculated a `projected_reach` by multiplying the entire 1D array by a scalar factor (1.1) to simulate a 10% growth.

## Execution

To verify the script, run the following command in your terminal:
```bash
python scripts/numpy_array_demo.py
```

## Conclusion

The script successfully demonstrates the foundational steps for using NumPy in data analysis: creating structured arrays, inspecting their properties, and performing efficient mathematical operations.
