![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-018-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Credit%20Card%20Lending%20Trends-orange?style=for-the-badge)

# Day 018 Notes — Credit Card Lending Trends

## Core Idea

Credit card lending trends describe how measured lending changes over time.

The time dimension in this workbook is month.

The bank dimension allows comparison among institutions.

The lending field is the primary business measure.

## Trend Analysis

A trend requires an ordered time dimension.

Monthly totals can reveal overall market direction.

Individual bank series can reveal different growth patterns.

Comparing first and last periods provides a simple growth view.

More periods would provide stronger evidence for long-term seasonality.

## Market Share

Market share compares a bank's lending with total measured lending.

Formula: Bank Lending / Total Market Lending × 100.

The denominator should be defined consistently.

Shares allow scale differences to be expressed relatively.

Market share can be recalculated for different months when monthly totals are used.

## Pivot Tables

Rows define the grouping dimension.

Values define the measure being summarized.

Months can be placed in Rows.

Banks can be placed in Columns.

Loans can be placed in Values with Sum aggregation.

This creates a useful bank-month matrix.

## Supporting Measures

Active cards indicate the number of active card units in the dataset.

Average ticket size gives another lending-related measure.

Delinquency percentage provides a risk-related descriptive measure.

Supporting measures should not be confused with the primary lending total.

## Excel Formulas

SUMIF can calculate total lending by month.

SUMIF can calculate total lending by bank.

SUMIFS can calculate one bank-month combination.

AVERAGEIF can calculate average delinquency by bank.

Percentage formulas can calculate market share.

## Visualization

Line charts are effective for ordered monthly trends.

A column chart is useful for comparing total bank lending.

Multiple line series allow bank-level trend comparison.

Chart titles should state the business measure.

Axes should include meaningful units.

## Interpretation

Scale and growth are different concepts.

A bank can have the largest total and still have a different growth rate.

Growth should be calculated from clearly defined start and end periods.

Descriptive trends do not establish causation.

Business interpretation should remain tied to the available dataset.

## Workflow

Inspect data.

Validate fields.

Aggregate monthly lending.

Aggregate bank lending.

Calculate market share.

Build bank-month pivot.

Visualize trends.

Check results.

Write insights.

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