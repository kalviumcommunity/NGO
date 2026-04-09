# Missing Values Detection Verification

## Script Details

- **File Name**: `missing_values_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates how to identify, count, and inspect incomplete data (missing values) within a Pandas DataFrame. Detecting missing values is a crucial prerequisite for data cleaning and ensuring the reliability of statistical analysis.

## Missing Value Detection

- **Function**: `isnull()`
- **Logic**: Returns a Boolean mask identifying `NaN` (Not a Number) entries. This highlights the locations of empty cells across the entire NGO program dataset.

## Missing Value Count

- **Function**: `isnull().sum()`
- **Logic**: Aggregates the Boolean mask to provide a per-column count of missing entries. This helps pinpoint which features are most affected by data entry gaps.

## Column Identification

- The script programmatically identifies columns that have at least one missing value, flagging them as areas needing attention from data managers.

## Row Inspection

- **Logic**: Extracts any row containing one or more missing values using `df[df.isnull().any(axis=1)]`.
- **Utility**: Allows analysts to see exactly which NGO program records are incomplete and decide whether to drop them or fill the gaps.

## Observations

- **Incomplete Features**: Missing data was detected in several key metrics: `cost`, `people_helped`, and `outcome_score`.
- **Incomplete Records**: 3 out of the 4 sample records contain at least one piece of missing information.

## Execution

Run the script from the project root:
```bash
python scripts/missing_values_demo.py
```

## Conclusion

The script successfully demonstrates the use of Pandas to audit dataset completeness. It proves that we can systematically find and isolate missing information, laying the groundwork for more advanced data cleaning tasks like imputation.
