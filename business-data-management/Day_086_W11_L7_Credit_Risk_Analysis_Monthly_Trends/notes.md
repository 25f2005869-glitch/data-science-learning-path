# 📘 Day 086 — Credit Risk Analysis: Monthly Trends

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 086  
**Topic:** Credit Risk Analysis — Monthly Trends

---

## 🎯 1. Learning Objective

Day 086 focuses on analysing credit-risk indicators across months.

The main purpose is to move from a single data snapshot to a time-based view.

The analysis covers:

- Customer volume
- Loan exposure
- Defaults
- Default rate
- Average credit score
- Average DTI
- High-risk customers
- High-risk share

---

## 📚 2. Dataset Context

The Day 086 workbook contains a synthetic monthly credit-risk dataset.

The data covers:

- January 2026
- February 2026
- March 2026
- April 2026
- May 2026
- June 2026
- July 2026
- August 2026
- September 2026
- October 2026
- November 2026
- December 2026

This monthly dataset is designed for educational practice.

It should not be treated as official banking or financial data.

---

## 🗓️ 3. Why Time Matters

A single dataset snapshot tells us what is happening at one point in time.

Monthly data allows us to observe movement.

For example:

January → February → March → April → ... → December

This makes it possible to investigate whether a metric is:

- Increasing
- Decreasing
- Stable
- Volatile
- Changing suddenly

---

## 👥 4. Monthly Customer Volume

Customer count represents the number of customers observed during a month.

For example, the dataset contains:

- January: 42 customers
- February: 45 customers
- March: 47 customers

Customer volume helps provide business context.

A higher customer count does not automatically mean higher credit risk.

It should be reviewed with other risk indicators.

---

## 💰 5. Monthly Loan Exposure

Loan exposure represents the total loan amount associated with the monthly records.

The dataset records monthly loan exposure in rupees.

For example:

- January: ₹52,50,000
- February: ₹57,20,000
- March: ₹61,00,000

Exposure provides context about the amount associated with lending activity.

---

## ⚠️ 6. Monthly Defaults

Defaults represent the number of default cases observed in a month.

For example:

- January: 3 defaults
- February: 3 defaults
- March: 4 defaults

Default count is useful, but it should not be interpreted independently.

The number of customers should also be considered.

---

## 📊 7. Default Rate

Default rate expresses defaults relative to the number of customers.

### Formula

Default Rate (%) = Defaults / Customers × 100

Example:

Defaults = 3  
Customers = 42

Default Rate = 3 / 42 × 100

Default Rate ≈ 7.14%

The rate makes comparison easier when customer volumes differ between months.

---

## 🚨 8. High-Risk Customers

High-risk customers are customers classified as high risk according to the dataset's risk framework.

The monthly data contains a count of high-risk customers.

For example:

- January: 7
- February: 7
- March: 8

An increase in high-risk customers can be investigated alongside other indicators.

The count alone does not explain the reason for the change.

---

## 📈 9. High-Risk Share

High-risk share expresses high-risk customers as a percentage of total customers.

### Formula

High-Risk Share (%) = High-Risk Customers / Customers × 100

Example:

High-Risk Customers = 7  
Customers = 42

High-Risk Share = 7 / 42 × 100

High-Risk Share ≈ 16.67%

This is useful when monthly customer volumes are different.

---

## 💳 10. Average Credit Score

Average credit score provides a monthly summary of credit-score values.

Example:

- January: 718
- February: 721
- March: 716

A monthly average can help identify changes in the observed customer portfolio.

However, an average does not show the complete distribution of individual scores.

---

## 📉 11. Average DTI

DTI means Debt-to-Income ratio.

The monthly dataset provides Average_DTI_% as a percentage.

Example:

- January: 31.5%
- February: 30.8%
- March: 32.1%

DTI provides an additional indicator for reviewing the debt burden represented in the dataset.

---

## 🔄 12. Month-to-Month Change

Month-to-month analysis compares a current month with the previous month.

### Customer Change

Current Customers − Previous Customers

### Exposure Change

Current Exposure − Previous Exposure

### Credit Score Change

Current Average Credit Score − Previous Average Credit Score

### DTI Change

Current DTI − Previous DTI

