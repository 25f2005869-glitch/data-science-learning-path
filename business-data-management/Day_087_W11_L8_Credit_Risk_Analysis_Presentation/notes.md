![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-087-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# Day 087 Notes — Credit Risk Analysis Presentation

Author: Saloni Tiwari  
Programme: IIT Madras BS Degree — Diploma Level  
Day: 087  
Topic: Credit Risk Analysis — Presentation

## 📚 Presentation Thinking

Credit-risk analysis becomes useful to a business when the results can be communicated clearly.

A presentation is different from a raw analytical workbook.

A workbook may contain many tables.

A presentation should select only the evidence required for the business question.

## 1️⃣ Start With the Business Question

The first step is defining the question.

For this lesson:

How has credit risk moved across the six-month period?

This question determines which metrics should be presented.

## 2️⃣ Introduce the Dataset

The audience should understand:

- Time period
- Number of records
- Products
- Regions
- Main variables

Without context, a chart can be difficult to interpret.

## 3️⃣ Explain the Time Dimension

The Month field allows the data to be compared over time.

The dataset covers January through June 2023.

Monthly grouping creates a consistent comparison framework.

## 4️⃣ Customer Count

Customer count represents the number of customer records in a month.

Formula:

Customers = COUNT(Customer_ID)

This value is important because several risk rates use customer count as their denominator.

## 5️⃣ Loan Exposure

Loan exposure represents the simulated amount of lending exposure.

Formula:

Loan Exposure = SUM(Loan_Exposure_Rupee)

Exposure measures portfolio scale.

It should not automatically be interpreted as risk.

## 6️⃣ Default Count

Default count is the number of records where Default_Flag equals 1.

Formula:

Defaults = SUM(Default_Flag)

A count alone does not show the rate of defaults.

## 7️⃣ Default Rate

Default rate converts default count into a percentage.

Formula:

Default Rate % = Defaults / Customers × 100

This allows comparison across periods with different customer counts.

## 8️⃣ High-Risk Customers

High-risk customers are represented by High_Risk_Flag.

Formula:

High Risk = SUM(High_Risk_Flag)

The flag in this exercise is based on a simplified learning rule.

## 9️⃣ High-Risk Share

High-risk share expresses high-risk customers as a percentage.

Formula:

High-Risk Share % = High Risk / Customers × 100

It is useful for observing portfolio composition.

## 🔟 Average Credit Score

Average credit score is calculated for each month.

Formula:

Average Score = AVERAGE(Credit_Score)

The metric gives a simple view of portfolio credit-score movement.

## 1️⃣1️⃣ Average DTI

Average DTI represents the average Debt_to_Income_% for the monthly records.

DTI is useful for understanding debt burden in the learning dataset.

## 1️⃣2️⃣ Month-over-Month Exposure Growth

MoM exposure growth compares one month with the previous month.

Formula:

(Current Exposure / Previous Exposure − 1) × 100

The first month has no previous month.

## 1️⃣3️⃣ Default Rate Change

Default-rate change is expressed in percentage points.

Formula:

Current Default Rate − Previous Default Rate

Percentage-point change is different from percentage growth.

## 1️⃣4️⃣ Product Presentation

Product-level analysis helps determine whether portfolio movement is concentrated in one product.

The same measures should be compared consistently.

## 1️⃣5️⃣ Regional Presentation

Regional analysis provides another business dimension.

Regions should be compared using both:

- Absolute values
- Rate-based measures

## 1️⃣6️⃣ Chart Selection

Line charts are useful for monthly trends.

Column charts are useful for magnitude comparisons.

Scatter charts can be used for relationship exploration.

Doughnut charts can be used for composition.

## 1️⃣7️⃣ Presentation Sequence

The recommended sequence is:

Business Question

Dataset

Portfolio Trend

Product View

Regional View

KPI Summary

Business Interpretation

Limitations

Next Steps

## 1️⃣8️⃣ Evidence-Based Language

Use:

- Increased
- Decreased
- Remained stable
- Changed
- Higher
- Lower
- Fluctuated

Avoid unsupported claims.

## 1️⃣9️⃣ Causality

A descriptive chart shows association or movement.

It does not automatically prove that one variable caused another.

Additional analysis would be required for causal conclusions.

## 2️⃣0️⃣ Presentation Limitations

Important limitations include:

- Synthetic dataset
- Short time period
- Simplified risk rules
- Limited customer attributes
- No production model validation

## 2️⃣1️⃣ Python Reproducibility

Python allows the same calculations to be repeated.

The script reads the Excel dataset.

It creates monthly summaries.

It creates product-month summaries.

It creates region-month summaries.

It exports CSV files.

It also generates PNG charts.

## 2️⃣2️⃣ Final Presentation Rule

Each slide should have a clear purpose.

Each chart should answer a question.

Each important statement should be supported by data.

## 🏅 Badges

- Credit Risk Analysis
- Monthly Trends
- Presentation Skills
- Excel Analytics
- Python Analytics
- Business Data Management