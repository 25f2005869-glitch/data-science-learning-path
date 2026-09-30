# Day 032 — W6_L4 Ledger and Average Days of Inventory

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

- BDM playlist: **W6_L4 — Ledger & average days of inventory**.
- The lecture focuses on inventory records and inventory-day analysis.
- The practical work uses an inventory ledger.
- Transactions are recorded chronologically.
- Purchases increase inventory.
- Sales reduce inventory.

## 🎯 Learning Objectives

- Understand an inventory ledger.
- Understand opening stock.
- Record purchases.
- Record sales.
- Calculate closing stock.
- Calculate average inventory.
- Understand inventory days.
- Present inventory analysis.

## 📒 Inventory Ledger

- An inventory ledger records stock movements.
- Each transaction is stored as a separate row.
- Date identifies when the transaction occurred.
- Product identifies the inventory item.
- Transaction type describes the movement.
- Opening stock represents stock available before movement.
- Purchases add stock.
- Sales reduce stock.
- Closing stock represents the remaining balance.

## 🔄 Inventory Movement

- Purchase increases available inventory.
- Sales decrease available inventory.
- Adjustments can change the balance.
- Chronological order is important.
- Product-level filtering makes analysis easier.
- Closing stock should be checked after transactions.
- The ledger provides transaction traceability.

## 📦 Average Inventory

- Average inventory represents a typical inventory level.
- Day 032 uses average recorded closing stock for practice.
- Average stock is useful when inventory changes during the period.
- A single closing balance may not represent the complete period.
- Average inventory should be interpreted with sales volume.

## 📅 Average Days of Inventory

- Average days connect inventory with sales velocity.
- The metric expresses inventory relative to the observed sales rate.
- Higher days mean more inventory relative to the sales rate.
- Lower days mean fewer inventory days relative to the sales rate.
- The calculation requires consistent units.
- The observation period must be considered.

## 🧮 Calculation Workflow

1. Calculate total sales units.
2. Determine the observation period.
3. Calculate average daily sales.
4. Calculate average inventory.
5. Divide average inventory by average daily sales.
6. Express the result in days.
7. Check the units and assumptions.

## 📊 Excel Workbook

- `Inventory_Ledger` contains transaction records.
- `Product_Inventory_Summary` contains product-level calculations.
- `Monthly_Inventory` contains monthly inventory movement.
- `Average_Days_Analysis` contains inventory-days analysis.
- `Ledger_Questions` contains revision questions.
- `Business_Insights` contains observations.
- `Inventory_Dashboard` contains presentation charts.
- `Data_Dictionary` explains the fields.
- `Instructions` provides the workflow.

## 📈 Dashboard

- KPI values are displayed.
- Average inventory days are compared by product.
- Monthly closing stock is visualized.
- Product sales units are visualized.
- Charts use explicit colours.
- The dashboard supports presentation practice.

## 🐍 Python Workflow

- Load the Excel workbook.
- Read `Inventory_Ledger`.
- Convert the date column.
- Group records by product.
- Calculate sales velocity.
- Calculate average stock.
- Calculate average days.
- Export summary CSV files.
- Generate charts.

## 💼 Business Interpretation

- Inventory should be viewed together with sales activity.
- Stock level alone does not explain inventory efficiency.
- Sales velocity provides useful context.
- Inventory days can help describe stock coverage.
- Product characteristics should be considered.
- The metric should not be interpreted without its assumptions.

## ✅ Data Quality Checklist

- Check dates.
- Check duplicate transactions.
- Check product names.
- Check opening stock.
- Check purchases.
- Check sales.
- Check closing stock.
- Check units.
- Check observation period.
- Validate calculations.

## 🎤 Presentation Flow

- Introduce the inventory problem.
- Explain the ledger.
- Explain inventory movements.
- Show average stock.
- Show inventory days.
- Compare products.
- Explain the observed pattern.
- Mention assumptions.
- Present evidence-based insights.

## ⚠️ Common Mistakes

- Confusing opening and closing stock.
- Mixing units.
- Ignoring dates.
- Ignoring sales velocity.
- Using inconsistent periods.
- Treating inventory days as profit.
- Making unsupported causal claims.
- Ignoring data quality.

## 🏁 Completion Checklist

- [ ] Lecture reviewed.
- [ ] Ledger understood.
- [ ] Excel workbook completed.
- [ ] Inventory calculations checked.
- [ ] Dashboard reviewed.
- [ ] Python script executed.
- [ ] CSV outputs checked.
- [ ] Business insights written.
- [ ] Repository updated.