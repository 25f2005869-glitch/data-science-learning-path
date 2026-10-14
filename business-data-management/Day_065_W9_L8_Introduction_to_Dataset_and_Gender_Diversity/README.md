![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-065-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📊 Day 065 — Introduction to Dataset and Gender Diversity

## 📌 Day Overview

Day 065 introduces an HR dataset and uses gender as a dimension for basic workforce-diversity analysis.

The package focuses on understanding the structure of the dataset before interpreting metrics.

The dataset is illustrative and is not official IIT Madras or company data.

## 🎯 Learning Objectives

1. Understand the HR dataset structure.
2. Identify categorical and numeric fields.
3. Review gender representation.
4. Segment gender by department.
5. Segment gender by region.
6. Examine role-level representation.
7. Calculate descriptive diversity KPIs.
8. Identify data-quality considerations.

## 🗂️ Dataset

The dataset contains 24 illustrative employee records.

Each row represents one employee.

The Gender field provides a categorical dimension.

Department and Region provide additional segmentation.

## 🧾 Important Fields

Employee_ID identifies the record.

Department identifies the organizational unit.

Region identifies the geographic group.

Gender identifies the dataset category.

Job_Title identifies the role.

Monthly_Salary stores salary.

Performance_Score stores a performance measure.

Training_Hours stores training participation.

Attendance_% stores attendance.

## 📊 Analysis Areas

- Overall gender representation
- Department-level gender composition
- Region-level gender composition
- Role-level gender composition
- Salary comparison
- Performance comparison
- Training comparison
- Attendance comparison

## 📗 Workbook

- HR_Dataset
- Gender_Summary
- Department_Gender
- Region_Gender
- Role_Gender
- Gender_KPIs
- Dataset_Context
- Data_Dictionary
- Diversity_Questions
- Business_Insights
- Gender_Diversity_Dashboard
- Instructions

## 📈 Dashboard

The dashboard contains four prepared charts.

1. Employees by Gender
2. Average Salary by Gender
3. Average Performance by Gender
4. Average Training Hours by Gender

## 🔎 Analysis Flow

Review the raw dataset.

Understand the field definitions.

Check category values.

Calculate gender counts.

Calculate gender shares.

Segment by department and region.

Review descriptive metrics.

Record limitations.

## ⚠️ Interpretation

The analysis is descriptive.

Salary or performance differences should not be treated as evidence of causation.

A deeper diversity study would require additional organizational context.

## 🐍 Python

The Python script uses pandas for grouping and aggregation.

It exports CSV summaries and creates four matplotlib charts.

## 🧠 Key Takeaway

A diversity analysis starts with reliable dataset structure, clearly defined categories and transparent denominators.

## 🏅 Badges

🔎 Dataset Analysis

👥 Gender Diversity

📊 HR Analytics

📗 Excel

🐍 Python

🎓 IIT Madras BDM

## 🔬 Practical Checks

- Check gender categories.
- Check missing values.
- Check employee IDs.
- Confirm percentage denominators.
- Separate descriptive analysis from causal interpretation.