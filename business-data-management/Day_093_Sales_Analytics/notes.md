# 📝 Day 093 — Sales Analytics Notes

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

## 1. Introduction to Sales Analytics

Sales Analytics is the process of analysing sales data to understand how a business is performing.

Sales data can help answer questions such as:

- How much revenue was generated?
- How much profit was earned?
- Which products are selling more?
- Which regions generate more revenue?
- How are sales changing over time?
- What is the average order value?
- Which customers contribute to sales?

The main purpose is to convert raw sales records into useful business information.

---

## 2. Sales Dataset

A sales dataset contains information about individual sales orders.

The Day 093 dataset contains fields such as:

- Order ID
- Order Date
- Customer ID
- Customer Name
- Region
- Salesperson
- Product Category
- Product
- Quantity
- Unit Price
- Revenue
- Cost
- Discount
- Profit
- Payment Method
- Order Status

Each row represents a sales order.

---

## 3. Data Inspection

Before analysing data, the dataset should be inspected.

Important checks include:

- Number of rows
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate records
- Inconsistent text values
- Invalid numeric values
- Date values

Data inspection helps understand the condition of the dataset before analysis.

---

## 4. Data Quality

Sales data may contain different types of quality issues.

Common issues include:

### Missing Values

Some fields may not contain values.

Examples:

- Missing Quantity
- Missing Unit Price

Missing values should be identified before calculations.

### Extra Spaces

Text values may contain unnecessary spaces.

Example:

- `North`
- ` North `
- `North `

These values should be standardised.

### Inconsistent Capitalisation

The same value may appear with different capitalization.

Example:

- `Electronics`
- `electronics`
- `ELECTRONICS`

These should be converted into a consistent format.

### Duplicate Records

Duplicate orders can cause incorrect totals.

Duplicate records should be identified and handled before analysis.

---

## 5. Sales Data Cleaning

The cleaning process prepares the dataset for reliable analysis.

Typical steps include:

1. Remove unnecessary spaces.
2. Standardise text values.
3. Check missing values.
4. Validate numeric fields.
5. Check date values.
6. Check duplicate records.
7. Verify important sales columns.
8. Create the cleaned dataset.

The cleaned dataset becomes the main source for further analysis.

---

## 6. Revenue

Revenue represents the sales value generated from an order.

For the sales dataset:

**Revenue = Quantity × Unit Price**

Example:

If:

- Quantity = 5
- Unit Price = ₹2,000

Then:

**Revenue = 5 × 2,000 = ₹10,000**

Revenue is one of the main measures used in sales analysis.

---

## 7. Cost

Cost represents the cost associated with the sale.

Cost is required to calculate profit.

If revenue and cost are available, profit can be calculated directly.

---

## 8. Profit

Profit represents the difference between revenue and cost.

**Profit = Revenue − Cost**

Example:

- Revenue = ₹10,000
- Cost = ₹7,000

Profit:

**₹10,000 − ₹7,000 = ₹3,000**

Profit analysis helps understand the financial contribution of sales.

---

## 9. Profit Margin

Profit Margin expresses profit as a percentage of revenue.

**Profit Margin (%) = (Profit ÷ Revenue) × 100**

Example:

- Profit = ₹3,000
- Revenue = ₹10,000

Profit Margin:

**(3,000 ÷ 10,000) × 100 = 30%**

Profit margin allows profitability to be compared using a percentage.

---

## 10. Average Order Value

Average Order Value, or AOV, represents the average revenue generated per order.

**AOV = Total Revenue ÷ Number of Orders**

Example:

If:

- Total Revenue = ₹1,00,000
- Number of Orders = 100

Then:

**AOV = ₹1,00,000 ÷ 100 = ₹1,000**

AOV is an important sales KPI.

---

## 11. Product Analysis

Product analysis studies sales performance across products.

Important measures include:

- Revenue by product
- Quantity sold by product
- Profit by product
- Product category performance

Product analysis helps identify how different products contribute to sales.

---

## 12. Region Analysis

Region analysis compares sales performance across regions.

Measures can include:

- Revenue by region
- Profit by region
- Number of orders by region
- Regional contribution to sales

This helps understand sales distribution across different regions.

---

## 13. Monthly Sales Analysis

Sales data can be grouped by month to understand trends over time.

Monthly analysis can include:

- Monthly revenue
- Monthly profit
- Monthly orders
- Monthly quantity sold

A monthly trend can show whether sales are increasing, decreasing, or changing over time.

---

## 14. Customer Analysis

Customer analysis examines sales activity at the customer level.

Important measures include:

