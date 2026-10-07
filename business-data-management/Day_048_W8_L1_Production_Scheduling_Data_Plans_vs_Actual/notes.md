![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-048-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 048 Notes — Production Scheduling Data

## 1. Introduction

Production scheduling creates a plan for expected production output.

Actual production records the output achieved.

Comparing both gives a basic scheduling performance view.

## 2. Planned Production

Planned production represents units scheduled for production.

The Production_Plan sheet provides the planned view.

## 3. Actual Production

Actual production represents units actually produced.

The Actual_Production sheet provides the actual view.

## 4. Plan vs Actual

Plan_vs_Actual combines planned and actual values.

It makes the production difference visible.

## 5. Variance Units

Variance Units equals actual production minus planned production.

Formula:

Actual Production - Planned Production

## 6. Positive Variance

A positive variance means actual production is higher than planned.

This indicates production exceeded the plan for that observation.

## 7. Negative Variance

A negative variance means actual production is lower than planned.

This indicates production was below the plan for that observation.

## 8. Variance Percentage

Variance percentage normalizes the difference.

Formula:

Variance Units / Planned Production

## 9. Plan Achievement

Plan achievement measures actual production relative to planned production.

Formula:

Actual Production / Planned Production

## 10. Product Analysis

Product_Summary aggregates production by product.

The products are Gears, Shafts and Bearings.

## 11. Monthly Analysis

Monthly_Production aggregates production by month.

It helps identify changes in production achievement over time.

## 12. Regional Analysis

Variance_Analysis includes Product and Region.

It helps locate product-region combinations with different plan performance.

## 13. Business Interpretation

A variance is an analytical signal.

It does not automatically explain why the difference occurred.

Possible causes require supporting operational information.

## 14. Excel Workflow

Start with Production_Scheduling_Data.

Read Data_Dictionary.

Open Production_Plan.

Open Actual_Production.

Open Plan_vs_Actual.

Open Product_Summary.

Open Monthly_Production.

Open Variance_Analysis.

## 15. Questions

Use Scheduling_Questions for guided practice.

Use Business_Insights for evidence-based observations.

## 16. Dashboard

The dashboard presents the main production comparisons.

The charts should be interpreted together with the summary tables.

## 17. Python

Python reads the Excel workbook.

Pandas groupby is used for aggregation.

Variance calculations are created using arithmetic operations.

Matplotlib is used for visualisation.

## 18. Dataset Limitation

The dataset is illustrative.

It is not official IIT Madras course data.

It is intended for learning and practice.

## 19. Key Learning

Plan tells us what was scheduled.

Actual tells us what was produced.

Variance tells us the difference.

Plan achievement tells us the relative completion.

## 20. Revision

Remember the sequence:

Plan → Actual → Variance → Achievement

## 21. Final Learning Outcome

You should be able to explain the difference between planned and actual production.

You should be able to calculate variance.

You should be able to interpret plan achievement.

You should be able to compare products and months.

## 🔁 Revision Line

Production Schedule → Plan → Actual → Variance → Analysis → Dashboard

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-Production%20Scheduling-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Plan%20vs%20Actual-green?style=flat-square)
![Analytics](https://img.shields.io/badge/Analytics-Variance-orange?style=flat-square)