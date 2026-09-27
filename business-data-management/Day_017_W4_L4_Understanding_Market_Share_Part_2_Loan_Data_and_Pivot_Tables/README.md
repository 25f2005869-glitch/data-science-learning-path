![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-017-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Market%20Share%20Part%202-orange?style=for-the-badge)

# Day 017 — W4_L4 | Understanding Market Share — Part 2

## Course Context

Business Data Management (BDM) uses business datasets to connect data handling with practical decision making.

Day 017 follows W4_L4 of the provided IIT Madras BDM lecture sequence.

The lecture focus is understanding market share using loan data and pivot tables.

This day continues the market-share work from Day 016.

The central task is to summarize loan information in useful business dimensions.

## Learning Objectives

Understand how loan data can be grouped by company.

Understand how loan data can be grouped by region.

Compare loan categories using aggregated totals.

Calculate a company's share of total measured loan volume.

Use pivot-table thinking for business data summarization.

Interpret a summary rather than only producing a table.

## Dataset

The workbook contains company, region, loan type, loan count, customer count, and average loan size.

Four companies are represented: Alpha Finance, Beta Finance, Gamma Finance, and Delta Finance.

Four regions are represented: North, South, East, and West.

Two loan types are represented: Personal and Home.

The dataset contains 16 company-region records.

## Workbook Structure

`Loan_Data` stores the row-level business data.

`Pivot_Company` summarizes total loans and customers by company.

`Pivot_Region` summarizes total loans and customers by region.

`Pivot_Loan_Type` compares Personal and Home loans.

`Company_Region` provides a company-by-region cross summary.

`Instructions` contains the practical workflow.

## Core Analysis

Start with total market loan volume.

Group loan counts by company.

Divide each company total by the market total to obtain measured market share.

Rank companies by loan volume or market share.

Group loan counts by region to identify geographic concentration.

Group by loan type to compare category contribution.

Use the company-region table to see where a company's volume is concentrated.

## Excel Practice

Select the Loan_Data table.

Insert a PivotTable.

Place Company in Rows.

Place Loans in Values.

Review the company totals.

Add Region to create a regional summary.

Add Loan_Type when category comparison is required.

Use percentage-of-grand-total when the objective is market share.

Create a simple column chart from a summary table.

## Business Interpretation

Market share is meaningful only when the market definition and measure are clear.

A larger loan count indicates larger measured volume in this dataset.

A regional summary can reveal concentration that a company-only table hides.

A loan-type summary can reveal which category contributes more loan volume.

A cross-tabulation can help identify company-region strengths.

Good analysis connects every observation to a number in the dataset.

## Quality Checks

Check that company totals reconcile with the grand total.

Check that regional totals reconcile with the same market total.

Check that loan-type totals reconcile with the same market total.

Check that market-share percentages add to approximately 100%.

Check that filters and grouping fields are correctly selected.

Do not interpret a percentage without knowing its denominator.

## Files Included

`README.md` — day overview and learning workflow.

`notes.md` — detailed study notes.

`cheat-sheet.md` — quick revision reference.

`practice.md` — exercises and answer-check guidance.

`resources.md` — learning resources and practice directions.

`Day_017...xlsx` — prepared Excel workbook with summaries and colored charts.

`code/market_share_part2_analysis.py` — Python implementation using Pandas and Matplotlib.

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