![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-076-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 076 Notes — Main Players and Dataset

## 1. Case Purpose

- The case introduces the financial ecosystem through business data.
- A player-level dataset helps connect organisations with industries.
- Classification makes a large dataset easier to analyse.
- The focus is descriptive business-data analysis.

## 2. Main Player

- A player is an organisation or participant represented by a record.
- Player_ID provides a unique identifier.
- Player_Name provides an illustrative label.
- Player_Type classifies the participant.

## 3. Bank

- A bank is represented as one financial ecosystem player type.
- Bank records can be associated with payments or lending.
- The dataset measures customer and transaction activity.
- The synthetic examples are not real bank statistics.

## 4. NBFC

- NBFC stands for non-bank financial company.
- The case associates NBFC records mainly with lending.
- Transaction value provides a business-scale measure.
- Customer segments provide another analytical dimension.

## 5. Insurance

- Insurance is represented as a separate player type.
- Insurance products can be analysed by region.
- Digital adoption is included as a descriptive measure.
- Satisfaction is included as a synthetic measure.

## 6. Capital Market

- Capital Market players are associated with investment activity.
- Products include brokerage, trading and mutual funds.
- Investor is a customer segment used in the synthetic dataset.
- Transaction value provides an aggregate activity measure.

## 7. FinTech

- FinTech represents technology-led financial services in this case.
- FinTech records span multiple industries.
- Payments, lending, investment and compliance examples are included.
- Digital adoption is useful for descriptive comparison.

## 8. Industry

- Industry identifies the primary business domain.
- Payments describes transaction-oriented services.
- Lending describes credit-related services.
- Insurance describes risk-protection services.
- Investment describes capital and wealth activities.
- Compliance describes regulatory-technology activity.

## 9. Region

- Region provides a geographic grouping.
- The synthetic dataset uses North, South, West and East.
- Regional totals can be calculated with groupby.
- Regional comparisons should use consistent measures.

## 10. Product

- Primary_Product identifies the main product or service.
- Products can occur across different player types.
- Product-level aggregation can reveal business activity patterns.
- Product summaries complement player-type summaries.

## 11. Customer Segment

- Customer_Segment describes the main customer group.
- Consumer represents individual-oriented activity.
- Retail represents retail-oriented activity.
- Business represents business-oriented activity.
- Investor represents investment-oriented activity.

## 12. Active Customers

- Active customers are measured in lakh in the dataset.
- The unit should always be shown in analysis.
- Totals describe aggregate customer scale.
- Average values answer a different question from totals.

## 13. Transactions

- Transaction volume is measured in lakh.
- Transactions can be grouped by player type.
- Transactions can be grouped by region.
- Transaction volume should not be confused with transaction value.

## 14. Transaction Value

- Transaction value is measured in crore.
- It represents monetary activity in the synthetic case.
- Total value can be compared across industries.
- Value per customer provides a normalised measure.

## 15. Digital Adoption

- Digital adoption is stored as a percentage.
- It is averaged in group summaries.
- It describes the synthetic dataset only.
- It should not be treated as a real digital-adoption benchmark.

## 16. Satisfaction

- Satisfaction score is a synthetic numeric measure.
- It supports descriptive comparison.
- It should not be interpreted as an audited customer metric.
- Group averages can hide individual variation.

## 17. Engagement Index

- Engagement Index is constructed for practice.
- Formula: digital adoption × satisfaction / 100.
- It combines two descriptive fields.
- It is not presented as an industry-standard metric.

## 18. Data Dictionary

- A data dictionary explains field meaning.
- It documents units and data types.
- It reduces ambiguity during analysis.
- It improves reproducibility.

## 19. Dashboard Reading

- Start with player-type composition.
- Move to industry transaction value.
- Inspect regional activity.
- Review the scatter relationship.
- Return to summary tables before writing observations.

## 20. Learning Outcome

- Classify financial players.
- Read a structured business dataset.
- Aggregate by multiple dimensions.
- Calculate descriptive KPIs.
- Interpret charts carefully.
- Document data limitations.

## 🏅 Badges

- 💳 Ecosystem.
- 🏢 Industry.
- 🗺️ Region.
- 📊 Dataset.
- 🐍 Python.
- 📗 Excel.