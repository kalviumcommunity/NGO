# Pandas Series Verification

## Script Details

- **File Name**: `pandas_series_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates the fundamental building block of Pandas: the **Series**. It shows how to create Series from standard Python lists and NumPy arrays, and how to inspect their core structural components.

## Series Creation

- **From Python List**: Demonstrates converting a simple list of "people helped" into a Series object.
- **From NumPy Array**: Demonstrates that Pandas works seamlessly with NumPy arrays, preserving data types and enhancing them with indexing.

## Series Structure

A Pandas Series is composed of two primary parts:
1. **Values**: The actual data stored in the Series (similar to a NumPy array).
2. **Index**: The sequence of labels used to identify each value.

## Indexing Behavior

The script highlights **Automatic Index Generation**:
- If no index is provided during creation, Pandas automatically assigns a `RangeIndex` starting from **0**.
- This makes a Series behave like an ordered list but with more powerful data alignment capabilities.

## Inspection

The script uses built-in properties to verify the structure:
- **`.values`**: Returns the raw data as a NumPy-like array.
- **`.index`**: Returns the index object (e.g., `RangeIndex(start=0, stop=3, step=1)`).

## Execution

To verify the creation and structure of the Series, run the script:
```bash
python scripts/pandas_series_demo.py
```

## Conclusion

The script successfully demonstrates that a Pandas Series is more than just an array—it is a labeled data structure. Understanding how values and indices work together is the first step toward mastering complex data manipulation in Pandas.
