![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-047-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 047 Notes — Region-wise Revenue and Sales Agent Planning

## 1. Introduction

Day 047 extends the region-wise revenue analysis.

The new dimension introduced in this practical is Sales_Agent.

The analysis connects geography with sales ownership.

## 2. Regional Revenue

Regional revenue is the total revenue associated with a particular region.

The Region_Revenue sheet summarizes this information.

It provides a high-level geographic view.

## 3. Sales Agent

Sales_Agent identifies the illustrative sales representative associated with a record.

Agent-level aggregation allows revenue contribution to be examined.

## 4. Agent Performance

Sales_Agent_Performance contains agent-level metrics.

Important fields include revenue, orders, sales units, gross margin and regions covered.

These measures provide descriptive performance information.

## 5. Revenue Contribution

Revenue contribution can be expressed using revenue share.

Formula:

Revenue Share = Revenue / Total Revenue

The calculation can be applied to regions or agents.

## 6. Region-Agent Combination

Region_Agent_Summary combines two dimensions.

The first dimension is Region.

The second dimension is Sales_Agent.

The resulting table shows revenue by assignment.

## 7. Region-Agent Matrix

Region_Agent_Matrix presents regions as rows and agents as columns.

This makes assignment distribution easier to inspect.

It can also support dashboard visualisation.

## 8. Agent Coverage

Regions_Covered measures the number of unique regions associated with an agent.

It is a descriptive coverage metric.

It does not independently measure workload.

## 9. Monthly Analysis

Monthly_Agent_Revenue introduces the time dimension.

Monthly revenue can reveal changes in agent contribution.

A line chart is suitable for this type of analysis.

## 10. Revenue Ranking

Revenue ranking orders agents or assignments by revenue.

Ranking provides a quick comparison.

It does not explain the reason for the ranking.

## 11. Planning

Agent_Planning provides a structured starting point for planning discussion.

Planning should use evidence.

Revenue, coverage and trend can be considered together.

## 12. Financial Context

Gross margin gives additional financial context.

Gross margin is revenue minus production cost in this practice dataset.

Margin percentage expresses gross margin relative to revenue.

## 13. Excel Workflow

Open the raw data first.

Read the data dictionary.

Review Region_Revenue.

Review Sales_Agent_Performance.

Review Region_Agent_Summary.

Review Monthly_Agent_Revenue.

Review Region_Agent_Matrix.

Review Agent_Planning.

Finish with the dashboard.

## 14. Business Questions

Which region has the highest revenue?

Which agent has the highest revenue?

Which region-agent pair contributes most?

Which agents cover multiple regions?

How does revenue change over time?

## 15. Evidence

Every numerical statement should be traceable to a worksheet.

Use exact values when presenting important results.

Avoid unsupported assumptions about agents.

## 16. Python Workflow

The Python script reads Revenue_Agent_Data.

It uses groupby for summaries.

It uses pivot_table for matrix and monthly analysis.

It exports CSV outputs.

It creates four charts.

## 17. Dataset Limitation

The dataset is illustrative.

It is not presented as official IITM course data.

Its purpose is practical learning.

## 18. Learning Outcome

The main learning outcome is connecting regional revenue analysis with sales-agent planning.

The workflow moves from raw records to a structured business dashboard.

## 🔁 Quick Revision

Review the regional summary.

Review the agent summary.

Review the region-agent matrix.

Review the monthly trend.

Review the planning table.

Use the dashboard to connect the analysis.

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-Region%20Revenue-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Analytics-green?style=flat-square)
![Practice](https://img.shields.io/badge/Practice-Business%20Analysis-orange?style=flat-square)