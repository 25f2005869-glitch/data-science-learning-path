![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-066-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📊 Day 066 — Selection Criteria

## 📌 Day Overview

Day 066 focuses on defining and analyzing selection criteria for candidates.

The practical model combines minimum thresholds with a weighted score.

The dataset is illustrative and is not official IIT Madras or company data.

## 🎯 Learning Objectives

1. Understand selection criteria.
2. Convert requirements into measurable thresholds.
3. Calculate criterion-level eligibility.
4. Count criteria passed by each candidate.
5. Construct a weighted score.
6. Compare criteria attainment across departments.
7. Compare experience levels.
8. Separate criteria-based status from actual selection.

## 🧩 Selection Criteria

Technical Score threshold: 70.

Communication Score threshold: 75.

Interview Score threshold: 80.

Overall Score threshold: 75.

Experience requirement: at least 1 year.

## ⚖️ Weighted Score

Technical Score contributes 30%.

Communication Score contributes 20%.

Interview Score contributes 30%.

Overall Score contributes 20%.

Weighted Score =
Technical × 0.30 +
Communication × 0.20 +
Interview × 0.30 +
Overall × 0.20.

## 🧮 Criteria Pass Count

Each threshold produces an eligibility flag.

The flags are added to obtain Criteria_Pass_Count.

A candidate with at least four passed criteria receives Criteria Met status in this learning model.

## 📗 Workbook

- Selection_Data
- Selection_Criteria
- Candidate_Summary
- Department_Analysis
- Role_Analysis
- Experience_Level
- Region_Analysis
- Selection_KPIs
- Dataset_Context
- Data_Dictionary
- Selection_Questions
- Business_Insights
- Selection_Criteria_Dashboard
- Instructions

## 📈 Dashboard

Candidates by Department.

Criteria Met Rate by Department.

Criteria Met Rate by Experience Level.

Average Score by Region.

## 🔎 Analysis Flow

Review candidate records.

Read criterion definitions.

Check thresholds.

Calculate eligibility flags.

Calculate weighted scores.

Summarize by department.

Summarize by role and experience level.

Review actual selection separately.

## ⚠️ Interpretation

Thresholds are assumptions for learning.

Weights are illustrative.

A scoring model does not capture every hiring consideration.

Real selection processes may use role-specific criteria.

## 🐍 Python

The Python script reproduces the threshold checks and grouped summaries.

It exports CSV files and four charts.

## 🧠 Key Takeaway

Selection criteria become analytically useful when requirements are explicit, measurable and consistently applied.

## 🏅 Badges

🎯 Selection Criteria

📊 Candidate Analytics

📗 Excel

🐍 Python

🎓 IIT Madras BDM

## 🔬 Practical Checks

- Confirm every threshold.
- Verify score scales.
- Check missing scores.
- Check denominator definitions.
- Keep criteria-based status separate from final selection.