# 📘 Day 100 — DAX Reference

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 100  
**Topic:** DAX Reference for Final Business Analytics Project

---

# 🎯 1. What is DAX?

DAX stands for **Data Analysis Expressions**.

DAX is the formula language used in Power BI for creating calculations such as:

- Measures
- Calculated columns
- Calculated tables
- KPIs
- Time-based calculations
- Business metrics

DAX is especially important when building interactive Power BI reports.

---

# 🗂️ 2. Project Data Model

The final project uses:

### Fact Table

`SalesData`

### Dimension Tables

- `Dim_Customer`
- `Dim_Product`
- `Dim_Date`

Main relationships:

`Dim_Customer[Customer_ID]`

→ `SalesData[Customer_ID]`

`Dim_Product[Product]`

→ `SalesData[Product]`

`Dim_Date[Date]`

→ `SalesData[Date]`

---

# 📊 3. Measures vs Calculated Columns

## Measure

A measure calculates a result dynamically according to the current filter context.

Examples:

- Total Revenue
- Total Profit
- Total Orders
- Average Order Value

Measures are commonly used in:

- Cards
- Charts
- Tables
- Matrices
- KPIs

---

## Calculated Column

A calculated column creates a value for each row.

It can be useful when the calculation needs to exist at row level.

Example concept:

`Profit = SalesData[Revenue] - SalesData[Cost]`

---

# 💰 4. Core Revenue Measures

## Total Revenue

`Total Revenue = SUM(SalesData[Revenue])`

Purpose:

Calculates the total revenue in the current filter context.

---

## Total Cost

`Total Cost = SUM(SalesData[Cost])`

Purpose:

Calculates the total recorded cost.

---

## Total Profit

`Total Profit = [Total Revenue] - [Total Cost]`

Purpose:

Calculates profit from revenue and cost.

---

# 📈 5. Profit Margin

## Profit Margin %

`Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)`

Purpose:

Calculates profit as a percentage of revenue.

### Formula

**Profit Margin % = Profit ÷ Revenue × 100**

Format the measure as a percentage in Power BI.

---

# 🧾 6. Order Measures

## Total Orders

`Total Orders = DISTINCTCOUNT(SalesData[Order_ID])`

Purpose:

Counts unique orders.

---

## Total Quantity

`Total Quantity = SUM(SalesData[Quantity])`

Purpose:

Calculates the total number of units sold.

---

## Average Order Value

`Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)`

Purpose:

Calculates average revenue per order.

### Formula

**AOV = Total Revenue ÷ Total Orders**

---

# 👥 7. Customer Measures

## Customers

`Customers = DISTINCTCOUNT(SalesData[Customer_ID])`

Purpose:

Counts unique customers.

This measure can change when filters are applied.

For example:

- Customers by Region
- Customers by Category
- Customers by Segment
- Customers by Month

---

# 📅 8. Date and Time Intelligence

The project contains a separate:

`Dim_Date`

table.

Important fields include:

- Date
- Year
- Quarter
- Month Number
- Month
- Month-Year
- Week Number
- Day
- Day Name

The Date Dimension is useful for time-based analysis.

---

# 📆 9. Revenue YTD

YTD means **Year to Date**.

## DAX

`Revenue YTD = TOTALYTD([Total Revenue], Dim_Date[Date])`

Purpose:

Calculates cumulative revenue from the beginning of the year up to the current date.

---

# 🗓️ 10. Revenue MTD

MTD means **Month to Date**.

## DAX

`Revenue MTD = TOTALMTD([Total Revenue], Dim_Date[Date])`

Purpose:

Calculates revenue from the beginning of the current month up to the current date.

---

# 🔢 11. SUM

`SUM(Column)`

Adds numeric values from a column.

### Example

`Total Revenue = SUM(SalesData[Revenue])`

Use `SUM` when the required calculation is a simple total.

---

# 📊 12. AVERAGE

`AVERAGE(Column)`

Calculates the arithmetic average.

### Example

`Average Unit Price = AVERAGE(SalesData[Unit_Price])`

Useful for:

- Average price
- Average cost
- Average quantity
- Other numerical averages

---

# 🔢 13. DISTINCTCOUNT

`DISTINCTCOUNT(Column)`

Counts unique values.

### Example

`Total Orders = DISTINCTCOUNT(SalesData[Order_ID])`

Another example:

`Customers = DISTINCTCOUNT(SalesData[Customer_ID])`

Useful for:

- Unique orders
- Unique customers
- Unique products

---

# ➗ 14. DIVIDE

`DIVIDE(Numerator, Denominator, AlternateResult)`

Used for division while providing an alternate result when the denominator cannot be used.

### Example

`Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)`

### Another Example

`Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)`

---

# 🧮 15. Basic Arithmetic Operators

DAX supports arithmetic operators such as:

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |

### Example

