![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-020-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Analysis%20of%20Aspirational%20Data-orange?style=for-the-badge)

# Day 020 — W4_L7 | Analysis of Aspirational Data

## Lecture Context

Day 020 corresponds to W4_L7 in the BDM lecture sequence.

The lecture topic is Analysis of Aspirational Data.

This day focuses on comparing development-style indicators across districts and regions.

The work continues the data-summary and business-analysis pattern used in earlier days.

## Objectives

Understand the structure of aspirational data.

Compare district-level scores.

Calculate regional averages.

Compare health, education, agriculture and financial-inclusion indicators.

Create rankings and visual summaries.

Develop evidence-based business observations.

## Dataset

The learning dataset contains district-level observations.

Each record contains a district and region.

The overall aspirational score is accompanied by thematic indicator scores.

Population is included as contextual information in the Excel workbook.

The data is designed for analysis practice and should not be treated as an official ranking.

## Workbook Structure

Aspirational_Data stores raw observations.

Region_Summary contains regional averages.

District_Ranking provides relative district ranking.

Indicator_Comparison supports multi-indicator comparison.

Insights contains analysis guidance.

## Analysis Flow

Inspect the raw data.

Check score fields.

Calculate the overall average.

Compare districts.

Aggregate by region.

Compare indicators.

Rank districts.

Visualize results.

Validate calculations.

Write conclusions.

## Excel Practice

Use a PivotTable to summarize average scores by region.

Use District in Rows and Aspirational Score in Values.

Change aggregation to Average when comparing scores.

Compare indicator averages.

Create a column chart for regional averages.

Create a district comparison chart.

Use the prepared workbook as a reference.

## Business Interpretation

A district score provides a compact summary of the measured indicators.

Regional averages help compare groups of districts.

Indicator-level analysis helps identify dimensions that differ in strength.

A high overall score does not automatically explain why a district performs differently.

Additional data is required for deeper causal analysis.

## Quality Checks

Check that score fields are numeric.

Check that regional groups are correctly assigned.

Check average calculations.

Check ranking order.

Check chart source ranges.

Remember that the workbook contains a learning dataset.

## Python Extension

Pandas groupby supports regional summaries.

rank supports district ordering.

Matplotlib can visualize district and indicator comparisons.

CSV outputs make summaries reusable.

The included Python file provides a reproducible workflow.

### Practical checkpoint

- Identify the unit of analysis before comparing records.
- Check the score fields and their scale.
- Compare districts using the same measure.
- Aggregate districts by region when a regional view is needed.
- Use a PivotTable to summarize indicator data.
- Compare overall score with individual indicators.
- Validate averages before interpreting them.
- Use rankings only within the defined dataset.
- Use charts to make comparisons easier to read.
- Write insights from observed values.

### Revision checklist

- Aspirational data can contain multiple development indicators.
- Overall scores can be compared across districts.
- Regional averages summarize district-level observations.
- Indicator averages provide a thematic view.
- Rankings require a consistent scoring measure.
- PivotTables support grouped analysis.
- Average is different from total.
- A chart supports interpretation but does not replace evidence.
- Correlation or causation should not be assumed from descriptive data.
- The dataset should be treated as a learning dataset.

### Day-end reflection

- What is the main score being analyzed?
- Which district has the highest score?
- Which district has the lowest score?
- Which region has the highest average?
- Which indicator has the strongest average?
- Which indicator appears comparatively weaker?
- Why are regional averages useful?
- What does the district ranking show?
- What additional variable would improve the analysis?
- What numerical evidence supports your conclusion?

## End of Day 020

Day 020 — W4_L7 completed.