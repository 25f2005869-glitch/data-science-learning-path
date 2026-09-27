# 📘 Day 021 — Notes: Introduction to E-Commerce

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-blue)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-orange)
![Day](https://img.shields.io/badge/Day-021-green)
![Topic](https://img.shields.io/badge/Topic-Introduction%20to%20E--Commerce-purple)

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 021  
**Topic:** Introduction to E-Commerce  

---

## 1. Lecture
**W5_L1 — Introduction to E-Commerce** is the focus of Day 021.
The objective is to understand e-commerce from a business-data perspective.
The later W5 lectures move into the e-commerce case study.

## 2. E-Commerce
E-commerce refers to business activity conducted through digital or online channels.
Customers can discover, compare and purchase products digitally.
Digital transactions create data that can be analysed.
Business analysis converts this data into useful summaries and observations.

## 3. Business View
An e-commerce business can be studied through time, product, channel and geography.
The workbook uses Month, Category, Channel and Region as dimensions.
These dimensions help split the data into meaningful groups.
Orders, Units and Revenue are the main measures.

## 4. Digital Channels
The sample workbook contains Website, App and Marketplace.
A website can operate as a direct digital sales channel.
An app provides another digital route for customer interaction.
A marketplace provides another route through a digital platform.

## 5. Categories
The sample categories are Electronics, Fashion and Grocery.
Categories help organise products into business groups.
Orders can be compared between categories.
Units and revenue can also be compared.

## 6. Time
Month is the time dimension in this workbook.
The sample period contains January through June.
Monthly grouping supports trend analysis.
A monthly summary makes comparison easier.

## 7. Orders
Orders represent transaction activity in the sample data.
Orders can be aggregated by month.
Orders can be aggregated by category.
Orders can also be compared by channel and region.

## 8. Units
Units represent the quantity sold.
Units are different from order count.
One order may contain more than one unit.
Therefore, units provide an additional business perspective.

## 9. Revenue
Revenue is a monetary measure.
The workbook records Revenue_Lakh.
Revenue can be aggregated by month.
Revenue can also be compared by category, channel and region.

## 10. Dimensions and Measures
Dimensions describe how records are grouped.
Measures are numerical quantities that can be calculated or aggregated.
Month, Category, Channel and Region are dimensions.
Orders, Units and Revenue are measures.

## 11. Aggregation
Aggregation combines detailed records into summaries.
SUM can calculate total values.
SUMIF can calculate conditional totals.
Pivot Tables can also group and aggregate business data.

## 12. Monthly Analysis
The Monthly_Summary sheet contains monthly Orders, Units and Revenue.
A revenue column chart supports month-to-month comparison.
An orders line chart supports trend interpretation.
The underlying numbers should always be checked before making conclusions.

## 13. Category Analysis
The Category_Summary sheet compares the three sample categories.
Orders show transaction activity.
Units show quantity.
Revenue shows monetary contribution.

## 14. Channel Analysis
The Channel_Summary sheet compares Website, App and Marketplace.
The same measures can be used for each channel.
Channel analysis can identify differences in sample performance.
Do not judge a channel using only one metric.

## 15. Regional Analysis
The Region_Summary sheet compares North, South, East and West.
Orders, Units and Revenue can be compared.
Region is useful as a geographical dimension.
The results describe the sample dataset only.

## 16. Dashboard
The Dashboard contains Total Orders, Total Units and Total Revenue.
It also contains Average Revenue per Order.
The dashboard includes monthly revenue, monthly orders and category revenue charts.
The charts use explicit colours for presentation.

## 17. Average Revenue per Order
The formula is:
**Total Revenue ÷ Total Orders**
It is a summary metric.
It should not automatically be interpreted as an individual customer order value.
It can be used for high-level comparison.

## 18. Data Quality
Inspect column names before analysis.
Check numerical fields and category labels.
Check for missing or inconsistent values.
Good data structure supports reliable analysis.

## 19. Python Extension
The repository contains `code/ecommerce_introduction.py`.
Pandas is used for tabular analysis.
Matplotlib is used for visualisation.
The script also exports summary CSV files.

## 20. Final Summary
E-commerce creates structured business data.
Dimensions provide useful ways to group that data.
Measures quantify business activity.
Day 021 provides the foundation for the following e-commerce case-study lectures.

**Status:** ✅ Complete