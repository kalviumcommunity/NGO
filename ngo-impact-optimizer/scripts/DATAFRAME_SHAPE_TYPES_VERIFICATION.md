# DataFrame Shape and Types Verification

## Script Details

- **File Name**: `dataframe_shape_types_demo.py`
- **Location**: `scripts/` folder

## Purpose

The script demonstrates the fundamental understanding of dataset dimensions (size) and the intrinsic data types of its columns. This is a critical step for determining which mathematical or categorical operations are valid for specific fields.

## Shape Interpretation

The dataset size is extracted using the `.shape` attribute:
- **Number of Rows (4)**: Represents 4 individual NGO program records (entries).
- **Number of Columns (6)**: Represents 6 strategic features (attributes) tracked for each program.

## Column Data Types

Pandas correctly interprets the data types based on the content of the `ngo_programs.csv` file:

### Numeric Columns
Used for mathematical analysis, calculations, and statistical summaries:
- `cost`: `int64`
- `people_helped`: `int64`
- `outcome_score`: `float64`

### Categorical/Text Columns
Used for grouping, filtering, and qualitative labels:
- `ngo_name`: `object`
- `program_type`: `object`
- `location`: `object`

## Dataset Understanding

- **Rows** represent the "instances" or "samples" in our data (the NGO programs themselves).
- **Columns** represent the "variables" or "descriptors" for each NGO program.

## Observations

- The dataset is structured correctly with **4 entries** and **6 attributes**.
- Data types are perfectly aligned with the numerical and categorical nature of the NGO metrics.

## Execution

Run the script to verify the structural and typing metadata:
```bash
python scripts/dataframe_shape_types_demo.py
```

## Conclusion

The script successfully demonstrates the ability to programmatically verify and interpret DataFrame structure and typing, ensuring a solid foundation for higher-level data science operations.