- Customer revenue
- Number of orders
- Purchase activity
- Customer contribution to total sales

This analysis helps understand customer-level sales behaviour.

---

## 15. Sales KPIs

Key Performance Indicators provide a quick summary of sales performance.

Important sales KPIs include:

### Total Revenue

The total sales revenue generated.

### Total Cost

The total cost associated with sales.

### Total Profit

The total profit generated.

### Profit Margin

The percentage of revenue represented by profit.

### Total Orders

The number of sales orders.

### Total Quantity Sold

The total quantity of products sold.

### Average Order Value

The average revenue generated per order.

---

## 16. Pivot Analysis

Pivot analysis summarises data into useful groups.

In Day 093, pivot-style analysis is performed for:

- Products
- Regions
- Monthly sales

For example, sales data can be grouped by product to calculate total revenue and profit for each product.

---

## 17. Sales Visualisation

Charts help communicate sales results clearly.

The Day 093 workbook includes charts for:

- Revenue by Product
- Revenue by Region
- Monthly Revenue Trend
- Profit by Region

Different charts can be used for different analytical purposes.

### Bar Chart

Useful for comparing categories such as products or regions.

### Line Chart

Useful for showing trends over time.

### Pie Chart

Useful for showing the contribution of different categories to a total.

---

## 18. Business Insights

After performing analysis, the results should be interpreted.

Useful questions include:

- Which product has the highest revenue?
- Which product contributes significant profit?
- Which region generates more revenue?
- How does monthly revenue change?
- What is the average order value?
- Which customers contribute more sales?
- Are there noticeable differences between regions or products?

Business insights should be based on the analysed data.

---

## 19. Excel Workflow

The Excel workflow for Day 093 is:

**Raw Sales Data**

↓

**Data Quality Check**

↓

**Sales Cleaning**

↓

**Cleaned Sales Data**

↓

**Sales Summary**

↓

**Product Analysis**

↓

**Region Analysis**

↓

**Monthly Sales**

↓

**Customer Analysis**

↓

**Sales KPIs**

↓

**Pivot Analysis**

↓

**Charts**

↓

**Business Insights**

↓

**Final Sales Analysis**

---

## 20. Python and Sales Analytics

Sales Analytics can also be performed using Python.

### Pandas

Pandas can be used for:

- Reading Excel files
- Inspecting data
- Cleaning data
- Grouping data
- Aggregating values
- Creating summary tables
- Exporting results

### NumPy

NumPy can support numerical calculations and data operations.

### Matplotlib

Matplotlib can be used to create sales visualisations.

---

## 21. Grouping Sales Data

Grouping is useful when analysing sales by categories.

Examples include:

- Group by Product
- Group by Region
- Group by Month
- Group by Customer

Grouping allows calculations such as:

- Total revenue
- Total profit
- Total quantity
- Number of orders

---

## 22. Sales Analysis Questions

Some useful questions for practice are:

1. What is the total revenue?
2. What is the total profit?
3. What is the overall profit margin?
4. What is the average order value?
5. Which product generates the highest revenue?
6. Which region generates the highest revenue?
7. Which region generates the highest profit?
8. How does revenue change month by month?
9. Which products have higher quantities sold?
10. Which customers contribute more to total revenue?

---

## 23. Important Formulas

### Revenue

**Revenue = Quantity × Unit Price**

### Profit

**Profit = Revenue − Cost**

### Profit Margin

**Profit Margin (%) = (Profit ÷ Revenue) × 100**

### Average Order Value

**AOV = Total Revenue ÷ Number of Orders**

---

## 24. Key Learning Points

- Always inspect data before analysing it.
- Data cleaning is an important part of analytics.
- Missing and inconsistent values can affect results.
- Revenue and profit are different measures.
- Profit margin expresses profitability as a percentage.
- AOV measures average revenue per order.
- Product analysis helps compare products.
- Region analysis helps compare geographical performance.
- Monthly analysis helps identify sales trends.
- Customer analysis helps understand customer contribution.
- KPIs provide a quick summary of performance.
- Charts make analytical results easier to communicate.
- Business insights should be derived from data.

---

## 25. Final Learning Flow

The complete Day 093 sales analytics process is:

**Inspect → Clean → Calculate → Analyse → Visualise → Interpret → Present**

The objective is to transform raw sales records into meaningful business information.

---

## 26. Day 093 Summary

Day 093 focuses on Sales Analytics.

The practical work covers the complete process of working with sales data, starting from data inspection and cleaning and continuing through revenue, profit, product, region, monthly, customer, KPI, pivot, and visual analysis.

The final step is to convert the analysis into clear business insights and a final sales analysis.