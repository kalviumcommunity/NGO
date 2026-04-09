# NumPy Broadcasting Verification

## Script Details

- **File Name**: `numpy_broadcasting_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates the power of NumPy's broadcasting mechanism, which allows operations between arrays of different shapes without the need for explicit loops or manual replication of data.

## Scalar Broadcasting

- **Description**: Adding a single scalar value (0-dimensional) to a 1D or 2D array.
- **Logic**: NumPy automatically "broadcasts" the scalar across every element of the target array, effectively treating it as an array of the same shape.
- **Example**: Incrementing all elements of a "people helped" array by a fixed correction factor.

## 1D to 2D Broadcasting

- **Description**: Adding a 1D array (vector) to a 2D array (matrix).
- **Logic**: If the trailing dimensions match (e.g., a (3, 2) matrix and a (2,) vector), NumPy replicates the vector across the rows of the matrix.
- **Benefits**: Allows applying row-wise or column-wise adjustments (like adding a specific cost and reach offset to every record) in a single, efficient operation.

## Shape Inspection

- The script clearly prints array shapes using the `.shape` property.
- It demonstrates how NumPy compares dimensions from right to left to determine if two arrays are "broadcast-compatible."

## Execution

To verify the broadcasting logic, run the script using the following command:
```bash
python scripts/numpy_broadcasting_demo.py
```

## Conclusion

The script successfully demonstrates both scalar-to-array and vector-to-matrix broadcasting. This confirms that NumPy can handle element-wise expansion for differing shapes correctly and intentionally, ensuring cleaner and faster data processing.