`Total Profit = [Total Revenue] - [Total Cost]`

---

# 🔍 16. Comparison Operators

Common comparison operators include:

| Operator | Meaning |
|---|---|
| `=` | Equal to |
| `<>` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

These are commonly used in conditional calculations.

---

# 🧠 17. IF

`IF(condition, value_if_true, value_if_false)`

Used for conditional logic.

### Example

`Sales Status = IF(SalesData[Revenue] > 10000, "High", "Low")`

This evaluates the condition for each row when used as a calculated column.

---

# 🎛️ 18. CALCULATE

`CALCULATE()` is an important DAX function for modifying filter context.

Basic structure:

`CALCULATE(Expression, Filter)`

Example concept:

`CALCULATE([Total Revenue], SalesData[Region] = "North")`

This evaluates Total Revenue under the specified filter.

---

# 🔎 19. FILTER

`FILTER()` returns a table containing rows that satisfy a condition.

Basic structure:

`FILTER(Table, Condition)`

Example concept:

`FILTER(SalesData, SalesData[Revenue] > 10000)`

`FILTER` is commonly used inside more advanced DAX calculations.

---

# 🌐 20. ALL

`ALL()` can remove filters from a table or column in a calculation.

Basic structure:

`ALL(TableOrColumn)`

It is useful when a calculation needs to compare a filtered value with a broader total.

---

# 📌 21. Filter Context

Filter context is one of the most important DAX concepts.

A measure can produce different results depending on:

- Slicers
- Filters
- Visual selections
- Page filters
- Cross-filtering
- Relationships

For example:

`Total Revenue`

can show:

- Overall revenue
- Revenue for one region
- Revenue for one category
- Revenue for one customer segment
- Revenue for one month

The measure itself does not need to be rewritten for each selection.

---

# 🔄 22. Row Context

Row context refers to the current row being evaluated.

It is commonly encountered with:

- Calculated columns
- Iterators

Example calculated-column concept:

`Profit = SalesData[Revenue] - SalesData[Cost]`

Each row is evaluated separately.

---

# 🔁 23. Measures and Filter Context

Suppose the report contains:

- Region on the axis
- Total Revenue as the value

The same measure:

`[Total Revenue]`

is evaluated separately for each region because the visual creates a different filter context for each row/category.

This is a key reason measures are powerful in Power BI.

---

# 📊 24. DAX for Category Analysis

The existing measures can be used directly.

Example:

`Total Revenue`

placed with:

`Category`

can produce:

**Revenue by Category**

Similarly:

`Total Profit`

with:

`Category`

can produce:

**Profit by Category**

---

# 🌍 25. DAX for Region Analysis

Use:

`Total Revenue`

with:

`Region`

to create:

**Revenue by Region**

Use:

`Total Profit`

with:

`Region`

to create:

**Profit by Region**

Use:

`Profit Margin %`

with:

`Region`

to compare profitability relative to revenue.

---

# 👥 26. DAX for Segment Analysis

Use:

`Customer_Segment`

with measures such as:

- Total Revenue
- Total Profit
- Total Orders
- Customers
- Profit Margin %

This produces customer-segment analysis.

---

# 📦 27. DAX for Product Analysis

Use:

`Product`

with:

- Total Revenue
- Total Cost
- Total Profit
- Total Quantity
- Total Orders

This provides product-level analysis.

---

# 📣 28. DAX for Channel Analysis

Use:

`Channel`

with:

- Total Revenue
- Total Orders
- Total Profit
- Profit Margin %

This provides channel-level performance analysis.

---

# 👤 29. DAX for Customer Analysis

Use:

`Customer_ID`

with:

- Customers
- Total Orders
- Total Revenue
- Total Profit
- Average Order Value

Customer attributes from `Dim_Customer` can also be used for filtering and grouping.

---

# 📆 30. DAX for Monthly Analysis

Use fields from:

`Dim_Date`

with:

- Total Revenue
- Total Cost
- Total Profit
- Total Orders
- Total Quantity
- Profit Margin %

A line chart can then show monthly performance.

---

# 📊 31. KPI Measures

Recommended KPI measures for the final dashboard:

### KPI 1

`Total Revenue`

### KPI 2

`Total Profit`

### KPI 3

`Total Orders`

### KPI 4

`Profit Margin %`

### Additional KPIs

- Total Quantity
- Average Order Value
- Customers

---

# 🃏 32. Card Visuals

Use measures in Card visuals.

Recommended cards:

1. Total Revenue
2. Total Profit
3. Total Orders
4. Profit Margin %

Additional cards:

5. Customers
6. Average Order Value
7. Total Quantity

---

# 📈 33. DAX + Visual Examples

