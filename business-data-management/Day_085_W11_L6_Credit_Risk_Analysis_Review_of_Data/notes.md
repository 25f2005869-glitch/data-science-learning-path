![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-085-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 085 — Detailed Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 085  
**Topic:** Credit Risk Analysis — Review of Data

## 1. Purpose of Data Review

Data review is performed before deeper analysis.

It helps an analyst understand:

- What the dataset contains.
- How observations are organised.
- Which fields are available.
- Whether important values are missing.
- Whether identifiers are duplicated.
- Whether categories are consistent.

## 2. Unit of Analysis

The unit of analysis describes what one row represents.

In this exercise, one row represents one customer-loan record.

This definition is important for every subsequent calculation.

## 3. Record Identifier

`Record_ID` is used to identify individual records.

A duplicate Record ID may indicate:

- Duplicate data.
- An incorrectly constructed dataset.
- A repeated record.
- A data-entry problem.

## 4. Customer Identifier

`Customer_ID` identifies the customer.

The analyst should determine whether one customer can legitimately have multiple records in the real business system.

## 5. Completeness

Completeness refers to whether required fields contain values.

The workbook provides a field-level missing-value review.

## 6. Missing Values

Missing values may occur because:

- Data was not collected.
- Data was not entered.
- A field was not applicable.
- A source system failed.
- A transformation removed a value.

## 7. Numeric Review

Numeric variables are reviewed using:

- Count
- Mean
- Median
- Minimum
- Maximum

These statistics provide an initial view of the data.

## 8. Age

Age is measured in years.

The analyst should inspect its minimum and maximum values.

Unusual values should be investigated rather than automatically deleted.

## 9. Monthly Income

`Monthly_Income_Rupee` represents illustrative monthly income.

Income provides context for loan exposure and affordability.

## 10. Loan Amount

`Loan_Amount_Rupee` represents illustrative credit exposure.

Exposure should be examined by product and other relevant segments.

## 11. Tenure

`Tenure_Months` represents the repayment horizon.

Loan amount without tenure may not provide the complete financial context.

## 12. Debt-to-Income

`Debt_to_Income_%` represents debt burden relative to income.

It is one risk-related variable.

It should not be treated as the complete definition of credit risk.

## 13. Credit Score

`Credit_Score` is an illustrative credit-history indicator.

The distribution of credit scores should be reviewed before segmentation.

## 14. Past Delinquencies

`Past_Delinquencies` records historical delinquency events.

It provides historical behavioural information.

## 15. Default Flag

`Default_Flag` represents the illustrative outcome.

It can be used to calculate the observed default rate.

## 16. High-Risk Flag

`High_Risk_Flag` represents a prepared risk indicator.

Its count and share can be reviewed separately from default.

## 17. Categorical Variables

Important categorical fields include:

- Employment type
- Region
- Loan product

Category frequencies should be inspected.

## 18. Category Consistency

Category values should be checked for:

- Spelling differences.
- Extra spaces.
- Different capitalisation.
- Unexpected categories.
- Blank categories.

## 19. Product Review

The product summary combines:

- Customer count
- Loan exposure
- Average credit score
- Average DTI
- Defaults
- Default rate

## 20. Regional Review

The regional summary provides descriptive comparisons across regions.

A regional difference does not automatically identify its cause.

## 21. Employment Review

Employment groups can be compared using:

- Customer count
- Income
- Loan amount
- Credit score
- DTI
- Defaults

## 22. Outcome Review

Outcome review separates:

- Default
- Non-default
- High-risk
- Not high-risk

This helps understand the sample composition.

## 23. Count Versus Rate

Counts and rates should not be confused.

A group with more customers can naturally have more defaults.

Default rate provides a denominator-based comparison.

## 24. Exposure

Exposure is the total amount of credit represented by the records.

It is different from customer count.

## 25. Data Types

Correct data types are essential.

Examples:

- Age → numeric
- Loan amount → numeric
- Region → categorical
- Loan product → categorical
- Default flag → binary

## 26. Outliers

An extreme value is not automatically an error.

The analyst should investigate:

- Source
- Business meaning
- Unit
- Timing
- Possible data-entry issue

## 27. Target Variable

For an illustrative default-prediction task, `Default_Flag` can serve as the target.

The target definition should be documented.

## 28. Feature Timing

A feature must be available at the time the prediction is supposed to be made.

Using future information can create leakage.

## 29. Target Leakage

Target leakage happens when information that should not be available at prediction time enters the modelling data.

Leakage can make evaluation misleading.

## 30. Sample Size

This exercise contains only 30 synthetic records.

Such a small educational dataset is useful for learning calculations.

It is not sufficient to represent a real lending population.

## 31. Business Definitions

Real projects require precise definitions for terms such as:

- Default
- Delinquency
- Exposure
- Income
- High risk

## 32. Review Sequence

The recommended sequence is:

**Structure → Completeness → Uniqueness → Types → Categories → Outcomes → Exposure → Business Meaning**

## 🏅 Badges

- 🧠 Credit Risk Concepts
- 🔎 Data Quality
- 📊 Dataset Review
- 💼 Business Interpretation