# 🧾 Day 093 — Sales Analytics Cheat Sheet

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Programme](https://img.shields.io/badge/Programme-Diploma%20Level-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-093-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Sales%20Analytics-orange?style=for-the-badge)

## 👩‍💻 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 093
- **Topic:** Sales Analytics

---

## 📌 Sales Analytics

Sales Analytics = analysing sales data to understand business performance.

Main areas:

- Revenue
- Cost
- Profit
- Profit Margin
- Orders
- Quantity
- Products
- Regions
- Customers
- Monthly Trends
- KPIs

---

## 🧹 Data Cleaning Checklist

Before analysis:

- Check rows and columns
- Check column names
- Check data types
- Check missing values
- Check duplicate records
- Remove extra spaces
- Standardise text
- Check numeric values
- Check dates
- Validate important fields

### Common Problems

- Missing values
- Duplicate records
- Extra spaces
- Different capitalisation
- Invalid dates
- Invalid numeric values
- Inconsistent categories

---

## 💰 Important Formulas

### Revenue

Revenue = Quantity × Unit Price

### Profit

Profit = Revenue − Cost

### Profit Margin

Profit Margin (%) = (Profit ÷ Revenue) × 100

### Average Order Value

AOV = Total Revenue ÷ Number of Orders

---

## 📊 Important Sales Metrics

| Metric | Meaning |
|---|---|
| Revenue | Total sales value |
| Cost | Cost associated with sales |
| Profit | Revenue minus cost |
| Profit Margin | Profit as a percentage of revenue |
| Orders | Number of sales orders |
| Quantity | Total units sold |
| AOV | Average revenue per order |

---

## 📦 Product Analysis

Analyse:

- Revenue by Product
- Quantity by Product
- Profit by Product
- Revenue by Product Category
- Product contribution

Useful question:

**Which products contribute most to revenue and profit?**

---

## 🌍 Region Analysis

Analyse:

- Revenue by Region
- Profit by Region
- Orders by Region
- Quantity by Region
- Regional contribution

Useful question:

**How does sales performance differ across regions?**

---

## 📅 Monthly Analysis

Group sales by month.

Analyse:

- Monthly Revenue
- Monthly Profit
- Monthly Orders
- Monthly Quantity

Useful for identifying:

- Increasing sales
- Decreasing sales
- Monthly patterns
- Changes over time

---

## 👥 Customer Analysis

Analyse:

- Revenue by Customer
- Orders by Customer
- Customer purchase activity
- Customer contribution

Useful question:

**Which customers contribute significantly to sales?**

---

## 🎯 Sales KPIs

Important KPIs:

- Total Revenue
- Total Cost
- Total Profit
- Profit Margin
- Total Orders
- Total Quantity Sold
- Average Order Value

---

## 🔄 Pivot Analysis

Useful pivot views:

- Product
- Region
- Month

Common aggregations:

- Sum of Revenue
- Sum of Profit
- Sum of Quantity
- Count of Orders
- Average values

---

## 📈 Charts

### Bar Chart

Best for category comparison.

Examples:

- Revenue by Product
- Revenue by Region

### Line Chart

Best for trends over time.

Example:

- Monthly Revenue Trend

### Pie Chart

Useful for showing contribution to a total.

Example:

- Profit by Region

---

## 🐍 Python Tools

### Pandas

Used for:

- Reading Excel
- Data inspection
- Data cleaning
- Grouping
- Aggregation
- Analysis
- Exporting results

### NumPy

Used for:

- Numerical calculations
- Numerical operations

### Matplotlib

Used for:

- Charts
- Sales visualisation
- Trend analysis

---

## 🧮 Common Pandas Operations

### Read Excel

`pd.read_excel()`

### View First Rows

`df.head()`

### View Data Types

`df.dtypes`

### Check Missing Values

`df.isna().sum()`

### Check Duplicates

`df.duplicated().sum()`

### Remove Extra Spaces

`df["Column"] = df["Column"].str.strip()`

### Standardise Text

`df["Column"] = df["Column"].str.title()`

### Group Data

`df.groupby("Column")`

### Calculate Sum

`df["Revenue"].sum()`

### Calculate Mean

`df["Revenue"].mean()`

### Count Orders

`df["Order_ID"].nunique()`

---

## 📅 Date Analysis

Convert dates into datetime values before time-based analysis.

Important concepts:

- Date
- Month
- Year
- Monthly grouping
- Time trends

A month column can be created for monthly sales analysis.

---

## 🔍 Business Questions

Use these questions during analysis:

1. What is the total revenue?
2. What is the total profit?
3. What is the profit margin?
4. What is the AOV?
5. Which product generates the most revenue?
6. Which product generates the most profit?
7. Which region generates the most revenue?
8. Which region generates the most profit?
9. How does revenue change monthly?
10. Which customers contribute more revenue?

---

## 🔄 Sales Analytics Workflow

**Raw Data**

→ **Inspect**

→ **Check Quality**

→ **Clean**

→ **Calculate Metrics**

→ **Analyse Products**

→ **Analyse Regions**

→ **Analyse Months**

→ **Analyse Customers**

→ **Calculate KPIs**

→ **Pivot Analysis**

→ **Visualise**

→ **Extract Insights**

→ **Final Analysis**

---

## 💡 Business Insight Checklist

A useful insight should:

- Be based on data
- Mention the relevant metric
- Identify a meaningful pattern
- Support business understanding

Avoid making conclusions without checking the data.

---

## ⚡ Quick Revision

**Revenue**

= Quantity × Unit Price

**Profit**

= Revenue − Cost

**Profit Margin**

= Profit ÷ Revenue × 100

**AOV**

= Total Revenue ÷ Number of Orders

**Product Analysis**

= Compare product performance

**Region Analysis**

= Compare regional performance

**Monthly Analysis**

= Understand sales trends

**Customer Analysis**

= Understand customer contribution

**KPI**

= Quick measure of business performance

---

## 🏁 One-Line Summary

**Sales Analytics = Clean sales data → Calculate metrics → Analyse products, regions, months and customers → Track KPIs → Visualise → Extract business insights.**