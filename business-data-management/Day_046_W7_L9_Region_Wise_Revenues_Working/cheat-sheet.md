![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-046-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 046 Cheat Sheet — Region Revenue

## 🔢 Key Formulas

Regional Revenue = Sum of revenue for a region.

Revenue Share = Regional Revenue / Total Revenue.

Gross Margin = Revenue - Production Cost.

Margin % = Gross Margin / Revenue.

Sales Conversion % = Sales Units / Production Units.

Scrap Rate % = Scrap Units / Production Units.

## 📌 Excel Functions

SUMIF can aggregate using one condition.

SUMIFS can aggregate using multiple conditions.

COUNTIF counts matching records.

COUNTIFS counts records using multiple conditions.

RANK orders numeric values.

IFERROR can handle formula errors.

## 🧮 Formula Patterns

=SUMIF(RegionRange,"North",RevenueRange)

=RegionalRevenue/TotalRevenue

=GrossMargin/Revenue

=SalesUnits/ProductionUnits

=ScrapUnits/ProductionUnits

## 🗂️ Workbook Map

Revenue_Data → raw practice data.

Region_Revenue → regional KPIs.

Monthly_Region_Revenue → monthly regional trend.

Product_Region_Revenue → product-region matrix.

Region_Ranking → ordered comparison.

Revenue_Share → regional contribution.

Region_Questions → practice questions.

Business_Insights → observations.

Data_Dictionary → field definitions.

Region_Working → calculation logic.

Region_Revenue_Dashboard → visual summary.

Instructions → execution sequence.

## 📊 Chart Selection

Column chart → compare regional totals.

Line chart → compare regional monthly trends.

Grouped columns → compare product-region values.

Bar chart → compare revenue shares.

## 🧠 Interpretation

High revenue means high revenue contribution.

High revenue does not automatically mean high profitability.

High revenue share indicates concentration.

A trend chart should be interpreted across the full period.

Product-region analysis identifies concentration across two dimensions.

Operating metrics provide supporting context.

## 🐍 Python Patterns

df.groupby("Region")["Revenue"].sum()

df.groupby("Region", as_index=False).agg(...)

df.pivot_table(index="Month", columns="Region", values="Revenue", aggfunc="sum")

summary.sort_values("Revenue", ascending=False)

## 🔍 Validation Checks

Total regional revenue should equal raw-data revenue.

Regional shares should sum to approximately 100%.

Revenue ranking should follow revenue order.

Monthly totals should reconcile with the full-period total.

Product-region totals should reconcile with regional totals.

## 🎯 Business Presentation

Start with regional revenue.

Show revenue share.

Show monthly trend.

Show product-region comparison.

Add profitability context.

Add an operational metric.

Use evidence for every insight.

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-Region%20Analysis-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Formulas-green?style=flat-square)
![Python](https://img.shields.io/badge/Python-pandas-orange?style=flat-square)