This helps identify the size and direction of monthly movement.

---

## 📌 13. Percentage-Point Change

For rates, percentage-point change is useful.

Example:

January Default Rate = 7.14%

February Default Rate = 6.67%

Change:

6.67 − 7.14 = −0.47 percentage points

The result is a decrease of 0.47 percentage points.

---

## 📈 14. Increasing Trend

An increasing trend means that a metric generally moves upward over time.

Example:

January → 42  
February → 45  
March → 47

The customer count is increasing across these observations.

A trend should normally be reviewed across multiple months rather than from only two observations.

---

## 📉 15. Decreasing Trend

A decreasing trend means that a metric generally moves downward.

For example, if average credit score moves lower across several months, the change can be described as a decreasing trend.

The next step is to examine related indicators and determine what requires investigation.

---

## ➖ 16. Stable Trend

A stable trend means the metric remains relatively similar across the observed period.

Small month-to-month changes may still occur.

Stable does not mean that every monthly value is exactly the same.

---

## 🔀 17. Volatile Trend

A volatile trend contains noticeable upward and downward movements.

For example:

January → 10  
February → 14  
March → 9  
April → 15

The metric does not move consistently in one direction.

---

## ⚡ 18. Sudden Change

A sudden change occurs when a metric moves sharply between consecutive months.

When a sudden change appears, review:

- The source data
- Related metrics
- Business context
- Possible data-quality issues

The data pattern itself does not automatically provide the reason.

---

## ⚖️ 19. Count vs Rate

Counts and rates answer different questions.

### Count

How many?

Example:

Defaults = 7

### Rate

What proportion?

Example:

Default Rate = 10.94%

Both are useful.

A larger number of defaults can occur simply because the customer population became larger.

Therefore, default rate provides additional context.

---

## 💰 20. Exposure Context

Loan exposure should be reviewed together with risk indicators.

For example, an increase in exposure should be considered alongside:

- Customer count
- Defaults
- Default rate
- Average credit score
- Average DTI
- High-risk customers
- High-risk share

One metric alone does not provide a complete credit-risk view.

---

## 📊 21. Monthly KPI Table

A monthly KPI table can contain:

| KPI | Purpose |
|---|---|
| Customers | Monthly business volume |
| Loan Exposure | Lending exposure |
| Defaults | Default count |
| Default Rate | Default proportion |
| Average Credit Score | Credit-quality summary |
| Average DTI | Debt-burden summary |
| High-Risk Customers | High-risk count |
| High-Risk Share | High-risk proportion |

This table provides a compact monthly overview.

---

## 📈 22. Trend Charts

Line charts are useful for displaying monthly movement.

Useful charts include:

1. Monthly Customer Volume
2. Monthly Loan Exposure
3. Monthly Default Rate
4. Average Credit Score
5. Average DTI
6. High-Risk Share

The horizontal axis represents time.

The vertical axis represents the selected metric.

---

## 📋 23. Correct Monthly Ordering

Months must be sorted chronologically before calculating changes.

Correct order:

January → February → March → April → May → June → July → August → September → October → November → December

Incorrect ordering can produce incorrect month-to-month comparisons.

---

## 🐍 24. Python Workflow

The Python analysis follows these steps:

1. Load the Excel workbook.
2. Read the monthly trend sheet.
3. Check dataset shape.
4. Check column names.
5. Check data types.
6. Check missing values.
7. Check duplicates.
8. Convert numeric columns.
9. Sort the data by Month.
10. Calculate Default Rate.
11. Calculate High-Risk Share.
12. Calculate month-to-month changes.
13. Create summary tables.
14. Export analysis files.
15. Create trend charts.

---

## 🐼 25. Pandas Operations

Important Pandas operations include:

- `read_excel()`
- `shape`
- `columns`
- `dtypes`
- `isna()`
- `duplicated()`
- `to_numeric()`
- `sort_values()`
- `diff()`
- `groupby()`
- `to_csv()`

These operations support the monthly analysis workflow.

---

## 📊 26. Business Questions

The analysis can be used to answer:

