![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-079-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 079 Cheat Sheet — Factors for Nudge Presentation

## Core Variables
- Nudge_Type → intervention category.
- Nudge_Shown → exposure indicator.
- Clicked → click outcome.
- Purchased_Flag → purchase outcome.
- Order_Value_Rupee → monetary outcome.
- Repeat_Visit_Flag → return behaviour.

## Core Formulas
- Click Rate % = Clicks / Exposures × 100.
- Conversion Rate % = Purchases / Exposures × 100.
- Repeat Visit Rate % = Repeat Visits / Exposures × 100.
- Average Order Value = Purchase Order Value / Purchases.
- Lift (pp) = Factor Conversion % − Baseline Conversion %.

## Baseline
- Reference = Default Recommendation.
- Calculate baseline using the same outcome definition.
- Keep denominator consistent.
- Compare like with like.

## Excel Functions
- SUMIF → factor totals.
- COUNTIF → factor counts.
- AVERAGEIF → factor averages.
- SUMIFS → multi-factor totals.
- COUNTIFS → multi-factor counts.
- IF → binary classification.
- PivotTable → multi-dimensional comparison.

## Pandas
- groupby() → grouped factor summary.
- agg() → multiple metrics.
- pivot_table() → cross-tabulation.
- value_counts() → category frequency.
- replace() → denominator protection.
- sort_values() → ordering.
- to_csv() → export.

## Factor Dimensions
- Nudge type.
- Customer segment.
- Region.
- Device.
- Category.

## Outcome Dimensions
- Click.
- Purchase.
- Order value.
- Repeat visit.

## Presentation Questions
- What is the business question?
- What is the baseline?
- What is the factor?
- What is the outcome?
- What is the denominator?
- What differs between groups?
- Could composition explain the difference?
- What evidence is still needed?

## Chart Selection
- Column → compare factor rates.
- Line → show ordered comparisons when appropriate.
- Scatter → inspect two numeric variables.
- KPI cards → headline metrics.
- Tables → exact values.

## Interpretation
- Descriptive difference ≠ causal effect.
- Lift ≠ guaranteed incremental impact.
- Higher order value ≠ higher conversion.
- More exposures ≠ better performance.
- Segment average ≠ individual behaviour.

## Quality Checks
- Unique IDs.
- Valid binary fields.
- Valid categories.
- Non-zero denominators.
- Correct units.
- Reconciled totals.

## Dashboard Map
- Chart 1 → nudge conversion.
- Chart 2 → baseline lift.
- Chart 3 → segment conversion.
- Chart 4 → device conversion.

## 🏅 Badges
- ⚡ Quick Revision.
- 📊 BDM.
- 🧩 Factor Analysis.
- 📗 Excel.
- 🐍 Python.
- 🎤 Presentation.

## 📝 Analysis Sequence
- Define → measure → normalise → compare → cross-tabulate → visualise → interpret → validate.