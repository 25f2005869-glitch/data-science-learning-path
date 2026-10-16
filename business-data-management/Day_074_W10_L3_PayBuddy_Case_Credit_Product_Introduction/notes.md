![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-074-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 074 Notes — PayBuddy Credit Product Introduction

## 1. Case Context

- Digital finance businesses can offer different credit products.
- Products can serve different customer groups.
- Business data can describe product usage.
- This case focuses on introductory descriptive analysis.

## 2. Dataset Design

- There are 30 customer records.
- Each has an identifier.
- Each has a segment and region.
- Each has a credit product.
- Each has credit and activity measures.

## 3. PayLater

- Modelled as short-term purchase credit.
- Useful for consumer-oriented analysis.
- Customer count and utilisation can be measured.
- The synthetic category is for practice.

## 4. Credit Line

- Modelled as reusable credit capacity.
- Credit limit is an important field.
- Utilisation shows used capacity.
- Regional and segment comparisons are possible.

## 5. Merchant Credit

- Modelled for merchant activity.
- Merchant records have transaction measures.
- Utilisation can be compared across merchants.
- The case does not represent real underwriting.

## 6. Working Capital

- Modelled as operating finance.
- Small Business records use this product.
- Credit exposure can be aggregated.
- Activity can be compared descriptively.

## 7. Credit Limit

- Represents credit capacity in the case.
- Stored in rupees.
- Should be interpreted with utilisation.
- A larger limit does not automatically mean larger usage.

## 8. Credit Utilised

- Represents used credit.
- Stored in rupees.
- Can be summed by product.
- Can be summed by region or segment.

## 9. Utilisation

- Formula is utilised credit divided by limit multiplied by 100.
- It is a percentage.
- It standardises usage relative to capacity.
- It is descriptive in this dataset.

## 10. Available Credit

- Formula is limit minus utilised credit.
- It represents unused capacity.
- It can be measured per customer.
- It can be aggregated by product.

## 11. Activity

- Transactions are measured in lakh units.
- Customer Activity Score is synthetic.
- The score is not a real bureau score.
- The variables are included for practice.

## 12. Activity Index

- The constructed index multiplies transactions by activity score and divides by 100.
- It combines two descriptive measures.
- It is not presented as an industry-standard metric.
- Use it only as an analytical exercise.

## 13. Repayment Score

- This field is synthetic.
- It demonstrates repayment-related data.
- It should not be treated as a real score.
- It cannot establish lending outcomes.

## 14. Product Summary

- Counts customers by product.
- Totals credit limit.
- Totals utilised credit.
- Calculates average utilisation.
- Totals transaction volume.
- Calculates average repayment score.

## 15. Region Summary

- Counts customers by region.
- Totals credit limit.
- Totals utilised credit.
- Calculates average utilisation.
- Totals transaction volume.
- Calculates average activity score.

## 16. Segment Summary

- Separates Consumer.
- Separates Merchant.
- Separates Small Business.
- Supports descriptive group comparison.

## 17. Data Quality

- Check IDs.
- Check blanks.
- Check numeric types.
- Check negative values.
- Check category spelling.
- Check utilised credit against limit.

## 18. Dashboard Reading

- Start with product composition.
- Read the utilised-credit comparison.
- Read regional activity.
- Inspect the scatter plot.
- Return to the raw table before making a strong claim.

## 19. Learning Outcome

- Explain product categories.
- Calculate utilisation.
- Calculate available credit.
- Group dimensions.
- Build KPIs.
- Choose chart types.
- State limitations.

## 🏅 Badges

- 💳 Credit Products
- 📊 Product Analytics
- 🗺️ Region Analysis
- 🧑‍💼 Segmentation
- 🧮 KPIs
- 🐍 Python