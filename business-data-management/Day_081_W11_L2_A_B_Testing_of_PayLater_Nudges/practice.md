![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-081-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 🧪 Day 081 Practice — A/B Testing of PayLater Nudges

## Task 1 — Dataset Inspection
- Open PayLater_AB_Data.
- Count all experiment records.
- Identify Control and Treatment.
- List every nudge type.
- Check Experiment_ID uniqueness.

## Task 2 — Eligibility
- Count eligible customers.
- Compare eligibility with exposure.
- Check whether every exposure is eligible.
- Explain why eligibility should be defined before analysis.

## Task 3 — Exposure
- Calculate Control exposures.
- Calculate Treatment exposures.
- Compare the denominators.
- Record the counts next to rates.

## Task 4 — Click Rate
- Count Control clicks.
- Count Treatment clicks.
- Calculate click rates.
- Compare the results descriptively.

## Task 5 — PayLater Conversion
- Count PayLater users by variant.
- Calculate Control conversion.
- Calculate Treatment conversion.
- Verify the denominator.

## Task 6 — Absolute Lift
- Subtract Control conversion from Treatment conversion.
- Express the result in percentage points.
- Check the sign.
- Explain the meaning without making a causal claim.

## Task 7 — Relative Lift
- Divide absolute lift by Control conversion.
- Multiply by 100.
- Compare relative and absolute lift.
- Explain why the two numbers have different units.

## Task 8 — Nudge-Level Analysis
- Group by Nudge_Type.
- Calculate exposure.
- Calculate clicks.
- Calculate PayLater users.
- Calculate conversion rate.

## Task 9 — Nudge Baseline
- Select No Nudge.
- Calculate its conversion rate.
- Calculate lift for each nudge category.
- Express lift in percentage points.

## Task 10 — Customer Segments
- Group by Customer_Segment and Variant.
- Calculate exposures.
- Calculate PayLater users.
- Calculate conversion.
- Compare within each segment.

## Task 11 — Region
- Group by Region and Variant.
- Calculate conversion rates.
- Check exposure counts.
- Identify small subgroups.

## Task 12 — Device
- Group by Device and Variant.
- Calculate click rates.
- Calculate conversion rates.
- Compare device-level response.

## Task 13 — Repayment
- Calculate repayment counts.
- Calculate repayment rates among PayLater users.
- Compare Control and Treatment.
- Keep repayment separate from conversion.

## Task 14 — Purchase Value
- Calculate total purchase value by variant.
- Calculate average purchase value among users.
- Compare monetary and conversion outcomes.
- Explain why they are not interchangeable.

## Task 15 — Excel
- Recreate Variant_Summary.
- Use COUNTIFS.
- Use SUMIFS.
- Calculate conversion.
- Calculate lift.
- Format percentages.

## Task 16 — PivotTable
- Build Variant × Customer Segment.
- Add exposure counts.
- Add PayLater user counts.
- Calculate conversion rates.
- Add Region as a second dimension.

## Task 17 — Python
- Read the Excel workbook.
- Convert numeric fields.
- Group by Variant.
- Group by Nudge_Type.
- Export summaries.

## Task 18 — Visualisation
- Create Control vs Treatment conversion chart.
- Create nudge conversion chart.
- Create segment comparison.
- Create regional comparison.

## Task 19 — Statistical Thinking
- Identify a suitable two-proportion test.
- Explain confidence intervals.
- Explain statistical significance.
- Explain practical significance.

## Task 20 — Experiment Design
- Write a PayLater nudge question.
- Define control.
- Define treatment.
- Define primary outcome.
- Define experimental unit.
- Define analysis population.

## Task 21 — Causal Reasoning
- Identify one possible confounder.
- Explain why observational comparison is weaker for causality.
- Explain the role of randomisation.
- State one limitation of the synthetic dataset.

## Task 22 — Presentation
- Prepare a six-slide analysis.
- Include design.
- Include sample counts.
- Include conversion.
- Include lift.
- Include segment analysis.
- Include limitations.

## 🏅 Practice Badges
- 🧪 Experiment.
- 💳 PayLater.
- 📊 Analysis.
- 📈 Metrics.
- 🐍 Python.
- 📗 Excel.

## Task 23 — Reporting Table
- Create a two-row Control/Treatment table.
- Add exposure count.
- Add click count.
- Add PayLater user count.
- Add conversion rate.
- Add absolute lift below the table.

## Task 24 — Audit
- Recalculate one rate manually.
- Recalculate one lift manually.
- Compare your values with Python output.
- Compare your values with Excel output.
- Record any rounding difference.

## Task 25 — Reflection
- Explain why Control is needed.
- Explain why exposure is the denominator.
- Explain why repayment is secondary.
- Explain why randomisation matters.