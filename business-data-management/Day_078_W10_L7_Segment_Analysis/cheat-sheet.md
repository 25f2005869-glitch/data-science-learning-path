![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-078-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 078 Cheat Sheet — Segment Analysis

## 👥 Segmentation

- Segment → meaningful customer group.
- Consumer → individual-oriented.
- Retail → retail-oriented.
- Business → business-oriented.
- Investor → investment-oriented.

## 📊 Core Measures

- Active customers.
- Transactions.
- Transaction value.
- Digital adoption.
- Satisfaction.

## 🧮 Formulas

- Customer Share % = segment customers / total customers × 100.
- Transaction Value Share % = segment value / total value × 100.
- Transactions per Customer = transactions / active customers.
- Value per Customer = transaction value / customer scale.
- Engagement Index = digital adoption × satisfaction / 100.
- Customer Value Index = value per customer × satisfaction.

## 📌 Interpretation

- Size → how large is the segment?
- Activity → how active is the segment?
- Value → how much monetary activity is represented?
- Adoption → how digitally engaged is the segment?
- Satisfaction → what synthetic experience score is observed?

## 📗 Excel

- COUNTIF → count segment records.
- SUMIF → segment totals.
- AVERAGEIF → segment averages.
- SUMIFS → multiple-condition totals.
- COUNTIFS → multiple-condition counts.
- PivotTable → multi-dimensional segmentation.
- IF → classification.
- XLOOKUP → lookup segment attributes.

## 🐼 Pandas

- df.groupby("Customer_Segment").
- df.pivot_table().
- df.value_counts().
- df["Customer_Segment"].nunique().
- df["Transactions_per_Customer"].
- pd.cut() → activity bands.
- df.merge() → combine tables.
- df.sort_values() → rank results.

## 📈 Charts

- Column → segment comparison.
- Line → ordered category comparison.
- Scatter → two numeric variables.
- Cross-tab → structural comparison.

## 🔍 Quality Checks

- Duplicate IDs.
- Missing segments.
- Missing numeric values.
- Invalid categories.
- Unit consistency.
- Denominator consistency.

## ⚠️ Do Not Confuse

- Customers ≠ records.
- Transactions ≠ transaction value.
- Transaction value ≠ profit.
- Segment size ≠ profitability.
- Correlation ≠ causation.
- Synthetic data ≠ real market evidence.

## 📂 Workbook Map

- Raw → Segment_Data.
- Segment metrics → Segment_Summary.
- Player mix → Player_Segment_Analysis.
- Geography → Region_Segment_Analysis.
- Industry → Industry_Segment_Analysis.
- Product → Product_Segment_Analysis.
- Activity → Activity_Level_Analysis.
- KPIs → Segment_KPIs.
- Quality → Data_Review.
- Dashboard → Segment_Analysis_Dashboard.

## 🏅 Badges

- ⚡ Quick Revision.
- 👥 Segmentation.
- 📊 Analytics.
- 📗 Excel.
- 🐍 Pandas.
- 💳 Finance.

## 📝 Analysis Sequence

- Define → measure → normalise → compare → cross-tabulate → visualise → interpret → validate.