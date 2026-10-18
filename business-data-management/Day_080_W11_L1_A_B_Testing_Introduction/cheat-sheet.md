![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-080-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 080 Cheat Sheet — A/B Testing Introduction

## Core Terms
- A/B Test → comparison experiment.
- Control → reference variant.
- Treatment → changed variant.
- Exposure → received experience.
- Outcome → measured response.
- Binary Outcome → 0/1 result.

## Core Variables
- Variant.
- Exposed_Flag.
- Clicked.
- Purchased_Flag.
- Order_Value_Rupee.
- Customer_Segment.
- Region.
- Device.

## Core Formulas
- Click Rate % = Clicks / Exposures × 100.
- Conversion Rate % = Purchases / Exposures × 100.
- Absolute Lift = Treatment Rate − Control Rate.
- Relative Lift % = Absolute Lift / Control Rate × 100.
- Average Order Value = Total Purchase Value / Purchases.

## Example
- Control = 5% conversion.
- Treatment = 6%.
- Absolute lift = 1 percentage point.
- Relative lift = 20%.
- Do not call 1 percentage point a 1% lift.

## Excel
- COUNTIF → count outcomes.
- COUNTIFS → filtered counts.
- SUMIF → aggregate value.
- SUMIFS → multi-condition value.
- AVERAGEIF → subgroup average.
- PivotTable → variant comparison.

## Pandas
- groupby() → variant summary.
- agg() → multiple metrics.
- pivot() → comparison table.
- pivot_table() → flexible cross-tab.
- value_counts() → frequency.
- replace() → denominator protection.
- to_csv() → export.

## Experiment Design
- Define the question.
- Define the experimental unit.
- Define control.
- Define treatment.
- Randomly assign when appropriate.
- Define primary outcome.
- Define denominator.
- Pre-specify analysis.

## Interpretation
- Difference ≠ automatic causality.
- Statistical significance ≠ practical significance.
- High conversion ≠ high revenue.
- High click rate ≠ high purchase rate.
- Small sample ≠ stable estimate.

## Quality Checks
- Valid exposure logic.
- Valid binary fields.
- No duplicate experiment IDs.
- Consistent outcome definition.
- Correct denominator.
- Correct units.

## Dashboard
- Conversion → primary outcome.
- Click → engagement.
- Segment → heterogeneity.
- Scatter → secondary relationship.

## Presentation
- Question.
- Design.
- Data.
- Control.
- Treatment.
- Outcome.
- Lift.
- Limitations.

## 🏅 Badges
- ⚡ Quick Revision.
- 🧪 A/B Testing.
- 📊 BDM.
- 📈 Experimentation.
- 🐍 Python.
- 📗 Excel.

## Analysis Sequence
- Define → assign → measure → compare → validate → interpret → present.