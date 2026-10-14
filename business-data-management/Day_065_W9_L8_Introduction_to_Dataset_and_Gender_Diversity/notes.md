![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-065-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 065 Notes — Introduction to Dataset and Gender Diversity

## 1. Dataset Introduction

A dataset is an organized collection of observations and variables.

In this exercise, each observation represents an employee.

## 2. Observation

An employee record is one observation.

Employee_ID distinguishes records.

## 3. Variable

A variable is a field describing an observation.

Examples include Department, Gender, Age and Monthly_Salary.

## 4. Categorical Variables

Department, Region, Employment_Type, Gender and Job_Title are categorical fields.

They are useful for grouping and segmentation.

## 5. Numeric Variables

Age, Monthly_Salary, Performance_Score, Training_Hours and Attendance_% are numeric fields.

Numeric variables can be summarized using averages and totals.

## 6. Gender as an Analytical Dimension

Gender can be used to describe representation within the dataset.

The analysis should clearly state the population being measured.

## 7. Gender Count

Gender count is the number of employee records in each gender category.

COUNTIF or groupby can calculate this.

## 8. Gender Share

Gender share expresses the category count as a percentage of the selected population.

Formula:

Gender Share % = Category Count / Total Count × 100

## 9. Department Segmentation

Department segmentation shows gender composition within organizational units.

It helps identify where representation differs across the dataset.

## 10. Regional Segmentation

Region segmentation provides a geographic view.

It can reveal differences in the composition of the illustrative workforce.

## 11. Role Segmentation

Job_Title provides a role-level dimension.

Role-level analysis can be useful when representation varies across positions.

## 12. Salary

Average salary is a descriptive measure.

It should not be interpreted without considering role, seniority, experience and other factors.

## 13. Performance

Average performance score provides a descriptive comparison.

It does not establish why any difference exists.

## 14. Training

Training hours can be compared across categories.

Training access and participation may require more detailed records for deeper analysis.

## 15. Attendance

Attendance percentage provides another descriptive workforce variable.

Its interpretation depends on organizational definitions.

## 16. Data Quality

Check missing values.

Check duplicate employee IDs.

Check category spelling.

Check numeric types.

Check percentage ranges.

## 17. Denominators

Percentages are meaningful only when the denominator is clearly defined.

Overall share and department share are different measures.

## 18. Descriptive vs Causal

A descriptive difference tells us what is observed in the dataset.

It does not by itself explain the reason for that difference.

## 19. Excel Workflow

Inspect HR_Dataset first.

Use Gender_Summary for overall metrics.

Use Department_Gender for departmental segmentation.

Use Region_Gender for regional segmentation.

## 20. Python Workflow

Read the workbook with pandas.

Group by Gender.

Calculate summary metrics.

Export CSV files.

Create charts.

## 21. Business Use

A structured dataset can support workforce reporting.

Diversity reporting benefits from consistent definitions and appropriate context.

## 22. Extension Data

Tenure

Experience

Job Level

Hiring Source

Promotion History

Compensation Band

Recruitment Funnel

Retention

## 🧠 Summary

The first stage of gender-diversity analysis is dataset understanding.

The second stage is segmentation.

The third stage is descriptive KPI analysis.

The fourth stage is contextual interpretation.