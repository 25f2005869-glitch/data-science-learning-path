# 📋 Day 086 — Credit Risk Analysis: Monthly Trends

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 086  
**Topic:** Credit Risk Analysis — Monthly Trends

---

## 🎯 Quick Objective

Analyse how credit-risk indicators change from month to month.

---

## 📊 Core Metrics

| Metric | Meaning |
|---|---|
| Customers | Number of customers in a month |
| Loan Exposure | Total loan exposure |
| Defaults | Number of default cases |
| Default Rate | Defaults as a percentage of customers |
| Average Credit Score | Monthly average credit score |
| Average DTI | Monthly average debt-to-income ratio |
| High-Risk Customers | Number of high-risk customers |
| High-Risk Share | High-risk customers as a percentage of customers |

---

## 🧮 Important Formulas

### Default Rate

Default Rate (%) = Defaults / Customers × 100

### High-Risk Share

High-Risk Share (%) = High-Risk Customers / Customers × 100

### Customer Change

Current Customers − Previous Customers

### Exposure Change

Current Exposure − Previous Exposure

### Credit Score Change

Current Average Credit Score − Previous Average Credit Score

### DTI Change

Current DTI − Previous DTI

---

## 📌 Percentage vs Percentage Point

For rates, use percentage-point change.

Example:

January Default Rate = 7.14%

February Default Rate = 6.67%

Change = 6.67 − 7.14

Change = −0.47 percentage points

---

## 📈 Trend Types

| Trend | Meaning |
|---|---|
| Increasing | Metric generally moves upward |
| Decreasing | Metric generally moves downward |
| Stable | Metric remains relatively similar |
| Volatile | Metric moves up and down |
| Sudden Change | Sharp movement between periods |

---

## ⚖️ Count vs Rate

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

Always consider both when reviewing monthly risk.

---

## 💰 Exposure Review

Review loan exposure together with:

- Customer count
- Defaults
- Default rate
- Average credit score
- Average DTI
- High-risk customers
- High-risk share

One metric alone does not provide a complete view.

---

## 🗓️ Monthly Order

Always keep months in chronological order:

January → February → March → April → May → June → July → August → September → October → November → December

Correct ordering is important for month-to-month calculations.

---

## 📊 Useful Charts

Use line charts for monthly trends:

1. Customer Volume
2. Loan Exposure
3. Default Rate
4. Average Credit Score
5. Average DTI
6. High-Risk Share

---

## 🐍 Python Quick Workflow

1. Load Excel file
2. Read `Monthly_Trend_Data`
3. Check shape
4. Check columns
5. Check data types
6. Check missing values
7. Check duplicates
8. Convert numeric columns
9. Sort by Month
10. Calculate Default Rate
11. Calculate High-Risk Share
12. Calculate monthly changes
13. Create summaries
14. Export CSV files
15. Create charts

---

## 🐼 Useful Pandas Functions

| Function | Purpose |
|---|---|
| `pd.read_excel()` | Read Excel workbook |
| `.shape` | Check rows and columns |
| `.columns` | View column names |
| `.dtypes` | Check data types |
| `.isna().sum()` | Check missing values |
| `.duplicated().sum()` | Check duplicates |
| `pd.to_numeric()` | Convert numeric data |
| `.sort_values()` | Sort months |
| `.diff()` | Calculate changes |
| `.groupby()` | Group data |
| `.to_csv()` | Export CSV |

---

## 🔍 Trend Analysis Checklist

- [ ] Sort months correctly
- [ ] Check missing values
- [ ] Check duplicates
- [ ] Check numeric columns
- [ ] Calculate default rate
- [ ] Calculate high-risk share
- [ ] Compare consecutive months
- [ ] Review customer volume
- [ ] Review loan exposure
- [ ] Review defaults
- [ ] Review credit score
- [ ] Review DTI
- [ ] Review high-risk customers
- [ ] Review high-risk share
- [ ] Create trend charts

---

## 🧠 Interpretation Framework

Use this sequence:

1. Identify the metric.
2. Review monthly values.
3. Compare consecutive months.
4. Identify direction.
5. Check the size of change.
6. Compare related indicators.
7. Record the observation.
8. Identify what needs further investigation.

---

## ⚠️ Observation vs Explanation

### Observation

The default rate increased.

### Explanation

The default rate increased because customers became financially stressed.

The second statement requires additional evidence.

First describe what the data shows.

---

## 🔐 Data Leakage Reminder

For predictive modeling:

- Features should respect timing.
- Future information should not be used to predict an earlier outcome.
- Information created after the outcome can cause data leakage.

---

## ⚠️ Dataset Reminder

The Day 086 monthly dataset is synthetic and educational.

It is not official banking data and should not be used for real financial decisions.

---

## 🔄 Day 085 → Day 086

Day 085:

Data Review → Structure → Completeness → Uniqueness → Categories → Outcomes

Day 086:

Monthly Data → KPIs → Month-to-Month Comparison → Trends → Dashboard

---

## 📌 Quick Memory Notes

Snapshot = One point in time

Trend = Movement across time

Count = How many

Rate = What proportion

Exposure = Lending amount represented

Average = Summary measure

Change = Difference from previous month

---

## 🎓 Final Formula

Monthly Credit Risk Analysis:

Monthly Data  
→ KPI Calculation  
→ Month-to-Month Comparison  
→ Trend Analysis  
→ Visualization  
→ Business Questions  
→ Evidence-Based Observation