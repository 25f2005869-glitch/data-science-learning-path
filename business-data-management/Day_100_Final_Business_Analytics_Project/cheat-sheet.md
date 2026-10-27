# 🧠 Day 100 — Final Business Analytics Project Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 100  
**Topic:** Final Business Analytics Project

---

# 🔄 Complete Business Analytics Workflow

**Business Understanding**

→ **Data Understanding**

→ **Data Cleaning**

→ **Data Validation**

→ **Data Analysis**

→ **KPI Development**

→ **Visualisation**

→ **Dashboard**

→ **Business Insights**

→ **Final Report**

---

# 📌 1. Business Understanding

Before analysing data, identify:

- Business objective
- Available data
- Business questions
- Important KPIs
- Required analysis
- Report audience

### Common Business Questions

- What is total revenue?
- What is total profit?
- How many orders are there?
- Which category generates more revenue?
- How do regions perform?
- Which customer segment contributes revenue?
- Which products perform well?
- Which channel generates sales?
- How does performance change monthly?

---

# 📊 2. Main Sales Fields

| Field | Purpose |
|---|---|
| Order_ID | Order identifier |
| Date | Transaction date |
| Customer_ID | Customer identifier |
| Product | Product |
| Category | Product category |
| Region | Region |
| City | City |
| Customer_Segment | Customer segment |
| Channel | Sales channel |
| Payment_Method | Payment method |
| Sales_Rep | Sales representative |
| Quantity | Units sold |
| Unit_Price | Price per unit |
| Discount_% | Discount |
| Revenue | Sales revenue |
| Cost | Business cost |

---

# 🧹 3. Data Cleaning Checklist

Check:

- Missing values
- Duplicate rows
- Incorrect data types
- Invalid dates
- Extra spaces
- Inconsistent capitalization
- Invalid numeric values
- Negative values
- Incorrect categories

### Basic Workflow

**Inspect → Clean → Validate → Analyse**

---

# ✅ 4. Data Validation

Check that:

- Required columns exist
- Dates are valid
- Numeric values are reasonable
- Duplicates are reviewed
- Calculated fields are correct
- Relationships are correct

### Remember

**Cleaning = prepare the data**

**Validation = check the prepared data**

---

# 🗂️ 5. Data Model

### Fact Table

`SalesData`

### Dimension Tables

- `Dim_Customer`
- `Dim_Product`
- `Dim_Date`

### Main Relationships

`Dim_Customer[Customer_ID]`

→ `SalesData[Customer_ID]`

`Dim_Product[Product]`

→ `SalesData[Product]`

`Dim_Date[Date]`

→ `SalesData[Date]`

---

# 💰 6. Core Business Formulas

### Revenue

**Revenue = Quantity × Unit Price**

### Profit

**Profit = Revenue − Cost**

### Profit Margin

**Profit Margin % = Profit ÷ Revenue × 100**

### Average Order Value

**AOV = Total Revenue ÷ Total Orders**

---

# 📈 7. Important KPIs

| KPI | Meaning |
|---|---|
| Total Revenue | Total sales value |
| Total Cost | Total recorded cost |
| Total Profit | Revenue − Cost |
| Profit Margin % | Profit relative to revenue |
| Total Orders | Unique orders |
| Total Quantity | Units sold |
| Average Order Value | Revenue per order |
| Customers | Unique customers |

---

# 🧮 8. Important DAX Measures

### Total Revenue

`Total Revenue = SUM(SalesData[Revenue])`

### Total Cost

`Total Cost = SUM(SalesData[Cost])`

### Total Profit

`Total Profit = [Total Revenue] - [Total Cost]`

### Profit Margin %

`Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)`

### Total Orders

`Total Orders = DISTINCTCOUNT(SalesData[Order_ID])`

### Total Quantity

`Total Quantity = SUM(SalesData[Quantity])`

### Average Order Value

`Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)`

### Customers

`Customers = DISTINCTCOUNT(SalesData[Customer_ID])`

---

# 📅 9. Time Intelligence

Use `Dim_Date` for:

- Year
- Quarter
- Month
- Month-Year
- Week
- Day

