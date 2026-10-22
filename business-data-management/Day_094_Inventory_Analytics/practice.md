# 📝 Day 094 — Inventory Analytics Practice

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

# 🎯 Practice Objective

Practice inventory data inspection, cleaning, calculations, analysis, KPI creation, pivot analysis, and visualisation using the Day 094 workbook.

---

# 📂 Practice File

Use:

`Day_094_Inventory_Analytics.xlsx`

Main data sheet:

`Cleaned_Inventory_Data`

---

# 🟢 Part 1 — Basic Understanding

### Q1. What is Inventory Analytics?

Write a short explanation.

### Q2. What is Opening Stock?

### Q3. What is Stock In?

### Q4. What is Stock Out?

### Q5. What is Closing Stock?

### Q6. What is Inventory Value?

### Q7. What is Reorder Level?

---

# 🟡 Part 2 — Formula Practice

### Q8. Calculate Closing Stock.

Use:

`Closing Stock = Opening Stock + Stock In − Stock Out`

### Q9. Calculate Inventory Value.

Use:

`Inventory Value = Closing Stock × Unit Cost`

### Q10. Calculate Net Movement.

Use:

`Net Movement = Stock In − Stock Out`

### Q11. Identify records that are at or below the reorder level.

Condition:

`Closing Stock ≤ Reorder Level`

---

# 🟠 Part 3 — Data Quality Practice

Check the inventory data for:

1. Missing values
2. Duplicate records
3. Extra spaces
4. Inconsistent text
5. Negative Stock Out values
6. Invalid dates
7. Missing Unit Cost
8. Missing Stock In
9. Missing Closing Stock

Write down the issues found.

---

# 🔵 Part 4 — Data Cleaning Practice

Perform the following cleaning tasks:

### Task 1

Remove unnecessary spaces from text fields.

### Task 2

Standardise Product, Category, Warehouse, Supplier, and Stock Status values.

### Task 3

Handle missing Unit Cost values.

### Task 4

Handle missing Stock In values.

### Task 5

Handle negative Stock Out values.

### Task 6

Recalculate missing Closing Stock values.

### Task 7

Recalculate Inventory Value.

### Task 8

Remove exact duplicate records.

### Task 9

Validate the cleaned dataset.

---

# 🟣 Part 5 — Product Analysis

Answer the following:

### Q12.

Which product has the highest Closing Stock?

### Q13.

Which product has the highest Inventory Value?

### Q14.

Which product has the highest Stock Out?

### Q15.

Which products have records at or below the Reorder Level?

### Q16.

Create a product-level summary containing:

- Product
- Category
- Closing Stock
- Stock In
- Stock Out
- Inventory Value

---

# 🟤 Part 6 — Category Analysis

### Q17.

Calculate total Closing Stock for each category.

### Q18.

Calculate total Stock In for each category.

### Q19.

Calculate total Stock Out for each category.

### Q20.

Calculate total Inventory Value for each category.

### Q21.

Compare inventory distribution across categories.

---

# 🟧 Part 7 — Warehouse Analysis

### Q22.

Calculate total Closing Stock for each warehouse.

### Q23.

Calculate total Stock In for each warehouse.

### Q24.

Calculate total Stock Out for each warehouse.

### Q25.

Calculate total Inventory Value for each warehouse.

### Q26.

Identify the warehouse with the largest inventory value.

---

# 🟥 Part 8 — Monthly Analysis

### Q27.

Calculate monthly Stock In.

### Q28.

Calculate monthly Stock Out.

### Q29.

Calculate monthly Closing Stock.

### Q30.

Calculate monthly Inventory Value.

### Q31.

Create a line chart showing the monthly Inventory Value trend.

---

# 🟩 Part 9 — Stock Movement Practice

### Q32.

Calculate Net Movement for every record.

### Q33.

Identify records with positive Net Movement.

### Q34.

Identify records with negative Net Movement.

### Q35.

Compare Stock In and Stock Out.

### Q36.

Explain what Net Movement tells us about inventory movement.

---

# ⭐ Part 10 — KPI Practice

