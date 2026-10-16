![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-074-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 074 Cheat Sheet — Credit Product Analysis

## 🔢 Formulas

- Utilisation % = utilised / limit × 100.
- Available credit = limit − utilised.
- Activity index = transactions × activity score / 100.
- Overall utilisation = total utilised / total limit × 100.

## 📌 Fields

- Customer_ID = identifier.
- Customer_Segment = grouping.
- Region = geography.
- Credit_Product = product.
- Credit_Limit_Rupee = capacity.
- Credit_Utilised_Rupee = usage.
- Transactions_Lakh = volume.
- Repayment_Score = synthetic repayment measure.
- Customer_Activity_Score = synthetic activity measure.

## 💳 Products

- PayLater → purchase credit.
- Credit Line → reusable facility.
- Merchant Credit → merchant activity.
- Working Capital → operating finance.

## 📊 KPIs

- Total customers.
- Total credit limit.
- Total utilised credit.
- Overall utilisation %.
- Total transactions.
- Average repayment score.
- Average activity score.

## 🐼 Pandas

- pd.read_excel loads the workbook.
- pd.to_numeric converts values.
- groupby creates groups.
- agg creates multiple summaries.
- to_csv exports results.

## 📈 Chart Choice

- Doughnut → composition.
- Column → category comparison.
- Line → ordered comparison.
- Scatter → two numeric variables.

## 🔍 Checks

- Check numerator.
- Check denominator.
- Check unit.
- Check population.
- Check missing values.
- Reconcile totals.

## ⚠️ Avoid

- Do not label synthetic data as real company data.
- Do not treat activity score as creditworthiness.
- Do not claim causation.
- Do not ignore denominators.

## 📂 Workbook Map

- Raw → PayBuddy_Credit_Data.
- Product → Credit_Product_Summary.
- Customer → Customer_Summary.
- Type → Credit_Product_Type.
- Region → Region_Summary.
- Segment → Customer_Segment_Summary.
- KPIs → Credit_KPIs.
- Dashboard → PayBuddy_Credit_Dashboard.

## 🧪 Examples

- 50,000 limit and 20,000 used gives 40% utilisation.
- 50,000 limit and 20,000 used leaves 30,000 available.
- 10 lakh transactions and score 80 gives activity index 8.

## 🏅 Badges

- ⚡ Quick Revision
- 💳 Credit
- 📊 KPI
- 🐍 Pandas
- 📗 Excel
- 🎯 BDM

## 📝 Exam Flow

- Define.
- Calculate.
- Compare.
- Visualise.
- Interpret.
- Validate.