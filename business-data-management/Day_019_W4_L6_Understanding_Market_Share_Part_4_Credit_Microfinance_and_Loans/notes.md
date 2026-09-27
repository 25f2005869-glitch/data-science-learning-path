![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-019-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Credit%20Microfinance%20and%20Loans-orange?style=for-the-badge)

# Day 019 Notes — Credit, Microfinance and Loans

## Core Idea

Credit and microfinance lending can be studied through grouped business data.

The analysis combines market-share thinking with time-based lending trends.

The objective is descriptive business analysis.

## Market Share

Market share compares one institution's lending with total measured lending.

Formula: Institution Lending / Total Lending × 100.

A consistent denominator is necessary for comparable shares.

The market definition should be stated before interpreting the percentage.

## Dimensions

Institution identifies the lending organization.

Month provides the time dimension.

Segment identifies the lending category.

These dimensions can be combined in a pivot table.

## Pivot Tables

Rows define the main grouping.

Columns create a second comparison dimension.

Values contain the measure.

Sum is appropriate for total lending.

Filters can narrow the analysis.

## Institution Analysis

Group by Institution.

Sum Loans_Cr.

Calculate market share.

Sort by lending or share.

Identify the largest measured institution.

## Monthly Analysis

Group by Month.

Sum lending across institutions.

Compare January through June.

Use a line chart for the overall direction.

Avoid treating one month as a complete trend.

## Segment Analysis

Group by Segment.

Sum lending for each category.

Calculate segment share if required.

Compare credit, microfinance and loans.

Investigate differences with additional data when available.

## Growth

Growth compares a starting period with an ending period.

Formula: (Ending − Starting) / Starting × 100.

The starting and ending periods must be explicitly defined.

Growth and total scale answer different questions.

## Risk Context

NPA_Percent is a supporting descriptive field.

Average NPA can be summarized by institution.

NPA should not be interpreted as a direct cause of lending movement.

Use the measure only for the question it represents.

## Workflow

Inspect.

Aggregate.

Calculate share.

Create pivot.

Validate.

Visualize.

Interpret.

Document.

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