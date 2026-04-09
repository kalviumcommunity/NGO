# Pandas DataFrame Verification

## Script Details

- **File Name**: `pandas_dataframe_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates the creation and inspection of **DataFrames**, the primary tabular data structure in Pandas. It shows how to represent structured NGO data as a collection of rows (records) and columns (features).

## DataFrame from Dictionary

- **Method**: Converting a Python dictionary where keys become column names and value lists become row data.
- **Tabular Structure**: This approach is ideal for small, in-memory datasets where labels and values are predefined.

## DataFrame from CSV

- **Method**: Loading external structured data using `pd.read_csv()`.
- **Loading Data**: This is the standard practice in data science for importing large datasets stored in files like `data/raw/ngo_sample_data.csv`.

## Structure Understanding

- **Rows**: Each row represents an individual NGO record or program instance.
- **Columns**: Each column represents an attribute or feature (e.g., `program_type`, `cost`, `people_helped`).

## Inspection Methods

The script utilize the following essential inspection tools:
- **`.columns`**: To retrieve the names of all features in the dataset.
- **`.head()`**: To preview the first few rows and ensure formatting is correct.
- **`.shape`**: To check the dimensions (number of rows and columns) of the DataFrame.

## Execution

To verify the creation and structure of the DataFrame, run the script:
```bash
python scripts/pandas_dataframe_demo.py
```

## Conclusion

The script successfully demonstrates that a Pandas DataFrame is a powerful and flexible tool for handling tabular data. It provides a clear demonstration of how to load, structure, and inspect real-world datasets for analysis.
