# Day 032 — Ledger and Average Days of Inventory Notes

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

## 📚 Lecture Mapping

- W6_L4 covers ledger and average days of inventory.
- The topic connects transaction records with inventory analysis.
- Inventory movement is recorded chronologically.
- Sales velocity is important for inventory-day calculations.

## 📒 Ledger Meaning

- A ledger is a structured record of transactions.
- Inventory ledgers track stock movement.
- Each row represents a transaction.
- The date gives chronological order.
- Product identifies the stock item.
- Transaction type identifies the movement.

## 📥 Opening Stock

- Opening stock is the stock available at the beginning of a transaction sequence.
- It provides the starting inventory position.
- Opening stock should be checked carefully.
- Incorrect opening stock affects subsequent balances.
- It is important for reconciliation.

## 🛒 Purchases

- Purchases add inventory.
- Purchase quantities should be recorded accurately.
- Purchase transactions can be reviewed by product.
- Purchase timing affects stock availability.
- Purchases should be checked against source records.

## 🛍️ Sales

- Sales represent inventory leaving the stock.
- Sales units reduce available inventory.
- Sales volume provides sales velocity.
- Sales should be recorded consistently.
- Sales are important for inventory-days calculations.

## 📦 Closing Stock

- Closing stock is the inventory remaining after movements.
- It is an important ledger balance.
- Closing stock can be reviewed after each transaction.
- Product-level closing stock helps comparison.
- Monthly closing stock can be used for trend analysis.

## 📊 Average Stock

- Inventory changes over time.
- Average stock gives a representative value.
- Day 032 uses average recorded closing stock.
- Average stock is useful when the inventory level fluctuates.
- It should be interpreted with the period and sales volume.

## 📅 Inventory Days

- Inventory days connect stock with sales velocity.
- The result is expressed in days.
- Average daily sales are required.
- The observation period must be consistent.
- The metric should be interpreted with its calculation basis.

## 🧮 Calculation Steps

- Find total sales units.
- Find the number of days.
- Calculate average daily sales.
- Calculate average inventory.
- Divide average inventory by average daily sales.
- Review the result.
- Check whether units are consistent.

## 📊 Excel Practice

- Open `Inventory_Ledger`.
- Inspect the transactions.
- Filter by product.
- Follow stock movements.
- Open `Product_Inventory_Summary`.
- Review `Average_Days_Analysis`.
- Open the dashboard.
- Compare products.

## 📈 Dashboard Notes

- The dashboard presents inventory KPIs.
- Product inventory days are shown visually.
- Monthly closing stock is presented as a trend.
- Sales units provide supporting context.
- Explicit chart colours are used.

## 🐍 Python Notes

- Pandas reads the workbook.
- Dates are converted to datetime.
- Product groups are created.
- Sales velocity is calculated.
- Average stock is calculated.
- Inventory days are calculated.
- CSV summaries are exported.
- Charts are generated.

## 💼 Business Meaning

- Inventory analysis helps understand stock position.
- Sales velocity gives context to inventory.
- A high inventory-days value means more stock relative to observed sales velocity.
- A lower value means fewer inventory days relative to observed sales velocity.
- Business context is necessary before interpreting the metric.

## ⚠️ Data Quality

- Dates should be valid.
- Products should be consistently named.
- Quantities should be numeric.
- Duplicate transactions should be checked.
- Opening and closing stock should be reviewed.
- Calculations should be reconciled.

## 🔁 Revision

- Ledger = inventory transaction record.
- Purchases increase stock.
- Sales decrease stock.
- Closing stock is the resulting balance.
- Average stock represents a typical stock level.
- Inventory days connect stock and sales velocity.