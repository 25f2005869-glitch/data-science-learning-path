# ⚡ Day 028 — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 028  
**Topic:** Trend Analysis — Sales and Revenue Trends

## 🎯 Core Concept

Trend analysis = studying movement across an ordered sequence.

Time-based trend = movement across dates or months.

Sales trend = movement in orders or units.

Revenue trend = movement in sales value.

Weekday analysis = comparison across day categories.

## 📌 Important Fields

Date → transaction date.

Month → monthly grouping.

Weekday → day-of-week grouping.

Product → product identity.

Category → product category.

Channel → sales channel.

Region → geographic region.

Orders → order volume.

Units → quantity sold.

Revenue_Lakh → revenue in lakh.

## 🧮 Main Formulas

Total Revenue = SUM(Revenue_Lakh).

Total Units = SUM(Units).

Total Orders = SUM(Orders).

Revenue per Order = Revenue / Orders.

Revenue per Unit = Revenue / Units.

Growth % = (Current − Previous) / Previous × 100.

Absolute Change = Current − Previous.

## 📈 Trend Logic

1. Start with raw data.

2. Validate the data.

3. Convert Date correctly.

4. Create the required time grouping.

5. Aggregate the measures.

6. Sort chronologically.

7. Calculate growth.

8. Visualize the trend.

9. Interpret the result.

10. Write business insights.

## 📅 Monthly Trend

Group by Month.

Sum Orders.

Sum Units.

Sum Revenue.

Sort months chronologically.

Compare each month.

Calculate month-over-month growth.

Look for sustained movement.

Avoid focusing on only one month.

## 💰 Revenue Trend

Revenue is a value metric.

Higher revenue means greater sales value.

Revenue can rise because units increase.

Revenue can also rise because the product mix changes.

Therefore revenue should be interpreted with units.

## 📦 Unit Trend

Units represent quantity.

Higher units mean higher volume.

Lower units mean lower volume.

Units do not directly represent revenue.

Different products can have different values.

## 🧾 Order Trend

Orders measure transaction count.

Units can exceed orders.

One order can contain multiple units.

Order growth and unit growth can therefore differ.

## 📅 Weekday Analysis

Group by Weekday.

Calculate Orders.

Calculate Units.

Calculate Revenue.

Compare weekdays.

Use a bar chart.

Do not treat weekdays as chronological monthly periods.

## 📊 Chart Selection

Monthly trend → Line chart.

Daily trend → Line chart.

Weekday comparison → Bar chart.

Product comparison → Bar chart.

Channel comparison → Bar chart.

Region comparison → Bar chart.

## 📉 Growth Interpretation

Positive growth → increase.

Negative growth → decrease.

Zero growth → no change.

Large positive growth → strong increase.

Large negative growth → strong decline.

Always check the underlying values.

## 🔍 Data Quality Checks

Missing values.

Duplicate rows.

Incorrect dates.

Incorrect month labels.

Invalid numeric values.

Unexpected categories.

Incorrect sorting.

Missing periods.

## 📊 Excel Functions

SUM() → adds values.

SUMIFS() → conditional sum.

AVERAGE() → average.

COUNT() → numeric count.

COUNTIF() → conditional count.

SORT() → sorting.

MONTH() → extracts month.

WEEKDAY() → extracts weekday.

TEXT() → formats dates.

## 📌 Excel Pivot Workflow

Insert Pivot Table.

Place Month in Rows.

Place Orders in Values.

Place Units in Values.

Place Revenue_Lakh in Values.

Check aggregation.

Sort months correctly.

Create the chart.

Format the chart.

## 🐍 Python Quick Reference

import pandas as pd

import matplotlib.pyplot as plt

pd.read_excel() → reads Excel.

pd.to_datetime() → converts dates.

groupby() → groups records.

agg() → aggregates values.

sort_values() → sorts data.

pct_change() → calculates percentage change.

to_csv() → exports CSV.

plt.plot() → line chart.

plt.bar() → bar chart.

plt.savefig() → saves chart.

## 📈 Interpretation Rules

Trend shows movement.

Trend does not automatically show cause.

Correlation does not prove causation.

A single point is not a trend.

Multiple periods provide stronger evidence.

Revenue and units should be compared.

Business context is important.

## ❌ Common Mistakes

Do not sort months alphabetically.

Do not confuse units with orders.

Do not interpret revenue as quantity.

Do not ignore missing values.

Do not ignore duplicate records.

Do not claim causation from a chart.

Do not use a pie chart for time trends.

Do not create misleading axis labels.

## 🧠 Quick Questions

What is a trend?

Why use a line chart for time?

What is growth percentage?

What does revenue measure?

What do units measure?

What do orders measure?

Why compare revenue and units?

What does weekday analysis provide?

Why check data quality?

## 🏅 Badges

- 🏅 **IIT Madras BS Degree**
- 🏅 **Business Data Management**
- 🏅 **Day 028 — Trend Analysis**
- 🏅 **Sales & Revenue Trends**
- 🏅 **E-Commerce Case Study**