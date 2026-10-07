![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-048-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 048 Cheat Sheet — Production Scheduling

## 🔢 Core Formulas

Variance Units = Actual Production - Planned Production.

Variance % = Variance Units / Planned Production.

Plan Achievement % = Actual Production / Planned Production.

## 📌 Excel Functions

SUMIF → aggregation using one condition.

SUMIFS → aggregation using multiple conditions.

COUNTIF → count one condition.

COUNTIFS → count multiple conditions.

RANK → ranking numeric values.

IFERROR → error handling.

## 🧮 Formula Patterns

=Actual-Planned

=Variance/Planned

=Actual/Planned

=SUMIF(ProductRange,"Gears",ActualRange)

=SUMIFS(ActualRange,ProductRange,"Gears",RegionRange,"North")

## 🗂️ Workbook Map

Production_Scheduling_Data → raw data.

Production_Plan → planned output.

Actual_Production → actual output.

Plan_vs_Actual → comparison.

Product_Summary → product analysis.

Monthly_Production → monthly analysis.

Variance_Analysis → product-region analysis.

Scheduling_Questions → practice.

Business_Insights → observations.

Data_Dictionary → field definitions.

Production_Working → calculation logic.

Production_Scheduling_Dashboard → visual summary.

Instructions → execution sequence.

## 📊 Chart Selection

Column chart → planned versus actual.

Line chart → monthly production trend.

Column chart → variance by product.

Column chart → plan achievement by month.

## 🧠 Interpretation

Positive variance means actual exceeds plan.

Negative variance means actual is below plan.

Achievement near 100% means actual is close to plan.

Variance identifies a difference.

Variance does not automatically identify the cause.

## 🐍 Python Patterns

df.groupby("Product")["Planned_Production"].sum()

df.groupby("Product")["Actual_Production"].sum()

df.groupby("Month")["Actual_Production"].sum()

df.groupby(["Product","Region"])["Actual_Production"].sum()

df.pivot_table(index="Month", values="Actual_Production", aggfunc="sum")

## 📊 Validation

Check total planned production.

Check total actual production.

Check variance calculation.

Check plan achievement.

Check product totals.

Check monthly totals.

Check product-region totals.

## 🎯 Presentation Order

Start with total plan.

Show total actual.

Show total variance.

Show product comparison.

Show monthly trend.

Show plan achievement.

Show product-region variance.

## 📝 Business Statement

Observation → Evidence → Interpretation

Example:

"Actual production differs from the plan. The difference is visible in the Plan_vs_Actual sheet."

## ⚠️ Important

Do not claim a cause without supporting data.

Do not treat illustrative data as official course data.

Always keep units visible.

## 🏁 Memory Line

Plan → Actual → Variance → Achievement → Product → Month → Region

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-Production%20Scheduling-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Plan%20vs%20Actual-green?style=flat-square)
![Analytics](https://img.shields.io/badge/Analytics-Variance-orange?style=flat-square)