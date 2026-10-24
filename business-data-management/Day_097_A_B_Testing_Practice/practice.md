# 📝 Day 097 — A/B Testing Practice

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-Day%20097-blue?style=for-the-badge)
![A/B Testing](https://img.shields.io/badge/A%2FB%20Testing-Practice-green?style=for-the-badge)
![Excel](https://img.shields.io/badge/Tool-Microsoft%20Excel-orange?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 097
- **Topic:** A/B Testing Practice

---

# 1. 📌 Data Understanding

### Q1. What is A/B testing?

### Q2. What is the purpose of a Control Group?

### Q3. What is the purpose of a Treatment Group?

### Q4. In this project, which group represents the Control?

### Q5. In this project, which group represents the Treatment?

### Q6. What is the main business metric being analysed?

### Q7. What other metrics are used in the experiment?

---

# 2. 🔍 Dataset Understanding

### Q8. What does `User_ID` represent?

### Q9. What does the `Group` column represent?

### Q10. What does `Customer_Segment` represent?

### Q11. What does the `Visitors` column represent?

### Q12. What does the `Converted` column represent?

### Q13. What does `Order_Value` represent?

### Q14. What does `Revenue` represent?

### Q15. What does `Conversion_Status` represent?

---

# 3. 🧹 Data Quality Practice

Inspect the `Raw_AB_Test_Data` sheet.

### Q16. Check whether duplicate User_ID records exist.

### Q17. Check whether Group contains values other than A and B.

### Q18. Check for extra spaces in text fields.

### Q19. Check for inconsistent capitalization in Customer_Segment.

### Q20. Check for missing Age values.

### Q21. Check for invalid or negative Age values.

### Q22. Check for missing Visitors values.

### Q23. Check for invalid Visitors values.

### Q24. Check whether Converted contains values other than 0 and 1.

### Q25. Check for missing Order_Value values.

### Q26. Check for negative Order_Value values.

### Q27. Check whether Revenue contains invalid values.

### Q28. Check whether Conversion_Status is consistent with Converted.

---

# 4. 🧼 Data Cleaning Practice

Use the `AB_Test_Cleaning` sheet.

### Q29. Remove unnecessary spaces from Group.

### Q30. Standardise Group values as A and B.

### Q31. Standardise Customer_Segment values.

### Q32. Standardise Device values.

### Q33. Standardise Channel values.

### Q34. Handle missing or invalid Age values.

### Q35. Handle missing or invalid Visitors values.

### Q36. Make sure Converted contains only 0 and 1.

### Q37. Handle missing Order_Value values.

### Q38. Handle negative Order_Value values.

### Q39. Recalculate Revenue.

### Q40. Rebuild Conversion_Status.

### Q41. Remove exact duplicate records.

---

# 5. 📊 Conversion Analysis

Use the `Conversion_Analysis` sheet.

### Q42. Calculate total Visitors for Group A.

### Q43. Calculate total Visitors for Group B.

### Q44. Calculate total Conversions for Group A.

### Q45. Calculate total Conversions for Group B.

### Q46. Calculate the Conversion Rate for Group A.

### Q47. Calculate the Conversion Rate for Group B.

### Q48. Calculate the difference between the two Conversion Rates.

### Q49. Create a chart comparing Conversion Rate by Group.

---

# 6. 💰 Revenue Analysis

Use the `Revenue_Analysis` sheet.

### Q50. Calculate total Revenue for Group A.

### Q51. Calculate total Revenue for Group B.

### Q52. Calculate Average Order Value for Group A.

### Q53. Calculate Average Order Value for Group B.

### Q54. Compare Revenue with Conversion volume.

### Q55. Create a chart comparing Revenue by Group.

---

# 7. 👥 Customer Segment Analysis

Use the `Segment_Analysis` sheet.

Analyse these segments:

- New
- Regular
- Loyal
- At Risk

### Q56. Calculate Visitors by Segment and Group.

### Q57. Calculate Conversions by Segment and Group.

### Q58. Calculate Conversion Rate by Segment and Group.

### Q59. Calculate Revenue by Segment and Group.

### Q60. Calculate Average Order Value by Segment and Group.

### Q61. Identify differences in conversion behaviour across segments.

---

# 8. 📅 Daily A/B Testing Analysis

Use the `Daily_AB_Test` sheet.

### Q62. Calculate daily Visitors for each group.

### Q63. Calculate daily Conversions for each group.

### Q64. Calculate daily Conversion Rate.

### Q65. Calculate daily Revenue.

### Q66. Create a line chart for daily Conversion Rate.

### Q67. Review whether the daily pattern is consistent throughout the experiment period.

---

# 9. 📈 KPI Practice

Use the `AB_Test_KPI` sheet.

Calculate:

### Q68. Total Visitors

### Q69. Total Conversions

### Q70. Conversion Rate

### Q71. Total Revenue

### Q72. Average Order Value

Create a KPI comparison between:

- Control (A)
- Treatment (B)

---

# 10. 🔄 Pivot-Style Analysis

Use the `Pivot_Group` sheet.

### Q73. Create a group-level summary.

Include:

- Group
- Visitors
- Conversions
- Conversion Rate
- Revenue

---

Use the `Pivot_Segment` sheet.

### Q74. Create a segment-level summary.

Include:

- Segment
- Group
- Visitors
- Conversions
- Revenue

---

# 11. 📊 Chart Practice

Using the `Charts` sheet, review:

### Q75. Conversion Rate by Group

What does the chart show?

### Q76. Revenue by Group

What does the chart show?

### Q77. Daily Conversion Rate Trend

What patterns can you observe?

---

# 12. 🧮 Excel Formula Practice

### Q78. Write the formula for Conversion Rate.

### Q79. Write the formula for Average Order Value.

### Q80. Write the formula for Revenue.

### Q81. Which Excel function can be used to count conversions?

### Q82. Which Excel function can be used to calculate total revenue by group?

### Q83. Which Excel functions can be used to clean text spaces?

---

# 13. 🧪 Statistical Concepts

### Q84. What is a Null Hypothesis?

### Q85. Write the conceptual Null Hypothesis for the conversion-rate experiment.

### Q86. What is an Alternative Hypothesis?

### Q87. Write the conceptual Alternative Hypothesis.

### Q88. What is a p-value?

### Q89. What is a confidence interval?

### Q90. Why is sample size important in A/B testing?

### Q91. Why is randomisation important?

---

# 14. 💼 Business Analysis

### Q92. What business question is this A/B test trying to examine?

### Q93. Which metrics should be considered together rather than individually?

### Q94. Why should revenue be analysed along with conversion volume?

### Q95. Why is segment-level analysis useful?

### Q96. Why is daily analysis useful?

### Q97. Why does a numerical difference between Group A and Group B not automatically establish statistical significance?

### Q98. What limitations should be mentioned when reporting this synthetic experiment?

---

# 15. 🐍 Python Practice

Use the `ab_testing_practice.py` file.

### Q99. Load the Excel workbook using Pandas.

### Q100. Read the `Raw_AB_Test_Data` sheet.

### Q101. Inspect the dataset using:

- `head()`
- `info()`
- `describe()`
- `isna().sum()`

### Q102. Clean the text columns.

### Q103. Handle missing numeric values.

### Q104. Validate the Converted column.

### Q105. Remove duplicate records.

### Q106. Recalculate Revenue.

### Q107. Separate Control and Treatment groups.

### Q108. Calculate Conversion Rate using Pandas.

### Q109. Calculate Revenue by Group.

### Q110. Calculate Average Order Value by Group.

### Q111. Analyse Customer Segments.

### Q112. Create a daily Conversion Rate analysis.

### Q113. Create charts using Matplotlib.

---

# 16. 🚀 Final A/B Testing Task

Create a short A/B testing report containing:

### Experiment Objective

Explain what the experiment is measuring.

### Control Group

Describe Group A.

### Treatment Group

Describe Group B.

### Data Quality

List the major data-quality issues and cleaning steps.

### Conversion Analysis

Report:

- Visitors
- Conversions
- Conversion Rate

### Revenue Analysis

Report:

- Revenue
- Average Order Value

### Segment Analysis

Summarise the segment-level observations.

### Daily Analysis

Describe the daily conversion-rate pattern.

### Statistical Consideration

Explain why statistical significance and uncertainty should be considered.

### Limitations

Mention the limitations of the synthetic dataset and experiment.

---

# 17. ⭐ Challenge Questions

### Q114. Why might two groups have different conversion rates even when there is no real treatment effect?

### Q115. Why should an A/B test define its primary metric before analysing the results?

### Q116. Why can looking at many metrics or segments create interpretation challenges?

### Q117. Why should an experiment not be judged using revenue alone?

### Q118. Why is data cleaning especially important in an A/B test?

### Q119. What could happen if duplicate visitors are included in the analysis?

### Q120. Why should statistical results be interpreted together with the experiment design?

---

# 18. 📋 Final Checklist

- [ ] Understand A/B testing
- [ ] Identify Control Group
- [ ] Identify Treatment Group
- [ ] Inspect raw data
- [ ] Identify data-quality issues
- [ ] Clean the dataset
- [ ] Validate the cleaned data
- [ ] Calculate Conversion Rate
- [ ] Calculate Revenue
- [ ] Calculate Average Order Value
- [ ] Analyse customer segments
- [ ] Analyse daily trends
- [ ] Calculate KPIs
- [ ] Create Pivot-style summaries
- [ ] Create charts
- [ ] Review statistical concepts
- [ ] Complete Python analysis
- [ ] Write final business analysis

---

# 🎯 Key Practice Goal

The main goal of Day 097 is to practise the complete A/B testing workflow:

**Raw Data**

→ **Data Quality**

→ **Cleaning**

→ **Validation**

→ **Conversion Analysis**

→ **Revenue Analysis**

→ **Segment Analysis**

→ **Daily Analysis**

→ **KPI Analysis**

→ **Visualisation**

→ **Statistical Consideration**

→ **Business Interpretation**

---

## 🔑 Key Takeaway

**A/B testing practice combines data cleaning, KPI calculation, group comparison, segmentation, visualisation and statistical thinking to understand experimental business data.**