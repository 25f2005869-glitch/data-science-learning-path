# Day 030 — Scatter Chart Presentation Notes

**Author:** Saloni Tiwari
**Programme:** IIT Madras BS Degree — Diploma Level
**Day:** 030
**Topic:** Scatter Chart Presentation

## Lecture Mapping

- BDM playlist: **W6_L2 — Scatter chart presentation**.
- This day focuses on presenting a scatter chart clearly.
- The goal is to communicate a relationship between numeric variables.
- A scatter chart should be connected to a clear business question.
- Visual evidence should be separated from assumptions.

## Learning Objectives

- Understand scatter-chart construction.
- Identify numeric variables.
- Understand X-axis and Y-axis roles.
- Read the direction of a relationship.
- Identify concentration and dispersion.
- Recognize possible unusual observations.
- Understand correlation.
- Avoid causal interpretation without evidence.

## What Is a Scatter Chart?

- A scatter chart displays observations as points.
- Every point represents one observation.
- The horizontal axis represents one numeric variable.
- The vertical axis represents another numeric variable.
- The position of each point is determined by the two values.
- Multiple points together reveal the overall pattern.
- Scatter charts are useful for relationship analysis.
- They are different from time-series line charts.

## Day 030 Dataset

- The workbook contains sales observations.
- Product identifies the product involved.
- Channel identifies the sales channel.
- Region identifies the geographic region.
- Orders records transaction volume.
- Units records quantity sold.
- Revenue_Lakh records sales value.
- Ad_Spend_Thousand records advertising expenditure.
- Ad spend and revenue are the primary scatter variables.

## X-Axis

- X-axis is the horizontal axis.
- Day 030 uses Ad_Spend_Thousand on the X-axis.
- It represents advertising expenditure in thousands.
- X-axis values are numeric.
- Axis units must be visible.
- The variable should be explained before presenting the chart.
- Changing X and Y can change the interpretation.

## Y-Axis

- Y-axis is the vertical axis.
- Day 030 uses Revenue_Lakh on the Y-axis.
- Revenue is expressed in lakh.
- Y-axis values are numeric.
- The label should contain the measurement unit.
- Revenue is sales value.
- Revenue should not be called profit.

## Relationship Pattern

- A rising point pattern suggests positive association.
- A falling pattern suggests negative association.
- A scattered pattern suggests weak visible association.
- Closely grouped points around a direction indicate stronger association.
- Widely dispersed points indicate weaker association.
- Individual points should not be interpreted in isolation.

## Correlation

- Correlation summarizes linear association.
- It ranges from -1 to +1.
- A value near +1 indicates strong positive linear association.
- A value near -1 indicates strong negative linear association.
- A value near 0 indicates weak linear association.
- Correlation does not prove causation.
- Business decisions should consider additional evidence.

## Presentation Method

- Begin with the question.
- Define the variables.
- Display the scatter chart.
- Describe the visible direction.
- Mention correlation.
- Discuss possible unusual observations.
- Explain the business relevance.
- State limitations.
- End with a concise conclusion.

## Excel Method

- Open the Sales_Data sheet.
- Review Ad_Spend_Thousand.
- Review Revenue_Lakh.
- Select both numeric variables.
- Insert a Scatter chart.
- Verify X and Y assignments.
- Add a chart title.
- Add axis titles.
- Add measurement units.
- Review the visual pattern.

## Python Method

- Import pandas.
- Import matplotlib.pyplot.
- Load the workbook.
- Select the two variables.
- Calculate correlation.
- Create a scatter plot.
- Add title and axis labels.
- Save the chart.
- Export useful summaries.

## Business Interpretation

- A positive pattern can indicate that higher ad spend is associated with higher revenue.
- This observation does not establish that advertising caused the revenue increase.
- Other variables may influence revenue.
- Product mix can influence revenue.
- Channel mix can influence revenue.
- Region can influence sales.
- Seasonality may also influence results.
- Additional analysis is required for causal conclusions.

## Data Quality

- Check missing values.
- Check numeric data types.
- Check duplicate observations.
- Check measurement units.
- Check extreme values.
- Check whether the data covers the intended period.
- Validate the workbook before presenting.
- Never present an unchecked chart.

## Revision Notes

- Scatter charts are relationship-analysis visuals.
- Each point represents an observation.
- X and Y should normally be numeric.
- Correlation supports relationship analysis.
- Correlation is not proof of causation.
- Good presentation combines visual and numerical evidence.
- Business interpretation must remain evidence-based.

## 🏅 Badges

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)

![Day](https://img.shields.io/badge/Day-030-green?style=for-the-badge)

![Topic](https://img.shields.io/badge/Topic-Scatter%20Chart%20Presentation-orange?style=for-the-badge)