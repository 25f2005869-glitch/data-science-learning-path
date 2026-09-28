# 🧠 Day 024 — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Business Data Management  
**Day:** 024  
**Topic:** Review of Key Questions  

## 🎯 Core Idea

Business Question → Data → Measure → Analysis → Result → Insight.

A business question should guide the analysis.

The data must be relevant to the question.

The measure must match the question.

The result should be checked before interpretation.

The insight should be evidence-based.

## ❓ Key Question Mapping

Total Revenue → `Revenue_Lakh`.

Monthly Revenue → `Month` + `Revenue_Lakh`.

Monthly Orders → `Month` + `Orders`.

Category Revenue → `Category` + `Revenue_Lakh`.

Channel Revenue → `Channel` + `Revenue_Lakh`.

Regional Revenue → `Region` + `Revenue_Lakh`.

Customer Revenue → `Customer_Type` + `Revenue_Lakh`.

Category Discount → `Category` + `Discount_Percent`.

## 💰 Revenue

Total Revenue → Sum of `Revenue_Lakh`.

Monthly Revenue → Revenue grouped by Month.

Category Revenue → Revenue grouped by Category.

Channel Revenue → Revenue grouped by Channel.

Regional Revenue → Revenue grouped by Region.

Customer Revenue → Revenue grouped by Customer Type.

Revenue shows sales value.

Revenue does not automatically mean profit.

Profit requires cost information.

## 📅 Monthly Analysis

Dimension → Month.

Measure → Revenue.

Operation → SUM.

Question → Which month has the highest revenue?

Method → Create monthly summary and rank values.

Additional measure → Orders.

Additional measure → Units.

Trend → Compare values in chronological order.

High point → Highest observed value.

Low point → Lowest observed value.

Caution → Trend does not prove causation.

## 🛍️ Category Analysis

Dimension → Category.

Measure → Revenue.

Operation → SUM.

Purpose → Compare product groups.

Additional measure → Orders.

Additional measure → Units.

Additional measure → Average Discount.

Ranking → Sort revenue descending.

Top category → First result after sorting.

Interpretation → Highest observed revenue contribution.

Caution → Revenue does not establish profitability.

## 📱 Channel Analysis

Dimension → Channel.

Measure → Revenue.

Operation → SUM.

Purpose → Compare sales platforms.

Possible channels → Website, App, Marketplace.

Ranking → Sort revenue descending.

Top channel → Highest revenue channel.

Additional context → Orders and Units.

Further analysis → Traffic and conversion rate.

Caution → Revenue alone does not explain channel performance.

## 🌍 Regional Analysis

Dimension → Region.

Measure → Revenue.

Operation → SUM.

Purpose → Compare geographic performance.

Ranking → Sort revenue descending.

Top region → Highest revenue region.

Additional measure → Orders.

Additional measure → Units.

Further information → Detailed geographic data.

Caution → High revenue does not mean every metric is high.

## 👥 Customer Analysis

Dimension → Customer_Type.

Groups → New and Returning.

Measure → Revenue.

Operation → SUM.

Additional measure → Orders.

Additional measure → Units.

Purpose → Compare customer groups.

Top group → Highest revenue group.

Further data → Repeat purchase frequency.

Further data → Customer acquisition cost.

Further data → Customer lifetime value.

## 🏷️ Discount Analysis

Dimension → Category.

Measure → Discount_Percent.

Operation → AVERAGE.

Purpose → Compare pricing context.

Highest discount → Category with highest average.

Discount is not profit.

Discount is not automatically a negative indicator.

Discount should be considered with revenue.

Discount should be considered with units.

Margin information would improve the analysis.

## 📊 Excel Functions

`SUM()` → Calculates a total.

`AVERAGE()` → Calculates an average.

`COUNT()` → Counts numeric values.

`COUNTA()` → Counts non-empty cells.

`SUMIF()` → Conditional sum.

`SUMIFS()` → Multiple-condition sum.

`COUNTIF()` → Conditional count.

`COUNTIFS()` → Multiple-condition count.

`MAX()` → Highest value.

`MIN()` → Lowest value.

## 📌 Pivot Tables

