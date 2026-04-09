# CSV Loading Verification

## Script Details

- **File Name**: `csv_loading_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates the safe and intentional loading of CSV data into a Pandas DataFrame. It focuses on using built-in Pandas methods to verify the structural integrity of the data before processing.

## CSV Loading

- **Function**: `pd.read_csv()` is used to load data from `data/raw/ngo_programs.csv`.
- **Logic**: This is the entry point for most data science workflows involving external data files.

## Data Verification

The script utilizes a comprehensive set of inspection tools:

- **`.head()`**: Provides a quick preview of the first 5 records to confirm data alignment.
- **`.columns`**: Verifies that all expected feature names are present.
- **`.shape`**: Confirms the total number of records (rows) and attributes (columns).
- **`.info()`**: Inspects the data types and captures the presence of null values or memory usage details.

## Structure Understanding

The dataset is interpreted as follows:
- **Rows**: Individual NGO program instances or budget records.
- **Columns**: Strategic features such as `ngo_name`, `program_type`, `location`, `cost`, `people_helped`, and `outcome_score`.

## Observations

- **Load Confirmation**: The data was parsed correctly into a tabular format.
- **Integrity Check**: An automated comparison was performed to ensure actual column names and counts match the target project structure.

## Execution

Run the loading demo from the project root:
```bash
python scripts/csv_loading_demo.py
```

## Conclusion

The script successfully demonstrates that loading CSV data into Pandas is more than just a single command—it involves a critical phase of structural verification to ensure the analysis starts with clean, expected data.
