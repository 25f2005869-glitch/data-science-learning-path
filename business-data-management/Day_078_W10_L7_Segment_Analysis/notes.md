![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-078-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 078 Notes — Segment Analysis

## 1. Meaning of Segmentation

- Segmentation divides a population into meaningful groups.
- A segment should have a clear definition.
- The same measure can behave differently across segments.
- Segmentation makes aggregate data easier to understand.

## 2. Customer Segment Field

- Customer_Segment is the main analysis dimension.
- The case uses Consumer, Retail, Business and Investor.
- Segment labels should remain consistent.
- Each record belongs to one illustrative segment.

## 3. Consumer

- Consumer represents individual-oriented activity.
- Consumer records can be studied using customer scale.
- Transaction activity provides a behavioural measure.
- Digital adoption provides a synthetic technology measure.

## 4. Retail

- Retail represents retail-oriented activity.
- Retail records can be compared with other segments.
- Transaction value measures monetary activity.
- Satisfaction provides an experience dimension.

## 5. Business

- Business represents business-oriented customers.
- Business activity can be linked with lending or compliance.
- Customer scale should be interpreted alongside transaction value.
- Average measures should not replace total measures.

## 6. Investor

- Investor represents investment-oriented customers.
- Investor records occur across capital-market and wealth-oriented products.
- Transaction activity provides a descriptive scale measure.
- Satisfaction and digital adoption add context.

## 7. Segment Size

- Segment size can be measured by record count.
- Active customers provide another size measure.
- Record count and customer count answer different questions.
- Customer share expresses segment scale relative to the dataset.

## 8. Transaction Volume

- Transactions_Lakh measures transaction volume.
- Volume indicates activity frequency at aggregate level.
- High volume does not necessarily mean high transaction value.
- Volume should be analysed with customer scale.

## 9. Transaction Value

- Transaction_Value_Crore measures monetary activity.
- Total value supports segment-level comparison.
- Transaction-value share expresses contribution to the dataset total.
- Value is not the same as revenue or profit.

## 10. Transactions per Customer

- Transactions per customer normalises volume by customer scale.
- Formula: transactions divided by active customers.
- Normalisation can make segments easier to compare.
- Units must remain consistent.

## 11. Transaction Value per Customer

- This metric normalises transaction value by active customers.
- In this workbook the output is expressed using lakh-based scaling.
- It helps compare monetary activity relative to customer scale.
- It should be interpreted as a synthetic analytical measure.

## 12. Engagement Index

- Engagement Index combines digital adoption and satisfaction.
- Formula: digital adoption × satisfaction / 100.
- It is created for learning.
- It is not a standard industry KPI.

## 13. Customer Value Index

- Customer Value Index combines value per customer and satisfaction.
- It is a constructed descriptive measure.
- The formula must be documented.
- It should not be interpreted as customer lifetime value.

## 14. Activity Levels

- Transactions per customer are used to create activity bands.
- Low Activity is the lowest band.
- Medium Activity represents the middle band.
- High Activity represents the highest band.
- The thresholds are synthetic learning assumptions.

## 15. Cross-Tabulation

- Player_Segment_Analysis connects player type and segment.
- Region_Segment_Analysis connects geography and segment.
- Industry_Segment_Analysis connects industry and segment.
- Product_Segment_Analysis connects products and segments.

## 16. Data Review

- Check duplicate player identifiers.
- Check missing segment values.
- Check numeric completeness.
- Check segment categories.
- Confirm units before calculations.

## 17. Dashboard

- Customer scale is shown by segment.
- Transaction value provides monetary comparison.
- Digital adoption provides a technology view.
- Scatter analysis connects customers and transaction value.

## 18. Business Interpretation

- Segmentation supports descriptive comparison.
- It can reveal differences hidden by overall averages.
- Segment metrics should be interpreted together.
- Synthetic data limits external conclusions.

## 19. Python

- pandas handles grouping.
- groupby creates segment summaries.
- pivot_table creates cross-tabulations.
- pd.cut creates activity bands.
- matplotlib creates charts.

## 20. Learning Outcome

- Define segments.
- Compare segment scale.
- Normalise activity.
- Analyse cross-segment structure.
- Build segment KPIs.
- Communicate findings responsibly.

## 🏅 Badges

- 👥 Segmentation.
- 📊 Data Analysis.
- 📐 Metrics.
- 🐍 Python.
- 📗 Excel.
- 💳 BDM.