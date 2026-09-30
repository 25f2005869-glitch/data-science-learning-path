# Day 032 — Ledger and Average Days of Inventory Cheat Sheet

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-032-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 032  
**Topic:** Ledger and Average Days of Inventory

## 📚 Core Topic

- W6_L4 = Ledger and Average Days of Inventory.
- Main focus = inventory movement and inventory coverage.
- Main practical tool = Excel.
- Supporting tool = Python.

## 📒 Ledger

- Ledger records inventory transactions.
- One row represents one transaction.
- Date = transaction date.
- Product = inventory item.
- Transaction Type = movement type.
- Opening Stock = starting stock.
- Purchases = stock added.
- Sales Units = stock sold.
- Closing Stock = remaining stock.

## 🔄 Movement Rules

- Purchase → inventory increases.
- Sale → inventory decreases.
- Adjustment → inventory can increase or decrease.
- Closing balance should be checked.
- Chronological order matters.

## 📦 Average Inventory

- Average inventory represents a typical inventory level.
- Use consistent observations.
- Check whether the average is calculated from appropriate stock values.
- Interpret average inventory with sales volume.
- Do not use a single closing value as the complete story.

## 📅 Inventory Days

- Inventory days express stock relative to sales velocity.
- Unit = days.
- Average daily sales are required.
- Average stock is required.
- Consistent units are essential.

## 🧮 Formula Workflow

- Total Sales Units = SUM of sales units.
- Observation Days = final date − first date + 1.
- Average Daily Sales = Total Sales Units / Observation Days.
- Average Days = Average Inventory / Average Daily Sales.

## 📊 Excel Functions

- `SUM()` → totals.
- `AVERAGE()` → average stock.
- `COUNT()` → numeric observations.
- `COUNTIF()` → conditional counts.
- `SUMIF()` → conditional totals.
- `SUMIFS()` → multiple-condition totals.
- Pivot Tables → product summaries.

## 📑 Workbook Sheets

- `Inventory_Ledger`
- `Product_Inventory_Summary`
- `Monthly_Inventory`
- `Average_Days_Analysis`
- `Ledger_Questions`
- `Business_Insights`
- `Inventory_Dashboard`
- `Data_Dictionary`
- `Instructions`

## 📈 Dashboard Charts

- Average Days of Inventory by Product.
- Monthly Closing Stock.
- Sales Units by Product.
- Charts contain explicit colours.
- Chart titles should identify the metric.
- Axes should include units.

## 🐍 Python

- `pandas` → data processing.
- `matplotlib` → charts.
- `Path` → file paths.
- `read_excel()` → load workbook.
- `groupby()` → product aggregation.
- `agg()` → multiple metrics.
- `to_csv()` → save summaries.

## 💼 Interpretation

- Higher inventory days = more inventory relative to sales velocity.
- Lower inventory days = fewer inventory days relative to sales velocity.
- Compare products using the same methodology.
- Check the underlying stock and sales values.
- Do not interpret the metric in isolation.

## ⚠️ Common Errors

- Wrong opening stock.
- Wrong closing stock.
- Wrong sales units.
- Wrong observation period.
- Inconsistent units.
- Missing transactions.
- Duplicate transactions.
- Unsupported business conclusions.

## ✅ Quick Revision

- What is a ledger?
- What increases inventory?
- What decreases inventory?
- What is closing stock?
- What is average inventory?
- What does inventory days measure?
- Why is sales velocity important?
- Why is data quality important?

## 🏁 Final Workflow

- Read lecture.
- Open ledger.
- Verify transactions.
- Calculate inventory metrics.
- Build product summary.
- Review dashboard.
- Run Python.
- Write insights.
- Commit work to GitHub.