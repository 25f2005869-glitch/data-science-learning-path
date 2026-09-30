# Day 033 — W6_L5 Days of Sales of Inventory

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

## 📚 Lecture Mapping

- Course: Business Data Management
- Week: W6
- Lecture: W6_L5
- Topic: Days of Sales of Inventory
- Previous topic: Ledger and Average Days of Inventory
- Current focus: Inventory coverage through sales velocity

## 🎯 Learning Objectives

- Understand Days of Sales of Inventory.
- Understand average inventory.
- Calculate average daily sales.
- Calculate DSI.
- Understand inventory turnover.
- Compare products.
- Interpret inventory coverage.
- Present inventory findings.

## 📦 Dataset

The practical workbook contains inventory records.

Important fields include:

- Date
- Product
- Opening_Stock
- Purchases
- Sales_Units
- Closing_Stock

The dataset is used for product-level inventory analysis.

## 🧮 DSI Formula

Average Daily Sales:

Average Daily Sales = Total Sales Units / Observation Days

Days of Sales of Inventory:

DSI = Average Inventory / Average Daily Sales

The final result is expressed in days.

## 📊 Average Inventory

Inventory changes over time.

A single closing-stock value may not represent the complete inventory position.

Average inventory gives a more useful basis for calculating inventory coverage.

## 🚀 Sales Velocity

Sales velocity represents how quickly inventory is being sold.

The practical calculation converts total sales into an average daily sales rate.

This daily sales rate is then used in the DSI calculation.

## 📈 DSI Interpretation

A higher DSI means more inventory days relative to the observed sales rate.

A lower DSI means fewer inventory days relative to the observed sales rate.

The comparison should use the same observation period and calculation method.

## 🔄 Inventory Turnover

Inventory turnover provides a complementary view.

For this practical exercise:

Inventory Turnover = Total Sales Units / Average Inventory

It connects sales volume with average inventory.

## 🗂️ Workbook Sheets

The Excel workbook contains:

- Inventory_Data
- Product_DSI_Analysis
- Monthly_Inventory
- Region_Analysis
- Key_Questions
- Business_Insights
- Data_Dictionary
- Instructions
- DSI_Dashboard

## 📊 Dashboard

The dashboard contains:

- DSI by Product
- Monthly Closing Inventory
- Inventory Turnover by Product

The charts use explicit colours for clear presentation.

## 💻 Python Analysis

Python is used as a supporting analysis tool.

The script uses:

- pandas
- matplotlib
- pathlib

The script reads the Excel workbook and creates product-level DSI analysis.

## 🐼 Pandas Workflow

The Python workflow includes:

1. Locate the workbook.
2. Read Inventory_Data.
3. Convert Date.
4. Calculate observation days.
5. Group records by Product.
6. Calculate sales units.
7. Calculate average inventory.
8. Calculate average daily sales.
9. Calculate DSI.
10. Calculate inventory turnover.

## 📤 Outputs

The Python script produces:

- Product DSI CSV
- Monthly inventory CSV
- DSI chart
- Monthly inventory chart

## 🔎 Data Quality

Before interpreting DSI:

- Check missing values.
- Check duplicate records.
- Check dates.
- Check product names.
- Check sales units.
- Check inventory values.
- Check the observation period.

## ⚠️ Common Mistakes

Do not:

- Mix different time periods.
- Mix units.
- Ignore average inventory.
- Ignore sales velocity.
- Treat DSI as profitability.
- Make unsupported causal claims.

## 💼 Business Interpretation

DSI should be interpreted together with:

- Sales volume
- Average inventory
- Product demand
- Replenishment patterns
- Inventory policy
- Observation period

A DSI number alone does not explain why inventory is at that level.

## 📝 Presentation Flow

A short business presentation can follow this structure:

1. State the inventory question.
2. Explain DSI.
3. Show the formula.
4. Present product-level DSI.
5. Compare sales velocity.
6. Show inventory turnover.
7. Explain observed differences.
8. State assumptions.
9. Present evidence-based insights.

## 🧠 Key Takeaways

- DSI is expressed in days.
- Average daily sales depend on the observation period.
- Average inventory is central to the calculation.
- DSI measures inventory coverage relative to sales velocity.
- Inventory turnover is a useful supporting metric.
- Consistent methodology is necessary for comparisons.

## ✅ Completion Checklist

- [x] Watched W6_L5.
- [x] Understood DSI.
- [x] Reviewed the dataset.
- [x] Calculated average daily sales.
- [x] Calculated DSI.
- [x] Reviewed inventory turnover.
- [x] Reviewed dashboard.
- [x] Practised Excel analysis.
- [x] Practised Python analysis.
- [x] Prepared business insights.

## 🏅 Badges

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-033-brightgreen?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Days%20of%20Sales%20of%20Inventory-purple?style=for-the-badge)

**Status:** Completed