Calculate the following KPIs:

### Q37.

Total Inventory Value

### Q38.

Total Stock In

### Q39.

Total Stock Out

### Q40.

Total Closing Stock

### Q41.

Average Inventory Value

### Q42.

Number of Reorder-Level Records

### Q43.

Inventory Utilisation

Use:

`Inventory Utilisation = Total Stock Out / Total Opening Stock × 100`

---

# 📊 Part 11 — Pivot Table Practice

Create a Pivot Table for:

### Pivot 1 — Product

Rows:

`Product`

Values:

- Closing Stock
- Stock In
- Stock Out
- Inventory Value

### Pivot 2 — Category

Rows:

`Category`

Values:

- Closing Stock
- Stock In
- Stock Out
- Inventory Value

### Pivot 3 — Warehouse

Rows:

`Warehouse`

Values:

- Closing Stock
- Stock In
- Stock Out
- Inventory Value

---

# 📈 Part 12 — Visualisation Practice

Create the following charts:

### Chart 1

Inventory Value by Product

**Chart Type:** Bar Chart

### Chart 2

Inventory Value by Warehouse

**Chart Type:** Bar Chart

### Chart 3

Monthly Inventory Value Trend

**Chart Type:** Line Chart

---

# 💼 Part 13 — Business Insight Practice

Write short answers for:

### Q44.

Which products require closer inventory monitoring?

### Q45.

Which categories contain the largest inventory value?

### Q46.

How is inventory distributed across warehouses?

### Q47.

Are there records at or below the reorder level?

### Q48.

How does inventory value change over time?

### Q49.

What business actions could be considered based on the inventory analysis?

---

# 🐍 Part 14 — Python Practice

Using Pandas:

### Task 1

Load the Excel workbook.

### Task 2

Read the `Raw_Inventory_Data` sheet.

### Task 3

Inspect:

- `head()`
- `shape`
- `columns`
- `dtypes`
- `isna().sum()`
- `duplicated().sum()`

### Task 4

Clean the dataset.

### Task 5

Calculate Closing Stock.

### Task 6

Calculate Inventory Value.

### Task 7

Calculate Net Movement.

### Task 8

Group inventory by Product.

### Task 9

Group inventory by Category.

### Task 10

Group inventory by Warehouse.

### Task 11

Perform monthly analysis.

### Task 12

Calculate inventory KPIs.

### Task 13

Export analysis results to CSV files.

### Task 14

Create inventory charts using Matplotlib.

---

# 🏆 Final Practice Task

Create a complete Inventory Analytics report containing:

1. Data Quality Check
2. Cleaned Inventory Data
3. Product Analysis
4. Category Analysis
5. Warehouse Analysis
6. Monthly Inventory Analysis
7. Stock Movement Analysis
8. Inventory KPIs
9. Pivot Analysis
10. Charts
11. Business Insights

---

# ✅ Final Checklist

- [ ] I understand inventory analytics.
- [ ] I understand Opening Stock.
- [ ] I understand Stock In.
- [ ] I understand Stock Out.
- [ ] I can calculate Closing Stock.
- [ ] I can calculate Inventory Value.
- [ ] I can calculate Net Movement.
- [ ] I can identify reorder-level records.
- [ ] I can clean inventory data.
- [ ] I can analyse products.
- [ ] I can analyse categories.
- [ ] I can analyse warehouses.
- [ ] I can perform monthly analysis.
- [ ] I can calculate inventory KPIs.
- [ ] I can create Pivot Tables.
- [ ] I can create inventory charts.
- [ ] I can write business insights.
- [ ] I can perform the analysis using Python.

---

# 🧠 Key Practice Formula

`Closing Stock = Opening Stock + Stock In − Stock Out`

`Inventory Value = Closing Stock × Unit Cost`

`Net Movement = Stock In − Stock Out`

`Reorder Condition = Closing Stock ≤ Reorder Level`

`Inventory Utilisation = Total Stock Out / Total Opening Stock × 100`

---

## 🚀 Day 094 Practice Goal

**Clean → Calculate → Analyse → Compare → Visualise → Interpret**