Pivot Tables summarise business data.

Rows → Dimension.

Values → Measure.

Columns → Optional second dimension.

Filters → Focused analysis.

Month → Useful row dimension.

Category → Useful row dimension.

Channel → Useful row dimension.

Region → Useful row dimension.

Customer Type → Useful row dimension.

Revenue → Useful value field.

Orders → Useful value field.

Units → Useful value field.

## 📈 Chart Selection

Column Chart → Compare categories.

Bar Chart → Compare groups.

Line Chart → Show time-based movement.

Pie Chart → Show simple composition.

Monthly Trend → Line or column chart.

Category Comparison → Column chart.

Channel Comparison → Bar or column chart.

Regional Comparison → Bar or column chart.

Customer Comparison → Column chart.

Chart title → Clearly describe the measure.

Axis labels → Identify dimensions and units.

Colours → Make comparisons clear.

## 🐍 Python — Pandas

`import pandas as pd` → Import Pandas.

`pd.read_excel()` → Read Excel workbook.

`df.head()` → Display first rows.

`df.tail()` → Display last rows.

`df.shape` → Show rows and columns.

`df.columns` → Show column names.

`df.dtypes` → Show data types.

`df.isna().sum()` → Count missing values.

`df.duplicated().sum()` → Count duplicates.

`df.groupby()` → Group data.

`.sum()` → Calculate totals.

`.mean()` → Calculate averages.

`.reset_index()` → Reset grouped index.

`.sort_values()` → Sort results.

`.idxmax()` → Locate maximum.

`.to_csv()` → Export CSV.

## 🐍 Python — Charts

`import matplotlib.pyplot as plt` → Import Matplotlib.

`plt.figure()` → Create chart figure.

`plt.bar()` → Create bar chart.

`plt.plot()` → Create line chart.

`plt.title()` → Add title.

`plt.xlabel()` → Label x-axis.

`plt.ylabel()` → Label y-axis.

`plt.xticks()` → Format x-axis labels.

`plt.tight_layout()` → Improve layout.

`plt.savefig()` → Save chart.

`plt.close()` → Close figure.

## 🔎 Data Quality

Check missing values.

Check duplicate records.

Check data types.

Check column names.

Check unexpected categories.

Check numerical values.

Check units.

Check calculation results.

Validate important outputs.

## 🧠 Interpretation Rules

State what the data shows.

Explain why the result matters.

Use the correct business terminology.

Avoid unsupported assumptions.

Do not call revenue profit.

Do not claim causation from a descriptive trend.

Use additional data when necessary.

Mention limitations when relevant.

## 🔄 Analysis Workflow

1. Read the question.

2. Identify the dimension.

3. Identify the measure.

4. Select the appropriate calculation.

5. Create the summary.

6. Check the result.

7. Rank or compare values.

8. Select a suitable chart.

9. Interpret the result.

10. Record the business insight.

## 📝 Quick Revision Questions

What is total revenue?

Which month has the highest revenue?

Which category has the highest revenue?

Which channel has the highest revenue?

Which region has the highest revenue?

Which customer type has higher revenue?

Which month has the highest orders?

Which category has the highest average discount?

What additional data is needed?

Why is revenue different from profit?

## ⚠️ Common Mistakes

Using the wrong dimension.

Using the wrong measure.

Forgetting aggregation.

Reading unsorted results as rankings.

Confusing orders with units.

Confusing revenue with profit.

Ignoring missing values.

Ignoring duplicate records.

Using an inappropriate chart.

Making unsupported causal claims.

## 🏅 Course Badges

🏅 **IIT Madras BS Degree**

🏅 **Business Data Management**

🏅 **Day 024 — Review of Key Questions**

🏅 **E-Commerce Case Study**

🏅 **Business Analytics Practice**

## 🚀 Final Quick Formula

Question → Dimension → Measure → Aggregation → Comparison → Visualisation → Insight.

Review the question before opening the answer.

Verify the calculation in Excel.

Run the Python analysis.

Compare the Excel and Python results.

Write the final interpretation in your own words.

Complete W5_L4.1 before moving to W5_L4.2.