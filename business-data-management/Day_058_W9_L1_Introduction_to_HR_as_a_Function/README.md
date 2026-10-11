![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-058-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 🏢 Day 058 — Introduction to HR as a Function

## 📌 Day Overview

Day 058 — W9_L1 introduces **Human Resources (HR) as a business function**.

This package uses an illustrative employee dataset to practice basic workforce analysis.

**Important:** The dataset is created for learning and is not official IIT Madras or company data.

## 🎯 Learning Objectives

1. Understand HR as a core organizational function.
2. Identify common HR activities across the employee lifecycle.
3. Distinguish workforce data from HR decisions.
4. Calculate basic HR metrics such as headcount and attrition rate.
5. Compare departments, regions, and employment types.
6. Interpret HR metrics with business context.

## 🏢 HR as a Business Function

HR manages and supports people-related processes within an organization.

Typical areas include workforce planning, recruitment, onboarding, training, performance management, compensation, employee relations, and retention.

HR data can help describe workforce structure and identify patterns that deserve further investigation.

Analytics supports HR by turning structured employee records into measurable indicators.

## 📊 Dataset & Workbook

The Excel workbook contains employee-level records for 24 illustrative employees.

Main fields include employee ID, department, region, employment type, age, salary, performance, attrition flag, training hours, and attendance.

Supporting sheets provide department, region, employment-type summaries, KPIs, questions, a formula guide, and a dashboard.

## 📈 Key Metrics

Headcount = number of employees represented in the dataset.

Average salary = mean monthly salary across employees.

Attrition rate = attrition cases ÷ total employees × 100.

Average performance = mean performance score.

Average training hours = mean recorded training hours.

Average attendance = mean attendance percentage.

## 🧪 Practice Flow

Start with the HR_Data sheet.

Check field names and data types.

Use filters to inspect departments and regions.

Compare departmental headcount and salary.

Compare performance and attrition indicators.

Review the dashboard after understanding the underlying tables.

Use the Python script for reproducible analysis.

## ⚠️ Interpretation Notes

An HR metric describes a pattern; it does not automatically explain its cause.

Small illustrative datasets should not be treated as representative workforce evidence.

Salary comparisons should consider role, experience, location, employment type, and other context.

Attrition should be investigated with additional information before drawing conclusions.

## 🛠️ Tools

- Microsoft Excel / compatible spreadsheet software
- Python
- pandas
- matplotlib
- VS Code
- Git and GitHub

## 📁 Folder Structure

Day_058_W9_L1_Introduction_to_HR_as_a_Function/
├── Day_058_W9_L1_Introduction_to_HR_as_a_Function.xlsx
├── README.md
├── notes.md
├── cheat-sheet.md
├── practice.md
├── resources.md
├── code/
│   └── introduction_to_hr_as_a_function.py
└── python_outputs/

## 📝 Suggested Workflow

1. Read the Day overview.
2. Study the HR concepts.
3. Open the Excel workbook.
4. Inspect HR_Data.
5. Review the summary sheets.
6. Study the KPI calculations.
7. Complete practice questions.
8. Run the Python script.
9. Compare Python and Excel results.
10. Review the dashboard.

## 💼 Business Questions

What is the current workforce size?

How is the workforce distributed across departments?

How does average salary vary across departments?

How does performance vary across departments?

What is the observed attrition rate?

How can training and attendance data support HR analysis?

## 🔍 Analytical Thinking

HR analytics starts with a business question.

The analyst should identify the relevant population.

The next step is checking data quality.

After validation, summary metrics can be calculated.

Charts can then communicate important patterns.

The final interpretation should remain connected to the available evidence.

## 🛡️ Data Responsibility

Real HR data may contain sensitive employee information.

Individual employee information should be protected.

Public dashboards should generally use aggregated information when possible.

Access to workforce data should be controlled appropriately.

## 🐍 Python Practice

The Python script loads the HR dataset with pandas.

It creates department summaries.

It creates region summaries.

It creates employment-type summaries.

It calculates HR KPIs.

It exports CSV files.

It creates PNG charts using matplotlib.

## 📗 Excel Practice

Excel is useful for initial HR data exploration.

Filters can be used to inspect employee groups.

PivotTables can summarize workforce data.

Formulas can calculate HR indicators.

Charts can communicate workforce patterns.

## 📊 Dashboard

The dashboard contains four charts:

1. Employees by Department
2. Average Salary by Department
3. Attrition Cases by Department
4. Average Performance by Department

## 🎓 Learning Outcome

After completing Day 058, you should be able to explain why HR is a business function and perform basic descriptive workforce analysis.

## 🔗 Connection to BDM

This day continues the business-data-analysis journey.

The focus moves from manufacturing and inventory analysis toward people and workforce data.

The same analytical process remains useful:

Business Question → Data → Cleaning → Summary → Visualization → Insight.

## 🧠 Key Takeaway

HR data becomes useful when it is connected to a clearly defined business question and interpreted with appropriate context.

## 🏅 Badges

- 🏢 HR Function
- 📊 Workforce Analytics
- 🐍 Python Analysis
- 📗 Excel Practice
- 🎓 IIT Madras BDM
- 🚀 100-Day Learning Path