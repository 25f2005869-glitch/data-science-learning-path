# Day 035 — Key Learnings from the Case Cheat Sheet

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-035-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 035  
**Topic:** Key Learnings from the Case

## 📚 Lecture

- W6_L7
- Key Learnings from the Case

## 📌 Core Idea

The case connects:

`Ledger → Summary → Metrics → Visuals → Insights`

## 📒 Ledger

Detailed inventory movement record.

## 📦 Main Fields

- Date
- Product
- Transaction_Type
- Opening_Stock
- Purchases
- Sales_Units
- Closing_Stock

## 📥 Purchase

Incoming inventory.

## 📤 Sale

Outgoing inventory.

## 📊 Closing Stock

Recorded inventory position after a movement.

## 🏷️ Product Summary

Group by:

`Product`

Calculate:

- Purchases
- Sales
- Average inventory
- Closing stock
- DSI
- Turnover

## 📅 Monthly Summary

Group by:

`Month`

Calculate:

- Purchases
- Sales
- Closing stock

## 📐 DSI

Days of Sales of Inventory.

Formula:

`Average Inventory / Average Daily Sales`

Unit:

`Days`

## 🧮 Average Daily Sales

Formula:

`Total Sales Units / Observation Days`

Unit:

`Units per day`

## 🔄 Inventory Turnover

Formula:

`Total Sales Units / Average Inventory`

Unit:

`Times`

## 📈 DSI Meaning

Higher DSI:

- More inventory days relative to sales velocity.

Lower DSI:

- Fewer inventory days relative to sales velocity.

## ⚠️ Important

Do not automatically label DSI as good or bad.

Business context is required.

## 📊 Presentation

Use:

`Question → Data → Summary → Chart → Observation`

## 🎨 Chart Rules

- Clear title
- Clear axes
- Visible units
- Appropriate chart
- Consistent colours

## 📊 Useful Charts

Product comparison:

Column chart.

Monthly movement:

Line chart.

Turnover comparison:

Column chart.

## 🔎 Data Quality

Check:

- Dates
- Products
- Transaction types
- Missing values
- Duplicates
- Numeric values
- Chronological order

## 💻 Excel

Useful tools:

- Sort
- Filter
- Pivot Table
- SUM
- AVERAGE
- COUNT
- SUMIF
- AVERAGEIF
- Charts
- Dashboard

## 🐍 Python

Libraries:

- pandas
- matplotlib
- pathlib

## 🐼 Pandas

`pd.read_excel()`

`pd.to_datetime()`

`df.groupby()`

`.agg()`

`.reset_index()`

`.to_csv()`

## 📈 Matplotlib

`plt.bar()`

`plt.plot()`

`plt.title()`

`plt.xlabel()`

`plt.ylabel()`

`plt.savefig()`

## 🧠 Key Learning

Raw data is not the final presentation.

The analyst needs to summarize the data.

## 💼 Business Learning

Inventory should be understood with sales.

Sales should be understood with time.

Metrics should be understood with their definitions.

## ❌ Avoid

- Confusing purchases and sales.
- Ignoring dates.
- Mixing units.
- Using unclear charts.
- Making unsupported explanations.

## 📝 Quick Questions

What is a ledger?

What is DSI?

What is turnover?

Why use product grouping?

Why use monthly grouping?

Why use charts?

## 🎯 Quick Workflow

`Read → Check → Summarize → Calculate → Visualize → Interpret`

## 🔁 Final Revision

Ledger = source.

Summary = organization.

Metric = measurement.

Chart = communication.

Insight = evidence-based interpretation.

## 🏁 Final Reminder

Always verify the source data before presenting the conclusion.

## 🏅 Badges

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-035-brightgreen?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Key%20Learnings%20from%20the%20Case-purple?style=for-the-badge)

**Status:** Completed