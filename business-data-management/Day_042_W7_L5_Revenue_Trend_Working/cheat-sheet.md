![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-042-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 042 Cheat Sheet — Revenue Trend Working

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 042  
**Topic:** W7_L5 Revenue Trend Working

## 🔑 Core Formula
Revenue = Sales value generated during the period.
Gross Margin = Revenue - Production Cost.
MoM Growth = (Current Revenue - Previous Revenue) / Previous Revenue.

## 📅 Monthly Trend
Group by Month → Sum Revenue → Sort chronologically → Calculate growth.

## 🧮 Excel Formulas
`=SUMIFS(Revenue,Month,TargetMonth)`
`=(CurrentMonth-PreviousMonth)/PreviousMonth`
`=SUM(RevenueRange)`
`=MAX(MonthlyRevenueRange)`

## 🐼 Python Patterns
`df.groupby('Month')['Revenue'].sum()`
`monthly['Revenue'].pct_change()`
`df.groupby('Product')['Revenue'].sum()`
`df.groupby('Region')['Revenue'].sum()`

## 📊 Chart Selection
Time trend → Line chart.
Category comparison → Column chart.

## 🔍 Questions
Highest month → MAX.
Top product → sort revenue descending.
Top region → sort revenue descending.

## ⚠️ Checks
Check chronological order.
Check missing values.
Check duplicate records.
Check units and currency.

## 💡 Interpretation Rules
Increasing revenue → growth pattern.
Flat revenue → stable pattern.
Falling revenue → decline pattern.
Do not infer a cause without supporting data.

## 📈 Dashboard KPIs
Total Revenue
Average Monthly Revenue
Highest Revenue Month
Top Product

## 🧭 Workflow
Raw Data → Monthly Summary → MoM Growth → Product View → Region View → Dashboard

## 🧪 Practice
Calculate monthly revenue.
Calculate MoM growth.
Find highest month.
Rank products.
Rank regions.

## 📌 Definitions
Trend = movement over time.
MoM = month over month.
Revenue contribution = category revenue relative to total.

## 🏅 Badges
![Excel](https://img.shields.io/badge/Excel-Intermediate-green)
![Analytics](https://img.shields.io/badge/Skill-Revenue%20Analytics-blue)
![Python](https://img.shields.io/badge/Python-Pandas-orange)