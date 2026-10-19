![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-087-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# Day 087 — Credit Risk Analysis Presentation

Author: Saloni Tiwari  
Programme: IIT Madras BS Degree — Diploma Level  
Day: 087  
Topic: Credit Risk Analysis — Presentation

## 📌 Overview

Day 087 focuses on presenting the credit-risk analysis completed in the previous lessons.

The main purpose is to convert analytical tables into a clear business presentation.

The presentation uses monthly credit-risk data.

The analysis covers January 2023 to June 2023.

The dataset is synthetic and created for educational practice.

## 🎯 Learning Objectives

- Understand presentation-oriented credit-risk analysis.
- Identify the main business question.
- Present portfolio-level risk indicators.
- Explain monthly trends.
- Compare loan products.
- Compare regions.
- Present important KPIs.
- Explain limitations.
- Prepare business-focused observations.
- Use Excel charts effectively.
- Reproduce analysis using Python.

## 📊 Dataset

The workbook contains customer-level credit-risk observations.

Important fields include:

- Record_ID
- Month
- Customer_ID
- Employment_Type
- Region
- Loan_Product
- Age
- Monthly_Income_Rupee
- Loan_Amount_Rupee
- Tenure_Months
- Debt_to_Income_%
- Credit_Score
- Past_Delinquencies
- Default_Flag
- High_Risk_Flag
- Loan_Exposure_Rupee

## 📅 Time Period

The analysis covers six months:

- January 2023
- February 2023
- March 2023
- April 2023
- May 2023
- June 2023

## 💳 Loan Products

The dataset contains three illustrative products:

1. Personal Loan
2. Two-Wheeler Loan
3. Consumer Durable Loan

## 🌍 Regions

The dataset contains four regions:

- North
- South
- West
- East

## 🧮 Important KPIs

The presentation focuses on:

- Customer count
- Loan exposure
- Average credit score
- Average DTI
- Default count
- Default rate
- High-risk customers
- High-risk share

## 📈 Default Rate

Default Rate is calculated as:

Default Rate % = Defaults / Customers × 100

The denominator is the number of customer records for the relevant month.

## ⚠️ High-Risk Share

High-Risk Share is calculated as:

High-Risk Share % = High-Risk Customers / Customers × 100

This measure uses the educational High_Risk_Flag field.

## 💰 Loan Exposure

Loan exposure represents the simulated amount associated with the lending portfolio.

Monthly exposure is calculated by summing Loan_Exposure_Rupee.

Exposure is a scale measure rather than a risk rate.

## 📊 Monthly Trend

The Monthly_Trend sheet provides the main portfolio view.

It includes:

- Customers
- Loan Exposure
- Average Credit Score
- Average DTI
- Defaults
- High Risk
- Default Rate
- High-Risk Share
- Exposure Growth
- Default Rate Change

## 💳 Product Analysis

Product_Monthly provides monthly analysis by loan product.

It helps answer questions about:

- Product exposure
- Product customer count
- Product credit score
- Product defaults
- Product high-risk customers
- Product default rate

## 🌍 Regional Analysis

Region_Monthly provides monthly regional analysis.

Regional analysis should consider both absolute values and rates.

A region with more customers can naturally have more absolute events.

## 🧭 Presentation Structure

A useful presentation sequence is:

1. Business Question
2. Dataset
3. Portfolio Trend
4. Product View
5. Regional View
6. KPI Summary
7. Business Interpretation
8. Limitations
9. Next Steps

## 📊 Dashboard

The dashboard includes:

- Monthly Default Rate
- Monthly Loan Exposure
- Average Credit Score
- High-Risk Customer Share
- Product Exposure by Month

Different chart types are used to make the presentation easier to understand.

## 🐍 Python Analysis

The Python script reads the Excel workbook.

It creates:

- Monthly trend summary
- Product-month summary
- Region-month summary

It also exports CSV files.

PNG charts are generated using Matplotlib.

## 🧠 Business Interpretation

A presentation should not simply repeat numbers.

It should explain:

- What changed?
- When did it change?
- How large was the change?
- Which segment was involved?
- Which metric supports the statement?

## ⚠️ Important Limitation

The dataset is synthetic.

The risk indicators are simplified educational constructs.

The workbook should not be used for actual lending, underwriting, credit approval, or customer decisions.

## 📝 Practice

The practice section asks you to prepare a short presentation.

Focus on evidence-based observations.

Do not make unsupported causal claims.

## 🏁 Final Takeaway

Credit-risk presentation combines analysis with communication.

A strong presentation connects:

Business Question → Data → KPI → Trend → Comparison → Interpretation → Limitation → Next Step

## 🏅 Badges

- Credit Risk Analysis
- Monthly Trends
- Presentation Skills
- Excel Analytics
- Python Analytics
- Business Data Management