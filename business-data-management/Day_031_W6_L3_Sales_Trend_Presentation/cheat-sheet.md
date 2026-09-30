# Day 031 — Sales Trend Presentation Cheat Sheet

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-031-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Author:** Saloni Tiwari
**Programme:** IIT Madras BS Degree — Diploma Level
**Day:** 031
**Topic:** Sales Trend Presentation

## Lecture Mapping

- BDM playlist: **W6_L3 — Sales trend presentation**.
- The focus is presentation of sales movement over time.
- Trend analysis uses an ordered time dimension.
- Monthly revenue and unit movement are central views.
- Product and weekday summaries provide supporting context.

## Learning Objectives

- Understand sales trend analysis.
- Compare monthly revenue.
- Compare monthly units.
- Compare monthly orders.
- Calculate month-over-month growth.
- Select appropriate trend charts.
- Explain trends in business language.
- Prepare a concise sales trend presentation.

## Trend Concept

- A trend describes movement over an ordered period.
- Time should remain chronological.
- A line chart is useful for time-based movement.
- Trend analysis can reveal direction and changes.
- One unusual month should not automatically define the overall trend.
- Trend interpretation should consider the complete observation period.

## Monthly Revenue

- Revenue is aggregated by month.
- Monthly values make period comparison easier.
- The dashboard contains a monthly revenue line chart.
- Rising values indicate an increasing observed revenue pattern.
- The first and last periods can be compared.
- Month-over-month growth adds numerical context.

## Monthly Units

- Units measure sales volume.
- Monthly units are aggregated using SUM.
- The unit trend can be compared with revenue.
- Increasing units may accompany increasing revenue.
- Unit movement and revenue movement are different metrics.
- High unit count does not automatically mean high profitability.

## Growth Analysis

- MoM means month-over-month.
- MoM compares the current month with the previous month.
- Formula: (Current − Previous) / Previous × 100.
- The first month has no previous month in this dataset.
- Growth should be interpreted with underlying values.
- Negative growth indicates a decline from the previous period.

## Product Context

- Product_Trend compares products.
- Revenue ranking shows product contribution.
- Units provide volume context.
- Orders provide transaction context.
- Product performance can explain part of overall sales movement.
- Ranking should use a clearly stated metric.

## Weekday Context

- Weekday_Trend groups observations by weekday.
- Monday through Sunday are kept in calendar order.
- Revenue, units and orders can be compared.
- Weekday analysis is a supporting view.
- It should not be confused with monthly trend analysis.

## Presentation Flow

- Slide 1: objective.
- Slide 2: KPI summary.
- Slide 3: monthly revenue trend.
- Slide 4: monthly unit trend.
- Slide 5: growth analysis.
- Slide 6: product context.
- Slide 7: weekday context.
- Slide 8: key insights.
- Slide 9: business focus.

## Excel Workflow

- Open Sales_Data.
- Review Monthly_Trend.
- Review Growth_Analysis.
- Review Product_Trend.
- Review Weekday_Trend.
- Open Sales_Trend_Dashboard.
- Verify chart titles and units.
- Prepare three evidence-based observations.

## Python Workflow

- Load Sales_Data.
- Convert Date.
- Create Month.
- Create Weekday.
- Aggregate monthly metrics.
- Calculate MoM growth.
- Aggregate product and weekday metrics.
- Export CSV summaries.
- Generate trend charts.

## Presentation Rules

- Keep the time axis chronological.
- Label all metrics.
- Show units.
- Use line charts for time trends.
- Explain the observation before interpretation.
- Avoid unsupported causes.
- Do not call revenue profit.
- Keep the conclusion tied to the data.

## Common Mistakes

- Mixing months out of order.
- Using the wrong metric.
- Confusing orders and units.
- Ignoring first-month growth limitation.
- Claiming causation from a trend.
- Omitting chart units.
- Overloading one slide with charts.
- Ignoring data quality.

## Data Quality

- Check missing dates.
- Check duplicate observations.
- Check numeric columns.
- Check revenue units.
- Check chronological order.
- Validate totals.
- Confirm all periods are included.
- Verify calculated growth values.

## Revision Notes

- Sales trend presentation converts time-based sales data into a visual story.
- Revenue, units and orders provide complementary views.
- MoM growth quantifies change between adjacent periods.
- Product and weekday analysis provide context.
- Good presentation separates measured facts from possible explanations.
- The dashboard should support a short, clear business presentation.