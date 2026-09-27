![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-019-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Credit%20Microfinance%20and%20Loans-orange?style=for-the-badge)

# Day 019 — W4_L6 | Understanding Market Share — Part 4

## Lecture Context

Day 019 follows W4_L6 in the BDM lecture sequence.

The lecture focus is credit, microfinance and loans within market-share analysis.

This day extends the lending analysis from Days 016–018.

The main skill is comparing lending across business segments and time.

## Objectives

Analyze lending data by institution.

Analyze lending data by month.

Compare credit, microfinance and loan segments.

Calculate measured market share.

Use pivot-style summaries for business questions.

Identify useful lending trends.

## Dataset

The dataset contains 24 observations.

Four institutions are represented.

Six months are represented from January through June.

The dataset contains a segment field.

Loans are measured in crore units.

Borrowers are measured in lakh units.

NPA percentage is included as a supporting measure.

## Workbook

Credit_Loan_Data contains raw observations.

Monthly_Market summarizes monthly lending.

Institution_Summary compares institutions.

Segment_Summary compares business segments.

Institution_Month provides a cross-dimensional summary.

Instructions contains the practice workflow.

## Analysis Flow

Inspect raw data.

Confirm units and fields.

Calculate total lending.

Aggregate by month.

Aggregate by institution.

Aggregate by segment.

Calculate market share.

Build institution-month pivot.

Visualize trends.

Write evidence-based insights.

## Excel Practice

Create a PivotTable with Month in Rows.

Place Loans_Cr in Values.

Create an institution-level PivotTable.

Create a segment-level PivotTable.

Create an institution-by-month matrix.

Use percentage of grand total for share.

Validate with SUMIF and SUMIFS.

Create line and column charts.

## Business Interpretation

Institution totals show relative lending scale.

Monthly totals show movement over time.

Segment totals show composition of lending.

Market share gives a relative comparison.

The institution-month table reveals concentration across time.

Supporting measures should be interpreted separately from lending volume.

## Quality Checks

Reconcile monthly totals with raw data.

Reconcile institution totals with raw data.

Reconcile segment totals with raw data.

Check market-share totals.

Confirm month order.

Confirm units.

Check chart source ranges.

## Python Extension

Pandas groupby creates grouped summaries.

pd.pivot_table creates cross-dimensional views.

Matplotlib can display lending trends.

CSV exports preserve summary outputs.

The included Python file reproduces the analysis.

### Practical checkpoint

- Identify the business measure before calculating market share.
- Confirm the time period and segment fields.
- Compare institution totals with the same denominator.
- Use a PivotTable for grouped business summaries.
- Validate important totals with formulas.
- Compare lending across credit, microfinance and loan segments.
- Inspect monthly movement before writing conclusions.
- Use charts to communicate the most important comparison.
- Record insights with numerical evidence.
- Keep raw data separate from derived summaries.

### Revision checklist

- Market share uses a defined denominator.
- Lending can be grouped by institution.
- Lending can be grouped by month.
- Lending can be grouped by segment.
- PivotTables support multidimensional analysis.
- SUMIF supports one-condition validation.
- SUMIFS supports multi-condition validation.
- Line charts show ordered time movement.
- Column charts compare categories.
- Descriptive analysis does not prove causation.

### Day-end reflection

- What is the primary lending measure?
- Which institution has the largest lending volume?
- Which month has the largest total lending?
- Which segment contributes the most lending?
- Which institution shows the strongest growth?
- Why is the denominator important?
- What does the institution-month pivot reveal?
- Which chart is most useful?
- What extra field would improve the analysis?
- What is your strongest evidence-based insight?

## End of Day 019

Day 019 — W4_L6 completed.