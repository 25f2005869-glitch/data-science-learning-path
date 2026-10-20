# 📘 Day 091 — Excel Revision — Notes

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Diploma Level](https://img.shields.io/badge/Level-Diploma-blue?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Subject-BDM-green?style=for-the-badge)
![Excel](https://img.shields.io/badge/Tool-Excel-green?style=for-the-badge)
![Day 091](https://img.shields.io/badge/Day-091-orange?style=for-the-badge)

---

## 👤 Metadata

| Field | Details |
|---|---|
| **Author** | Saloni Tiwari |
| **Programme** | IIT Madras BS Degree — Diploma Level |
| **Day** | 091 |
| **Topic** | Excel Revision |

---

# 1. Introduction

Excel is an important spreadsheet tool for working with business data.

In Business Data Management, Excel can be used to:

- Enter data
- Organise data
- Clean data
- Perform calculations
- Apply functions
- Analyse business performance
- Calculate KPIs
- Create summaries
- Create charts
- Build dashboards
- Support business decisions

Day 091 is a complete revision of the Excel concepts used during the learning journey.

---

# 2. Excel Workbook Basics

An Excel file is called a **workbook**.

A workbook can contain multiple **worksheets**.

A worksheet contains:

- Rows
- Columns
- Cells
- Ranges

### Cell

A cell is the basic unit where data is stored.

Example:

`A1`

Here:

- `A` represents the column.
- `1` represents the row.

### Range

A group of cells is called a range.

Example:

`A1:C10`

---

# 3. Types of Data in Excel

Common types of data include:

- Text
- Numbers
- Dates
- Percentages
- Currency
- Logical values

Examples:

| Data | Type |
|---|---|
| Saloni | Text |
| 500 | Number |
| 15/09/2026 | Date |
| 25% | Percentage |
| ₹10,000 | Currency |
| TRUE | Logical |

Correct data types are important for accurate calculations and analysis.

---

# 4. Data Entry and Formatting

Excel allows users to enter and format business data.

Common formatting operations include:

- Font formatting
- Font size
- Bold
- Alignment
- Borders
- Number formatting
- Currency formatting
- Percentage formatting
- Date formatting
- Decimal formatting

Good formatting improves readability and makes business reports easier to understand.

---

# 5. Formulas

A formula is an expression used to perform calculations.

Excel formulas normally begin with `=`.

Examples:

`=A1+B1`

`=A1-B1`

`=A1*B1`

`=A1/B1`

Parentheses can be used to control calculation order.

Example:

`=(A1+B1)*C1`

---

# 6. Cell References

Cell references allow formulas to use values stored in other cells.

### Relative Reference

Example:

`A1`

When a formula is copied, the reference can change.

### Absolute Reference

Example:

`$A$1`

The row and column remain fixed when the formula is copied.

### Mixed Reference

Examples:

`$A1`

`A$1`

One part remains fixed while the other can change.

---

# 7. Common Excel Functions

Functions are predefined formulas that perform specific operations.

### SUM

Used to calculate a total.

`=SUM(A1:A10)`

### AVERAGE

Used to calculate the average.

`=AVERAGE(A1:A10)`

### COUNT

Counts cells containing numbers.

`=COUNT(A1:A10)`

### COUNTA

Counts non-empty cells.

`=COUNTA(A1:A10)`

### MIN

Returns the smallest value.

`=MIN(A1:A10)`

### MAX

Returns the largest value.

`=MAX(A1:A10)`

---

# 8. Logical Functions

Logical functions are useful when analysis depends on conditions.

## IF

The `IF()` function returns one result when a condition is true and another result when it is false.

Example:

`=IF(A2>=50,"Pass","Fail")`

The formula checks whether the value in `A2` is at least 50.

---

## AND

`AND()` checks whether multiple conditions are true.

Example:

`=AND(A2>=50,B2>=50)`

The result is TRUE only when both conditions are true.

---

## OR

`OR()` checks whether at least one condition is true.

Example:

`=OR(A2>=50,B2>=50)`

The result is TRUE when at least one condition is true.

---

## NOT

`NOT()` reverses a logical result.

Example:

`=NOT(A2>50)`

---

# 9. Conditional Functions

Conditional functions allow calculations based on criteria.

## COUNTIF

Counts values that satisfy a condition.

Example:

`=COUNTIF(A2:A20,"Sales")`

---

## SUMIF

Adds values that satisfy a condition.

Example:

`=SUMIF(A2:A20,"Sales",B2:B20)`

---

## AVERAGEIF

Calculates the average of values satisfying a condition.

Example:

`=AVERAGEIF(A2:A20,"Sales",B2:B20)`

These functions are useful for business-function and category-level analysis.

---

# 10. Sorting

Sorting changes the order of records according to a selected column.

Examples:

- Sort revenue from low to high.
- Sort revenue from high to low.
- Sort dates from oldest to newest.
- Sort customer satisfaction from highest to lowest.

Sorting helps identify:

- Highest-performing records
- Lowest-performing records
- Recent records
- Business rankings

---

# 11. Filtering

Filtering displays only records that satisfy selected conditions.

Examples:

- Show only Sales records.
- Show only North region.
- Show orders greater than 100.
- Show records with high customer satisfaction.

Filtering is useful when working with large datasets.

---

# 12. Data Cleaning

Before analysing data, it is important to check its quality.

Common data-cleaning tasks include:

- Removing duplicates
- Handling blank values
- Correcting inconsistent text
- Checking dates
- Checking numeric values
- Standardising formats
- Identifying incorrect entries

Clean data produces more reliable analysis.

---

# 13. Text Functions

Text functions help process text values.

### LEFT

Returns characters from the left side.

`=LEFT(A2,3)`

### RIGHT

Returns characters from the right side.

`=RIGHT(A2,3)`

### MID

Returns characters from the middle.

`=MID(A2,2,4)`

### LEN

Counts the number of characters.

`=LEN(A2)`

### TRIM

Removes unnecessary spaces.

`=TRIM(A2)`

### UPPER

Converts text to uppercase.

`=UPPER(A2)`

### LOWER

Converts text to lowercase.

`=LOWER(A2)`

These functions are useful for cleaning and standardising business data.

---

# 14. Date Functions

Dates are commonly used in business analysis.

Useful functions include:

### TODAY

Returns the current date.

`=TODAY()`

### YEAR

Extracts the year.

`=YEAR(A2)`

### MONTH

Extracts the month number.

`=MONTH(A2)`

### DAY

Extracts the day.

`=DAY(A2)`

Date functions can be used to create monthly, yearly and daily analysis.

---

# 15. Lookup Functions

Lookup functions are used to find information from a table.

## VLOOKUP

`VLOOKUP()` searches for a value in the first column of a table and returns a corresponding value from another column.

It can be useful for:

- Finding prices
- Finding customer information
- Matching product IDs
- Retrieving business categories

---

## XLOOKUP

`XLOOKUP()` is a modern lookup function that can search for a value and return a corresponding result.

It can be useful when working with structured business datasets.

---

# 16. Excel Tables

An Excel Table converts a normal data range into a structured table.

Benefits include:

- Automatic filtering
- Structured references
- Automatic expansion
- Easier formatting
- Better organisation

Tables are useful when working with continuously growing business datasets.

---

# 17. Conditional Formatting

Conditional formatting changes the appearance of cells based on rules.

Examples:

- Highlight high revenue.
- Highlight low profit.
- Highlight duplicate values.
- Highlight values above a target.
- Use data bars for comparison.
- Use colour scales for numerical patterns.

Conditional formatting helps important information stand out visually.

---

# 18. Business Data Analysis

Excel can be used to analyse business performance.

The Day 091 workbook contains business data related to:

- Orders
- Revenue
- Cost
- Profit
- Delivery
- Returns
- Customer satisfaction
- Customers
- Marketing spend

The data can be analysed by:

- Business function
- Process
- Region
- Time period

---

# 19. Important Business KPIs

KPIs are measurable values used to understand business performance.

## Profit

`Profit = Revenue - Cost`

---

## Average Order Value

`AOV = Revenue / Orders`

AOV represents the average revenue generated per order.

---

## Cost per Order

`Cost per Order = Cost / Orders`

This shows the average cost associated with an order.

---

## Profit Margin

`Profit Margin = Profit / Revenue × 100`

This represents profit as a percentage of revenue.

---

## Return Rate

`Return Rate = Returned Orders / Orders × 100`

This measures the proportion of orders that were returned.

---

## On-Time Delivery Rate

`On-Time Delivery Rate = On-Time Deliveries / Deliveries × 100`

This measures delivery performance.

---

# 20. Summary Analysis

Business data can be summarised to make large datasets easier to understand.

Useful summaries include:

- Total orders
- Total revenue
- Total cost
- Total profit
- Average order value
- Return rate
- On-time delivery rate
- Customer satisfaction

Summaries can be created by:

- Business function
- Process
- Region
- Month

---

# 21. Pivot-Style Analysis

Pivot-style summaries help analyse large datasets by categories.

For example, revenue can be summarised by:

- Business Function
- Region
- Process
- Month

A summary table makes it easier to compare categories and identify patterns.

The Day 091 workbook includes summary sheets for process and regional analysis.

---

# 22. Charts

Charts convert numerical data into visual information.

The Day 091 workbook includes actual Excel chart objects for major chart types.

## Column Chart

Useful for comparing categories.

Example:

Revenue by Business Function.

---

## Bar Chart

Useful for horizontal category comparisons and rankings.

Example:

Orders by Process.

---

## Line Chart

Useful for showing trends over time.

Example:

Monthly Revenue Trend.

---

## Pie Chart

Useful for showing parts of a whole.

Example:

Revenue contribution by category.

---

## Doughnut Chart

Similar to a pie chart and useful for part-to-whole comparisons.

---

## Area Chart

Useful for showing trends together with the magnitude of values.

---

## Scatter Chart

Useful for examining relationships between two numerical variables.

Example:

Ad Spend versus Revenue.

---

## Radar Chart

Useful for comparing multiple metrics across categories.

Example:

Comparing business functions across several KPIs.

---

# 23. Choosing the Right Chart

| Requirement | Suitable Chart |
|---|---|
| Compare categories | Column / Bar |
| Show trend | Line |
| Show part-to-whole | Pie / Doughnut |
| Show trend and volume | Area |
| Show relationship | Scatter |
| Compare multiple metrics | Radar |

The choice of chart should depend on the type of information being communicated.

---

# 24. Dashboard

A dashboard combines important business information into one visual report.

A useful dashboard can contain:

- KPI cards
- Charts
- Summary tables
- Trends
- Comparisons
- Key observations

The Day 091 workbook contains an `Excel_Revision_Dashboard` sheet.

The dashboard includes KPI information and business trend analysis.

---

# 25. Business Analysis Workflow

A practical Excel analysis can follow this workflow:

**1. Collect Data**

↓

**2. Review Data**

↓

**3. Clean Data**

↓

**4. Calculate Metrics**

↓

**5. Summarise Data**

↓

**6. Analyse KPIs**

↓

**7. Create Charts**

↓

**8. Build Dashboard**

↓

**9. Interpret Results**

This workflow helps convert raw business data into useful information.

---

# 26. Common Excel Mistakes

Some common mistakes include:

- Incorrect cell references
- Missing parentheses
- Wrong data types
- Inconsistent date formats
- Extra spaces in text
- Duplicate records
- Incorrect ranges
- Using the wrong lookup column
- Incorrect percentage calculations
- Creating misleading charts

Checking formulas and data before presenting results is important.

---

# 27. Practical Revision

The Day 091 workbook provides practice across multiple areas:

- Excel basics
- Formula practice
- Function practice
- Logical functions
- Conditional functions
- Sorting and filtering
- Data cleaning
- Text and date functions
- Lookup functions
- KPI analysis
- Summary analysis
- Charts
- Dashboard

The workbook also contains revision questions and a final Excel project.

---

# 28. Final Excel Project

The final project combines the concepts revised during Day 091.

The project follows:

**Data → Cleaning → Calculation → KPI → Summary → Visualisation → Dashboard → Insights**

The objective is to practise Excel as a complete business data-analysis tool.

---

# 29. Key Learning Points

- Excel is useful for business data analysis.
- Formulas perform calculations.
- Functions simplify repeated calculations.
- Logical functions help evaluate conditions.
- Conditional functions support category-based analysis.
- Sorting and filtering help explore datasets.
- Data cleaning improves data quality.
- Lookup functions help connect related information.
- KPIs measure business performance.
- Summary tables simplify large datasets.
- Charts communicate patterns visually.
- Dashboards combine important information into a single view.

---

# 30. Final Summary

Day 091 revises Excel from basic spreadsheet operations to practical business analysis.

The complete learning flow is:

**Excel Basics → Formulas → Functions → Logical Analysis → Conditional Analysis → Sorting & Filtering → Data Cleaning → Lookups → KPIs → Summary → Charts → Dashboard → Final Project**

The main objective is to become comfortable using Excel to process, analyse and communicate business data.