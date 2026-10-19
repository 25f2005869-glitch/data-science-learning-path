# 📊 Day 086 — Credit Risk Analysis: Monthly Trends

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 086  
**Topic:** Credit Risk Analysis — Monthly Trends

---

## 🏷️ Badges

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Diploma Level](https://img.shields.io/badge/Level-Diploma-blue?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Subject-BDM-green?style=for-the-badge)
![Day 086](https://img.shields.io/badge/Day-086-orange?style=for-the-badge)
![Excel](https://img.shields.io/badge/Tool-Excel-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Tool-Python-yellow?style=for-the-badge)

---

## 📌 Overview

Day 086 focuses on **Credit Risk Analysis — Monthly Trends**.

In Day 085, the credit-risk dataset was reviewed as a data snapshot.

In Day 086, the focus moves to **time-based analysis**.

Monthly trend analysis helps us understand how important credit-risk indicators change from one month to another.

The analysis includes:

- Customer volume
- Loan exposure
- Defaults
- Default rate
- Average credit score
- Average debt-to-income ratio
- High-risk customers
- High-risk customer share

---

## 🎯 Learning Objectives

By completing Day 086, you should be able to:

- Understand monthly credit-risk data.
- Calculate monthly KPIs.
- Calculate default rate.
- Calculate high-risk customer share.
- Compare consecutive months.
- Identify increasing and decreasing trends.
- Understand count versus rate.
- Analyze loan exposure over time.
- Create monthly trend charts.
- Use Excel for trend analysis.
- Use Python and Pandas for trend analysis.
- Interpret changes without confusing observation with explanation.

---

## 📚 Dataset Context

The Day 086 workbook contains a **synthetic monthly credit-risk dataset** for educational practice.

The dataset covers:

January 2026 → December 2026

Each row represents a monthly observation containing business-level credit-risk indicators.

The monthly dataset is designed for learning and should not be treated as official financial or banking data.

---

## 📊 Monthly Data Fields

| Field | Description |
|---|---|
| Month | Month of observation |
| Customers | Number of customers |
| Loan_Exposure_Rupee | Total loan exposure |
| Defaults | Number of defaults |
| Average_Credit_Score | Average credit score |
| Average_DTI_% | Average debt-to-income ratio |
| High_Risk_Customers | Number of high-risk customers |

Additional analytical metrics are calculated from these fields.

---

## 🧮 Key Metrics

### 1. Default Rate

Default rate measures defaults relative to the number of customers.

Default Rate (%) = Defaults / Customers × 100

---

### 2. High-Risk Share

High-risk share measures high-risk customers relative to total customers.

High-Risk Share (%) = High-Risk Customers / Customers × 100

---

### 3. Month-to-Month Change

Monthly changes can be calculated as:

Current Month Value - Previous Month Value

This can be applied to:

- Customer count
- Loan exposure
- Average credit score
- Average DTI

For rates, percentage-point change can be used.

---

## 📈 Why Monthly Trends Matter

A single snapshot shows the situation at one point in time.

A monthly trend shows how the situation changes.

For example:

January → February → March → April → ... → December

This makes it possible to investigate questions such as:

- Is customer volume increasing?
- Is loan exposure increasing?
- Are defaults increasing?
- Is default rate changing?
- Is average credit score changing?
- Is average DTI increasing?
- Is the high-risk share changing?

---

## 📊 Trend Analysis

A trend can be described as:

### Increasing

The metric generally moves upward.

### Decreasing

The metric generally moves downward.

### Stable

The metric remains relatively similar.

### Volatile

The metric moves up and down noticeably.

### Sudden Change

The metric changes sharply between consecutive months.

These descriptions identify patterns in the data. They do not automatically explain why the pattern occurred.

---

## ⚠️ Count vs Rate

Counts and rates provide different information.

### Count

Answers:

How many?

Example:

Defaults = 7

### Rate

Answers:

What proportion?

Example:

Default Rate = 10.94%

Both should be considered when reviewing monthly credit risk.

---

## 💰 Exposure Context

Loan exposure is an important part of credit-risk analysis.

If exposure increases, the amount associated with the lending portfolio is also increasing.

However, exposure should be reviewed together with:

- Defaults
- Default rate
- High-risk share
- Credit score
- DTI
- Customer volume

One metric alone does not provide a complete view.

---

## 📁 Workbook Structure

The Excel workbook contains the following sheets:

- Instructions
- Monthly_Trend_Data
- Monthly_KPIs
- Monthly_Risk_Summary
- Monthly_Product_Trends
- Monthly_Outcome_Review
- Dataset_Context
- Trend_Questions
- Risk_Framework
- Credit_Risk_Monthly_Dashboard

---

## 📋 Important Workbook Sheets

### `Monthly_Trend_Data`

Contains the monthly source data used for analysis.

### `Monthly_KPIs`

Contains calculated monthly indicators such as:

- Default Rate
- High-Risk Share
- Customer changes
- Exposure changes
- Credit-score changes
- DTI changes

### `Monthly_Risk_Summary`

Provides a summarized view of monthly risk indicators.

### `Monthly_Product_Trends`

Provides product-level trend analysis.

### `Monthly_Outcome_Review`

Provides a review of monthly outcomes.

### `Credit_Risk_Monthly_Dashboard`

Provides visual trend charts for important monthly indicators.

---

## 📊 Dashboard Charts

The dashboard includes trend visualizations for:

1. Monthly Customer Volume
2. Monthly Loan Exposure
3. Monthly Default Rate
4. Average Credit Score
5. Average DTI
6. High-Risk Share

Line charts are useful for showing movement across months.

---

## 🐍 Python Analysis

Python is used to perform the same type of analysis programmatically.

The Python workflow includes:

1. Load Excel file
2. Read monthly data
3. Check structure
4. Check missing values
5. Check duplicates
6. Convert numeric columns
7. Sort by Month
8. Calculate KPIs
9. Calculate monthly changes
10. Create summary tables
11. Export CSV files
12. Create trend charts

---

## 🛠️ Tools Used

### Excel

Used for:

- Data review
- Formula calculations
- KPI tables
- Trend analysis
- Dashboard creation

### Python

Used for:

- Pandas
- Data validation
- KPI calculation
- Grouped analysis
- Month-to-month comparison
- CSV export
- Matplotlib charts

---

## 🔍 Business Questions

Day 086 helps answer questions such as:

1. Which month had the highest number of customers?
2. Which month had the highest loan exposure?
3. Which month had the highest number of defaults?
4. Which month had the highest default rate?
5. How did average credit score change over time?
6. How did average DTI change over time?
7. Which month had the highest number of high-risk customers?
8. Which month had the highest high-risk share?
9. Are exposure and risk indicators changing together?
10. Are there months that require further investigation?

---

## 🧠 Interpretation Framework

When reviewing a monthly trend, use the following sequence:

1. Identify the metric
2. Check the monthly values
3. Compare consecutive months
4. Identify the direction of change
5. Check related indicators
6. Check the size of the change
7. Record the observation
8. Identify what requires further investigation

---

## ⚠️ Observation vs Explanation

A good analysis separates what the data shows from what might explain it.

### Observation

The default rate increased from one month to the next.

### Explanation

The default rate increased because customers became financially stressed.

The second statement requires additional evidence.

Therefore, Day 086 focuses first on identifying and describing patterns in the available data.

---

## 🔐 Data Leakage Consideration

When credit-risk analysis is later used for predictive modeling, the timing of variables is important.

A feature should not use information that became available only after the outcome occurred.

Using future information to predict a past or current outcome can create **data leakage**.

Time-based analysis helps build awareness of this issue.

---

## ⚠️ Dataset Limitation

The monthly dataset is synthetic and created for educational practice.

Therefore:

- It is not official banking data.
- It should not be used for real financial decisions.
- Observed patterns are intended for learning.
- Real-world analysis would require appropriate production data, definitions, and validation.

---

## 🔄 Day 085 → Day 086

### Day 085

Credit Risk Analysis → Review of Data → Structure → Completeness → Uniqueness → Categories → Outcomes → Exposure

### Day 086

Credit Risk Analysis → Monthly Trends → Time-based comparison → Monthly KPIs → Trend interpretation → Dashboard

Day 086 therefore extends the previous data-review work into time-based business analysis.

---

## 📝 Suggested Workflow

1. Open the Excel workbook
2. Read Instructions
3. Review Monthly_Trend_Data
4. Review Monthly_KPIs
5. Review Monthly_Risk_Summary
6. Study the dashboard
7. Answer Trend_Questions
8. Run the Python script
9. Review generated CSV files
10. Review generated charts
11. Write your own observations

---

## 📌 Key Takeaways

Remember:

Snapshot → One point in time

Trend → Movement across time

Count → How many

Rate → What proportion

Exposure → Amount associated with lending

Average → Summary measure

Change → Difference from previous period

Monthly credit-risk analysis is useful because it combines **time, business volume, exposure, and risk indicators** into one analytical view.

---

## ✅ Day 086 Completion Checklist

- [ ] Understand monthly trend analysis
- [ ] Review monthly dataset
- [ ] Calculate default rate
- [ ] Calculate high-risk share
- [ ] Compare consecutive months
- [ ] Review customer volume
- [ ] Review loan exposure
- [ ] Review defaults
- [ ] Review credit score
- [ ] Review DTI
- [ ] Review high-risk customers
- [ ] Create or review trend charts
- [ ] Complete Excel analysis
- [ ] Run Python analysis
- [ ] Review exported CSV files
- [ ] Answer trend questions
- [ ] Write final observations

---

## 🎓 Final Learning Outcome

After completing Day 086, you should be able to take monthly credit-risk data and turn it into a structured trend analysis using **Excel and Python**.

The main goal is to move from:

Raw Monthly Data → Monthly KPIs → Trend Comparison → Visual Analysis → Business Questions → Evidence-based Observations

This forms an important foundation for the next stages of Business Data Management and Business Analytics.