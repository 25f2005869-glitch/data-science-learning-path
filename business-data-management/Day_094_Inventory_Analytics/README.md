# 📦 Day 094 — Inventory Analytics

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

## 📌 Overview

Inventory Analytics is the process of analysing inventory data to understand stock levels, stock movement, inventory value, product performance, warehouse performance, and replenishment requirements.

Day 094 focuses on taking inventory data through a complete analytics workflow:

**Raw Inventory Data → Data Quality Check → Cleaning → Analysis → KPIs → Visualisation → Business Insights**

---

## 🎯 Learning Objectives

By completing Day 094, I will learn how to:

- Understand inventory data
- Inspect inventory records
- Identify data-quality issues
- Clean inventory data
- Analyse opening stock
- Analyse stock received
- Analyse stock issued
- Analyse closing stock
- Calculate inventory value
- Analyse products
- Analyse categories
- Analyse warehouses
- Analyse monthly inventory
- Analyse stock movement
- Calculate inventory KPIs
- Perform pivot-style analysis
- Create inventory charts
- Extract business insights
- Prepare a final inventory analysis

---

## 📚 Topics Covered

### 1. Inventory Data

The inventory dataset contains information about inventory records.

Important fields include:

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

---

## 🔍 2. Data Inspection

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
- Inventory-related calculations

Data inspection helps identify problems before analysis begins.

---

## 🧹 3. Inventory Data Cleaning

Inventory data may contain inconsistencies.

The cleaning process includes:

- Removing unnecessary spaces
- Standardising text values
- Handling missing values
- Checking numeric values
- Checking stock movement
- Checking closing stock
- Removing duplicate records
- Recalculating derived values
- Validating inventory data

The cleaned dataset is then used for analysis.

---

## 📦 4. Stock Movement

Inventory movement can be understood through:

- Opening Stock
- Stock In
- Stock Out
- Closing Stock

A basic inventory relationship is:

**Closing Stock = Opening Stock + Stock In − Stock Out**

This helps track how inventory changes.

---

## 💰 5. Inventory Value

Inventory value represents the value of the available closing stock.

**Inventory Value = Closing Stock × Unit Cost**

This helps measure the amount of value held in inventory.

---

## 🔄 6. Product Inventory Analysis

Product-level analysis helps compare inventory across products.

The analysis includes:

- Closing Stock
- Stock Out
- Inventory Value
- Reorder Level
- Reorder Records

This helps identify products that require closer inventory monitoring.

---

## 🗂️ 7. Category Analysis

Inventory can also be analysed by product category.

The analysis includes:

- Closing Stock by Category
- Stock In by Category
- Stock Out by Category
- Inventory Value by Category
- Number of Records

Category-level analysis helps compare inventory distribution.

---

## 🏢 8. Warehouse Analysis

Warehouse analysis compares inventory across different warehouses.

The analysis includes:

- Closing Stock
- Stock In
- Stock Out
- Inventory Value
- Reorder Records
- Number of Records

This helps understand how inventory is distributed across warehouses.

---

## 📅 9. Monthly Inventory Analysis

Inventory records can be grouped by month.

Monthly analysis includes:

- Opening Stock
- Stock In
- Stock Out
- Closing Stock
- Inventory Value

This helps identify changes in inventory over time.

---

## 🚚 10. Stock Movement Analysis

Stock movement analysis compares stock entering and leaving inventory.

Important measures include:

- Total Stock In
- Total Stock Out
- Net Movement

**Net Movement = Stock In − Stock Out**

This provides a simple view of inventory movement.

---

## 🎯 11. Reorder Level

The reorder level indicates a stock threshold used to identify inventory that may require replenishment.

In the workbook, records are checked against the reorder level.

A record can be identified as:

- Healthy Stock
- Below Reorder Level

This helps highlight inventory that may need attention.

---

## 📊 12. Inventory KPIs

Important inventory KPIs include:

- Total Inventory Value
- Total Stock In
- Total Stock Out
- Total Closing Stock
- Average Inventory Value
- Reorder-Level Records
- Inventory Utilisation

KPIs provide a quick summary of inventory performance.

---

## 🔄 13. Pivot Analysis

Pivot-style analysis is included for:

- Products
- Categories
- Warehouses

Pivot analysis makes it easier to summarise and compare inventory data.

---

## 📈 14. Inventory Visualisation

The workbook contains charts for:

