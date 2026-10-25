# 📘 Day 098 — Credit Risk Analysis — Notes

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-Day%20098-blue?style=for-the-badge)
![Credit Risk Analysis](https://img.shields.io/badge/Credit%20Risk-Analysis-green?style=for-the-badge)
![Excel](https://img.shields.io/badge/Excel-Analytics-orange?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 098
- **Topic:** Credit Risk Analysis

---

# 1. Introduction to Credit Risk Analysis

Credit Risk Analysis is the process of studying customer and loan-related data to understand credit exposure, risk categories, loan status and default patterns.

Businesses and financial institutions can analyse information such as:

- Customer income
- Credit Score
- Loan Amount
- Existing Loans
- Debt-to-Income Ratio
- Interest Rate
- Loan Tenure
- Loan Status
- Risk Category

The objective of this analysis is to convert raw credit-related data into structured information that can support business analysis.

---

# 2. Credit Risk

Credit Risk refers to the possibility that a borrower may not meet the required repayment obligations associated with a loan.

Credit risk analysis therefore focuses on understanding the financial characteristics of borrowers and the characteristics of their loans.

Important variables include:

- Credit Score
- Monthly Income
- Loan Amount
- Debt-to-Income Ratio
- Existing Loans
- Loan Status

---

# 3. Credit Risk Analysis Workflow

A basic credit-risk analysis workflow is:

**Raw Data**

↓

**Data Inspection**

↓

**Data Quality Check**

↓

**Data Cleaning**

↓

**Data Validation**

↓

**Risk Classification**

↓

**Loan Analysis**

↓

**Customer Analysis**

↓

**Monthly Analysis**

↓

**KPI Analysis**

↓

**Visualisation**

↓

**Business Insights**

---

# 4. Credit Risk Dataset

The Day 098 workbook contains a synthetic credit-risk dataset created for learning and practice.

The main fields are:

| Field | Description |
|---|---|
| Customer_ID | Unique customer identifier |
| Loan_Date | Loan-related date |
| Age | Customer age |
| City | Customer location |
| Employment_Type | Employment category |
| Monthly_Income | Customer monthly income |
| Credit_Score | Credit score |
| Loan_Amount | Loan amount |
| Interest_Rate_% | Loan interest rate |
| Loan_Tenure_Months | Loan duration |
| Existing_Loans | Existing loan count |
| Debt_to_Income_Ratio_% | Debt-to-income ratio |
| Risk_Category | Calculated risk category |
| Loan_Status | Loan status |

---

# 5. Customer_ID

`Customer_ID` identifies a customer.

It is useful for:

- Identifying individual customers
- Checking duplicate records
- Customer-level analysis
- Linking customer-related information

A duplicate customer ID is not necessarily an error because a customer may have multiple loan records.

However, an exact duplicate row should be checked carefully.

---

# 6. Loan_Date

`Loan_Date` represents the date associated with the loan record.

It can be used for:

- Monthly analysis
- Time-based analysis
- Loan exposure trends
- Default trends
- Risk trends

The Day 098 dataset contains records across multiple dates in January 2026.

---

# 7. Age

`Age` represents the age of the customer.

Age can be used to understand the customer population.

For the cleaning exercise:

**Missing or invalid Age → Median valid Age**

The median is used as an educational missing-value treatment in this dataset.

---

# 8. City

The dataset contains customer cities such as:

- Patna
- Delhi
- Mumbai
- Bengaluru
- Kolkata

City can be used for additional descriptive analysis.

Before analysis, city names should be standardised.

Example:

` Patna `

becomes:

`Patna`

---

# 9. Employment Type

Employment type describes the customer's employment category.

The dataset contains:

- Salaried
- Self-Employed
- Business

Employment information can be useful when studying customer financial characteristics.

---

# 10. Monthly Income

`Monthly_Income` represents the customer's monthly income.

Income can be compared with:

- Loan Amount
- Credit Score
- Existing Loans
- DTI
- Risk Category

Missing or invalid income values need to be handled before analysis.

For this practice dataset:

**Missing or non-positive income → Median valid income**

---

# 11. Credit Score

`Credit_Score` is a numerical credit-related variable.

For this educational dataset, the valid credit-score range is:

**300 to 850**

Credit Score is one of the variables used to calculate the practice `Risk_Category`.

---

# 12. Credit Score Cleaning

During cleaning:

1. Convert Credit Score to numeric.
2. Identify invalid values.
3. Identify missing values.
4. Keep values within the valid range.
5. Replace missing or invalid values using the median valid score.

This produces a cleaner field for subsequent analysis.

---

# 13. Loan Amount

`Loan_Amount` represents the amount associated with the loan.

Loan Amount is important for measuring:

- Total loan exposure
- Average loan size
- Loan exposure by risk category
- Loan exposure by status
- Monthly loan exposure

Negative loan amounts are invalid.

For this practice dataset:

**Missing or negative Loan Amount → Median valid Loan Amount**

---

# 14. Interest Rate

`Interest_Rate_%` represents the interest rate associated with a loan.

The field can be analysed by:

- Risk Category
- Loan Status
- Loan records

For the cleaning exercise, valid interest rates are considered greater than 0 and less than or equal to 30%.

Invalid or missing values are replaced using the median valid interest rate.

---

# 15. Loan Tenure

`Loan_Tenure_Months` represents the duration of a loan in months.

Examples include:

- 12 months
- 24 months
- 36 months
- 48 months
- 60 months

Loan tenure should be positive.

For this project:

**Invalid or missing tenure → Median valid tenure**

---

# 16. Existing Loans

`Existing_Loans` represents the number of existing loans associated with the customer.

A negative number is not valid.

Cleaning rule:

**Negative or missing Existing Loans → 0**

This allows the field to be used safely in subsequent analysis.

---

# 17. Debt-to-Income Ratio

`Debt_to_Income_Ratio_%` represents the Debt-to-Income Ratio.

DTI is used in this educational project as one of the inputs for risk categorisation.

The practice validation range is:

**0% to 100%**

Invalid or missing DTI values are replaced with the median valid DTI.

---

# 18. Risk Category

The cleaned dataset contains four risk categories:

- Low
- Medium
- High
- Very High

The risk category is calculated using:

**Credit Score + Debt-to-Income Ratio**

---

# 19. Risk Categorisation Rules

The Day 098 practice dataset uses the following rules.

### Low

Credit Score ≥ 740

and

DTI < 30%

### Medium

Credit Score ≥ 680

and

DTI < 40%

### High

Credit Score ≥ 620

and

DTI < 50%

### Very High

Other combinations that do not satisfy the above conditions.

These rules are specifically defined for this educational dataset.

---

# 20. Why Recalculate Risk Category?

The raw dataset contains deliberately inconsistent risk labels.

Therefore, relying directly on the raw `Risk_Category` column could produce inconsistent analysis.

Instead:

**Clean Credit Score**

+

**Clean DTI**

↓

**Recalculate Risk Category**

This makes the risk classification consistent with the project's defined rules.

---

# 21. Loan Status

The dataset contains four loan statuses:

- Approved
- Active
- Closed
- Defaulted

Loan Status can be used to understand the distribution of loan records.

---

# 22. Defaulted Loans

A record with:

**Loan_Status = Defaulted**

is treated as a default record in this educational project.

Default Count can be calculated using:

**COUNTIF**

or equivalent Pandas filtering.

---

# 23. Default Rate

Default Rate measures the proportion of records classified as defaulted.

### Formula

**Default Rate (%) =**

**Defaulted Loans / Total Customers × 100**

The denominator used here follows the structure of the Day 098 workbook.

---

# 24. Total Loan Exposure

Total Loan Exposure represents the total loan amount present in the cleaned dataset.

### Formula

**Total Loan Exposure = SUM(Loan_Amount)**

This metric gives a high-level view of the loan amount represented in the dataset.

---

# 25. Average Loan Amount

Average Loan Amount measures the average size of loans.

### Formula

**Average Loan Amount =**

**Total Loan Amount / Number of Loan Records**

In Excel:

`=AVERAGE(Loan_Amount_Range)`

---

# 26. Average Credit Score

Average Credit Score provides the mean credit score across the cleaned customer records.

### Formula

**Average Credit Score =**

**Total Credit Score / Number of Customers**

Excel:

`=AVERAGE(Credit_Score_Range)`

---

# 27. Average Monthly Income

Average Monthly Income represents the average monthly income of customers.

### Formula

**Average Monthly Income =**

**Total Monthly Income / Number of Customers**

Excel:

`=AVERAGE(Monthly_Income_Range)`

---

# 28. Average DTI

Average DTI represents the average Debt-to-Income Ratio.

### Formula

**Average DTI =**

**Total DTI / Number of Customers**

Excel:

`=AVERAGE(DTI_Range)`

---

# 29. High / Very High Risk Customers

The project combines:

- High
- Very High

into one KPI.

### Formula

**High / Very High Risk Customers =**

**High Risk Customers + Very High Risk Customers**

This provides a combined count of customers classified into the two higher-risk categories under the project's rules.

---

# 30. High / Very High Risk Rate

### Formula

**High / Very High Risk Rate (%) =**

**(High Risk + Very High Risk) / Total Customers × 100**

This is a descriptive KPI based on the project's risk classification.

---

# 31. Data Quality

Data quality should be checked before performing credit-risk analysis.

Poor-quality data can affect:

- Risk classification
- Loan exposure
- Default rate
- Credit Score averages
- DTI averages
- KPI calculations

---

# 32. Deliberate Data Issues

The raw Day 098 dataset contains practice issues such as:

- Extra spaces
- Inconsistent capitalization
- Missing Monthly Income
- Invalid Credit Score
- Negative Loan Amount
- Missing Interest Rate
- Invalid Loan Tenure
- Negative Existing Loans
- Invalid DTI
- Inconsistent Risk Category
- Inconsistent Loan Status
- Missing Age
- Invalid numeric values
- Duplicate row

These issues are intentionally included for data-cleaning practice.

---

# 33. Text Cleaning

Text fields should be standardised before grouping.

Common operations include:

- Removing leading spaces
- Removing trailing spaces
- Standardising capitalization
- Standardising category labels

Example:

` high `

becomes:

`High`

Example:

` defaulted `

becomes:

`Defaulted`

---

# 34. Numeric Cleaning

Numeric fields should be converted to numeric data types before analysis.

Important numeric fields include:

- Age
- Monthly Income
- Credit Score
- Loan Amount
- Interest Rate
- Loan Tenure
- Existing Loans
- DTI

Invalid text such as:

`N/A`

should not remain in numeric columns.

---

# 35. Missing Value Handling

Missing values should be identified before analysis.

The Day 098 cleaning rules include:

| Field | Cleaning Rule |
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

# 36. Duplicate Removal

Exact duplicate rows can distort analysis.

Duplicates may increase:

- Customer count
- Loan exposure
- Default count
- Risk counts

Therefore, exact duplicate rows are removed during cleaning.

---

# 37. Data Validation

After cleaning, validation should be performed.

Examples:

### Age

Check for missing or invalid values.

### Credit Score

Check:

**300 ≤ Credit Score ≤ 850**

### Loan Amount

Check:

**Loan Amount ≥ 0**

### Interest Rate

Check:

**0 < Interest Rate ≤ 30**

### Loan Tenure

Check:

**Loan Tenure > 0**

### Existing Loans

Check:

**Existing Loans ≥ 0**

### DTI

Check:

**0 ≤ DTI ≤ 100**

---

# 38. Credit Risk Summary

The `Credit_Risk_Summary` sheet provides high-level metrics.

Main metrics include:

- Total Customers
- Total Loan Amount
- Average Credit Score
- Average Monthly Income
- Average Debt-to-Income Ratio
- High / Very High Risk Customers
- Active Loans
- Defaulted Loans
- Default Rate

This sheet provides a quick overview of the dataset.

---

# 39. Risk Category Analysis

The `Risk_Category_Analysis` sheet compares risk categories.

Metrics include:

- Customers
- Total Loan Amount
- Average Credit Score
- Average Income
- Average DTI
- Default Count
- Default Rate

This allows descriptive comparison across risk groups without relying on a single metric.

---

# 40. Loan Analysis

The `Loan_Analysis` sheet analyses loan records by status.

Metrics include:

- Customers
- Total Loan Amount
- Average Loan Amount
- Average Interest Rate
- Average Tenure

Loan status categories are:

- Approved
- Active
- Closed
- Defaulted

---

# 41. Customer Analysis

The `Customer_Analysis` sheet provides a detailed customer-level view.

Important fields include:

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

# 42. Monthly Credit Risk Analysis

The `Monthly_Credit_Risk` sheet provides time-based analysis.

Metrics include:

- Month
- Customers
- Total Loan Amount
- Average Credit Score
- Average DTI
- High / Very High Risk Customers
- Default Count

Monthly analysis helps organise credit-risk information over time.

---

# 43. Credit Risk KPIs

The `Credit_Risk_KPI` sheet contains the major project KPIs.

These include:

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

# 44. Pivot Risk Analysis

The `Pivot_Risk` sheet provides a pivot-style summary by Risk Category.

Main fields:

- Risk Category
- Customers
- Loan Amount
- Default Count

This structure allows quick comparison of risk groups.

---

# 45. Pivot Loan Status Analysis

The `Pivot_Loan_Status` sheet provides a pivot-style summary by Loan Status.

Main fields:

- Loan Status
- Customers
- Loan Amount
- Average Credit Score

This provides another structured view of the credit dataset.

---

# 46. Credit Risk Charts

The workbook includes three main visualisations.

### 1. Customers by Risk Category

Shows the number of customers in each risk category.

### 2. Loan Amount by Risk Category

Shows loan exposure associated with each risk category.

### 3. Monthly Loan Exposure Trend

Shows the loan amount pattern across months.

---

# 47. Reading a Risk Category Chart

When reviewing a risk-category chart, examine:

- Number of customers
- Loan exposure
- Distribution across categories

Do not rely on only one chart.

For example, a category with fewer customers may still represent a meaningful amount of loan exposure.

---

# 48. Reading Loan Exposure

Loan exposure should be considered separately from customer count.

Two risk categories may have:

- Different customer counts
- Different average loan amounts
- Different total loan exposure

Therefore, customer count alone does not describe the entire loan portfolio represented by the dataset.

---

# 49. Reading Default Rate

Default Rate should be interpreted together with:

- Default Count
- Customer Count
- Loan Amount
- Risk Category

A rate without its underlying count may not provide enough context.

---

# 50. Excel Functions for Credit Risk Analysis

Useful functions include:

- `SUM()`
- `AVERAGE()`
- `COUNT()`
- `COUNTA()`
- `COUNTIF()`
- `COUNTIFS()`
- `SUMIF()`
- `SUMIFS()`
- `AVERAGEIF()`
- `AVERAGEIFS()`
- `IF()`
- `IFERROR()`
- `TRIM()`
- `PROPER()`
- `UPPER()`
- `LOWER()`

---

# 51. Example Excel Formulas

### Total Loan Amount

`=SUM(H2:H81)`

### Average Credit Score

`=AVERAGE(G2:G81)`

### Average Monthly Income

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

# 52. Conditional Risk Classification in Excel

A nested `IF()` structure can be used to implement the project's risk rules.

Conceptually:

**Credit Score + DTI**

↓

Check Low condition

↓

Check Medium condition

↓

Check High condition

↓

Otherwise Very High

The exact formula should follow the rules defined for the Day 098 workbook.

---

# 53. Python for Credit Risk Analysis

Python can automate the analysis workflow.

The main libraries are:

### Pandas

Useful for:

- Reading Excel
- Cleaning data
- Grouping data
- Aggregating metrics
- Exporting CSV files

### NumPy

Useful for:

- Conditional calculations
- Numerical operations
- Risk classification

### Matplotlib

Useful for:

- Risk charts
- Loan exposure charts
- Monthly trend charts

---

# 54. Python Workflow

A typical Python workflow is:

**Import Libraries**

↓

**Locate Workbook**

↓

**Read Raw Data**

↓

**Inspect Data**

↓

**Clean Data**

↓

**Validate Data**

↓

**Calculate Risk Category**

↓

**Create Summaries**

↓

**Calculate KPIs**

↓

**Create Charts**

↓

**Export Outputs**

---

# 55. Groupby Analysis

Pandas `groupby()` can be used to analyse credit risk.

Examples:

- Group by Risk Category
- Group by Loan Status
- Group by City
- Group by Employment Type
- Group by Month

Conceptually:

**Risk Category → Aggregate Metrics**

This is similar to a Pivot Table in Excel.

---

# 56. Risk Category Analysis Using Pandas

A typical analysis can calculate:

- Customer count
- Total loan amount
- Average credit score
- Average income
- Average DTI
- Default count

This creates a structured risk-category summary.

---

# 57. Monthly Analysis Using Pandas

Monthly analysis generally involves:

1. Converting Loan Date to datetime.
2. Extracting the month.
3. Grouping records by month.
4. Calculating required metrics.

Possible metrics include:

- Customer count
- Loan amount
- Average Credit Score
- Average DTI
- High/Very High risk count
- Default count

---

# 58. Business Questions

Credit Risk Analysis can answer descriptive questions such as:

1. How many customers are in each risk category?
2. What is the total loan exposure?
3. What is the average credit score?
4. What is the average monthly income?
5. What is the average DTI?
6. How many customers are classified as High or Very High risk?
7. What is the default count?
8. What is the default rate?
9. How much loan exposure belongs to each risk category?
10. What is the average loan amount?
11. What is the average interest rate?
12. What is the average loan tenure?
13. How does loan exposure vary by loan status?
14. How does credit score vary across risk categories?
15. How does DTI vary across risk categories?
16. How does loan exposure change over time?

---

# 59. Business Insight Framework

A useful business insight should contain:

**Observation**

→ What does the data show?

**Metric**

→ Which number supports the observation?

**Context**

→ Which group, period or category is being analysed?

**Business Meaning**

→ What does the observation mean within the dataset?

Example structure:

**Observation:** A particular risk category contains a certain share of customers.

**Metric:** Customer count and percentage.

**Context:** Risk Category Analysis.

**Business Meaning:** This describes the distribution of customers across the defined risk categories.

---

# 60. Important Interpretation Rule

Credit-risk analysis should not be interpreted using only one variable.

For example:

**Credit Score alone**

is not enough to describe the complete customer profile.

Other variables include:

- Income
- Loan Amount
- DTI
- Existing Loans
- Loan Status

A structured analysis considers multiple relevant fields.

---

# 61. Limitations of the Day 098 Project

This project is designed for educational practice.

Important limitations include:

- The dataset is synthetic.
- The dataset is relatively small.
- Data-quality issues were intentionally introduced.
- Risk rules are simplified.
- The dataset does not represent an actual lending portfolio.
- The analysis is descriptive.
- The risk categories are based on the rules defined for this exercise.
- The results should not be treated as a real-world credit decision system.

---

# 62. Real-World Credit Risk Analysis

A real-world credit-risk system may involve additional data and modelling techniques.

Examples can include:

- Historical repayment behaviour
- Credit history
- Income verification
- Existing debt
- Loan performance
- Customer behaviour
- Statistical modelling
- Machine learning
- Model validation
- Risk governance

These areas go beyond the simplified Day 098 educational project.

---

# 63. Day 098 Workbook Structure

The workbook contains the following sheets:

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

# 64. Recommended Study Order

For Day 098, follow this order:

### Step 1
Read the raw dataset.

### Step 2
Understand every column.

### Step 3
Review the Data Quality Check sheet.

### Step 4
Study the cleaning rules.

### Step 5
Review the cleaned dataset.

### Step 6
Study Risk Category Analysis.

### Step 7
Study Loan Analysis.

### Step 8
Study Customer Analysis.

### Step 9
Study Monthly Credit Risk.

### Step 10
Review Credit Risk KPIs.

### Step 11
Study Pivot-style summaries.

### Step 12
Review charts.

### Step 13
Write business observations.

### Step 14
Repeat the analysis using Python.

---

# 65. Revision Questions

### Basic

1. What is Credit Risk?
2. What is Credit Risk Analysis?
3. What is a Credit Score?
4. What is Loan Amount?
5. What is DTI?
6. What is Loan Tenure?
7. What is Loan Status?
8. What is Default?
9. What is Risk Category?
10. Why is data cleaning important?

### Intermediate

11. How is Total Loan Exposure calculated?
12. How is Default Rate calculated?
13. Why are duplicate records removed?
14. Why should Credit Score be validated?
15. Why should DTI be validated?
16. Why should Loan Amount not be negative?
17. Why is Risk Category recalculated?
18. What is the purpose of Pivot-style analysis?
19. Why is monthly analysis useful?
20. Why should multiple metrics be analysed together?

### Practical

21. Calculate total loan exposure.
22. Calculate average credit score.
23. Calculate average monthly income.
24. Calculate average DTI.
25. Count High-risk customers.
26. Count Very High-risk customers.
27. Calculate High/Very High risk rate.
28. Count defaulted loans.
29. Calculate default rate.
30. Compare loan exposure across risk categories.

---

# 66. Key Learning Points

- Credit Risk Analysis studies customer and loan-related data.
- Credit Score and DTI are important variables in this practice dataset.
- Loan Amount can be used to measure loan exposure.
- Loan Status helps organise loan records.
- Risk Category is calculated using defined rules.
- Data cleaning should happen before analysis.
- Missing and invalid values must be handled carefully.
- Duplicate records can distort KPIs.
- Risk analysis should include several metrics.
- Pivot-style summaries help organise grouped information.
- Charts help communicate patterns.
- Monthly analysis adds a time dimension.
- Python can automate the same workflow performed in Excel.
- Synthetic educational results should not be treated as real-world lending decisions.

---

# 67. Final Summary

Credit Risk Analysis converts customer and loan information into structured risk-related analysis.

The complete process is:

**Data Understanding**

→ **Data Quality**

→ **Data Cleaning**

→ **Validation**

→ **Risk Classification**

→ **Loan Analysis**

→ **Customer Analysis**

→ **Monthly Analysis**

→ **KPI Analysis**

→ **Pivot Analysis**

→ **Visualisation**

→ **Business Insights**

The main learning objective is to understand how business data can be cleaned, organised and analysed to study credit-risk patterns.

---

# 🔑 Key Takeaway

**Credit Risk Analysis combines customer, financial and loan information to study credit exposure, risk categories and loan outcomes. Reliable analysis depends on clean data, clearly defined rules, appropriate KPIs and careful interpretation.**

---

## 🚀 Day 098 Complete

**Business Data Management — Credit Risk Analysis**