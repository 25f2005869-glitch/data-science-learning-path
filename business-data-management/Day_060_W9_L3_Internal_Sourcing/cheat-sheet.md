![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-060-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 060 Cheat Sheet — Internal Sourcing

## Internal Sourcing

Internal sourcing = fulfilling a requirement using internal organizational capability.
Internal Source = team providing the service.
Requesting Department = department needing the service.

## Core Metrics

Request Count = number of requests.
Total Cost = sum of internal costs.
Average Cost = total cost ÷ requests.
Time Variance = Actual Days − Planned Days.
Completion Rate % = Completed ÷ Requests × 100.
On-Time Rate % = On-Time Requests ÷ Requests × 100.
Cost per Day = Internal Cost ÷ Actual Days.

## Excel Functions

COUNT()
COUNTA()
SUM()
AVERAGE()
COUNTIF()
SUMIF()
AVERAGEIF()
PivotTables

## Dimensions

Department
Internal Source
Region
Month
Requirement

## Time Interpretation

Variance > 0 → actual time exceeded plan.
Variance = 0 → actual time matched plan.
Variance < 0 → actual time was below plan.

## Analysis Flow

Business Question
Data
Quality Check
Grouping
Aggregation
Visualization
Insight

## Python Pattern

import pandas as pd
df = pd.read_excel(...)
df['Time_Variance_Days'] = df['Actual_Days'] - df['Planned_Days']
summary = df.groupby('Department').agg(...)
summary.to_csv(...)

## Interpretation Rules

Define the period.
Define the population.
Check missing values.
Check category consistency.
Validate totals.
Do not infer causation from simple comparisons.

## Dashboard

Requests by Department.
Cost by Department.
Actual Days by Internal Source.
Satisfaction by Department.

## Quick Revision

Internal sourcing uses internal capabilities.
Cost measures resource use.
Time variance compares plan and actual.
Completion measures recorded completion.
On-time measures a defined timing threshold.
Satisfaction measures the recorded service experience.

## 🏅 Badges

⚡ Quick Revision
🏢 Internal Sourcing
📊 Business Metrics
🐍 Python
📗 Excel

- Revision checkpoint 96: connect internal sourcing concepts to a measurable business question.

- Revision checkpoint 98: connect internal sourcing concepts to a measurable business question.

- Revision checkpoint 100: connect internal sourcing concepts to a measurable business question.

- Revision checkpoint 102: connect internal sourcing concepts to a measurable business question.

- Revision checkpoint 104: connect internal sourcing concepts to a measurable business question.

- Revision checkpoint 106: connect internal sourcing concepts to a measurable business question.

- Revision checkpoint 108: connect internal sourcing concepts to a measurable business question.