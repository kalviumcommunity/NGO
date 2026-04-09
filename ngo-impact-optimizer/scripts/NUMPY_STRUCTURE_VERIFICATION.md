# NumPy Structure Verification

## Script Details

- **File Name**: `numpy_structure_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates a deep understanding of NumPy array architecture, focusing on how data is laid out in memory across different dimensions and how to precisely retrieve information using indexing.

## Array Creation

- **1D Array**: A sequence of integers representing the impact reach of different programs.
- **2D Array (Matrix)**: A table of data where each row represents a distinct NGO record and each column represents a specific metric (Cost vs. Reach).

## Array Structure

The script uses built-in NumPy attributes to inspect the array layout:

- **Shape (`.shape`)**: Explains the size of each dimension. 
    - For the 1D array, this identifies the number of elements.
    - For the 2D array, this identifies the number of **Rows** and **Columns** (e.g., `(4, 2)`).
- **Dimensions (`.ndim`)**: Identifies the rank of the array. The script contrasts a 1D vector (1 dimension) with a 2D matrix (2 dimensions).

## Indexing

A critical part of data science is retrieving specific values. The script demonstrates:

- **1D Indexing**: Accessing a value using a single integer index (e.g., `array[2]`).
- **2D Indexing**: Accessing values using a coordinate system of the form `array[row_index, col_index]`. This allows targeting specific variables for a specific record.

## Execution

Run the script to see the structural breakdown and data retrieval in action:
```bash
python scripts/numpy_structure_demo.py
```

## Conclusion

The script successfully demonstrates that NumPy arrays provide a structured and efficient way to handle multidimensional data, offering powerful tools for both inspecting data layout and accessing individual data points.
