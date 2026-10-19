# 📚 Day 086 — Credit Risk Analysis: Monthly Trends — Resources

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 086  
**Topic:** Credit Risk Analysis — Monthly Trends

---

## 🎯 Purpose

This file contains the resources and reference areas for studying Day 086.

The main focus is:

- Monthly trend analysis
- Credit-risk KPIs
- Excel analysis
- Python analysis
- Data visualization
- Business interpretation

---

## 📁 1. Day 086 Workbook

The main practice resource is:

`Day_086_W11_L7_Credit_Risk_Analysis_Monthly_Trends.xlsx`

Important workbook sheets include:

- `Instructions`
- `Monthly_Trend_Data`
- `Monthly_KPIs`
- `Monthly_Risk_Summary`
- `Monthly_Product_Trends`
- `Monthly_Outcome_Review`
- `Dataset_Context`
- `Trend_Questions`
- `Risk_Framework`
- `Credit_Risk_Monthly_Dashboard`

Start with the `Instructions` sheet and then move through the analysis sheets.

---

## 📊 2. Monthly Trend Data

The `Monthly_Trend_Data` sheet is the main source table for Day 086.

Important fields:

| Field | Purpose |
|---|---|
| Month | Time period |
| Customers | Monthly customer volume |
| Loan_Exposure_Rupee | Monthly loan exposure |
| Defaults | Number of defaults |
| Average_Credit_Score | Average credit score |
| Average_DTI_% | Average DTI |
| High_Risk_Customers | High-risk customer count |

---

## 🧮 3. KPI Formulas

### Default Rate

Default Rate (%) = Defaults / Customers × 100

### High-Risk Share

High-Risk Share (%) = High-Risk Customers / Customers × 100

### Month-to-Month Change

Current Month Value − Previous Month Value

These formulas are the basic calculations used throughout the lesson.

---

## 📈 4. Trend Analysis Concepts

Review these concepts:

- Increasing trend
- Decreasing trend
- Stable trend
- Volatile trend
- Sudden change
- Month-to-month change
- Percentage-point change
- Count versus rate

The purpose is to describe how metrics move over time.

---

## 💰 5. Credit-Risk Indicators

The main indicators to review together are:

- Customer volume
- Loan exposure
- Defaults
- Default rate
- Average credit score
- Average DTI
- High-risk customers
- High-risk share

Avoid relying on a single metric when interpreting the monthly data.

---

## 📊 6. Excel Skills

Practice the following Excel skills:

- Reading structured tables
- Sorting data
- Creating formulas
- Calculating percentages
- Calculating differences
- Creating KPI tables
- Filtering data
- Creating line charts
- Reviewing dashboards
- Comparing monthly values

---

## 🐍 7. Python Skills

The Python practice focuses on:

- Pandas
- Excel file reading
- Data inspection
- Data cleaning
- Numeric conversion
- Sorting
- Difference calculations
- KPI calculations
- CSV export
- Matplotlib visualization

Useful Pandas functions include:

- `pd.read_excel()`
- `.shape`
- `.columns`
- `.dtypes`
- `.isna()`
- `.duplicated()`
- `pd.to_numeric()`
- `.sort_values()`
- `.diff()`
- `.groupby()`
- `.to_csv()`

---

## 📈 8. Visualization Resources

For monthly trend analysis, review the use of line charts.

Recommended charts for Day 086:

1. Monthly Customer Volume
2. Monthly Loan Exposure
3. Monthly Default Rate
4. Average Credit Score
5. Average DTI
6. High-Risk Share

A line chart is useful when the main question is how a metric changes across time.

---

## 🔍 9. Business Interpretation

When interpreting a chart or KPI table, ask:

1. What metric am I reviewing?
2. What is its value each month?
3. Is it increasing or decreasing?
4. Are there sudden changes?
5. What happened to related metrics?
6. Is the change in count or rate?
7. Does exposure provide additional context?
8. What does the data directly show?
9. What requires additional evidence?
10. What should be investigated next?

---

## ⚖️ 10. Count vs Rate

Review the difference between:

### Count

How many cases occurred?

Example:

`Defaults = 7`

### Rate

What proportion of customers does the count represent?

Example:

`Default Rate = 10.94%`

Both measures provide different information.

---

## 💡 11. Exposure Context

When reviewing loan exposure, also review:

- Customer volume
- Defaults
- Default rate
- Credit score
- DTI
- High-risk customers
- High-risk share

An increase in exposure should be interpreted using the other available indicators.

---

## 📝 12. Observation and Explanation

Keep these two concepts separate.

### Observation

Something directly visible in the data.

Example:

`The default rate increased from one month to another.`

### Explanation

A possible reason for the observed change.