| Analysis | Dimension | Measure |
|---|---|---|
| Revenue by Category | Category | Total Revenue |
| Revenue by Region | Region | Total Revenue |
| Profit by Region | Region | Total Profit |
| Revenue by Segment | Customer Segment | Total Revenue |
| Product Revenue | Product | Total Revenue |
| Channel Revenue | Channel | Total Revenue |
| Monthly Revenue | Month-Year | Total Revenue |
| Monthly Profit | Month-Year | Total Profit |
| Customer Revenue | Customer | Total Revenue |
| Quantity by Product | Product | Total Quantity |

---

# 📅 34. Time Intelligence Reference

| Requirement | DAX |
|---|---|
| Revenue YTD | `TOTALYTD()` |
| Revenue MTD | `TOTALMTD()` |
| Date-based analysis | `Dim_Date` |
| Monthly trend | `Month-Year` |
| Year analysis | `Year` |
| Quarter analysis | `Quarter` |

---

# 🧩 35. Common DAX Functions

| Function | Purpose |
|---|---|
| `SUM()` | Total |
| `AVERAGE()` | Average |
| `COUNT()` | Count |
| `DISTINCTCOUNT()` | Unique count |
| `DIVIDE()` | Safe division |
| `IF()` | Conditional logic |
| `CALCULATE()` | Modify filter context |
| `FILTER()` | Filter a table |
| `ALL()` | Remove filters |
| `TOTALYTD()` | Year-to-date |
| `TOTALMTD()` | Month-to-date |

---

# ⚠️ 36. Common DAX Mistakes

### Mistake 1 — Using simple count for unique orders

Incorrect approach:

`COUNT(SalesData[Order_ID])`

when the requirement is unique orders.

Use:

`DISTINCTCOUNT(SalesData[Order_ID])`

---

### Mistake 2 — Dividing directly

Instead of:

`[Total Profit] / [Total Revenue]`

use:

`DIVIDE([Total Profit], [Total Revenue], 0)`

when you want an alternate result for an unusable denominator.

---

### Mistake 3 — Confusing a measure with a column

Measures are evaluated dynamically according to filter context.

Calculated columns are evaluated row by row.

---

### Mistake 4 — Ignoring the Date Dimension

Time-intelligence calculations should use the project's Date Dimension.

---

### Mistake 5 — Creating unnecessary measures

Create measures that answer actual business questions.

---

# 🧪 37. DAX Practice Tasks

Create these measures yourself:

### Task 1

Calculate Total Revenue.

### Task 2

Calculate Total Cost.

### Task 3

Calculate Total Profit.

### Task 4

Calculate Profit Margin %.

### Task 5

Calculate Total Orders.

### Task 6

Calculate Total Quantity.

### Task 7

Calculate Average Order Value.

### Task 8

Calculate Customers.

### Task 9

Calculate Revenue YTD.

### Task 10

Calculate Revenue MTD.

---

# 🎯 38. Practical DAX Exercise

Create a Power BI report using the following measures:

- Total Revenue
- Total Cost
- Total Profit
- Profit Margin %
- Total Orders
- Total Quantity
- Average Order Value
- Customers
- Revenue YTD
- Revenue MTD

Then create visuals using:

- Category
- Region
- Customer Segment
- Product
- Channel
- Month-Year

---

# 🏆 39. Final DAX Checklist

## Basic Measures

- [ ] Total Revenue
- [ ] Total Cost
- [ ] Total Profit
- [ ] Profit Margin %
- [ ] Total Orders
- [ ] Total Quantity
- [ ] Average Order Value
- [ ] Customers

## Time Intelligence

- [ ] Revenue YTD
- [ ] Revenue MTD
- [ ] Date Dimension connected

## Analysis

- [ ] Category analysis
- [ ] Region analysis
- [ ] Segment analysis
- [ ] Product analysis
- [ ] Channel analysis
- [ ] Customer analysis
- [ ] Monthly analysis

## Dashboard

- [ ] KPI cards
- [ ] Charts
- [ ] Slicers
- [ ] Matrix
- [ ] Tooltips
- [ ] Drillthrough
- [ ] Bookmarks

---

# 🧠 40. Quick DAX Revision

**SUM**

→ Add values

**AVERAGE**

→ Calculate average

**DISTINCTCOUNT**

→ Count unique values

**DIVIDE**

→ Perform division safely

**IF**

→ Apply conditions

**CALCULATE**

→ Modify filter context

**FILTER**

→ Return filtered rows

**ALL**

→ Remove filters

**TOTALYTD**

→ Year-to-date calculation

**TOTALMTD**

→ Month-to-date calculation

---

# 🎓 Final DAX Takeaway

For the Day 100 project, focus first on a small set of reliable measures:

**Revenue**

→ **Cost**

→ **Profit**

→ **Margin**

→ **Orders**

→ **Quantity**

→ **AOV**

→ **Customers**

Then use these measures with different dimensions to answer business questions.

The most important DAX concept for the final dashboard is:

**Measures + Filter Context = Dynamic Business Analysis**