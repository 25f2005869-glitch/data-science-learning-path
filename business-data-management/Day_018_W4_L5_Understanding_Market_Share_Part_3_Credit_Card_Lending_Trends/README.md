![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-018-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Credit%20Card%20Lending%20Trends-orange?style=for-the-badge)

# Day 018 — W4_L5 | Understanding Market Share — Part 3

## Lecture Context

Day 018 follows W4_L5 in the BDM lecture sequence.

The lecture focus is credit card lending trends and market-share analysis.

This day extends the market-share work from Days 016 and 017.

The analysis introduces a stronger time-series view of lending data.

## Objectives

Analyze credit card lending across months.

Compare lending scale across banks.

Calculate measured market share.

Observe month-to-month movement.

Use PivotTable-style summaries for business analysis.

Translate numerical trends into concise business insights.

## Dataset

The workbook contains monthly credit card lending data.

Four banks are represented.

Six months are represented from January to June.

The dataset also includes active cards and delinquency percentage.

The lending measure is recorded in crore units.

The active-card measure is recorded in lakh units.

## Workbook Sheets

Credit_Card_Data stores row-level observations.

Monthly_Market summarizes total monthly lending.

Bank_Summary compares banks and their measured shares.

Bank_Monthly_Trend provides a bank-by-month matrix.

Instructions contains the practical workflow.

## Analysis Flow

Start with the raw data.

Check the month and bank fields.

Calculate total lending.

Group lending by month.

Group lending by bank.

Calculate bank market share.

Compare monthly movement.

Inspect bank-specific trends.

Create visualizations.

Write evidence-based conclusions.

## Excel Skills

Use SUMIF for monthly summaries.

Use SUMIF for bank summaries.

Use AVERAGEIF for average delinquency.

Use SUMIFS for bank-month combinations.

Use PivotTables to reproduce summaries.

Use percentage-of-total for market share.

Use line charts for time trends.

Use column charts for bank comparison.

## Business Interpretation

A rising monthly total indicates increasing measured lending in the dataset.

A bank's market share depends on its lending relative to the defined total.

A trend should be interpreted across multiple periods rather than one isolated value.

Bank-wise trends can reveal whether growth is broad or concentrated.

Active-card movement can provide additional context.

## Quality Checks

Check that monthly totals reconcile with the raw records.

Check that bank totals reconcile with the overall total.

Check market-share percentages.

Check that month labels are ordered correctly.

Check that lending units remain consistent.

Check that chart categories match the summary table.

## Python Extension

Pandas groupby supports bank and month summaries.

Pivot tables can be created with pd.pivot_table.

Matplotlib can display line and column charts.

CSV exports make summary results reusable.

The code file included with Day 018 provides a reproducible workflow.

### Practical checkpoint

- Identify the time dimension before analyzing a trend.
- Confirm the lending measure and its unit.
- Compare monthly totals before comparing individual banks.
- Calculate market share using a consistent denominator.
- Inspect both level and direction of lending.
- Use a PivotTable to summarize the raw data.
- Validate important totals with formulas.
- Use charts to communicate the trend clearly.
- Record evidence-based business observations.
- Keep the raw dataset unchanged.

### Revision checklist

- Credit card lending can be analyzed over time.
- Monthly aggregation makes trend movement easier to see.
- Bank-level aggregation compares overall scale.
- Market share expresses relative contribution.
- Pivot tables reduce repetitive manual calculations.
- A line chart is useful for time trends.
- A column chart is useful for category comparison.
- Growth percentage compares beginning and ending values.
- Trend does not automatically prove causation.
- Business conclusions should reference the dataset.

### Day-end reflection

- What is the main time dimension?
- What is the main lending measure?
- Which bank has the largest measured lending?
- Which month has the highest total lending?
- Which bank shows the strongest Jan-to-Jun growth?
- How does market share help comparison?
- What does the bank-wise trend reveal?
- Which chart communicates the trend best?
- What additional data would improve the analysis?
- What insight can be supported directly by a number?

## End of Day 018

Day 018 — W4_L5 completed.