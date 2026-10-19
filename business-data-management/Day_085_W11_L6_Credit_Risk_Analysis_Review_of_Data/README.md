![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-085-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📊 Day 085 — Credit Risk Analysis: Review of Data

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 085  
**Topic:** Credit Risk Analysis — Review of Data

## 🎯 Objective

- Review the structure of the credit-risk dataset.
- Check data completeness.
- Check identifier uniqueness.
- Review numeric variables.
- Review categorical variables.
- Inspect outcome fields.
- Prepare the dataset for deeper analysis.

## 🧩 Dataset Context

This project uses 30 synthetic customer-loan records.

The dataset is designed for educational practice in:

- Excel
- Python
- Business Data Management
- Credit-risk analysis
- Data-quality review

The dataset is not an official financial dataset.

It must not be used for real lending decisions.

## 🔎 What Is Data Review?

Data review is the process of understanding and checking data before performing advanced analysis.

A good review should answer:

1. What does one row represent?
2. Are important fields complete?
3. Are identifiers unique?
4. Are data types appropriate?
5. Are categories consistent?
6. Are numeric values reasonable?
7. What does the outcome distribution look like?
8. Is the dataset suitable for the next analytical step?

## 🗂️ Main Review Areas

| Area | Question |
|---|---|
| Structure | What does one row represent? |
| Completeness | Are values missing? |
| Uniqueness | Are IDs duplicated? |
| Numeric quality | Are numeric fields reasonable? |
| Categories | Are category labels consistent? |
| Outcomes | What are default and high-risk shares? |
| Exposure | What loan exposure is represented? |
| Modelling | Are target and feature definitions clear? |

## 📚 Workbook Structure

### Raw Dataset

`Credit_Risk_Data`

Contains the customer-loan observations.

### Quality Review

`Missing_Value_Review`

Checks field-level missing values.

`Duplicate_Check`

Checks duplicate records and identifiers.

### Numeric Review

`Numeric_Data_Review`

Contains descriptive statistics for important numeric fields.

### Category Review

`Category_Data_Review`

Shows category frequencies and shares.

### Risk Review

`Product_Risk_Review`

Summarises credit-risk indicators by loan product.

`Region_Risk_Review`

Summarises indicators by region.

`Employment_Risk_Review`

Summarises indicators by employment type.

### Outcome Review

`Outcome_Review`

Summarises default and high-risk outcomes.

### KPI Review

`Credit_Risk_KPIs`

Contains important headline metrics.

### Questions

`Review_Questions`

Contains questions for reviewing the dataset.

### Context

`Dataset_Context`

Explains the purpose and limitations.

### Framework

`Risk_Framework`

Connects major risk variables with their meaning.

### Dashboard

`Credit_Risk_Review_Dashboard`

Contains five prepared visualisations.

## 📊 Dashboard Charts

1. Default Rate by Loan Product
2. Average Credit Score by Region
3. Outcome Composition
4. Loan Exposure by Product
5. Credit Score vs Debt-to-Income

## 💳 Important Credit-Risk Fields

### Credit Score

`Credit_Score`

A numeric credit-history indicator in this educational dataset.

### Debt-to-Income

`Debt_to_Income_%`

Represents debt burden relative to income.

### Loan Amount

`Loan_Amount_Rupee`

Represents loan exposure.

### Monthly Income

`Monthly_Income_Rupee`

Represents monthly income.

### Tenure

`Tenure_Months`

Represents the repayment period.

### Past Delinquencies

`Past_Delinquencies`

Represents previous delinquency events.

### Default Flag

`Default_Flag`

Illustrative default outcome.

### High-Risk Flag

`High_Risk_Flag`

Prepared high-risk indicator.

## 🧮 Important Metrics

### Default Rate

`Default Rate = Defaults / Total Records × 100`

### High-Risk Share

`High-Risk Share = High-Risk Records / Total Records × 100`

### Category Share

`Category Share = Category Count / Total Records × 100`

## 🔍 Review Workflow

**Inspect → Check → Summarise → Visualise → Interpret → Document**

## 🧪 Data Quality Checks

The review covers:

- Missing values
- Duplicate Record IDs
- Duplicate Customer IDs
- Duplicate rows
- Numeric ranges
- Numeric descriptive statistics
- Category frequencies
- Outcome counts
- Exposure
- Business definitions

## ⚠️ Interpretation

A clean dataset does not automatically mean that it is ready for real-world modelling.

A real credit-risk project also requires:

- Source validation
- Business definitions
- Sampling review
- Target definition
- Feature timing
- Leakage checks
- Data governance

## 🐍 Python Analysis

The Python script:

- Reads the Excel workbook.
- Converts numeric columns.
- Checks missing values.
- Checks duplicates.
- Creates summary tables.
- Calculates default rates.
- Calculates exposure.
- Exports CSV files.
- Generates charts.

## 📁 Output Folder

Generated analysis files are stored inside:

`python_outputs/`

These include:

- CSV summaries
- Review tables
- PNG charts

## 🧾 Portfolio Evidence

This Day can be represented in a learning portfolio using:

- Dataset
- Data dictionary
- Quality review
- KPI table
- Dashboard
- Python script
- Generated outputs
- Short business summary

## 🏁 Day 085 Takeaway

Data review is a foundation step in credit-risk analytics.

Before building a model, understand:

**Structure + Quality + Variables + Outcomes + Business Meaning**

## 🏅 Badges

- 🔎 Data Review
- 💳 Credit Risk
- 📊 Excel Analytics
- 🐍 Python Analytics
- 🧠 Data Quality