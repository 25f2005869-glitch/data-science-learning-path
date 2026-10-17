![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-077-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 077 Notes — Review of Data and Basic Statistics

## 1. Why Data Review Comes First
- Analysis should begin with understanding the dataset.
- A statistic is meaningful only when its underlying field is understood.
- Data review reduces avoidable interpretation errors.
- The PayBuddy dataset is synthetic for learning.

## 2. Record Structure
- Each row represents one player record.
- Player_ID identifies the record.
- Player_Name is an illustrative label.
- Player_Type identifies the ecosystem category.
- Industry identifies the business domain.

## 3. Dimensions
- Region provides geographic grouping.
- Primary_Product identifies the main product.
- Customer_Segment identifies the customer group.
- Dimensions are useful for grouped analysis.
- Dimensions should use consistent category labels.

## 4. Numeric Measures
- Active_Customers_Lakh measures customer scale.
- Transactions_Lakh measures transaction volume.
- Transaction_Value_Crore measures monetary activity.
- Digital_Adoption_% measures digital adoption.
- Satisfaction_Score is a synthetic score.

## 5. Data Quality
- Duplicate IDs can distort counts.
- Missing values can change averages.
- Incorrect numeric types prevent valid calculations.
- Inconsistent category labels split groups.
- Units must be checked before aggregation.

## 6. Count
- Count tells us how many observations are present.
- It is not the same as total transaction value.
- Count can be used to assess dataset coverage.
- Category frequency is a count-based analysis.

## 7. Mean
- Mean equals total divided by number of observations.
- It is sensitive to unusually large or small observations.
- Mean is useful for average business measures.
- Mean should be accompanied by units.

## 8. Median
- Median is the middle value after sorting.
- It is less sensitive to extreme values than the mean.
- Comparing mean and median can reveal distribution shape.
- Median is especially useful when values are unevenly distributed.

## 9. Standard Deviation
- Standard deviation measures dispersion.
- A larger value indicates greater spread around the mean.
- It should be interpreted with the scale of the variable.
- It is not the same as the range.

## 10. Range
- Range equals maximum minus minimum.
- It describes the full observed spread.
- Range depends only on two observations.
- It can be affected by extreme values.

## 11. Quartiles
- Q1 marks the 25th percentile.
- Q3 marks the 75th percentile.
- The middle 50% lies between Q1 and Q3.
- IQR equals Q3 minus Q1.

## 12. Group Analysis
- Player_Type groups ecosystem participants.
- Industry groups business domains.
- Region groups geographic records.
- Product groups services.
- Customer segment groups customer categories.

## 13. Correlation
- Correlation measures linear association.
- Values near +1 indicate strong positive linear association.
- Values near -1 indicate strong negative linear association.
- Values near 0 indicate weak linear association.
- Correlation alone does not establish causality.

## 14. Derived Measures
- Transaction value per customer normalises monetary activity.
- Transactions per customer normalises volume.
- Engagement Index is a constructed learning metric.
- Derived metrics require clear formulas.

## 15. Dashboard Reading
- Begin with category-level charts.
- Check the scatter plot for relationship patterns.
- Confirm chart observations in summary tables.
- Use statistics to explain, not replace, the raw data.

## 16. Business Interpretation
- Descriptive statistics summarise the observed dataset.
- They do not automatically generalise to a wider market.
- Synthetic values should remain clearly labelled.
- Business conclusions need appropriate context.

## 17. Python Workflow
- pandas handles tabular analysis.
- groupby creates category summaries.
- agg calculates multiple statistics.
- corr creates a correlation matrix.
- matplotlib creates charts.

## 18. Learning Outcome
- Review data before analysis.
- Calculate basic statistics.
- Compare central tendency.
- Measure dispersion.
- Analyse categories.
- Interpret relationships responsibly.

## 🏅 Badges
- 📐 Statistics.
- 🔎 Data Review.
- 📊 Analysis.
- 🐍 Python.
- 📗 Excel.
- 💳 Finance.