### Revenue YTD

`Revenue YTD = TOTALYTD([Total Revenue], Dim_Date[Date])`

### Revenue MTD

`Revenue MTD = TOTALMTD([Total Revenue], Dim_Date[Date])`

---

# 🏷️ 10. Category Analysis

Analyse:

- Orders
- Quantity
- Revenue
- Cost
- Profit
- Profit Margin %

Main question:

**How does performance differ across categories?**

---

# 🌍 11. Region Analysis

Analyse:

- Orders
- Quantity
- Revenue
- Cost
- Profit
- Profit Margin %

Regions:

- North
- South
- East
- West

---

# 👥 12. Customer Segment Analysis

Segments:

- New
- Regular
- Loyal
- At Risk

Analyse:

- Orders
- Quantity
- Revenue
- Profit
- Profit Margin %

---

# 📦 13. Product Analysis

Analyse each product using:

- Orders
- Quantity
- Revenue
- Cost
- Profit
- Profit Margin %

---

# 📣 14. Channel Analysis

Compare sales channels using:

- Orders
- Revenue
- Profit

---

# 👤 15. Customer Analysis

Important measures:

- Orders
- Quantity
- Revenue
- Profit
- Average Order Value

Customer attributes:

- Segment
- Region
- City
- Gender
- Age

---

# 📆 16. Monthly Analysis

Track:

- Orders
- Revenue
- Cost
- Profit
- Quantity
- Profit Margin %

### Best visual

**Line Chart**

---

# 📊 17. Visual Selection Cheat Sheet

| Business Question | Visual |
|---|---|
| Single KPI | Card |
| Category comparison | Column Chart |
| Ranking | Bar Chart |
| Trend over time | Line Chart |
| Composition | Pie / Donut |
| Contribution | Treemap |
| Relationship | Scatter |
| Increase/decrease | Waterfall |
| Two measures together | Combo Chart |
| Detailed values | Table |
| Hierarchical detail | Matrix |
| Interactive filtering | Slicer |

---

# 🃏 18. Card Visual

Use for:

- Total Revenue
- Total Profit
- Total Orders
- Customers
- Profit Margin %

Keep KPI cards near the top of the dashboard.

---

# 📊 19. Bar / Column Chart

### Column Chart

Useful for:

- Revenue by Category
- Revenue by Segment

### Bar Chart

Useful for:

- Product comparison
- Regional comparison
- Rankings

---

# 📈 20. Line Chart

Best for:

**Time-based trends**

Example:

**Monthly Revenue Trend**

- X-axis → Month
- Y-axis → Revenue

---

# 🍩 21. Donut Chart

Useful for showing composition.

Example:

**Revenue by Customer Segment**

Avoid using too many categories in one donut chart.

---

# 🌳 22. Treemap

Useful for showing contribution.

Example:

**Revenue by Product**

Larger area represents a larger value.

---

# 🔵 23. Scatter Chart

Useful for relationships between numerical variables.

Example:

**Revenue vs Quantity**

Possible dimensions:

- Product
- Customer
- Category

---

# 🌊 24. Waterfall Chart

Useful for showing changes from one value to another.

Example:

**Revenue → Cost → Profit**

---

# 📋 25. Matrix

Useful for detailed business analysis.

Example:

**Region → Category → Revenue → Profit**

Matrix can display hierarchical information.

---

# 🎛️ 26. Slicers

Useful slicers:

- Region
- Category
- Customer Segment
- Channel
- Date

Slicers make reports interactive.

---

# 🖱️ 27. Interactive Features

Important Power BI features:

- Slicers
- Filters
- Cross-filtering
- Tooltips
- Drillthrough
- Bookmarks
- Buttons
- Conditional Formatting

---

# 💬 28. Tooltips

Tooltips provide additional information when hovering over a visual.

Possible fields:

- Revenue
- Profit
- Orders
- Quantity
- Profit Margin %

---

# 🔍 29. Drillthrough

Drillthrough moves from summary information to detailed analysis.

Example:

**Region → Regional Detail Page**

A detailed page can contain:

