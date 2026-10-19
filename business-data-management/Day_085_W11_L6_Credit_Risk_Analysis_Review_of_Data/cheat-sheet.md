![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-085-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 085 — Credit Risk Data Review Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 085  
**Topic:** Credit Risk Analysis — Review of Data

## 🔑 First Checks

- Unit of analysis
- Row count
- Unique IDs
- Missing values
- Data types
- Categories
- Numeric ranges
- Outcome distribution
- Loan exposure
- Target definition
- Leakage
- Sampling

## 🧮 Core Formulas

`Missing % = Missing Values / Total Rows × 100`

`Default Rate % = Defaults / Total Records × 100`

`High-Risk Share % = High-Risk Records / Total Records × 100`

`Category Share % = Category Count / Total Records × 100`

## 📊 Numeric Functions

- `COUNT`
- `AVERAGE`
- `MEDIAN`
- `MIN`
- `MAX`
- `SUM`

## 🧪 Excel Quality Functions

- `COUNTBLANK`
- `COUNTIF`
- `COUNTIFS`
- `COUNTA`
- `UNIQUE`
- `SUMIF`
- `SUMIFS`

## 🐍 Pandas Checks

`df.shape`

`df.dtypes`

`df.isna().sum()`

`df.nunique()`

`df.duplicated().sum()`

`df.describe()`

`df.value_counts()`

## 🔎 Identifier Checks

`Record_ID` → row identifier.

`Customer_ID` → customer identifier.

## 💳 Core Credit Variables

`Credit_Score`

`Debt_to_Income_%`

`Loan_Amount_Rupee`

`Monthly_Income_Rupee`

`Tenure_Months`

`Past_Delinquencies`

`Default_Flag`

`High_Risk_Flag`

## 📌 Variable Types

| Variable | Type |
|---|---|
| Age | Numeric |
| Monthly Income | Numeric |
| Loan Amount | Numeric |
| Tenure | Numeric |
| Credit Score | Numeric |
| DTI | Numeric |
| Region | Categorical |
| Employment Type | Categorical |
| Loan Product | Categorical |
| Default Flag | Binary |

## ⚠️ Important Distinctions

Count ≠ Rate.

Exposure ≠ Customer Count.

Outlier ≠ Error.

Correlation ≠ Causation.

Flag ≠ Explanation.

Synthetic Data ≠ Production Data.

## 📈 Chart Selection

- Product comparison → Column.
- Regional trend/comparison → Line.
- Outcome composition → Doughnut.
- Numeric relationship → Scatter.

## 🔍 Five Questions

1. What does one row represent?
2. Are identifiers unique?
3. Are values missing?
4. Are data types correct?
5. Is the target clearly defined?

## 🧠 Modelling Checks

Before modelling:

- Check target.
- Check missing values.
- Check categories.
- Check ranges.
- Check leakage.
- Check feature timing.
- Check sample size.
- Check class balance.

## 🎯 Review Formula

**Understand → Validate → Summarise → Visualise → Document**

## 🏅 Badges

- ⚡ Quick Revision
- 🔎 Data Quality
- 💳 Credit Risk
- 🐍 Python
- 📊 Excel