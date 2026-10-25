# 📊 Day 098 — Credit Risk Analysis

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-Day%20098-blue?style=for-the-badge)
![Credit Risk](https://img.shields.io/badge/Topic-Credit%20Risk%20Analysis-green?style=for-the-badge)
![Excel](https://img.shields.io/badge/Tool-Microsoft%20Excel-orange?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 098
- **Topic:** Credit Risk Analysis

---

## 📌 Overview

Day 098 focuses on **Credit Risk Analysis**.

Credit risk analysis involves studying customer and loan information to understand patterns related to:

- Credit Score
- Income
- Loan Amount
- Interest Rate
- Loan Tenure
- Existing Loans
- Debt-to-Income Ratio
- Risk Category
- Loan Status

This project uses a **synthetic educational dataset** created for practising business data analysis.

The workflow covers data inspection, data cleaning, risk segmentation, loan analysis, customer analysis, monthly analysis, KPI calculation, visualisation and business insights.

---

## 🎯 Learning Objectives

By completing Day 098, you will learn how to:

- Understand the basic concept of credit risk.
- Understand a credit-risk dataset.
- Identify important credit-risk variables.
- Inspect credit-risk data.
- Identify data-quality issues.
- Clean and validate credit-risk data.
- Analyse customers by risk category.
- Analyse loan amounts and loan status.
- Analyse credit scores and income.
- Analyse Debt-to-Income Ratio.
- Study monthly credit-risk trends.
- Calculate credit-risk KPIs.
- Create Pivot-style summaries.
- Create credit-risk charts.
- Extract business insights.
- Connect Excel analysis with Python.

---

## 📚 Topics Covered

### 1. Credit Risk Fundamentals

- Credit Risk
- Credit Risk Analysis
- Customer Credit Profile
- Loan Exposure
- Credit Score
- Debt-to-Income Ratio
- Risk Category
- Loan Status

### 2. Customer Information

The dataset contains customer-level information such as:

- Customer ID
- Age
- City
- Employment Type
- Monthly Income

### 3. Loan Information

Loan-related fields include:

- Loan Date
- Loan Amount
- Interest Rate
- Loan Tenure
- Existing Loans
- Loan Status

### 4. Credit Information

Important credit variables include:

- Credit Score
- Debt-to-Income Ratio
- Risk Category

---

## 📊 Risk Categories

The project uses four risk categories:

- **Low**
- **Medium**
- **High**
- **Very High**

Risk categories are recalculated using the cleaned **Credit Score** and **Debt-to-Income Ratio** values.

---

## 🏦 Loan Status

The dataset contains:

- Approved
- Active
- Closed
- Defaulted

Loan status is used for loan-level analysis and default analysis.

---

## 🧮 Important Metrics

### Total Loan Exposure

Total amount of loans represented in the dataset.

**Formula:**

Total Loan Exposure = Sum of Loan Amount

### Average Credit Score

**Formula:**

Average Credit Score = Sum of Credit Scores / Number of Customers

### Average Monthly Income

**Formula:**

Average Monthly Income = Sum of Monthly Income / Number of Customers

### Average Debt-to-Income Ratio

**Formula:**

Average DTI = Sum of DTI Ratios / Number of Customers

### Default Rate

**Formula:**

Default Rate = (Defaulted Loans / Total Customers) × 100

### High / Very High Risk Rate

**Formula:**

High / Very High Risk Rate =  
(High + Very High Risk Customers / Total Customers) × 100

---

## 🧹 Data Quality

The raw dataset contains deliberately introduced practice issues such as:

- Extra spaces
- Inconsistent capitalization
- Missing income
- Invalid credit score
- Negative loan amount
- Missing interest rate
- Invalid loan tenure
- Negative existing loans
- Invalid Debt-to-Income Ratio
- Inconsistent risk category
- Inconsistent loan status
- Missing age
- Invalid numeric values
- Duplicate records

---

## 🧼 Data Cleaning Workflow

The cleaning process follows:

**Inspect**

↓

**Identify Issues**

↓

**Clean**

↓

**Validate**

↓

**Analyse**

Important cleaning activities include:

- Removing unnecessary spaces.
- Standardising text values.
- Converting numeric fields.
- Handling missing income.
- Handling invalid credit scores.
- Handling missing or negative loan amounts.
- Handling invalid interest rates.
- Handling invalid loan tenure.
- Correcting negative existing-loan counts.
- Handling invalid DTI values.
- Recalculating risk category.
- Standardising loan status.
- Removing exact duplicates.

---

## 📈 Risk Category Analysis

The `Risk_Category_Analysis` sheet contains:

- Risk Category
- Customers
- Total Loan Amount
- Average Credit Score
- Average Income
- Average DTI
- Default Count
- Default Rate

This analysis helps examine how customer and loan characteristics vary across risk categories.

---

## 💰 Loan Analysis

The `Loan_Analysis` sheet contains:

- Loan Status
- Customers
- Total Loan Amount
- Average Loan Amount
- Average Interest Rate
- Average Tenure

This provides a structured view of loan exposure and loan status.

---

## 👤 Customer Analysis

The `Customer_Analysis` sheet contains customer-level information including:

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
- Debt-to-Income Ratio
- Risk Category
- Loan Status

---

## 📅 Monthly Credit Risk Analysis

The `Monthly_Credit_Risk` sheet provides monthly analysis of:

- Customers
- Total Loan Amount
- Average Credit Score
- Average DTI
- High / Very High Risk Customers
- Default Count

Monthly analysis helps examine changes in credit-risk-related metrics over time.

---

## 📊 Credit Risk KPIs

The `Credit_Risk_KPI` sheet contains:

- Total Customers
- Total Loan Exposure
- Average Credit Score
- Average Monthly Income
- Average DTI
- High / Very High Risk Rate
- Default Count
- Default Rate
- Active Loan Count

---

## 🔄 Pivot-Style Analysis

### Risk Analysis

The `Pivot_Risk` sheet summarises:

- Risk Category
- Customers
- Loan Amount
- Default Count

### Loan Status Analysis

The `Pivot_Loan_Status` sheet summarises:

- Loan Status
- Customers
- Loan Amount
- Average Credit Score

---

## 📈 Visualisation

The workbook includes charts for:

- Customers by Risk Category
- Loan Amount by Risk Category
- Monthly Loan Exposure Trend

Charts help communicate patterns in the credit-risk dataset.

---

## 💼 Business Questions

This project can be used to explore questions such as:

1. How many customers are in each risk category?
2. What is the total loan exposure?
3. What is the average credit score?
4. What is the average monthly income?
5. What is the average Debt-to-Income Ratio?
6. How much loan exposure exists in each risk category?
7. How does credit score vary across risk categories?
8. How does DTI vary across risk categories?
9. How many loans are defaulted?
10. What is the default rate?
11. How does loan amount vary by loan status?
12. What is the average interest rate?
13. How does loan exposure change over time?
14. How many high or very high risk customers are present?
15. What patterns can be observed from the available credit-risk metrics?

---

## 🐍 Python Connection

The same credit-risk workflow can be performed using Python.

Common tools include:

- Python
- Pandas
- NumPy
- Matplotlib

Python can be used for:

- Reading Excel data
- Data inspection
- Data cleaning
- Numeric validation
- Risk categorisation
- Grouped analysis
- KPI calculation
- Monthly analysis
- Visualisation
- CSV output generation

---

## 🛠️ Tools Used

- Microsoft Excel
- Python
- Pandas
- NumPy
- Matplotlib
- VS Code

---

## 📂 Workbook Structure

The Excel workbook contains 17 sheets:

1. **Instructions**
2. **Raw_Credit_Risk_Data**
3. **Data_Quality_Check**
4. **Credit_Risk_Cleaning**
5. **Cleaned_Credit_Risk_Data**
6. **Credit_Risk_Summary**
7. **Risk_Category_Analysis**
8. **Loan_Analysis**
9. **Customer_Analysis**
10. **Monthly_Credit_Risk**
11. **Credit_Risk_KPI**
12. **Pivot_Risk**
13. **Pivot_Loan_Status**
14. **Chart_Data**
15. **Charts**
16. **Credit_Risk_Insights**
17. **Final_Credit_Risk_Analysis**

---

## 📂 Project Structure

Day_098_Credit_Risk_Analysis/
│
├── README.md
├── notes.md
├── cheat-sheet.md
├── practice.md
├── resources.md
│
├── code/
│   └── credit_risk_analysis.py
│
├── data/
│   └── Day_098_Credit_Risk_Analysis.xlsx
│
└── outputs/
    ├── credit_risk_summary.csv
    ├── risk_category_analysis.csv
    ├── loan_analysis.csv
    ├── customer_analysis.csv
    ├── monthly_credit_risk_analysis.csv
    ├── credit_risk_kpi_summary.csv
    ├── risk_distribution.png
    ├── loan_amount_by_risk.png
    └── monthly_risk_trend.png

---

## 🔄 Complete Credit Risk Workflow

**Raw Credit Risk Data**

→ **Data Quality Check**

→ **Data Cleaning**

→ **Validation**

→ **Risk Segmentation**

→ **Loan Analysis**

→ **Customer Analysis**

→ **Monthly Analysis**

→ **KPI Analysis**

→ **Pivot-style Analysis**

→ **Visualisation**

→ **Business Insights**

→ **Final Credit Risk Analysis**

---

## ⚠️ Data Note

The dataset used in this project is **synthetic** and has been created specifically for educational practice.

The raw dataset contains intentionally introduced data-quality issues to provide practice with:

- Data inspection
- Data cleaning
- Data validation
- Risk classification
- Business analysis

The results should not be used to make actual lending or credit decisions.

---

## 🎓 Learning Outcome

After completing Day 098, you will have practical experience in taking credit-risk data from **raw records to cleaned data, risk segmentation, loan analysis, customer analysis, KPI analysis, visualisation and business reporting**.

---

## ✅ Day 098 Checklist

- [ ] Understand Credit Risk
- [ ] Understand the credit-risk dataset
- [ ] Understand Credit Score
- [ ] Understand Loan Amount
- [ ] Understand Interest Rate
- [ ] Understand Loan Tenure
- [ ] Understand Existing Loans
- [ ] Understand Debt-to-Income Ratio
- [ ] Understand Risk Categories
- [ ] Inspect raw data
- [ ] Identify data-quality issues
- [ ] Clean the dataset
- [ ] Validate the cleaned data
- [ ] Analyse risk categories
- [ ] Analyse loan status
- [ ] Analyse customers
- [ ] Analyse monthly trends
- [ ] Calculate credit-risk KPIs
- [ ] Create Pivot-style summaries
- [ ] Create charts
- [ ] Review business insights
- [ ] Complete final credit-risk analysis
- [ ] Connect the workflow with Python

---

## 🔑 Key Takeaway

**Credit Risk Analysis combines customer information, financial information, credit indicators and loan data to understand patterns in credit exposure and risk. Reliable analysis requires clean data, clear metrics, structured segmentation and careful interpretation of the available evidence.**

---

### 🚀 Day 098 Complete

**Business Data Management — Credit Risk Analysis**