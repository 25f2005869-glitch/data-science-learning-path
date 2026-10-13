![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-061-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 061 Cheat Sheet — Basic Statistics

## Data Review

Records → count observations.
Missing values → identify blanks/nulls.
Duplicates → check unique IDs.
Categories → inspect distinct values.
Numerical fields → inspect minimum and maximum.

## Central Tendency

Mean = SUM / COUNT.
Median = middle value.
Mode = most frequent value.

## Dispersion

Range = MAX − MIN.
Variance measures squared dispersion.
Standard deviation = square root of variance.
IQR = Q3 − Q1.

## Quartiles

Q1 = 25th percentile.
Q2 = 50th percentile = Median.
Q3 = 75th percentile.

## Excel Functions

COUNT()
COUNTA()
SUM()
AVERAGE()
MEDIAN()
MODE.SNGL()
MIN()
MAX()
STDEV.S()
VAR.S()
QUARTILE.INC()

## Python Functions

df.describe()
df.mean()
df.median()
df.mode()
df.min()
df.max()
df.std()
df.var()
df.quantile()

## Grouped Analysis

df.groupby("Department")["Internal_Cost"].mean()
df.groupby("Region")["Actual_Days"].median()
df.groupby("Internal_Source")["Internal_Cost"].sum()

## Interpretation

Mean > Median can indicate higher values pulling the average upward.
Mean < Median can indicate lower values pulling the average downward.
Large standard deviation means more dispersion.
Small standard deviation means less dispersion.
Large range means extreme observations are far apart.

## Data Quality

Check missing values.
Check duplicates.
Check category spelling.
Check numeric types.
Check unrealistic values.
Check definitions.

## Dashboard

Requests by Department.
Mean versus Median Cost.
Actual Days by Source.
Monthly Cost.

## Quick Revision

1. What is mean?
2. What is median?
3. What is mode?
4. What is range?
5. What is standard deviation?
6. What is IQR?
7. Why review data first?
8. Why can averages be misleading?
9. Why use grouped statistics?
10. Why does context matter?

## 🏅 Badges

⚡ Cheat Sheet
📊 Statistics
🔍 Data Quality
🐍 Python
📗 Excel