# Day 034 — W6_L6 Presentation of Ledger

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

## 📚 Lecture Mapping

- Course: Business Data Management
- Week: W6
- Lecture: W6_L6
- Topic: Presentation of Ledger
- Previous lecture: Days of Sales of Inventory
- Current focus: Presenting inventory ledger information clearly.

## 🎯 Learning Objectives

- Understand the role of an inventory ledger.
- Read inventory movements chronologically.
- Present opening stock.
- Present purchases.
- Present sales.
- Present closing stock.
- Summarize ledger information by product.
- Summarize ledger information by month.
- Use charts to communicate ledger information.

## 📦 Ledger Structure

- Date records when a movement occurs.
- Product identifies the inventory item.
- Transaction_Type identifies the movement.
- Opening_Stock represents stock before the recorded movement.
- Purchases represent incoming units.
- Sales_Units represent outgoing units.
- Closing_Stock represents stock after the recorded movement.

## 📊 Presentation Focus

A ledger contains detailed transaction-level information.

A presentation converts detailed records into understandable summaries.

Product summaries make comparisons easier.

Monthly summaries show changes over time.

Charts help communicate the main patterns.

A good presentation should retain the connection to source data.

## 📈 Product Summary

- Product_Ledger_Summary groups the ledger by product.
- Total purchases show incoming units.
- Total sales units show outgoing units.
- Average inventory summarizes recorded closing stock.
- Closing stock shows the latest recorded position.
- Net stock change provides an additional summary.

## 📅 Monthly Summary

Monthly_Ledger groups movements by month.

Purchases can be compared with sales.

Closing stock can be tracked over time.

Monthly analysis helps identify changes in inventory position.

The same date definition should be used consistently.

## 💼 Business Questions

- What is the purpose of the ledger?
- Which products have higher sales?
- Which products receive more purchases?
- How does closing stock change over time?
- What inventory movements need further investigation?
- Which observations are directly supported by the data?

## 📊 Excel Presentation

Start from Inventory_Ledger.

Verify the source records.

Review Product_Ledger_Summary.

Review Monthly_Ledger.

Review Transaction_Summary.

Use Ledger_Dashboard for visual presentation.

Keep chart titles and units clear.

## 📊 Dashboard Charts

- Sales Units by Product is presented as a column chart.
- Monthly Closing Stock is presented as a line chart.
- Charts use explicit colours.
- Chart titles identify the metric.
- Axis labels identify the measurement.
- Dashboard KPIs provide quick context.

## 🔎 Data Quality

Check for missing dates.

Check product names.

Check transaction types.

Check numeric stock values.

Check for unexpected negative values.

Check chronological order.

Check whether closing stock follows the recorded movement logic.

## 💻 Python Support

Python provides a reproducible way to summarize the ledger.

Pandas can group records by product and month.

Matplotlib can create presentation charts.

Pathlib can locate the workbook.

CSV outputs can preserve summary tables.

Python should reproduce the logic used in Excel.

## 📝 Recommended Presentation Flow

1. Introduce the inventory question.
2. Explain the ledger fields.
3. Show transaction movements.
4. Present product summary.
5. Present monthly summary.
6. Show dashboard charts.
7. Highlight data-supported observations.
8. State limitations and assumptions.

## ⚠️ Common Mistakes

- Presenting raw rows without a summary.
- Confusing purchases with sales.
- Ignoring dates.
- Mixing products.
- Using unclear chart titles.
- Removing units from axis labels.
- Making causal claims unsupported by the ledger.

## 🧠 Key Takeaways

The ledger is the detailed source of inventory movements.

Presentation converts detailed records into useful summaries.

Product and monthly views provide different perspectives.

Charts should communicate one clear message.

Data quality is necessary before presentation.

Business interpretation must remain connected to recorded data.

## 🗂️ Repository Structure

- README.md documents the day.
- notes.md contains learning notes.
- cheat-sheet.md provides quick revision.
- practice.md contains exercises.
- resources.md records study resources.
- Excel contains practical analysis.
- Python provides supporting analysis.

## ✅ Completion Checklist

- [x] Watched W6_L6.
- [x] Reviewed inventory ledger.
- [x] Reviewed product summary.
- [x] Reviewed monthly summary.
- [x] Reviewed dashboard.
- [x] Practised presentation questions.
- [x] Reviewed Python workflow.
- [x] Completed Day 034.

## 🏅 Badges

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-034-brightgreen?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Presentation%20of%20Ledger-purple?style=for-the-badge)

**Status:** Completed