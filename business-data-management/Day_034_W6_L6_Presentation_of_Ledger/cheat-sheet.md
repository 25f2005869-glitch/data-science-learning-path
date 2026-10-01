# Day 034 — Presentation of Ledger Cheat Sheet

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-034-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 034  
**Topic:** Presentation of Ledger

## 📚 Lecture

- Week: W6
- Lecture: W6_L6
- Topic: Presentation of Ledger

## 📌 Ledger

A ledger records inventory movements.

## 📦 Main Fields

- Date
- Product
- Transaction_Type
- Opening_Stock
- Purchases
- Sales_Units
- Closing_Stock

## 🔄 Transaction Types

- Opening
- Purchase
- Sale

## 📥 Purchase

Purchase = incoming inventory.

## 📤 Sale

Sale = outgoing inventory.

## 📊 Closing Stock

Closing Stock = recorded stock position after the movement.

## 📈 Product Summary

Group by Product.

Calculate:

- Total purchases
- Total sales
- Average inventory
- Closing stock

## 📅 Monthly Summary

Group by Month.

Calculate:

- Purchases
- Sales units
- Closing stock

## 🧮 Useful Excel Functions

- `SUM`
- `AVERAGE`
- `COUNT`
- `COUNTIF`
- `SUMIF`
- `AVERAGEIF`
- `MAX`
- `MIN`

## 📊 Pivot Table

Basic workflow:

1. Select data.
2. Insert Pivot Table.
3. Put Product in Rows.
4. Put Sales_Units in Values.
5. Put Purchases in Values.
6. Review totals.

## 📈 Chart Selection

Product comparison:

Column chart.

Monthly movement:

Line chart.

Transaction comparison:

Column or bar chart.

## 🎨 Chart Rules

- Use clear title.
- Label axes.
- Show units.
- Use consistent colours.
- Avoid unnecessary decoration.

## 🔎 Data Checks

Check:

- Missing values
- Duplicate records
- Invalid dates
- Invalid products
- Invalid transaction types
- Negative stock
- Unexpected movements

## 💻 Dashboard

Dashboard can show:

- Total purchases
- Total sales
- Average closing stock
- Number of products
- Sales by product
- Monthly closing stock

## 🐍 Python

Libraries:

- pandas
- matplotlib
- pathlib

## 🐼 Pandas

Read Excel:

`pd.read_excel()`

Convert dates:

`pd.to_datetime()`

Group:

`df.groupby()`

Aggregate:

`.agg()`

Export:

`.to_csv()`

## 📊 Matplotlib

Useful commands:

`plt.bar()`

`plt.plot()`

`plt.title()`

`plt.xlabel()`

`plt.ylabel()`

`plt.savefig()`

## 💼 Business Questions

Ask:

- What happened?
- Which product has more sales?
- Which product has more purchases?
- How does stock change?
- What needs further investigation?

## ⚠️ Avoid

- Confusing purchases and sales.
- Ignoring dates.
- Mixing products.
- Using unclear charts.
- Unsupported explanations.

## 📝 Quick Definitions

Ledger = inventory movement record.

Purchase = incoming inventory.

Sale = outgoing inventory.

Opening stock = starting recorded stock.

Closing stock = ending recorded stock.

Product summary = grouped product view.

Monthly summary = time view.

Dashboard = presentation view.

## 🎯 Presentation Flow

`Question → Ledger → Summary → Chart → Observation → Insight`

## 🔁 Revision

The ledger is the source.

The summary simplifies the source.

The chart communicates the summary.

The insight interprets the evidence.

## 🏁 Final Reminder

Always verify the source ledger before presenting the result.

## 🏅 Badges

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-034-brightgreen?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Presentation%20of%20Ledger-purple?style=for-the-badge)

**Status:** Completed