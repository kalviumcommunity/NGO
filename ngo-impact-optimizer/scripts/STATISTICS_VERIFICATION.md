# Summary Statistics Verification

This document verifies the computation and interpretation of basic summary statistics for the NGO impact dataset.

## Computation Results
The following statistics were calculated for `budget_usd` (Financial) and `peoplereached` (Impact).

| Metric | budget_usd | peoplereached |
| :--- | :--- | :--- |
| **Count** | 7.00 | 7.00 |
| **Mean** | $51,428.57 | 3,628.57 |
| **Median** | $45,000.00 | 1,200.00 |
| **Std Dev** | $36,022.48 | 5,247.45 |
| **Min** | $15,000.00 | 300.00 |
| **Max** | $120,000.00 | 15,000.00 |

## Key Interpretations

### 1. Central Tendency & Skewness
- **Finding**: For `peoplereached`, the Mean (3,629) is significantly higher than the Median (1,200).
- **Interpretation**: This indicating right-skewed data, where a small number of massive-reach projects (outliers in scale, like vaccinations) are driving the average up while most projects have a smaller, more localized reach.

### 2. Dispersion & Scalability
- **Finding**: The Standard Deviation for budget is high (~$36k on a $51k mean).
- **Interpretation**: This reflects a diverse project portfolio with varying resource requirements.
- **Correlation**: High Max Budget ($120k) aligns with High Max Reach (15,000 people), indicating that larger investments are indeed yielding larger community results.

## Execution Log
```text
=== Interpretation of Results ===

1. Budget Overview: The average project budget is $51,428.57.
   Insight: With a Standard Deviation of $36,022.48, there is significant variability
   between project sizes, ranging from small local gardens to large vaccination drives.

2. Reach Overview: The average impact per project is 3,629 people.
   Insight: The median (1,200) is lower than the mean, suggesting that a few
   high-impact projects (like vaccinations) are pulling the average upward.
```

## Verification Status: PASSED
- [x] All basic statistics (Mean, Median, Std Dev, etc.) computed.
- [x] Numeric column selection verified.
- [x] Comparative interpretation provided.
