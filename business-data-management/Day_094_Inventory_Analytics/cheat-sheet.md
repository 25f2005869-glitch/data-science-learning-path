# 🧾 Day 094 — Inventory Analytics Cheat Sheet

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

## 📌 Inventory Analytics

Inventory Analytics = analysing inventory data to understand:

- Stock levels
- Stock movement
- Inventory value
- Products
- Categories
- Warehouses
- Reorder requirements
- Inventory KPIs

---

## 📦 Important Inventory Fields

| Field | Meaning |
|---|---|
| Inventory ID | Unique inventory record |
| Date | Inventory record date |
| Product ID | Product identifier |
| Product | Product name |
| Category | Product category |
| Warehouse | Inventory location |
| Opening Stock | Stock at the beginning |
| Stock In | Stock received |
| Stock Out | Stock issued/moved out |
| Closing Stock | Remaining stock |
| Unit Cost | Cost per unit |
| Inventory Value | Value of closing stock |
| Reorder Level | Stock threshold |
| Supplier | Supplier name |
| Stock Status | Current stock condition |

---

## 🧮 Important Formulas

### Closing Stock

**Closing Stock = Opening Stock + Stock In − Stock Out**

### Inventory Value

**Inventory Value = Closing Stock × Unit Cost**

### Net Movement

**Net Movement = Stock In − Stock Out**

### Reorder Condition

**Closing Stock ≤ Reorder Level**

---

## 🔍 Data Inspection

Check:

- Rows
- Columns
- Column names
- Data types
- Missing values
- Duplicate records
- Text inconsistencies
- Negative values
- Stock calculations

---

## 🧹 Data Cleaning Checklist

- Remove unnecessary spaces
- Standardise text
- Handle missing values
- Check numeric values
- Validate dates
- Check duplicate records
- Check negative stock movement
- Recalculate derived values
- Validate cleaned data

---

## 📊 Inventory Analysis

### Product Analysis

Analyse:

- Closing Stock
- Stock Out
- Inventory Value
- Reorder Level
- Reorder Records

### Category Analysis

Analyse:

- Closing Stock
- Stock In
- Stock Out
- Inventory Value
- Number of Records

### Warehouse Analysis

Analyse:

- Closing Stock
- Stock In
- Stock Out
- Inventory Value
- Reorder Records
- Number of Records

### Monthly Analysis

Analyse:

- Opening Stock
- Stock In
- Stock Out
- Closing Stock
- Inventory Value

---

## 🚚 Stock Movement

**Stock In** → Inventory entering the system

**Stock Out** → Inventory leaving the system

**Net Movement = Stock In − Stock Out**

Positive net movement means more stock entered than left during the analysed period.

---

## 🎯 Reorder Level

Reorder Level is a threshold used to identify inventory that may require replenishment.

If:

**Closing Stock ≤ Reorder Level**

the inventory record is at or below the reorder level.

Possible workbook categories:

- Healthy Stock
- Below Reorder Level

---

## 📈 Inventory KPIs

Important KPIs:

- Total Inventory Value
- Total Stock In
- Total Stock Out
- Total Closing Stock
- Average Inventory Value
- Reorder-Level Records
- Inventory Utilisation

---

## 🔄 Pivot Analysis

Useful pivot views:

- Product
- Category
- Warehouse

Common measures:

- Closing Stock
- Stock In
- Stock Out
- Inventory Value
- Number of Records
- Reorder Records

---

## 📊 Charts

### Bar Chart

Useful for comparing:

- Inventory Value by Product
- Inventory Value by Warehouse

### Line Chart

Useful for:

- Monthly Inventory Value Trend

---

## 🐍 Python Tools

### Pandas

Used for:

- Reading Excel files
- Data inspection
- Data cleaning
- Grouping
- Aggregation
- Analysis
- Exporting results

### NumPy

Used for:

- Numerical calculations
- Conditional calculations

### Matplotlib

Used for:

- Bar charts
- Line charts
- Inventory visualisation

---

## 💻 Useful Pandas Operations

**Read Excel**

`pd.read_excel()`

**First rows**

`df.head()`

**Dataset size**

`df.shape`

**Column names**

`df.columns`

**Data types**

`df.dtypes`

**Missing values**

`df.isna().sum()`

**Duplicate rows**

`df.duplicated().sum()`

**Remove spaces**

`df["Column"].str.strip()`

**Group data**

`df.groupby("Column")`

**Sum**

`df["Column"].sum()`

**Mean**

`df["Column"].mean()`

---

## 💡 Business Questions

1. Which products have the highest inventory value?
2. Which products have higher stock movement?
3. Which categories hold more inventory?
4. Which warehouses hold more inventory?
5. Which records are at or below the reorder level?
6. How does inventory value change over time?
7. Which products may require replenishment?
8. How is inventory distributed across warehouses?

---

## 🔄 Inventory Analytics Workflow

**Raw Data**

→ **Inspect**

→ **Check Quality**

→ **Clean**

→ **Calculate**

→ **Product Analysis**

→ **Category Analysis**

→ **Warehouse Analysis**

→ **Monthly Analysis**

→ **Stock Movement**

→ **KPIs**

→ **Pivot Analysis**

→ **Visualise**

→ **Business Insights**

→ **Final Analysis**

---

## ⚡ Quick Revision

**Closing Stock**

= Opening Stock + Stock In − Stock Out

**Inventory Value**

= Closing Stock × Unit Cost

**Net Movement**

= Stock In − Stock Out

**Reorder**

= Closing Stock ≤ Reorder Level

**Product Analysis**

= Product-level inventory performance

**Category Analysis**

= Category-level inventory performance

**Warehouse Analysis**

= Warehouse-level inventory performance

**Monthly Analysis**

= Inventory changes over time

**Inventory KPI**

= Quick measure of inventory performance

---

## 🏁 Key Takeaway

**Inventory Analytics = Clean Inventory Data → Calculate Stock & Value → Analyse Products, Categories, Warehouses & Time → Track KPIs → Visualise → Extract Business Insights**