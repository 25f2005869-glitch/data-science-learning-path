![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-065-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 065 Cheat Sheet — Dataset and Gender Diversity

## Dataset Basics

Row → observation.

Column → variable.

Categorical → groups or labels.

Numeric → measurable values.

## Key Categories

Gender

Department

Region

Job_Title

Employment_Type

## Key Numeric Fields

Age

Monthly_Salary

Performance_Score

Training_Hours

Attendance_%

## Core Formula

Gender Share % = Gender Count / Total Employees × 100

## Department Share

Department Gender Share % = Gender Count in Department / Department Total × 100

## Attrition Rate

Attrition Rate % = Attrition Count / Employee Count × 100

## Excel Functions

COUNTIF → count a category.

COUNTIFS → count multiple conditions.

SUMIF → conditional total.

AVERAGEIF → conditional average.

AVERAGEIFS → average with multiple conditions.

PivotTable → multidimensional summary.

## Python Functions

pd.read_excel()

groupby()

agg()

mean()

sum()

pd.crosstab()

to_csv()

## Quality Checks

Employee IDs should be unique.

Gender labels should be standardized.

Numeric fields should be numeric.

Attendance should use a valid percentage scale.

Performance scores should use a defined scale.

## Analysis Questions

How many employees are in each gender category?

What is the overall gender share?

How does composition vary by department?

How does it vary by region?

How does it vary by role?

How do descriptive salary averages compare?

How do performance averages compare?

## Interpretation Rules

Use explicit denominators.

State the population.

Separate correlation from causation.

Consider role and seniority context.

Avoid unsupported explanations.

## Dashboard

Employees by Gender.

Average Salary by Gender.

Average Performance by Gender.

Average Training Hours by Gender.

## Quick Revision

1. What is an observation?
2. What is a categorical variable?
3. How is gender share calculated?
4. Why use department segmentation?
5. Why can average salary be misleading?
6. Why are denominators important?
7. What is crosstab used for?
8. Why are data definitions necessary?

## Formula Check

Total gender counts should equal total employee count.

Gender shares should sum to approximately 100%.

Department gender counts should match department totals.

Regional gender counts should match regional totals.

## 🏅 Quick Badges

📊 Data Review

👥 Diversity Analytics

📗 Excel

🐍 Python