- Revenue
- Profit
- Orders
- Products
- Customers
- Trends

---

# 🔖 30. Bookmarks

Bookmarks save a specific report state.

Can be used for:

- Navigation
- Alternate views
- Show/hide sections
- Button interactions

---

# 🎨 31. Conditional Formatting

Useful in:

- Tables
- Matrices

Methods:

- Background formatting
- Font formatting
- Data bars
- Rules

---

# 📊 32. Dashboard Layout

### Top

- Total Revenue
- Total Profit
- Total Orders
- Profit Margin %

### Middle

- Monthly Revenue Trend
- Revenue by Category
- Revenue by Region
- Revenue by Segment

### Bottom

- Product Analysis
- Detailed Matrix
- Additional visual
- Slicers

---

# 💡 33. Business Insights

A good insight should be:

- Data-based
- Specific
- Clear
- Relevant to the business question

Examples:

- A category contributes a large share of revenue.
- Regional revenue differs across locations.
- Customer segments show different sales patterns.
- Monthly revenue changes over time.
- Product profitability varies across products.

---

# ⚠️ 34. Insight vs Assumption

### Observation

**Revenue increased during a particular month.**

### Assumption

**Revenue increased because customers preferred a particular product.**

The second statement requires additional evidence.

Remember:

**Correlation or observation does not automatically prove causation.**

---

# 📝 35. Final Report Structure

1. Executive Summary
2. Business Questions
3. Data Preparation
4. KPI Analysis
5. Category Analysis
6. Region Analysis
7. Customer Analysis
8. Trend Analysis
9. Business Insights
10. Possible Actions
11. Limitations
12. Conclusion

---

# 🐍 36. Python Connection

Important libraries:

- Pandas
- NumPy
- Matplotlib

Python can be used for:

- Data loading
- Cleaning
- Transformation
- Aggregation
- KPI calculation
- Analysis
- Exporting results

---

# 📗 37. Excel vs Power BI

| Excel | Power BI |
|---|---|
| Data preparation | Power Query |
| Formulas | DAX |
| Pivot Tables | Interactive visuals |
| Excel Charts | Power BI visuals |
| Static reports | Interactive reports |
| Worksheet analysis | Dashboard/report pages |

Both can be part of the same business analytics workflow.

---

# 🏆 38. Final Project Checklist

### Data

- [ ] Understand business problem
- [ ] Inspect dataset
- [ ] Check missing values
- [ ] Check duplicates
- [ ] Clean data
- [ ] Validate data

### Analysis

- [ ] Calculate KPIs
- [ ] Analyse categories
- [ ] Analyse regions
- [ ] Analyse segments
- [ ] Analyse products
- [ ] Analyse channels
- [ ] Analyse customers
- [ ] Analyse monthly trends

### Power BI

- [ ] Import data
- [ ] Create relationships
- [ ] Create DAX measures
- [ ] Create KPI cards
- [ ] Create charts
- [ ] Add slicers
- [ ] Add interactions
- [ ] Add tooltip
- [ ] Add drillthrough
- [ ] Add bookmarks
- [ ] Format dashboard

### Reporting

- [ ] Identify insights
- [ ] Document limitations
- [ ] Prepare final report
- [ ] Validate numbers
- [ ] Present findings

---

# 🔄 39. Quick Revision

**Business Question**

→ What do we need to know?

**Data**

→ What information do we have?

**Cleaning**

→ Is the data usable?

**Validation**

→ Is the prepared data reliable?

**Analysis**

→ What does the data show?

**KPI**

→ How do we measure performance?

**Visualisation**

→ How do we communicate the result?

**Dashboard**

→ How can users explore the result?

**Insight**

→ What evidence-based observation can be communicated?

**Report**

→ How should the findings be presented?

---

# 🎓 Final Takeaway

**Business Analytics = Data + Analysis + Business Context + Communication**

The goal is not simply to create charts.

The goal is to convert:

**Raw Business Data**

→ **Clean Data**

→ **Analysis**

→ **KPIs**

→ **Visualisations**

→ **Dashboard**

→ **Business Insights**

→ **Clear Business Report**