An explanation requires supporting evidence.

The analysis should not present an unsupported explanation as a fact.

---

## 🔐 13. Data Leakage Resource

When moving toward predictive modeling, review:

- Feature timing
- Outcome timing
- Future information
- Data leakage

A feature should not use information that became available only after the outcome when that feature is intended for prediction.

---

## 🔄 14. Connection with Day 085

Day 085 focused on reviewing the credit-risk data.

Key areas included:

- Structure
- Completeness
- Uniqueness
- Data types
- Categories
- Outcomes
- Exposure
- Business meaning

Day 086 extends this into monthly trend analysis.

Study sequence:

`Day 085 Data Review → Day 086 Monthly Trends`

---

## 🗂️ 15. Recommended File Sequence

Study the Day 086 files in this order:

1. `README.md`
2. `notes.md`
3. `cheat-sheet.md`
4. `practice.md`
5. `resources.md`
6. `Day_086_W11_L7_Credit_Risk_Analysis_Monthly_Trends.xlsx`
7. `credit_risk_analysis_monthly_trends.py`

This sequence moves from overview to detailed learning, practice, data analysis, and Python implementation.

---

## 🧪 16. Practice Resources

Use `practice.md` for:

- Time-structure exercises
- Customer analysis
- Exposure analysis
- Default analysis
- Default-rate calculations
- High-risk analysis
- Credit-score analysis
- DTI analysis
- Trend classification
- Dashboard practice
- Python practice
- Excel practice
- Mini case study
- Final assignment
- Reflection

---

## 📊 17. Dashboard Resource

Use the:

`Credit_Risk_Monthly_Dashboard`

sheet to review visual trends.

Focus on:

- Direction of movement
- Changes between months
- High and low points
- Related indicators
- Sudden changes

Write observations based on the displayed data.

---

## 🔁 18. Reproducibility

A reproducible analysis should:

- Use the same source workbook
- Use consistent column names
- Keep the monthly order correct
- Apply the same formulas
- Save calculated outputs
- Save charts
- Record the analysis steps

The Python script helps repeat the analysis programmatically.

---

## 📂 19. Python Output Resources

The Python analysis can produce:

- `monthly_kpis.csv`
- `monthly_risk_trend_analysis.csv`
- `credit_risk_monthly_summary.csv`

It also creates trend charts for important monthly indicators.

---

## 🧠 20. Study Questions

Use these questions while studying:

- What is a monthly trend?
- Why is time important?
- What is default rate?
- What is high-risk share?
- Why compare count and rate?
- Why review exposure?
- Why sort months chronologically?
- What does a sudden change indicate?
- What is the difference between observation and explanation?
- Why does feature timing matter?

---

## ⚠️ 21. Dataset Limitation

The Day 086 monthly dataset is synthetic and educational.

Therefore:

- It is not official banking data.
- It does not represent a real bank portfolio.
- Observed patterns are for learning.
- Results should not be used for real financial decisions.
- Real-world analysis requires suitable data and validation.

---

## 🎓 22. Learning Extension

After completing Day 086, continue practising:

- Time-series summaries
- KPI dashboards
- Excel trend analysis
- Pandas transformations
- Matplotlib charts
- Business storytelling
- Data-quality checks
- Credit-risk interpretation

These skills support later Business Data Management and Business Analytics work.

---

## 🧭 23. Recommended Study Flow

Use this workflow:

`Read README`

↓

`Study notes`

↓

`Review cheat-sheet`

↓

`Open Excel workbook`

↓

`Complete practice questions`

↓

`Run Python script`

↓

`Review CSV outputs`

↓

`Review charts`

↓

`Write business observations`

↓

`Complete final assignment`

---

## 📌 24. Quick Reference

Remember:

`Snapshot = One point in time`

`Trend = Movement across time`

`Count = How many`

`Rate = What proportion`

`Exposure = Lending amount represented`

`Average = Summary measure`

`Change = Difference from previous period`

---

## ✅ 25. Day 086 Resource Checklist

- [ ] Read `README.md`
- [ ] Study `notes.md`
- [ ] Review `cheat-sheet.md`
- [ ] Complete `practice.md`
- [ ] Review Excel workbook
- [ ] Review monthly KPI sheet
- [ ] Review dashboard
- [ ] Run Python script
- [ ] Review CSV outputs
- [ ] Review generated charts
- [ ] Write observations
- [ ] Complete final assignment

---

## 🎯 Final Resource Goal

The resources for Day 086 are designed to help build a complete monthly credit-risk analysis workflow:

`Monthly Data → Data Review → KPI Calculation → Trend Analysis → Visualization → Business Interpretation`

The main tools are **Excel and Python**, supported by structured practice and dashboard analysis.