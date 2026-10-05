![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-042-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 042 Notes — Revenue Trend Working

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 042  
**Topic:** W7_L5 Revenue Trend Working

## 1. Revenue Trend
Revenue trend analysis studies how revenue changes over time.
For this day the time unit is month.

## 2. Revenue
Revenue is the monetary value generated from sales.
In the dataset, `Revenue` is the main trend measure.

## 3. Monthly Aggregation
Group records by Month and sum Revenue.
This converts transaction-level observations into a management-level monthly view.

## 4. Month-on-Month Growth
MoM growth = (Current Month Revenue - Previous Month Revenue) / Previous Month Revenue.
Multiply by 100 when expressing the result as a percentage.

## 5. Why Trend Analysis Matters
Managers need to know whether revenue is increasing, decreasing, or stable.
Trend analysis supports planning and performance review.

## 6. Product View
Product-level revenue shows which products contribute most.
Comparing products prevents the monthly total from hiding product differences.

## 7. Region View
Regional revenue shows geographical contribution.
A region with lower revenue may require separate investigation rather than being judged only by the total.

## 8. Sales Units
Revenue should be considered alongside sales units.
Revenue can rise because of more units, higher prices, or a combination.

## 9. Production
Production units provide operational context.
Production and sales should be compared to understand supply and demand alignment.

## 10. Inventory
Closing inventory is useful for checking whether inventory movement accompanies revenue movement.
High inventory with weak sales may need investigation.

## 11. Gross Margin
Gross Margin = Revenue - Production Cost.
Revenue growth does not automatically mean margin growth.

## 12. Working Sequence
1. Read raw data.
2. Aggregate revenue by month.
3. Calculate MoM growth.
4. Compare products.
5. Compare regions.
6. Interpret the pattern.

## 13. Chart Choice
A line chart is suitable for a time trend.
A column chart is useful for product or region comparison.

## 14. Business Questions
Which month has the highest revenue?
Which product contributes most revenue?
Which region contributes most revenue?

## 15. Interpretation
Describe what the data shows before suggesting possible causes.
Possible causes should be treated as hypotheses unless the dataset provides evidence.

## 16. Data Quality
Check month order before calculating growth.
Check for missing revenue values and duplicates.

## 17. Excel Working
Use SUMIFS or PivotTables for monthly aggregation.
Use a percentage formula for MoM growth.

## 18. Python Working
Pandas `groupby()` performs aggregation.
`pct_change()` can calculate period-to-period percentage change.

## 19. Dashboard
The dashboard presents headline KPIs and three comparison charts.
Keep the dashboard focused on the revenue-trend question.

## 20. Dataset Limitation
This practical uses an illustrative dataset.
Do not present its values as official course figures.

## 21. Key Takeaway
Revenue trend analysis converts dated business records into a time-based performance story.