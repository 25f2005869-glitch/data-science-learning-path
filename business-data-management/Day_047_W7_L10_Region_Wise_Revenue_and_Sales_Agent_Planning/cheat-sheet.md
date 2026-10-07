![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-047-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 047 Cheat Sheet — Revenue & Sales Agent Planning

## 🔢 Core Metrics

Regional Revenue = Sum of revenue by region.

Agent Revenue = Sum of revenue by sales agent.

Region-Agent Revenue = Sum of revenue by both dimensions.

Revenue Share = Revenue / Total Revenue.

Gross Margin = Revenue - Production Cost.

Margin % = Gross Margin / Revenue.

Regions Covered = Number of unique regions per agent.

## 📌 Excel Functions

SUMIF → aggregate using one condition.

SUMIFS → aggregate using multiple conditions.

COUNTIF → count one condition.

COUNTIFS → count multiple conditions.

RANK → order numeric values.

UNIQUE → identify unique values.

FILTER → retrieve matching records.

## 🧮 Formula Patterns

=SUMIF(RegionRange,"North",RevenueRange)

=SUMIF(AgentRange,"Amit",RevenueRange)

=SUMIFS(RevenueRange,RegionRange,"North",AgentRange,"Amit")

=Revenue/TotalRevenue

=GrossMargin/Revenue

## 🗂️ Workbook Map

Revenue_Agent_Data → raw data.

Region_Agent_Summary → region-agent metrics.

Sales_Agent_Performance → agent metrics.

Region_Revenue → regional baseline.

Monthly_Agent_Revenue → monthly trend.

Region_Agent_Matrix → assignment matrix.

Agent_Planning → planning view.

Planning_Questions → questions.

Business_Insights → observations.

Data_Dictionary → definitions.

Agent_Planning_Working → calculation logic.

Dashboard → visual summary.

Instructions → execution sequence.

## 📊 Chart Selection

Column chart → compare regional revenue.

Column chart → compare agent revenue.

Line chart → monthly agent revenue.

Grouped column chart → region-agent comparison.

## 🧠 Interpretation

Revenue measures contribution.

Revenue share measures concentration.

Agent ranking orders agents by revenue.

Coverage describes geographic representation.

Monthly analysis adds time.

Region-agent analysis adds assignment context.

Revenue alone does not establish workload quality.

## 🐍 Python Patterns

df.groupby("Region")["Revenue"].sum()

df.groupby("Sales_Agent")["Revenue"].sum()

df.groupby(["Region","Sales_Agent"])["Revenue"].sum()

df.pivot_table(
    index="Month",
    columns="Sales_Agent",
    values="Revenue",
    aggfunc="sum"
)

df.pivot_table(
    index="Region",
    columns="Sales_Agent",
    values="Revenue",
    aggfunc="sum"
)

summary.sort_values("Revenue", ascending=False)

## ✅ Validation Checks

Regional revenue should reconcile with raw data.

Agent revenue should reconcile with raw data.

Region-agent totals should reconcile with both dimensions.

Revenue shares should total approximately 100%.

Monthly totals should reconcile with the full period.

## 🎯 Presentation Flow

Start with regional revenue.

Show agent contribution.

Show region-agent distribution.

Show monthly trend.

Show coverage.

Add relevant financial context.

Use evidence for every statement.

## 🏁 Memory Line

Region → Revenue → Agent → Region-Agent Pair → Coverage → Trend → Planning → Dashboard

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-Region%20Analysis-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Formulas-green?style=flat-square)
![Python](https://img.shields.io/badge/Python-pandas-orange?style=flat-square)