![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-017-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Market%20Share%20Part%202-orange?style=for-the-badge)

# Day 017 Notes — Loan Data and Pivot Tables

## Lecture Focus

W4_L4 focuses on loan data and pivot-table based market-share analysis.

The practical context is understanding loan volume across companies and business dimensions.

The key skill is moving from raw rows to grouped business summaries.

## Market Share

Market share expresses one entity's measured contribution relative to the total market measure.

Formula: Market Share = Entity Measure / Total Market Measure.

Percentage form: Market Share % = Entity Measure / Total Market Measure × 100.

The denominator must remain consistent when comparing entities.

## Loan Data Fields

Company identifies the financial institution in the dataset.

Region identifies the geographic segment.

Loan_Type identifies the product category.

Loans represents the measured loan volume.

Customers represents customer volume.

Avg_Loan_Size gives an additional descriptive business measure.

## Pivot Table Logic

Rows define the grouping dimension.

Values define the measure to aggregate.

SUM is appropriate for total loan volume.

COUNT may be used when counting records, but it is not the same as summing loan volume.

Filters can narrow the business view.

Columns can create a cross-dimensional comparison.

## Company Analysis

Group rows by Company.

Sum Loans for each company.

Calculate each company's share of total loans.

Sort the summary from largest to smallest share.

Use the ranking to identify the largest measured participant.

## Regional Analysis

Group rows by Region.

Sum Loans for each region.

Compare regional totals.

Calculate regional contribution if required.

Use regional concentration as a starting point for further investigation.

## Loan-Type Analysis

Group rows by Loan_Type.

Sum Loans for each category.

Compare Personal and Home loan volume.

Calculate category share using the same total market denominator.

## Company × Region

A two-dimensional pivot places Company on rows and Region on columns.

The resulting matrix shows the loan volume for each company-region combination.

This view is useful for identifying geographic concentration.

## Excel Validation

SUMIF can validate company-level totals.

SUMIF can validate region-level totals.

SUMIF can validate loan-type totals.

SUMIFS can validate a company-region cell.

Validation is useful before writing business conclusions.

## Interpretation Rules

State the measure before stating the conclusion.

Use percentages with their denominator understood.

Do not confuse customer count with loan count.

Do not assume causation from a descriptive pivot table.

Treat the dataset as the evidence for the stated analysis.

## Practical Workflow

Inspect raw data.

Confirm fields and data types.

Calculate the market total.

Build company summary.

Build region summary.

Build loan-type summary.

Build company-region pivot.

Validate totals.

Visualize important comparisons.

Write evidence-based insights.

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