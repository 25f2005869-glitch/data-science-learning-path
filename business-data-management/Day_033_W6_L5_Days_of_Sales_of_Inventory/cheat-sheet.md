
### 3. cheat-sheet.md

```markdown
# Day 033 — Days of Sales of Inventory Cheat Sheet

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-033-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 033  
**Topic:** Days of Sales of Inventory

## 📚 Lecture

- Week: W6
- Lecture: W6_L5
- Topic: Days of Sales of Inventory

## 🎯 Core Idea

DSI measures inventory coverage in days relative to sales velocity.

## 🧮 Main Formula

Average Daily Sales:

`Total Sales Units / Observation Days`

DSI:

`Average Inventory / Average Daily Sales`

## 🔢 Units

Average Inventory:

`Units`

Average Daily Sales:

`Units per day`

DSI:

`Days`

Inventory Turnover:

`Times`

## 📦 Required Fields

- Date
- Product
- Purchases
- Sales_Units
- Closing_Stock

## 📅 Observation Days

Use:

`MAX(Date) - MIN(Date) + 1`

This avoids excluding either endpoint of the observation period.

## 📊 Average Inventory

Use the average of recorded inventory values.

Example:

`AVERAGE(Closing_Stock)`

## 🚀 Sales Velocity

Sales velocity is represented by average daily sales.

Formula:

`Sales Units / Observation Days`

## 📐 DSI Calculation

Step 1:

Find total sales units.

Step 2:

Find observation days.

Step 3:

Calculate average daily sales.

Step 4:

Find average inventory.

Step 5:

Divide average inventory by average daily sales.

## 🔄 Inventory Turnover

Formula used in this practical:

`Total Sales Units / Average Inventory`

It complements DSI.

## 📈 DSI Interpretation

Higher DSI:

- More inventory days.
- Lower sales velocity relative to inventory.

Lower DSI:

- Fewer inventory days.
- Higher sales velocity relative to inventory.

## ⚠️ Do Not Assume

High DSI does not automatically mean bad inventory management.

Low DSI does not automatically mean perfect inventory management.

Business context is required.

## 📊 Excel Functions

Useful functions:

- `SUM`
- `AVERAGE`
- `COUNT`
- `COUNTIF`
- `SUMIF`
- `AVERAGEIF`
- `MAX`
- `MIN`

## 🧩 Excel Workflow

1. Open workbook.
2. Review Inventory_Data.
3. Check Date.
4. Check Product.
5. Check Sales_Units.
6. Check Closing_Stock.
7. Review Product_DSI_Analysis.
8. Review dashboard.

## 📊 Dashboard Charts

The dashboard contains:

- DSI by Product
- Monthly Closing Inventory
- Inventory Turnover by Product

## 🐍 Python

Main libraries:

- pandas
- matplotlib
- pathlib

Basic pandas:

`pd.read_excel()`

Date conversion:

`pd.to_datetime()`

Grouping:

`df.groupby("Product")`

## 📤 Python Outputs

- product_dsi_analysis.csv
- monthly_inventory_summary.csv
- days_of_sales_inventory.png
- monthly_closing_inventory.png

## 🔎 Data Checks

Check:

- Missing values
- Duplicate records
- Invalid dates
- Invalid products
- Missing sales
- Missing inventory
- Observation period

## ❌ Common Mistakes

- Wrong denominator
- Wrong observation period
- Mixing units
- Using closing stock as total inventory
- Ignoring average inventory
- Ignoring sales velocity
- Treating DSI as profitability

## 📝 Quick Questions

What is DSI?

Answer:

Inventory coverage expressed in days relative to average daily sales.

What is average daily sales?

Answer:

Total sales divided by observation days.

What is inventory turnover?

Answer:

Sales volume relative to average inventory.

## 🎯 Exam Reminder

Remember these three formulas:

`Average Daily Sales = Sales / Days`

`DSI = Average Inventory / Average Daily Sales`

`Turnover = Sales / Average Inventory`

## 🏁 Final Revision

DSI is an inventory metric.

It should be calculated consistently.

Product comparison should use the same methodology.

Always check the data before interpreting the result.

## 🏅 Badges

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-033-brightgreen?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Days%20of%20Sales%20of%20Inventory-purple?style=for-the-badge)

**Status:** Completed