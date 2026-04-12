# Distribution Comparison Verification

This document verifies the comparative analysis of distributions across multiple NGO metrics.

## Statistical Comparison Table

| Metric | Mean | Median | CV (Dispersion) | Skewness | Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **budget_usd** | $61,100 | $52,500 | 0.63 | 0.73 | Moderately spread, balanced. |
| **impact_reach** | 4,245 | 1,650 | 1.46 | 2.43 | Extremely volatile, highly right-skewed. |
| **success_rate** | 0.84 | 0.86 | 0.11 | -0.56 | Highly consistent and stable. |

## Key Insights Verified

### 1. Dispersion Analysis (CV)
- **Finding**: The Coefficient of Variation for `impact_reach` (1.46) is more than **10x higher** than that of `success_rate` (0.11).
- **Verification**: This confirms that while the quality of programs is consistent, the scale of impact varies wildly across different types of interventions.

### 2. Central Tendency & Skewness
- **Finding**: `impact_reach` has a massive positive skew of 2.43.
- **Verification**: The mean (4,245) is nearly **3x the median (1,650)**, proving that the organization's total impact is heavily dependent on a few outlier "super-projects".

### 3. Resource Allocation Logic
- **Finding**: `budget_usd` is more normally distributed than `impact_reach`.
- **Verification**: This reveals an opportunity for optimization—the organization is spending money relatively evenly, but the results (reach) are concentrated. Reallocating budget toward high-reach distributions could maximize total impact.

## Execution Log
```text
=== Multi-Column Summary Statistics ===

                   mean    median           std  ...        CV  skewness
budget_usd    61100.000  52500.00  38579.923876  ...  0.631423  0.725926
impact_reach   4245.000   1650.00   6213.607732  ...  1.463747  2.426701
success_rate      0.841      0.86      0.089378  ...  0.106276 -0.563457
```

## Verification Status: PASSED
- [x] Multi-column summary statistics computed.
- [x] Coefficient of Variation used for dispersion comparison.
- [x] Skewness used to identify outlier impact.
- [x] Meaningful interpretation of distribution differences provided.
