![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-084-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 084 — Detailed Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 084  
**Topic:** Explanation of Credit Risk Dataset

## 1. Dataset Purpose
A credit-risk dataset combines customer, financial, loan and repayment information.
The first analytical task is understanding what every field represents.

## 2. Unit of Analysis
One row in this exercise represents one customer-loan record.
This definition controls how counts and rates should be calculated.

## 3. Identifiers
`Record_ID` identifies a row.
`Customer_ID` identifies a customer.
Identifiers are useful for uniqueness checks but are not automatically predictive variables.

## 4. Customer Information
`Age` describes the customer age in years.
`Employment_Type` provides an illustrative employment category.
These fields support descriptive segmentation.

## 5. Geographic Information
`Region` groups records geographically.
Regional comparisons are descriptive and require context before explanations are made.

## 6. Loan Information
`Loan_Product` identifies the loan category.
`Loan_Amount_Rupee` measures exposure.
`Tenure_Months` represents the repayment horizon.

## 7. Income Information
`Monthly_Income_Rupee` is the income input.
`Annual_Income_Rupee` is derived by multiplying monthly income by twelve.

## 8. Affordability
`Debt_to_Income_%` describes debt burden relative to income.
`Loan_to_Annual_Income_%` compares loan exposure with annual income.

## 9. Credit History
`Credit_Score` is a numeric credit-history indicator in this synthetic exercise.
`Past_Delinquencies` records previous delinquency events.

## 10. Outcome Fields
`Default_Flag` is the illustrative default outcome.
`High_Risk_Flag` is a prepared high-risk indicator.

## 11. Credit Score Bands
The workbook creates five descriptive score groups:
Very Low, Low, Moderate, Good and Very Good.
Banding simplifies segment comparisons.

## 12. Risk Level
A score-derived risk level is also provided.
The labels are intended for educational grouping rather than real underwriting.

## 13. Risk Score
The illustrative composite score combines:
- credit-score distance from 750,
- DTI,
- past delinquencies,
- default history.

## 14. Risk Band
The composite score is grouped into Low, Medium and High.
The thresholds are learning assumptions.

## 15. Product Summary
Product analysis combines customer count, exposure, score, DTI, defaults and high-risk count.
Default rate should always be interpreted with its denominator.

## 16. Region Summary
Region analysis compares customer count, exposure, score, DTI and defaults.
A regional pattern does not automatically reveal its cause.

## 17. Employment Summary
Employment groups can be compared on income, loan amount, score, DTI and defaults.
No single field should be treated as a complete risk explanation.

## 18. Data Dictionary
A data dictionary records the field name, type and meaning.
It helps prevent incorrect interpretation.

## 19. Data Quality
Check missing values, duplicate identifiers, inconsistent categories, invalid ranges and flag values.
These checks should occur before modelling.

## 20. Target
If default prediction is being demonstrated, `Default_Flag` can act as the target.
The target definition must be explicit.

## 21. Leakage
A feature that contains information from after the target event can cause leakage.
Feature timing must therefore be reviewed.

## 22. Counts and Rates
A count tells how many records meet a condition.
A rate places that count against an appropriate denominator.

## 23. Exposure Context
Two groups can have similar customer counts but different total loan exposure.
Exposure should therefore be analysed separately.

## 24. Correlation
A relationship between two variables does not prove causation.
Descriptive analysis should not be written as a causal conclusion.

## 25. Sample Size
The workbook contains only 30 synthetic records.
Small samples can make percentages sensitive to individual observations.

## 26. Synthetic Data
The records are designed for education.
They are not official financial records.

## 27. Recommended Workflow
**Understand → Validate → Summarise → Visualise → Interpret → Document**

## 28. Reading a Numeric Field
A numeric field can be measured, averaged and grouped, but its business meaning still matters.
For example, a loan amount is meaningful only when the currency and exposure definition are known.

## 29. Reading a Categorical Field
Categorical values should be checked for consistent spelling.
Different spellings can create separate groups during analysis.

## 30. Counts Versus Rates
A group with more defaults may simply contain more customers.
Default rate normalises the count by the number of customers.

## 31. Exposure Context
Two groups can have similar customer counts but very different total loan exposure.
Therefore exposure should be included in risk interpretation.

## 32. Reproducible Analysis
The same calculation should produce the same result when the same input and formula are used.
Documenting formulas makes the analysis easier to audit.

## 🏅 Badges
- 🧠 Credit Risk Concepts
- 🗂️ Data Dictionary
- 📊 Descriptive Analysis
- 💼 Business Interpretation