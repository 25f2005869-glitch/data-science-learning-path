![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-049-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 049 Cheat Sheet — Scrap Analysis

## 🔢 Formulas

Good Units = Production Units - Scrap Units.
Scrap Rate = Scrap Units / Production Units.
Scrap Cost = Scrap Units × Unit Scrap Cost.

## 📌 Excel Functions

SUMIF → one-condition aggregation.
SUMIFS → multiple-condition aggregation.
COUNTIF → conditional count.
COUNTIFS → multiple conditional count.
IFERROR → error handling.
ROUND → rounding.

## 🧮 Formula Examples

=Production-Scrap

=Scrap/Production

=Scrap*Unit_Cost

=SUMIF(ProductRange,"Gears",ScrapRange)

=SUMIFS(ScrapRange,ProductRange,"Gears",RegionRange,"North")

## 🗂️ Sheets

Scrap_Analysis_Data → raw data.
Product_Scrap_Summary → product summary.
Monthly_Scrap → monthly summary.
Region_Scrap → regional summary.
Product_Region_Scrap → detailed summary.
Scrap_Questions → questions.
Business_Insights → insights.
Data_Dictionary → fields.
Scrap_Working → logic.
Dashboard → charts.
Instructions → workflow.

## 📊 Charts

Production versus scrap → column chart.
Monthly scrap rate → line chart.
Scrap units by product → column chart.
Scrap rate by region → column chart.

## 🧠 Interpretation

Scrap units measure volume.
Scrap rate measures proportion.
Good units measure usable output.
Scrap cost gives an illustrative cost view.

## ⚠️ Important

Do not infer a root cause from scrap rate alone.
Use supporting operational data.
Keep production volume in context.

## 🐍 Python

pd.read_excel() → read workbook.
groupby() → aggregate.
agg() → multiple metrics.
to_csv() → export summaries.
plt.bar() → bar chart.
plt.plot() → line chart.

## ✅ Validation

Check total production.
Check total scrap.
Check good units.
Check scrap rate.
Check product totals.
Check monthly totals.
Check regional totals.

## 🎯 Presentation

Start with total production.
Show total scrap.
Show overall scrap rate.
Show product comparison.
Show monthly trend.
Show regional comparison.
Show illustrative cost.

## 📝 Business Statement

Observation → Evidence → Interpretation.

## 🏭 Manufacturing Flow

Production
→ Scrap
→ Good Units
→ Scrap Rate
→ Cost
→ Analysis

## 🏁 Memory Line

Production → Scrap → Good Units → Scrap Rate → Cost → Analysis

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-Scrap%20Analysis-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Scrap%20Analysis-green?style=flat-square)
![Analytics](https://img.shields.io/badge/Analytics-Manufacturing-orange?style=flat-square)