1. Which month had the highest customer count?
2. Which month had the highest loan exposure?
3. Which month had the highest number of defaults?
4. Which month had the highest default rate?
5. How did average credit score change?
6. How did average DTI change?
7. Which month had the highest high-risk customer count?
8. Which month had the highest high-risk share?
9. Are exposure and risk indicators changing together?
10. Which monthly changes require further investigation?

---

## 🔍 27. Observation vs Explanation

An important analytical skill is separating observation from explanation.

### Observation

The default rate increased from one month to another.

### Explanation

The default rate increased because customers experienced financial stress.

The second statement requires additional evidence.

Therefore, first describe what the data shows.

Then identify possible areas that need further investigation.

---

## 🔎 28. Multiple Indicators

Credit-risk analysis should use multiple indicators together.

A useful review can include:

Customer Volume  
↓  
Loan Exposure  
↓  
Defaults  
↓  
Default Rate  
↓  
Average Credit Score  
↓  
Average DTI  
↓  
High-Risk Customers  
↓  
High-Risk Share

This provides broader context than looking at only one metric.

---

## ⚠️ 29. Data Quality

Before interpreting trends, basic quality checks should be performed.

Check:

- Missing values
- Duplicate records
- Numeric values
- Month ordering
- Data types
- Unexpected values

Incorrect or incomplete data can affect trend calculations.

---

## 🔐 30. Feature Timing and Data Leakage

Time is important when analysis later becomes predictive modeling.

A predictive feature should not use information that became available only after the outcome.

Using future information can create data leakage.

Therefore, analysts should consider when each variable becomes available.

---

## 🧠 31. Monthly Trend Interpretation

A useful interpretation follows this structure:

1. Identify the metric.
2. Review monthly values.
3. Compare consecutive periods.
4. Identify direction.
5. Check the size of change.
6. Compare related indicators.
7. Record the observation.
8. Identify what needs further investigation.

This creates a structured analytical process.

---

## ⚠️ 32. Synthetic Data Limitation

The Day 086 monthly dataset is synthetic.

It is created for learning and practice.

Therefore:

- It is not official financial data.
- It does not represent a real bank portfolio.
- Trends are educational examples.
- Conclusions should not be applied to real customers.
- Real analysis requires appropriate real-world data and validation.

---

## 🔄 33. Day 085 to Day 086

### Day 085

Focused on reviewing the credit-risk dataset:

- Structure
- Completeness
- Uniqueness
- Data types
- Categories
- Outcomes
- Exposure
- Business meaning

### Day 086

Extends the analysis into:

- Monthly data
- Monthly KPIs
- Time-based comparison
- Trend analysis
- Monthly charts
- Business interpretation

---

## 📁 34. Workbook Sheets

The Day 086 workbook includes:

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

Each sheet supports a different part of the monthly analysis exercise.

---

## 📝 35. Recommended Study Process

Follow this sequence:

1. Open the workbook.
2. Read the Instructions sheet.
3. Review Monthly_Trend_Data.
4. Review Monthly_KPIs.
5. Study Monthly_Risk_Summary.
6. Review trend questions.
7. Study the dashboard.
8. Run the Python script.
9. Check generated CSV files.
10. Review generated charts.
11. Write your own observations.

---

## 🎯 36. Key Takeaways

Remember these concepts:

Snapshot = One point in time

Trend = Movement across time

Count = How many

Rate = What proportion

Exposure = Lending amount represented in the analysis

Average = Summary measure

Change = Difference from the previous period

Monthly analysis becomes more useful when multiple indicators are reviewed together.

---

## ✅ 37. Day 086 Outcome

After completing Day 086, you should be able to:

- Understand monthly credit-risk data.
- Calculate default rate.
- Calculate high-risk share.
- Compare consecutive months.
- Identify trend direction.
- Review exposure alongside risk indicators.
- Create monthly KPI tables.
- Build trend charts.
- Perform the analysis in Excel.
- Perform the analysis in Python.
- Separate observations from explanations.
- Recognize limitations of synthetic data.

---

## 🧠 Final Summary

The main idea of Day 086 is:

Data Snapshot → Monthly Data → KPI Calculation → Month-to-Month Comparison → Trend Analysis → Visualization → Business Questions → Evidence-Based Observation

The goal is to understand how credit-risk indicators change over time and how those changes can be reviewed systematically using Excel and Python.