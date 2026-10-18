![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-081-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 081 Cheat Sheet — A/B Testing of PayLater Nudges

## Core Terms
- A/B Test → controlled comparison.
- Control → reference experience.
- Treatment → changed experience.
- Nudge → behavioural intervention.
- Exposure → nudge shown.
- Conversion → PayLater usage.

## Core Variables
- Variant.
- Nudge_Type.
- Eligibility_Flag.
- Nudge_Shown.
- Clicked.
- PayLater_Used_Flag.
- Purchase_Value_Rupee.
- Repayment_Flag.

## Main Formulas
- Click Rate % = Clicks / Exposures × 100.
- PayLater Conversion % = PayLater Users / Exposures × 100.
- Repayment Rate % = Repayments / PayLater Users × 100.
- Absolute Lift = Treatment Rate − Control Rate.
- Relative Lift % = Absolute Lift / Control Rate × 100.

## Baseline
- Control is the main A/B reference.
- No Nudge is the nudge-level reference.
- Use identical outcome definitions.
- Use consistent denominators.

## Excel Functions
- COUNTIF → category counts.
- COUNTIFS → multi-condition counts.
- SUMIF → category totals.
- SUMIFS → multi-condition totals.
- AVERAGEIF → subgroup average.
- PivotTable → variant and segment analysis.

## Pandas
- groupby() → grouped analysis.
- agg() → multiple metrics.
- pivot() → comparison matrix.
- pivot_table() → flexible aggregation.
- replace() → protect denominators.
- to_csv() → output files.

## Nudge Types
- No Nudge.
- Reminder Nudge.
- Social Proof.
- Limited Time Message.

## Analysis Dimensions
- Variant.
- Nudge type.
- Customer segment.
- Region.
- Device.
- Category.

## Outcome Dimensions
- Click.
- PayLater usage.
- Purchase value.
- Repayment.

## Interpretation
- Absolute lift → percentage points.
- Relative lift → percent change relative to control.
- Conversion ≠ purchase value.
- Click ≠ conversion.
- Repayment ≠ conversion.

## Causal Reasoning
- Random assignment is important.
- Observed difference alone is insufficient.
- Confounding can distort observational comparisons.
- Sample size affects precision.
- Confidence intervals quantify uncertainty.

## Dashboard
- Variant conversion.
- Nudge conversion.
- Segment conversion.
- Regional conversion.

## Quality Checks
- Valid variant labels.
- Valid binary fields.
- Correct exposure denominator.
- No duplicate experiment IDs.
- Correct units.
- Reconciled totals.

## Presentation Flow
- Question.
- Experiment design.
- Data.
- Control.
- Treatment.
- Outcome.
- Lift.
- Segmentation.
- Limitations.

## 🏅 Badges
- ⚡ Quick Revision.
- 🧪 A/B Testing.
- 💳 PayLater.
- 📊 BDM.
- 🐍 Python.
- 📗 Excel.

## Quick Reporting Template
- Control: ___%.
- Treatment: ___%.
- Absolute lift: ___ pp.
- Relative lift: ___%.
- Exposures: ___.
- Purchases: ___.
- Limitation: synthetic educational dataset.

## Common Errors
- Mixing percentage points with percentages.
- Using purchases as the exposure denominator.
- Ignoring subgroup size.
- Treating click rate as conversion.
- Treating association as causation.