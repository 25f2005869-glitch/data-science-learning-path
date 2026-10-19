![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-084-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📊 Day 084 — Explanation of Credit Risk Dataset

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 084  
**Topic:** Explanation of Credit Risk Dataset

## 🎯 Objective
- Understand the structure of a credit-risk dataset.
- Identify customer, loan, income, credit-history and outcome fields.
- Distinguish raw fields from derived fields.
- Connect variables with business questions.
- Prepare the data for descriptive analysis.

## 🧩 Dataset Context
This workbook contains 30 **synthetic educational records**.
One row represents one customer-loan record.
The data is created for learning Excel, Python and business-data interpretation.
It is not an official lender dataset and is not suitable for real lending decisions.

## 🗂️ Main Variable Groups
| Group | Examples |
|---|---|
| Customer | Customer_ID, Age, Employment_Type |
| Geography | Region |
| Loan | Loan_Product, Loan_Amount_Rupee, Tenure_Months |
| Income | Monthly_Income_Rupee, Annual_Income_Rupee |
| Affordability | Debt_to_Income_%, Loan_to_Annual_Income_% |
| Credit history | Credit_Score, Past_Delinquencies |
| Outcomes | Default_Flag, High_Risk_Flag |
| Derived risk | Risk_Score, Risk_Band |

## 📚 Workbook
`Credit_Risk_Data` is the raw learning table.
`Data_Dictionary` explains every field.
`Risk_Framework` connects variables with analytical use.
`Product_Risk_Summary` compares loan products.
`Region_Risk_Summary` compares regions.
`Employment_Risk` compares employment categories.
`Credit_Score_Bands` groups score ranges.
`Risk_Band_Analysis` groups composite risk scores.
`Credit_Risk_KPIs` contains headline metrics.
`Analysis_Questions` provides practice.
`Credit_Risk_Dashboard` contains prepared charts.

## 🧮 Key Derived Fields
Annual income equals monthly income multiplied by 12.
Loan-to-annual-income percentage compares exposure with annual income.
The simple installment estimate divides loan amount by tenure.
The illustrative risk score combines credit score, DTI, delinquency and default indicators.

## 📊 Dashboard
- Default rate by loan product.
- Average credit score by region.
- Customers by risk band.
- Loan exposure by product.
- Credit score versus debt-to-income scatter.

## 🔍 Study Method
1. Read the raw table.
2. Identify the unit of analysis.
3. Read the data dictionary.
4. Classify the fields.
5. Review quality checks.
6. Read summary tables.
7. Inspect charts.
8. Answer the practice questions.
9. Run the Python script.
10. Document limitations.

## ⚠️ Interpretation
A count and a rate answer different questions.
An average does not show the whole distribution.
A risk flag is an indicator, not an explanation.
Correlation does not prove causation.
Small synthetic samples should not drive real policy.

## 🏁 Takeaway
A good credit-risk analysis starts with understanding the dataset.
Before modelling, the analyst should know what each field means, its unit, its timing, its business purpose and its limitations.

## 🧭 Field-to-Question Map
| Field | Main analytical question |
|---|---|
| Credit_Score | What is the observed credit-score profile? |
| Debt_to_Income_% | How large is debt burden relative to income? |
| Loan_Amount_Rupee | What is the current credit exposure? |
| Monthly_Income_Rupee | What income capacity is represented? |
| Past_Delinquencies | What prior delinquency history is recorded? |
| Default_Flag | Which records are marked as default? |
| High_Risk_Flag | Which records are marked as high risk? |

## 🧾 File Map
The Excel workbook is the primary learning artifact.
The Python script reproduces the descriptive calculations.
CSV files contain reusable analysis tables.
PNG files contain regenerated learning visuals.

## 🔁 Reproducibility
Keep the workbook beside the `code` folder.
Run the saved Python script from its location.
The script reads the Excel input using a relative project path.
Analysis outputs are written into `python_outputs`.

## 🏅 Badges
- 💳 Credit Risk Analytics
- 📊 Dataset Interpretation
- 🧮 Feature Engineering
- 🐍 Python + Excel
- 💼 Business Data Analysis