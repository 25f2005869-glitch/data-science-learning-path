# 📚 Day 098 — Credit Risk Analysis — Resources

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-Day%20098-blue?style=for-the-badge)
![Credit Risk](https://img.shields.io/badge/Credit%20Risk-Resources-green?style=for-the-badge)
![Excel](https://img.shields.io/badge/Excel-Analytics-orange?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 098
- **Topic:** Credit Risk Analysis

---

# 1. Resource Guide

Day 098 focuses on analysing customer and loan data to understand:

- Credit Risk
- Credit Score
- Loan Amount
- Monthly Income
- Debt-to-Income Ratio
- Loan Status
- Risk Category
- Default Rate
- Loan Exposure
- Credit Risk KPIs
- Business Insights

The resources below are organised in the same learning sequence as the project.

---

# 2. Credit Risk Fundamentals

Before working with the workbook, understand these concepts:

- Credit Risk
- Credit Risk Analysis
- Credit Score
- Loan Amount
- Interest Rate
- Loan Tenure
- Existing Loans
- Debt-to-Income Ratio
- Default
- Loan Status
- Risk Category
- Loan Exposure

### Study Focus

Understand what each term means and how it is represented in the dataset.

---

# 3. Credit Risk Dataset

Use the Day 098 workbook as the primary practice resource.

### Main workbook

`Day_098_Credit_Risk_Analysis.xlsx`

### Important sheets

- `Raw_Credit_Risk_Data`
- `Data_Quality_Check`
- `Credit_Risk_Cleaning`
- `Cleaned_Credit_Risk_Data`
- `Credit_Risk_Summary`
- `Risk_Category_Analysis`
- `Loan_Analysis`
- `Customer_Analysis`
- `Monthly_Credit_Risk`
- `Credit_Risk_KPI`
- `Pivot_Risk`
- `Pivot_Loan_Status`
- `Charts`
- `Credit_Risk_Insights`
- `Final_Credit_Risk_Analysis`

---

# 4. Data Cleaning Resources

Focus on:

- Missing values
- Invalid values
- Duplicate records
- Text standardisation
- Numeric conversion
- Date conversion
- Validation
- Recalculation of derived fields

### Important Excel Functions

- `TRIM()`
- `PROPER()`
- `UPPER()`
- `LOWER()`
- `IF()`
- `IFERROR()`

### Practice

Take the raw dataset and identify every deliberately introduced data-quality issue before looking at the cleaned dataset.

---

# 5. Credit Score Resources

Study:

- Meaning of Credit Score
- Credit-score ranges
- Credit-score validation
- Use of Credit Score in risk analysis

For Day 098 practice:

**Valid Credit Score Range = 300–850**

The project uses Credit Score as one input for Risk Category classification.

---

# 6. Debt-to-Income Ratio Resources

Study:

- Meaning of DTI
- DTI percentage
- DTI validation
- DTI in risk analysis

For this project:

**Valid DTI Range = 0%–100%**

DTI is combined with Credit Score for the educational risk-classification rules.

---

# 7. Risk Classification Resources

Review the Day 098 risk rules:

### Low

Credit Score ≥ 740 and DTI < 30%

### Medium

Credit Score ≥ 680 and DTI < 40%

### High

Credit Score ≥ 620 and DTI < 50%

### Very High

Other combinations

> These rules are specific to the Day 098 practice dataset.

---

# 8. Loan Analysis Resources

Study these concepts:

- Loan Amount
- Average Loan Amount
- Interest Rate
- Loan Tenure
- Loan Status
- Total Loan Exposure

### Questions to Practise

- How much loan exposure is present?
- How does loan exposure vary by Loan Status?
- What is the average loan amount?
- What is the average interest rate?
- What is the average loan tenure?

---

# 9. Default Analysis Resources

Focus on:

- Defaulted Loans
- Default Count
- Default Rate
- Default analysis by Risk Category
- Default analysis by Loan Status

### Formula

**Default Rate (%) =**

**Default Count / Total Customers × 100**

For this educational project, follow the denominator used in the workbook.

---

# 10. Customer Analysis Resources

Study customer-level analysis using:

- Customer ID
- Age
- City
- Employment Type
- Monthly Income
- Credit Score
- Existing Loans
- DTI
- Risk Category
- Loan Status

Possible analysis dimensions:

- City
- Employment Type
- Risk Category
- Loan Status

---

# 11. Monthly Analysis Resources

Study time-based analysis using:

- Loan Date
- Month
- Customer Count
- Loan Amount
- Average Credit Score
- Average DTI
- High/Very High Risk Count
- Default Count

### Practice

Create a monthly summary and a line chart showing loan exposure over time.

---

# 12. Excel Resources

Important Excel topics for Day 098:

### Basic Functions

- `SUM`
- `AVERAGE`
- `COUNT`
- `COUNTA`

### Conditional Functions

- `COUNTIF`
- `COUNTIFS`
- `SUMIF`
- `SUMIFS`
- `AVERAGEIF`
- `AVERAGEIFS`

### Logical Functions

- `IF`
- `IFERROR`

### Text Functions

- `TRIM`
- `PROPER`
- `UPPER`
- `LOWER`

---

# 13. Excel Pivot Table Resources

Practise creating Pivot Tables using:

### Risk Category

Rows:

`Risk_Category`

Values:

- Customer Count
- Loan Amount
- Default Count

### Loan Status

Rows:

`Loan_Status`

Values:

- Customer Count
- Loan Amount
- Average Credit Score

---

# 14. Excel Chart Resources

Practise these charts:

### Customers by Risk Category

Recommended chart:

**Column Chart**

### Loan Amount by Risk Category

Recommended chart:

**Bar/Column Chart**

### Monthly Loan Exposure

Recommended chart:

**Line Chart**

---

# 15. Excel Dashboard Practice

Create a simple credit-risk dashboard containing:

### KPI Cards

- Total Customers
- Total Loan Exposure
- Average Credit Score
- Average DTI
- Default Rate

### Charts

- Customers by Risk Category
- Loan Amount by Risk Category
- Monthly Loan Exposure Trend

### Insight Section

Write 3–5 observations from the data.

---

# 16. Python — Pandas Resources

Use Pandas for:

- Excel reading
- Data inspection
- Data cleaning
- Missing-value handling
- Duplicate removal
- Grouping
- Aggregation
- KPI calculation
- CSV export

Important methods:

- `pd.read_excel()`
- `.head()`
- `.info()`
- `.describe()`
- `.isna()`
- `.duplicated()`
- `.drop_duplicates()`
- `.groupby()`
- `.agg()`
- `.to_csv()`

---

# 17. Python — NumPy Resources

Use NumPy for:

- Conditional logic
- Numerical calculations
- Data transformations

Useful concepts:

- `np.where()`
- Numeric arrays
- Conditional calculations
- Missing-value handling

---

# 18. Python — Matplotlib Resources

Use Matplotlib for:

- Risk distribution
- Loan exposure charts
- Monthly trend charts

Practice creating:

- Bar charts
- Column charts
- Line charts

---

# 19. Python Analysis Practice

Follow this sequence:

**Load Excel**

↓

**Inspect Data**

↓

**Clean Data**

↓

**Validate Data**

↓

**Recalculate Risk**

↓

**Group by Risk**

↓

**Group by Loan Status**

↓

**Calculate Monthly Metrics**

↓

**Calculate KPIs**

↓

**Create Charts**

↓

**Export CSV Files**

---

# 20. Business Analytics Resources

Focus on converting numbers into structured business observations.

Study:

- KPI analysis
- Category comparison
- Trend analysis
- Exposure analysis
- Default analysis
- Risk distribution
- Business reporting

A useful structure is:

**Observation → Metric → Context → Business Meaning**

---

# 21. Data Visualisation Resources

When reviewing a chart, ask:

1. What is being measured?
2. Which categories are being compared?
3. What is the unit?
4. What period is covered?
5. Is the chart showing count, amount, rate or average?
6. What numerical value supports the observation?

---

# 22. Important Analysis Concepts

Revise these concepts from previous BDM work:

- Data Cleaning
- Data Validation
- Aggregation
- Groupby
- Pivot Tables
- KPIs
- Trend Analysis
- Category Analysis
- Business Insights
- Data Visualisation

Day 098 combines many of these earlier concepts into one credit-risk project.

---

# 23. Suggested Learning Platforms

### Microsoft Excel

Use Microsoft's official Excel learning resources for:

- Formulas
- Functions
- Pivot Tables
- Charts
- Data analysis

### Python

Use official Python documentation for Python fundamentals.

### Pandas

Use Pandas documentation for:

- DataFrames
- Reading Excel
- Cleaning
- Groupby
- Aggregation

### NumPy

Use NumPy documentation for numerical operations and conditional calculations.

### Matplotlib

Use Matplotlib documentation for charts and visualisation.

---

# 24. Recommended Search Topics

When searching for additional learning material, use focused topics such as:

- `credit risk analysis basics`
- `credit score explained`
- `debt to income ratio explained`
- `loan portfolio analysis`
- `default rate calculation`
- `Excel credit risk analysis`
- `Excel COUNTIFS SUMIFS`
- `Excel Pivot Table analysis`
- `Pandas groupby aggregation`
- `Pandas read Excel`
- `Matplotlib bar chart`
- `Matplotlib line chart`

---

# 25. Practice Resources

Use the following Day 098 files together:

### Notes

`notes.md`

Use for detailed concept learning.

### Cheat Sheet

`cheat-sheet.md`

Use for quick revision.

### Practice

`practice.md`

Use for questions and hands-on exercises.

### Workbook

`Day_098_Credit_Risk_Analysis.xlsx`

Use for Excel-based analysis.

### Python Code

`code/credit_risk_analysis.py`

Use for Python implementation.

---

# 26. Recommended Study Sequence

### First

Read:

`notes.md`

### Second

Open:

`Day_098_Credit_Risk_Analysis.xlsx`

### Third

Study:

`Raw_Credit_Risk_Data`

### Fourth

Review:

`Data_Quality_Check`

### Fifth

Study:

`Credit_Risk_Cleaning`

### Sixth

Review:

`Cleaned_Credit_Risk_Data`

### Seventh

Study:

`Risk_Category_Analysis`

### Eighth

Study:

`Loan_Analysis`

### Ninth

Study:

`Customer_Analysis`

### Tenth

Study:

`Monthly_Credit_Risk`

### Eleventh

Review:

`Credit_Risk_KPI`

### Twelfth

Review:

`Charts`

### Thirteenth

Write:

`Credit_Risk_Insights`

### Fourteenth

Repeat the workflow using Python.

---

# 27. Resource-Based Practice Questions

1. What is Credit Risk?
2. What is a Credit Score?
3. What is DTI?
4. What is Loan Exposure?
5. How is Default Rate calculated?
6. How is Risk Category calculated in this project?
7. Why is data cleaning necessary?
8. Why are duplicate records removed?
9. How can Excel calculate Default Count?
10. How can Pandas group customers by Risk Category?
11. How can monthly loan exposure be visualised?
12. Why should customer count and loan exposure be analysed separately?

---

# 28. Final Revision Checklist

## Concepts

- [ ] Credit Risk
- [ ] Credit Score
- [ ] Loan Amount
- [ ] Interest Rate
- [ ] Loan Tenure
- [ ] Existing Loans
- [ ] DTI
- [ ] Risk Category
- [ ] Loan Status
- [ ] Default Rate

## Excel

- [ ] SUM
- [ ] AVERAGE
- [ ] COUNTIF
- [ ] COUNTIFS
- [ ] SUMIF
- [ ] SUMIFS
- [ ] AVERAGEIF
- [ ] IF
- [ ] TRIM
- [ ] Pivot Tables
- [ ] Charts

## Python

- [ ] Pandas
- [ ] NumPy
- [ ] Matplotlib
- [ ] read_excel
- [ ] Data cleaning
- [ ] groupby
- [ ] aggregation
- [ ] CSV export
- [ ] chart creation

## Analysis

- [ ] Risk Category Analysis
- [ ] Loan Analysis
- [ ] Customer Analysis
- [ ] Monthly Analysis
- [ ] KPI Analysis
- [ ] Pivot Analysis
- [ ] Visualisation
- [ ] Business Insights

---

# 29. Day 098 Resource Map

**Credit Risk Fundamentals**

→ **Dataset Understanding**

→ **Data Quality**

→ **Data Cleaning**

→ **Credit Score + DTI**

→ **Risk Classification**

→ **Loan Analysis**

→ **Customer Analysis**

→ **Monthly Analysis**

→ **KPIs**

→ **Pivot Tables**

→ **Charts**

→ **Business Insights**

→ **Python Automation**

---

# 🔑 Final Takeaway

The most useful resources for Day 098 are not only credit-risk concepts. The main goal is to combine previously learned Business Data Management skills:

**Excel + Data Cleaning + Pivot Tables + KPIs + Visualisation + Python + Business Analysis**

The Day 098 workbook should be treated as the primary hands-on practice resource, while the notes, cheat sheet, practice questions and Python code support the same analysis workflow.

---

## 🚀 Day 098 — Resources Complete

**Credit Risk Analysis → Data Cleaning → Risk Classification → Loan Analysis → KPI → Visualisation → Business Insights**