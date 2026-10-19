![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-084-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 084 — Credit Risk Dataset Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 084  
**Topic:** Explanation of Credit Risk Dataset

## 🔑 Variable Groups
- Customer → `Customer_ID`, `Age`, `Employment_Type`
- Geography → `Region`
- Loan → `Loan_Product`, `Loan_Amount_Rupee`, `Tenure_Months`
- Income → `Monthly_Income_Rupee`
- Affordability → `Debt_to_Income_%`
- Credit → `Credit_Score`, `Past_Delinquencies`
- Outcome → `Default_Flag`, `High_Risk_Flag`

## 🧮 Core Formulas
`Annual Income = Monthly Income × 12`

`Loan-to-Income % = Loan Amount / Annual Income × 100`

`Installment Estimate = Loan Amount / Tenure`

`Default Rate % = Defaults / Customers × 100`

`High-Risk Share % = High-Risk Customers / Total Customers × 100`

## 📊 Excel Functions
- `SUM`
- `AVERAGE`
- `COUNT`
- `COUNTIF`
- `COUNTIFS`
- `SUMIF`
- `SUMIFS`
- `AVERAGEIF`
- `AVERAGEIFS`
- `IF`
- `AND`
- `OR`
- `ROUND`
- `MAX`
- `MIN`
- `MEDIAN`

## 🧪 Quality Checks
1. Count rows.
2. Check unique `Record_ID`.
3. Check unique `Customer_ID`.
4. Check missing values.
5. Check data types.
6. Check category spelling.
7. Check age range.
8. Check income range.
9. Check loan range.
10. Check 0/1 flags.

## 📌 Score Bands
| Score | Band |
|---|---|
| ≤649 | Very Low |
| 650–699 | Low |
| 700–749 | Moderate |
| 750–799 | Good |
| 800+ | Very Good |

## 📌 Composite Risk Bands
| Risk Score | Band |
|---|---|
| ≤35 | Low |
| 36–60 | Medium |
| >60 | High |

## 🐍 Python Pattern
`read_excel()` loads the input.
`to_numeric()` standardises numeric columns.
`groupby()` creates business summaries.
`agg()` calculates several measures.
`pd.cut()` creates bands.
`to_csv()` exports tables.
`matplotlib` creates charts.

## 📈 Chart Selection
- Category comparison → Column.
- Regional ordered comparison → Line.
- Simple composition → Doughnut.
- Two numeric variables → Scatter.

## 🚨 Avoid
- Treating IDs as predictors.
- Comparing default counts without denominators.
- Ignoring loan exposure.
- Ignoring income.
- Mixing units.
- Treating correlation as causation.
- Treating synthetic risk scores as real policy.
- Ignoring feature timing.

## 🧷 Field Classification
- ID → identify records.
- Category → segment observations.
- Numeric → measure quantity.
- Flag → represent a binary outcome.
- Derived → calculated from other fields.

## 🔎 Five Questions Before Any Metric
1. What is the unit of analysis?
2. Which denominator should be used?
3. What unit is being measured?
4. When is the field known?
5. Is the field raw or derived?

## 📐 Rate Reminder
Never report a percentage without its denominator.
Default rate requires both default count and customer count.

## 🧮 Python Grouping Pattern
`df.groupby("Loan_Product").agg(...)`
Use grouping to convert row-level data into business summaries.

## 🗃️ Audit Reminder
Save the input file, formula definitions and output tables together.
That makes the analysis easier to reproduce.

## 🎯 Revision Formula
**Customer + Income + Loan + Credit History + Outcome = Core Credit-Risk Dataset**

## 🏅 Badges
- ⚡ Quick Revision
- 💳 Credit Analytics
- 🧮 Formula Practice
- 🐍 Python