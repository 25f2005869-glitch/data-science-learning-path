# Day 030 — Scatter Chart Presentation Cheat Sheet

**Author:** Saloni Tiwari
**Programme:** IIT Madras BS Degree — Diploma Level
**Day:** 030
**Topic:** Scatter Chart Presentation

## Quick Definitions

- Scatter chart = relationship between two numeric variables.
- Observation = one plotted point.
- X-axis = first numeric variable.
- Y-axis = second numeric variable.
- Correlation = measure of linear association.
- Outlier = observation distant from the general pattern.
- Positive association = variables generally rise together.
- Negative association = one variable generally rises while the other falls.

## Day 030 Variables

- X-axis: Ad_Spend_Thousand.
- Y-axis: Revenue_Lakh.
- Orders = transaction count.
- Units = quantity sold.
- Product = product category.
- Channel = sales channel.
- Region = geographic region.

## Quick Interpretation

- Upward pattern → positive association.
- Downward pattern → negative association.
- No clear pattern → weak visible association.
- Tight pattern → stronger relationship.
- Wide pattern → weaker relationship.
- Extreme point → investigate as a possible unusual observation.

## Correlation

- Correlation ranges from -1 to +1.
- Positive value → positive linear association.
- Negative value → negative linear association.
- Value near zero → weak linear association.
- Use Excel `CORREL()`.
- Use Python `.corr()`.
- Correlation does not prove causation.

## Formula Reference

- Revenue per order = Revenue / Orders.
- Revenue per unit = Revenue / Units.
- Correlation = linear association measure.
- Excel: `=CORREL(X_range,Y_range)`.
- Python: `df["X"].corr(df["Y"])`.

## Excel Quick Steps

- Open Sales_Data.
- Select Ad Spend.
- Select Revenue.
- Insert Scatter chart.
- Check X-axis.
- Check Y-axis.
- Add chart title.
- Add axis labels.
- Add units.
- Inspect the pattern.

## Python Quick Steps

- `pd.read_excel()`
- `pd.to_datetime()` when dates are required.
- `.corr()`
- `plt.scatter()`
- `plt.title()`
- `plt.xlabel()`
- `plt.ylabel()`
- `plt.savefig()`
- `.to_csv()`

## Presentation Checklist

- Business question stated.
- X variable stated.
- Y variable stated.
- Chart readable.
- Units displayed.
- Pattern described.
- Correlation interpreted.
- Causation avoided.
- Final insight evidence-based.

## Common Mistakes

- Using a line chart for independent observations.
- Reversing X and Y without explaining it.
- Omitting measurement units.
- Treating correlation as causation.
- Ignoring unusual observations.
- Calling revenue profit.
- Using non-numeric variables as scatter axes.
- Presenting the chart without context.

## 🏅 Badges

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)

![Day](https://img.shields.io/badge/Day-030-green?style=for-the-badge)

![Topic](https://img.shields.io/badge/Topic-Scatter%20Chart%20Presentation-orange?style=for-the-badge)