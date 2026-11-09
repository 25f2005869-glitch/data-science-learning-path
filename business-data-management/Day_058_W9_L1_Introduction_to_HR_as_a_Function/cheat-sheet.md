![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-058-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 058 Cheat Sheet — HR Function

## HR Function

HR = Human Resources.

Focus: people + organizational processes.

Typical areas: hiring, onboarding, training, performance, compensation, relations, retention.

## Core Metrics

Headcount = employee count.

Average Salary = total salary / employee count.

Attrition Rate % = attrition cases / relevant population × 100.

Average Performance = sum of scores / number of scores.

Average Training Hours = total training hours / employees.

Average Attendance % = sum of attendance percentages / employees.

## Useful Excel Functions

COUNT() counts numeric cells.

COUNTA() counts non-empty cells.

AVERAGE() calculates a mean.

SUM() adds values.

COUNTIF() counts values matching a condition.

SUMIF() sums values matching a condition.

AVERAGEIF() averages values matching a condition.

PivotTables summarize grouped HR data.

## HR Dimensions

Department

Region

Employment Type

Role

Tenure

Age group

Performance band

## Interpretation Rules

Define the population.

Define the time period.

Check missing values.

Check duplicate records.

Separate description from explanation.

Avoid causal claims from simple comparisons.

Protect employee privacy in real-world data.

## Python Pattern

import pandas as pd

df = pd.read_excel(...)

summary = df.groupby("Department").agg(...)

summary.to_csv(...)

Use matplotlib for reproducible charts.

## Day 058 Formula Box

Attrition Rate = Attrition Cases ÷ Employees × 100

Department Average Salary = Department Salary Sum ÷ Department Employees

Department Headcount = Count of Employee IDs

Performance Gap = Group Average − Overall Average

## HR Lifecycle

Planning

Recruitment

Selection

Onboarding

Training

Performance

Compensation

Retention

Exit

## HR Analytics Flow

Business Question

↓

Identify Population

↓

Collect Data

↓

Check Data Quality

↓

Calculate Metrics

↓

Visualize

↓

Interpret

↓

Communicate

## Quick Revision

HR supports the employee lifecycle.

Workforce data supports measurement.

KPIs summarize patterns.

Dashboards communicate results.

Business context guides interpretation.

## Important Caution

A metric is evidence about a dataset.

A metric is not automatically an explanation.

A correlation is not automatically causation.

Small samples require careful interpretation.

## Dashboard Charts

Employees by Department

Average Salary by Department

Attrition Cases by Department

Average Performance by Department

## Tools

Excel

Python

pandas

matplotlib

VS Code

Git

GitHub

## 🏅 Badges

- ⚡ Quick Revision
- 📊 HR Metrics
- 🏢 HR
- 🐍 Python
- 📗 Excel
- 🎓 IIT Madras BDM