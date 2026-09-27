![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-017-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Market%20Share%20Part%202-orange?style=for-the-badge)

# Day 017 Cheat Sheet — Market Share & Pivot Tables

## Key Formulas

Market Share = Company Loans / Total Market Loans.

Market Share % = Company Loans / Total Market Loans × 100.

SUMIF aggregates a measure using one condition.

SUMIFS aggregates a measure using multiple conditions.

## Pivot Table Steps

Select the complete dataset.

Choose Insert → PivotTable.

Put the required dimension in Rows.

Put Loans in Values.

Confirm the aggregation is Sum.

Add a second dimension only when the business question needs it.

## Useful Views

Company → Total Loans.

Region → Total Loans.

Loan Type → Total Loans.

Company → Market Share %.

Company × Region → Total Loans.

## Market Share Checks

Use the same market total for all company shares.

Check that shares sum to approximately 100%.

Check that source totals equal pivot totals.

Check filters before interpreting results.

## Chart Selection

Column chart is useful for comparing company totals.

Column chart is useful for comparing regions.

Pie charts can show composition when categories are limited.

Use a chart title that states the business measure.

Keep chart labels readable.

## Business Questions

Which company has the largest loan volume?

Which region has the largest loan volume?

Which loan type contributes the largest volume?

Where is each company's loan volume concentrated?

Which company-region combination deserves further investigation?

## Do Not Confuse

Loan count is not the same as customer count.

Market share is not the same as revenue share.

Pivot aggregation is not automatically a causal explanation.

A chart does not replace data validation.

## Python Equivalent

`groupby()` creates grouped summaries.

`agg()` defines aggregation measures.

`pd.pivot_table()` creates cross-dimensional summaries.

`sort_values()` supports ranking.

`to_csv()` saves analysis outputs.

## Final Checklist

Raw data reviewed.

Company summary created.

Region summary created.

Loan-type summary created.

Company-region pivot created.

Market share calculated.

Totals validated.

Charts reviewed.

Insights written from evidence.

### Practical checkpoint

- Identify the business question before creating a summary.
- Select the correct measure for the question.
- Check totals before interpreting percentages.
- Compare company, region, and loan-type patterns.
- Use a pivot table to reduce manual aggregation.
- Validate a pivot result with a formula when useful.
- Record one evidence-based business insight.
- Save the workbook with a clear day-wise filename.
- Keep raw data separate from analysis outputs.
- Use consistent field names throughout the workbook.

### Revision checklist

- Market share is based on a defined market measure.
- Loan volume can be summarized by company.
- Loan volume can be summarized by region.
- Loan volume can be summarized by loan type.
- Pivot tables support grouping and aggregation.
- SUMIF can reproduce a one-dimensional summary.
- SUMIFS can reproduce a multi-condition summary.
- Percentage of grand total can express share.
- Charts should answer a specific business question.
- A chart is not a substitute for interpretation.

### Day-end reflection

- What was the main business question?
- Which field was used as the measure?
- Which dimension gave the most useful comparison?
- Which company had the largest loan volume?
- Which region had the largest loan volume?
- Which loan type dominated the dataset?
- Did the percentage shares sum to approximately 100%?
- What would you investigate next?
- Which Excel operation was most useful?
- What evidence supports your final insight?

## End of Day 017

Day 017 — W4_L4 completed.