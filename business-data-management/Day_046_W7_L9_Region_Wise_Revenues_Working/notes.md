![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-046-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 046 Notes — Region-wise Revenues Working

## 1. Concept

Region-wise revenue analysis groups business revenue by geographic region.

The grouping makes it possible to compare regional contribution.

A regional view is useful when management needs to understand where revenue is generated.

## 2. Regional Revenue

Regional revenue is the sum of revenue records belonging to one region.

The Region_Revenue sheet provides a prepared regional summary.

Revenue should be compared using the same time period and scope.

## 3. Revenue Share

Revenue share measures the percentage contribution of a region to total revenue.

Formula:

Regional Revenue / Total Revenue

The result can be expressed as a percentage.

Revenue share helps describe revenue concentration.

## 4. Ranking

Ranking orders regions by a selected metric.

Revenue rank provides a quick management comparison.

Ranking alone does not explain why a region has a particular result.

## 5. Monthly View

Monthly regional revenue adds a time dimension.

It can reveal whether a region changes across the observation period.

A line chart is useful for a monthly trend.

## 6. Product-region View

Product-region analysis combines two dimensions.

It helps identify which products contribute within each region.

This view can expose concentration hidden by a region-only total.

## 7. Gross Margin Context

Revenue is not the same as profit.

Gross margin is revenue minus production cost in this practice dataset.

Margin percentage is gross margin divided by revenue.

A revenue comparison can therefore be read together with profitability context.

## 8. Operational Context

Sales conversion percentage compares sales units with production units.

Scrap rate compares scrap units with production units.

Closing inventory provides an additional operating signal.

These metrics provide supporting context.

## 9. Excel Workflow

Start with Revenue_Data.

Use Region_Revenue for the regional summary.

Use Revenue_Share for contribution.

Use Region_Ranking for ordered comparison.

Use Monthly_Region_Revenue for trends.

Use Product_Region_Revenue for two-dimensional comparison.

## 10. Presentation

A concise presentation can start with regional revenue comparison.

Next show revenue share.

Then show monthly regional trends.

Finish with a product-region observation.

Add one relevant operating metric where appropriate.

## 11. Evidence

Business statements should be supported by a workbook sheet.

Avoid statements that cannot be traced to a number or chart.

Use exact percentages when contribution is important.

## 12. Python

The Python script uses pandas groupby operations.

It also uses pivot_table for monthly and product-region analysis.

The results are exported to CSV files.

Four visualisations are generated.

## 13. Dataset Limitation

The practice dataset is illustrative.

It should not be interpreted as the official IITM dataset.

The purpose is to practise the analytical workflow.

## 14. Key Questions

Which region has the highest revenue?

Which region has the largest revenue share?

Which product contributes most within each region?

How does regional revenue change over time?

What operational metrics should be considered alongside revenue?

## 15. Practical Learning

The main skill is moving from raw records to a business-ready regional view.

The analysis should remain reproducible.

The same logic can later be applied to other business datasets.

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-Region%20Revenue-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Analytics-green?style=flat-square)
![Practice](https://img.shields.io/badge/Practice-Business%20Analysis-orange?style=flat-square)