# DataFrame Selection Verification

## Script Details

- **File Name**: `dataframe_selection_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates the variety of ways to extract specific subsets of data from a Pandas DataFrame. Mastering selection methods is essential for filtering records and isolating variables for analysis.

## Column Selection

- **Single Column**: Accessing data using `df["column_name"]`. This operation returns a Pandas Series.
- **Multiple Columns**: Accessing data using a list of names `df[["col1", "col2"]]`. This returns a new DataFrame containing only the selected features.

## Row Selection

- **Slicing**: Demonstrates basic Python-style slicing `df[start:stop]` to extract a range of records.

## loc vs iloc

A key part of the script is distinguishing between the two primary indexers in Pandas:

| Method | Type | Description |
|---|---|---|
| **`.loc`** | Label-based | Selects data using index labels and column names. Slicing with `loc` is **inclusive** of the end index. |
| **`.iloc`** | Position-based | Selects data using numeric integer positions. Slicing with `iloc` is **exclusive** of the end index (standard Python behavior). |

## Combined Selection

The script shows how to simultaneously select rows and columns using:
- `df.loc[row_list, col_list]`
- `df.iloc[row_range, col_range]`

## Execution

Run the selection demo to see various filtered views of the NGO program data:
```bash
python scripts/dataframe_selection_demo.py
```

## Conclusion

The script successfully demonstrates that Pandas provides robust and flexible methods for data slicing and indexing, allowing for precise control over data retrieval from complex tables.