- Inventory Value by Product
- Inventory Value by Warehouse
- Monthly Inventory Value Trend

### Bar Chart

Useful for comparing inventory value across products or warehouses.

### Line Chart

Useful for understanding inventory value over time.

---

## 💡 15. Business Insights

Inventory analysis can help answer questions such as:

- Which products have higher inventory value?
- Which products have more stock movement?
- Which records are at or below the reorder level?
- How is inventory distributed across warehouses?
- Which categories hold more inventory?
- How does inventory value change over time?

Business insights should be based on the analysed inventory data.

---

## 📁 Workbook Structure

The Day 094 workbook contains the following sheets:

1. Instructions
2. Raw_Inventory_Data
3. Data_Quality_Check
4. Inventory_Cleaning
5. Cleaned_Inventory_Data
6. Inventory_Summary
7. Product_Inventory_Analysis
8. Category_Analysis
9. Warehouse_Analysis
10. Monthly_Inventory
11. Stock_Movement_Analysis
12. Inventory_KPI
13. Pivot_Product
14. Pivot_Category
15. Pivot_Warehouse
16. Chart_Data
17. Charts
18. Inventory_Insights
19. Final_Inventory_Analysis

---

## 🔄 Recommended Workflow

**Raw Inventory Data**

→ **Data Quality Check**

→ **Inventory Cleaning**

→ **Cleaned Inventory Data**

→ **Inventory Summary**

→ **Product Analysis**

→ **Category Analysis**

→ **Warehouse Analysis**

→ **Monthly Inventory**

→ **Stock Movement Analysis**

→ **Inventory KPIs**

→ **Pivot Analysis**

→ **Charts**

→ **Inventory Insights**

→ **Final Inventory Analysis**

---

## 🐍 Python Connection

Inventory Analytics can also be performed using Python.

Important libraries include:

- Pandas
- NumPy
- Matplotlib

### Pandas

Useful for:

- Reading Excel data
- Inspecting data
- Cleaning data
- Grouping inventory records
- Aggregating inventory values
- Creating summary tables
- Exporting analysis results

### NumPy

Useful for numerical calculations and conditional operations.

### Matplotlib

Useful for creating inventory charts and visualisations.

---

## 🛠️ Tools Used

- Microsoft Excel
- Python
- Pandas
- NumPy
- Matplotlib
- VS Code
- GitHub

---

## 📝 Practical Work

During Day 094, the practical work includes:

- Inspecting inventory data
- Checking data quality
- Cleaning inventory records
- Creating cleaned inventory data
- Calculating inventory value
- Analysing stock movement
- Analysing products
- Analysing categories
- Analysing warehouses
- Analysing monthly inventory
- Checking reorder levels
- Calculating inventory KPIs
- Creating pivot-style summaries
- Creating charts
- Writing inventory insights
- Preparing final inventory analysis

---

## 📌 Data Note

The workbook uses a synthetic educational inventory dataset created for learning and practice.

The dataset includes examples of data-quality issues such as missing values, inconsistent text, duplicate records, and invalid stock movement values so that the cleaning and validation process can be practised.

---

## 🎯 Day 094 Outcome

After completing Day 094, I can take inventory data through a complete analytics workflow:

**Inspect → Clean → Calculate → Analyse → Visualise → Interpret → Present**

I can use inventory data to understand stock levels, inventory value, stock movement, product performance, category performance, warehouse distribution, and reorder requirements.

---

## ✅ Completion Checklist

- [ ] Understand Inventory Analytics
- [ ] Understand inventory data
- [ ] Inspect inventory records
- [ ] Check data quality
- [ ] Clean inventory data
- [ ] Validate stock values
- [ ] Calculate closing stock
- [ ] Calculate inventory value
- [ ] Analyse products
- [ ] Analyse categories
- [ ] Analyse warehouses
- [ ] Analyse monthly inventory
- [ ] Analyse stock movement
- [ ] Check reorder levels
- [ ] Calculate inventory KPIs
- [ ] Perform pivot analysis
- [ ] Create inventory charts
- [ ] Write business insights
- [ ] Complete final inventory analysis
- [ ] Practise inventory analysis using Python

---

## 🔑 Key Takeaway

Inventory Analytics converts raw inventory records into useful information about stock levels, movement, inventory value, products, categories, warehouses, and replenishment requirements.

**Inventory Data → Clean Data → Stock Analysis → KPIs → Visualisation → Business Insights**