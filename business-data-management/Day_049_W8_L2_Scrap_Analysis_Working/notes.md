![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-049-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 049 Notes — Scrap Analysis Working

## 1. Introduction

Scrap is production output that is not counted as usable good output.
Scrap analysis helps quantify production losses.

## 2. Production Units

Production Units represent total manufactured units.

## 3. Scrap Units

Scrap Units represent units classified as scrap.

## 4. Good Units

Good Units are production units excluding scrap.

Formula:

Good Units = Production Units - Scrap Units.

## 5. Scrap Rate

Scrap Rate measures scrap relative to total production.

Formula:

Scrap Rate = Scrap Units / Production Units.

## 6. Why Rate Matters

Scrap units alone depend on production volume.
A rate provides a normalized comparison.

## 7. Product Analysis

Product_Scrap_Summary aggregates results by product.
It supports product comparison.

## 8. Monthly Analysis

Monthly_Scrap aggregates results by month.
It supports trend analysis.

## 9. Regional Analysis

Region_Scrap aggregates results by region.
It supports regional comparison.

## 10. Product-Region Analysis

Product_Region_Scrap combines product and region.
It helps locate detailed differences.

## 11. Scrap Cost

The workbook includes illustrative scrap cost.
Scrap cost is calculated from scrap units and illustrative unit cost assumptions.

## 12. Excel Working

Use SUMIF or SUMIFS for aggregation.
Use division for scrap rate.
Use charts for comparison.

## 13. Dashboard

Use the dashboard after checking summary tables.
Charts should support the numerical analysis.

## 14. Python Working

Read the workbook with pandas.
Group data using groupby.
Calculate rates with arithmetic.
Export summaries as CSV.
Create charts with matplotlib.

## 15. Interpretation

High scrap rate indicates more scrap relative to production.
Low scrap rate indicates less scrap relative to production.
A pattern should be investigated before explaining its cause.

## 16. Business Use

Scrap analysis can support quality monitoring.
It can support production review.
It can support cost review.

## 17. Dataset Limitation

The data is illustrative.
It is not official IITM data.

## 18. Revision

Production → Scrap → Good Units → Scrap Rate.

## 19. Learning Outcome

You should be able to calculate scrap rate.
You should be able to compare scrap across dimensions.

## 🔁 Important Relationship

Production Units = Good Units + Scrap Units.

Scrap Units = Production Units - Good Units.

Scrap Rate = Scrap Units / Production Units.

## 📊 Analysis Dimensions

Product is one dimension.
Month is one dimension.
Region is one dimension.

Each dimension can reveal a different pattern.

## 🧠 Analytical Discipline

Do not assume a high scrap rate automatically proves poor quality.
Use the available data to describe the observed pattern.
Additional data may be needed for explanation.

## 🏁 Final Revision

Production → Scrap → Good Units → Scrap Rate → Cost → Analysis

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-Scrap%20Analysis-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Scrap%20Analysis-green?style=flat-square)
![Analytics](https://img.shields.io/badge/Analytics-Manufacturing-orange?style=flat-square)