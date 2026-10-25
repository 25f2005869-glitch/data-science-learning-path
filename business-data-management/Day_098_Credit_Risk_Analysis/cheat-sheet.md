# 📌 Day 098 — Credit Risk Analysis — Cheat Sheet

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-Day%20098-blue?style=for-the-badge)
![Credit Risk](https://img.shields.io/badge/Credit%20Risk-Analysis-green?style=for-the-badge)
![Excel](https://img.shields.io/badge/Excel-Analytics-orange?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 098
- **Topic:** Credit Risk Analysis

---

# 1. Credit Risk — Quick Definition

**Credit Risk:** The possibility that a borrower may not meet loan repayment obligations.

**Credit Risk Analysis:** Analysing customer and loan data to understand credit exposure, risk categories and loan outcomes.

---

# 2. Credit Risk Workflow

**Raw Data**

→ **Inspect**

→ **Data Quality Check**

→ **Clean**

→ **Validate**

→ **Risk Classification**

→ **Analyse**

→ **KPI**

→ **Visualise**

→ **Business Insights**

---

# 3. Important Dataset Fields

| Field | Meaning |
|---|---|
| Customer_ID | Customer identifier |
| Loan_Date | Loan-related date |
| Age | Customer age |
| City | Customer location |
| Employment_Type | Employment category |
| Monthly_Income | Monthly income |
| Credit_Score | Credit score |
| Loan_Amount | Loan amount |
| Interest_Rate_% | Interest rate |
| Loan_Tenure_Months | Loan duration |
| Existing_Loans | Existing loan count |
| Debt_to_Income_Ratio_% | Debt-to-income ratio |
| Risk_Category | Risk classification |
| Loan_Status | Loan status |

---

# 4. Risk Categories

The practice dataset contains:

- **Low**
- **Medium**
- **High**
- **Very High**

---

# 5. Risk Classification Rules

### Low

**Credit Score ≥ 740 AND DTI < 30%**

### Medium

**Credit Score ≥ 680 AND DTI < 40%**

### High

**Credit Score ≥ 620 AND DTI < 50%**

### Very High

**All other combinations**

> These rules are specific to the Day 098 educational dataset.

---

# 6. Loan Status

The dataset contains:

- Approved
- Active
- Closed
- Defaulted

---

# 7. Important Credit Risk Metrics

### Total Loan Exposure

**SUM(Loan Amount)**

### Average Credit Score

**Total Credit Score / Number of Customers**

### Average Monthly Income

**Total Monthly Income / Number of Customers**

### Average DTI

**Total DTI / Number of Customers**

### Default Count

**Number of Defaulted Records**

### Default Rate

**Defaulted Loans / Total Customers × 100**

### High / Very High Risk Rate

**(High Risk + Very High Risk) / Total Customers × 100**

---

# 8. Data Cleaning Checklist

Before analysis:

- Remove extra spaces
- Standardise capitalization
- Convert dates
- Convert numeric columns
- Check missing values
- Check invalid values
- Check negative values
- Remove exact duplicates
- Recalculate Risk Category
- Validate cleaned data

---

# 9. Missing Value Rules

| Field | Practice Cleaning Rule |
|---|---|
| Age | Median valid age |
| Monthly Income | Median valid income |
| Credit Score | Median valid score |
| Loan Amount | Median valid amount |
| Interest Rate | Median valid rate |
| Loan Tenure | Median valid tenure |
| Existing Loans | 0 |
| DTI | Median valid DTI |

---

# 10. Validation Rules

### Credit Score

**300 ≤ Score ≤ 850**

### Loan Amount

**Loan Amount ≥ 0**

### Interest Rate

**0 < Rate ≤ 30**

### Loan Tenure

**Tenure > 0**

### Existing Loans

**Existing Loans ≥ 0**

### DTI

**0 ≤ DTI ≤ 100**

---

# 11. Risk Category Analysis

Analyse:

- Customer Count
- Total Loan Amount
- Average Credit Score
- Average Income
- Average DTI
- Default Count
- Default Rate

---

# 12. Loan Analysis

Analyse by Loan Status:

- Customer Count
- Total Loan Amount
- Average Loan Amount
- Average Interest Rate
- Average Tenure

---

# 13. Customer Analysis

Important fields:

- Customer ID
- Age
- City
- Employment Type
- Monthly Income
- Credit Score
- Loan Amount
- Interest Rate
- Loan Tenure
- Existing Loans
- DTI
- Risk Category
- Loan Status

---

# 14. Monthly Credit Risk Analysis

Track by month:

- Customers
- Total Loan Amount
- Average Credit Score
- Average DTI
- High / Very High Risk Customers
- Default Count

---

# 15. Credit Risk KPIs

Main KPIs:

1. Total Customers
2. Total Loan Exposure
3. Average Credit Score
4. Average Monthly Income
5. Average DTI
6. High / Very High Risk Rate
7. Default Count
8. Default Rate
9. Active Loan Count

---

# 16. Pivot Analysis

### Pivot_Risk

**Risk Category → Customers → Loan Amount → Default Count**

### Pivot_Loan_Status

**Loan Status → Customers → Loan Amount → Average Credit Score**

---

# 17. Important Excel Functions

### Basic

- `SUM()`
- `AVERAGE()`
- `COUNT()`
- `COUNTA()`

### Conditional

- `COUNTIF()`
- `COUNTIFS()`
- `SUMIF()`
- `SUMIFS()`
- `AVERAGEIF()`
- `AVERAGEIFS()`

### Logical

- `IF()`
- `IFERROR()`

### Text Cleaning

- `TRIM()`
- `PROPER()`
- `UPPER()`
- `LOWER()`

---

# 18. Useful Excel Formulas

### Total Loan Amount

`=SUM(H2:H81)`

### Average Credit Score

`=AVERAGE(G2:G81)`

### Average Income

`=AVERAGE(F2:F81)`

### Default Count

`=COUNTIF(N2:N81,"Defaulted")`

### High Risk Count

`=COUNTIF(M2:M81,"High")`

### Very High Risk Count

`=COUNTIF(M2:M81,"Very High")`

### Active Loan Count

`=COUNTIF(N2:N81,"Active")`

---

# 19. Useful Python Libraries

### Pandas

Used for:

- Reading Excel
- Cleaning data
- Filtering
- Grouping
- Aggregation
- Exporting CSV

### NumPy

Used for:

- Numerical operations
- Conditional calculations
- Risk classification

### Matplotlib

Used for:

- Charts
- Risk visualisation
- Monthly trends

---

# 20. Python Analysis Pattern

**Read Excel**

→ **Inspect**

→ **Clean**

→ **Validate**

→ **Classify Risk**

→ **Group Data**

→ **Calculate KPIs**

→ **Create Charts**

→ **Export Results**

---

# 21. Common Groupby Analysis

Useful grouping dimensions:

- Risk Category
- Loan Status
- City
- Employment Type
- Month

Typical aggregation:

- `count`
- `sum`
- `mean`

---

# 22. Main Charts

### Chart 1
**Customers by Risk Category**

### Chart 2
**Loan Amount by Risk Category**

### Chart 3
**Monthly Loan Exposure Trend**

---

# 23. Business Questions

Use these questions for analysis:

1. How many customers are in each risk category?
2. What is the total loan exposure?
3. What is the average credit score?
4. What is the average monthly income?
5. What is the average DTI?
6. How many High-risk customers are present?
7. How many Very High-risk customers are present?
8. What is the default count?
9. What is the default rate?
10. How much loan exposure belongs to each risk category?
11. What is the average loan amount?
12. What is the average interest rate?
13. What is the average loan tenure?
14. How does loan exposure vary by loan status?
15. How does loan exposure change over time?

---

# 24. Business Insight Structure

Use:

**Observation**

→ What does the data show?

**Metric**

→ Which number supports it?

**Context**

→ Which category or period?

**Business Meaning**

→ What does it mean within this dataset?

---

# 25. Important Interpretation Points

- Do not analyse only Credit Score.
- Consider Income and DTI together.
- Consider Loan Amount separately from customer count.
- Review Default Count along with Default Rate.
- Check data quality before calculating KPIs.
- Use multiple metrics for descriptive analysis.
- Clearly state the analysis period.
- Remember that this is synthetic educational data.

---

# 26. Workbook Sheet Map

1. `Instructions`
2. `Raw_Credit_Risk_Data`
3. `Data_Quality_Check`
4. `Credit_Risk_Cleaning`
5. `Cleaned_Credit_Risk_Data`
6. `Credit_Risk_Summary`
7. `Risk_Category_Analysis`
8. `Loan_Analysis`
9. `Customer_Analysis`
10. `Monthly_Credit_Risk`
11. `Credit_Risk_KPI`
12. `Pivot_Risk`
13. `Pivot_Loan_Status`
14. `Chart_Data`
15. `Charts`
16. `Credit_Risk_Insights`
17. `Final_Credit_Risk_Analysis`

---

# 27. Quick Revision

### Credit Risk

Possibility of non-repayment.

### Credit Score

Credit-related numerical score.

### Loan Exposure

Total loan amount.

### DTI

Debt-to-Income Ratio.

### Risk Category

Low / Medium / High / Very High.

### Default

Loan status classified as Defaulted.

### Default Rate

**Default Count / Total Customers × 100**

### KPI

A metric used to summarise an important aspect of the dataset.

---

# 28. Final Workflow

**Understand Data**

→ **Check Quality**

→ **Clean Data**

→ **Validate**

→ **Calculate Risk**

→ **Analyse Risk**

→ **Analyse Loans**

→ **Analyse Customers**

→ **Analyse Monthly Trends**

→ **Calculate KPIs**

→ **Create Pivot Analysis**

→ **Visualise**

→ **Write Insights**

---

# 🔑 Key Takeaway

**Credit Risk Analysis uses customer, financial and loan data to understand credit exposure, risk categories and loan outcomes. Clean data, consistent risk rules, useful KPIs and clear visualisation are the foundation of the Day 098 analysis.**

---

## 🚀 Day 098 — Quick Revision Complete

**Credit Risk Analysis → Data Cleaning → Risk Classification → Loan Analysis → Customer Analysis → KPI → Visualisation → Business Insights**