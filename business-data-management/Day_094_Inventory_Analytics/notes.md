# 📝 Day 094 — Inventory Analytics Notes

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Programme](https://img.shields.io/badge/Programme-Diploma%20Level-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-094-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Inventory%20Analytics-orange?style=for-the-badge)

## 👩‍💻 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 094
- **Topic:** Inventory Analytics

---

## 1. Introduction to Inventory Analytics

Inventory Analytics is the process of analysing inventory data to understand stock levels, stock movement, inventory value, product performance, warehouse performance, and replenishment requirements.

Inventory analysis helps a business understand:

- How much stock is available
- How much stock enters inventory
- How much stock leaves inventory
- How much inventory is currently held
- Which products have high inventory value
- Which warehouses hold more inventory
- Which products may require replenishment

The main goal is to convert inventory records into useful business information.

---

## 2. Inventory Data

An inventory dataset contains information about inventory records.

Important fields in the Day 094 dataset include:

- Inventory ID
- Date
- Product ID
- Product
- Category
- Warehouse
- Opening Stock
- Stock In
- Stock Out
- Closing Stock
- Unit Cost
- Inventory Value
- Reorder Level
- Supplier
- Stock Status

Each inventory record provides information about stock and its movement.

---

## 3. Opening Stock

Opening Stock represents the quantity of inventory available at the beginning of an inventory period or record.

It provides the starting point for calculating inventory movement.

Opening Stock is useful when analysing how stock changes after receiving and issuing inventory.

---

## 4. Stock In

Stock In represents inventory received into the warehouse or inventory system.

Examples include:

- New stock received from suppliers
- Inventory replenishment
- Incoming products

Stock In increases the available inventory.

---

## 5. Stock Out

Stock Out represents inventory that leaves the available stock.

Examples include:

- Products sold
- Products issued
- Inventory transferred out
- Other stock movements

Stock Out decreases available inventory.

---

## 6. Closing Stock

Closing Stock represents the inventory remaining after stock movement.

The basic relationship is:

**Closing Stock = Opening Stock + Stock In − Stock Out**

Example:

- Opening Stock = 100
- Stock In = 40
- Stock Out = 30

Closing Stock:

**100 + 40 − 30 = 110 units**

Closing Stock is one of the main inventory measures.

---

## 7. Inventory Value

Inventory Value represents the value of the available closing stock.

The basic formula is:

**Inventory Value = Closing Stock × Unit Cost**

Example:

- Closing Stock = 100 units
- Unit Cost = ₹500

Inventory Value:

**100 × ₹500 = ₹50,000**

Inventory value helps measure the value held in inventory.

---

## 8. Unit Cost

Unit Cost represents the cost associated with one unit of a product.

Unit Cost is used to calculate inventory value.

**Inventory Value = Closing Stock × Unit Cost**

A change in unit cost can affect the total inventory value even when the stock quantity remains unchanged.

---

## 9. Inventory Data Inspection

Before analysing inventory data, inspect the dataset.

Important checks include:

- Number of records
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate records
- Text inconsistencies
- Negative values
- Stock calculations

Inspection helps identify problems before analysis.

---

## 10. Inventory Data Quality

Inventory data can contain several quality problems.

Common examples include:

### Missing Values

A field may have no value.

Examples:

- Missing Unit Cost
- Missing Stock In
- Missing Closing Stock

Missing values should be identified before analysis.

### Extra Spaces

Text values may contain unnecessary spaces.

Example:

- `North Warehouse`
- ` North Warehouse `

These should be standardised.

### Inconsistent Capitalisation

The same category or warehouse may appear with different capitalization.

Example:

- `Electronics`
- `electronics`
- `ELECTRONICS`

Standardisation makes grouping and analysis more reliable.

### Duplicate Records

Duplicate inventory records can affect totals and inventory values.

Duplicates should be identified and handled before analysis.

### Negative Stock Movement

Stock Out should normally represent a quantity leaving inventory.

Negative values should be checked and flagged during data validation.

---

## 11. Inventory Data Cleaning

The cleaning workflow includes:

1. Inspect the dataset.
2. Identify data-quality problems.
3. Remove unnecessary spaces.
4. Standardise text values.
5. Handle missing values.
6. Validate numeric values.
7. Check stock movement.
8. Remove duplicate records.
9. Recalculate derived values.
10. Validate the cleaned dataset.

The cleaned dataset is used for further analysis.

---

## 12. Product Inventory Analysis

Product analysis compares inventory performance across products.

Important measures include:

- Closing Stock
- Stock Out
- Inventory Value
- Reorder Level
- Reorder Records

Questions include:

- Which product has a high inventory value?
- Which products have higher stock movement?
- Which products are at or below their reorder level?

---

## 13. Category Analysis

Products can be grouped by category.

Category analysis can include:

- Closing Stock by Category
- Stock In by Category
- Stock Out by Category
- Inventory Value by Category
- Number of Records

This helps understand how inventory is distributed across categories.

---

## 14. Warehouse Analysis

Warehouse analysis compares inventory across different warehouses.

Important measures include:

- Closing Stock
- Stock In
- Stock Out
- Inventory Value
- Reorder Records
- Number of Records

Warehouse analysis helps understand the distribution of inventory.

---

## 15. Monthly Inventory Analysis

Inventory records can be grouped by month.

Monthly analysis can include:

- Opening Stock
- Stock In
- Stock Out
- Closing Stock
- Inventory Value

Monthly analysis helps identify changes in inventory over time.

---

## 16. Stock Movement Analysis

Stock movement compares inventory entering and leaving the system.

Important measures include:

- Total Stock In
- Total Stock Out
- Net Movement

Formula:

**Net Movement = Stock In − Stock Out**

Example:

- Stock In = 500 units
- Stock Out = 350 units

Net Movement:

**500 − 350 = 150 units**

---

## 17. Reorder Level

Reorder Level is a stock threshold used to identify inventory that may require replenishment.

The Day 094 workbook compares Closing Stock with Reorder Level.

If:

**Closing Stock ≤ Reorder Level**

the record can be identified as being at or below the reorder level.

This helps identify inventory that may require attention.

---

## 18. Stock Status

Stock Status provides information about the current inventory condition.

The Day 094 analysis uses categories such as:

- Healthy Stock
- Below Reorder Level

Stock status can be used together with closing stock and reorder level for inventory monitoring.

---

## 19. Inventory KPIs

Key Performance Indicators provide a quick summary of inventory performance.

Important Day 094 KPIs include:

### Total Inventory Value

The total value of closing inventory.

### Total Stock In

The total quantity received.

### Total Stock Out

The total quantity issued or moved out.

### Total Closing Stock

The total quantity remaining.

### Average Inventory Value

The average inventory value across inventory records.

### Reorder-Level Records

The number of records at or below the reorder level.

### Inventory Utilisation

A measure used in the workbook to compare stock-out quantity with opening stock.

---

## 20. Pivot Analysis

Pivot-style analysis summarises inventory data by different dimensions.

The Day 094 workbook contains pivot analysis for:

- Products
- Categories
- Warehouses

Pivot analysis makes it easier to compare inventory measures.

---

## 21. Inventory Visualisation

Charts help communicate inventory results visually.

The workbook includes:

- Inventory Value by Product
- Inventory Value by Warehouse
- Monthly Inventory Value Trend

### Bar Chart

Useful for comparing inventory value across products or warehouses.

### Line Chart

Useful for showing inventory value over time.

---

## 22. Business Insights

Inventory analysis can be used to identify useful patterns.

Questions include:

- Which products have higher inventory value?
- Which products have higher stock movement?
- Which categories hold more inventory?
- Which warehouses hold more inventory?
- Which records are at or below the reorder level?
- How does inventory value change over time?

Insights should be based on the analysed data.

---

## 23. Excel Workflow

The Day 094 Excel workflow is:

**Raw Inventory Data**

↓

**Data Quality Check**

↓

**Inventory Cleaning**

↓

**Cleaned Inventory Data**

↓

**Inventory Summary**

↓

**Product Analysis**

↓

**Category Analysis**

↓

**Warehouse Analysis**

↓

**Monthly Inventory**

↓

**Stock Movement Analysis**

↓

**Inventory KPIs**

↓

**Pivot Analysis**

↓

**Charts**

↓

**Inventory Insights**

↓

**Final Inventory Analysis**

---

## 24. Python and Inventory Analytics

Inventory Analytics can also be performed using Python.

Important libraries include:

- Pandas
- NumPy
- Matplotlib

### Pandas

Pandas can be used for:

- Reading Excel files
- Inspecting data
- Cleaning data
- Grouping inventory records
- Aggregating stock values
- Creating summary tables
- Exporting analysis results

### NumPy

NumPy can be used for:

- Numerical calculations
- Conditional calculations
- Array-based operations

### Matplotlib

Matplotlib can be used for:

- Inventory charts
- Product comparisons
- Warehouse comparisons
- Monthly trends

---

## 25. Important Inventory Formulas

### Closing Stock

**Closing Stock = Opening Stock + Stock In − Stock Out**

### Inventory Value

**Inventory Value = Closing Stock × Unit Cost**

### Net Movement

**Net Movement = Stock In − Stock Out**

### Reorder Condition

**Closing Stock ≤ Reorder Level**

---

## 26. Important Analysis Questions

1. What is Inventory Analytics?
2. What is Opening Stock?
3. What is Stock In?
4. What is Stock Out?
5. How is Closing Stock calculated?
6. How is Inventory Value calculated?
7. Why is Unit Cost important?
8. Why should inventory data be cleaned?
9. Which products have higher inventory value?
10. Which categories hold more inventory?
11. Which warehouses hold more inventory?
12. Which records are at or below the reorder level?
13. How does inventory change over time?
14. What are the important inventory KPIs?
15. Why are charts useful in inventory analysis?

---

## 27. Key Learning Points

- Inventory Analytics helps understand stock performance.
- Data should be inspected before analysis.
- Missing values and duplicates can affect results.
- Text values should be standardised.
- Stock movement should be validated.
- Closing Stock represents remaining inventory.
- Inventory Value measures the value of available stock.
- Product analysis compares inventory across products.
- Category analysis compares inventory categories.
- Warehouse analysis compares inventory locations.
- Monthly analysis helps understand inventory changes over time.
- Reorder levels help identify stock that may require replenishment.
- KPIs provide a quick summary of inventory performance.
- Charts make inventory analysis easier to communicate.
- Business insights should be based on data.

---

## 28. Day 094 Summary

Day 094 focuses on Inventory Analytics.

The practical workflow starts with raw inventory data and continues through data-quality checking, cleaning, inventory calculations, product analysis, category analysis, warehouse analysis, monthly analysis, stock movement analysis, KPI calculation, pivot analysis, visualisation, and business insights.

The complete process is:

**Inspect → Clean → Calculate → Analyse → Visualise → Interpret → Present**

---

## 🔑 Final Takeaway

Inventory Analytics converts raw inventory records into useful information about:

**Stock Levels + Stock Movement + Inventory Value + Products + Categories + Warehouses + Reorder Requirements**

The goal is to understand inventory data clearly and use it to support better business analysis.