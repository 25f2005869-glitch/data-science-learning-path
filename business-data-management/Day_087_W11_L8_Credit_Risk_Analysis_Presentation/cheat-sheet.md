![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-087-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# Day 087 Cheat Sheet — Credit Risk Presentation

Author: Saloni Tiwari  
Programme: IIT Madras BS Degree — Diploma Level  
Day: 087  
Topic: Credit Risk Analysis — Presentation

## ⚡ Presentation Flow

Question → Data → KPI → Trend → Comparison → Interpretation → Limitation → Next Step

## 📌 Core Metrics

Customers

Loan Exposure

Average Credit Score

Average DTI

Defaults

Default Rate

High-Risk Customers

High-Risk Share

## 🧮 Customer Count

Customers = COUNT(Customer_ID)

## 💰 Exposure

Exposure = SUM(Loan_Exposure_Rupee)

## ❌ Defaults

Defaults = SUM(Default_Flag)

## ⚠️ High Risk

High Risk = SUM(High_Risk_Flag)

## 📊 Default Rate

Default Rate % = Defaults / Customers × 100

## 🚨 High-Risk Share

High-Risk Share % = High Risk / Customers × 100

## 📈 Average Credit Score

Average Score = AVERAGE(Credit_Score)

## 📊 Average DTI

Average DTI = AVERAGE(Debt_to_Income_%)

## 📅 MoM Exposure Growth

MoM Growth % = (Current Exposure / Previous Exposure − 1) × 100

## 📉 Default Rate Change

Default Rate Change pp = Current Rate − Previous Rate

## 🔢 Percentage Points

Use percentage points when subtracting two percentages.

Example:

8% − 5% = 3 percentage points

## 💳 Product Grouping

Group by:

Month + Loan_Product

## 🌍 Region Grouping

Group by:

Month + Region

## 📊 Line Chart

Best for:

Monthly trends

Time-based movement

## 📊 Column Chart

Best for:

Magnitude comparison

Category comparison

## 🥧 Composition Chart

Useful for:

Portfolio mix

Selected-period composition

## 🔵 Scatter Chart

Useful for:

Relationship exploration

Two numeric variables

## 🧠 Interpretation

Ask:

What changed?

When did it change?

How much did it change?

Which category changed?

Which KPI supports the statement?

## ⚠️ Avoid

Do not confuse count and rate.

Do not confuse percentage points and percentage growth.

Do not infer causality from a trend.

Do not use synthetic data for real lending decisions.

## 🐍 Python Pattern

read_excel

groupby

agg

pct_change

diff

to_csv

plot

bar

savefig

## 🎤 Presentation Checklist

Business question clear

Dataset explained

Time period shown

KPI definitions checked

Units shown

Charts readable

Observations supported

Limitations stated

Next steps included

## 🏅 Badges

- Credit Risk Analysis
- Monthly Trends
- Presentation Skills
- Excel Analytics
- Python Analytics
- Business Data Management