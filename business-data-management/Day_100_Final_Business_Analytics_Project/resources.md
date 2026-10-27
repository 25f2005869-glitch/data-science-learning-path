# 📚 Day 100 — Final Business Analytics Project Resources

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 100  
**Topic:** Final Business Analytics Project

---

# 🎯 Resource Purpose

This resource guide collects the main topics and learning areas needed to complete the Final Business Analytics Project.

The recommended learning order is:

**Business Understanding**

→ **Data Understanding**

→ **Data Cleaning**

→ **Data Analysis**

→ **KPI Development**

→ **Excel**

→ **Power BI**

→ **DAX**

→ **Visualisation**

→ **Dashboard**

→ **Business Insights**

→ **Final Report**

---

# 1. Business Analytics Fundamentals

### Topics to Study

- Business Analytics
- Business Understanding
- Business Questions
- Data-Driven Decision Making
- Descriptive Analytics
- KPI
- Business Metrics
- Business Insights
- Data Storytelling

### Practice Focus

Learn how to convert a business problem into:

**Business Question → Metric → Analysis → Insight**

### Suggested Search Topics

- Business analytics fundamentals
- Business intelligence fundamentals
- KPI and business metrics
- Data-driven decision making
- Business data analysis

---

# 2. Data Understanding

### Topics

- Dataset structure
- Rows and columns
- Data types
- Dimensions
- Measures
- Categorical data
- Numerical data
- Date data
- Unique identifiers

### Important Questions

- What does each column mean?
- Which column identifies a record?
- Which fields are dimensions?
- Which fields are numerical measures?
- Which fields can be used for grouping?
- Which fields can be used for time analysis?

---

# 3. Data Cleaning

### Topics

- Missing values
- Duplicate records
- Invalid values
- Incorrect data types
- Inconsistent text
- Extra spaces
- Invalid dates
- Numeric validation
- Standardisation

### Practice

Take a raw dataset and create:

1. Data Quality Check
2. Cleaning Rules
3. Cleaned Dataset
4. Validation Check

### Suggested Search Topics

- Data cleaning fundamentals
- Excel data cleaning
- Power Query data cleaning
- Pandas data cleaning

---

# 4. Excel

Excel is useful for initial business data preparation and analysis.

### Topics to Revise

- SUM
- AVERAGE
- COUNT
- COUNTA
- COUNTIF
- SUMIF
- SUMIFS
- AVERAGEIF
- IF
- AND
- OR
- IFERROR
- XLOOKUP
- VLOOKUP
- Sorting
- Filtering
- Remove Duplicates
- Text functions
- Date functions
- Pivot Tables
- Pivot Charts
- Conditional Formatting

### Practice

Create:

- KPI summary
- Category summary
- Regional summary
- Monthly summary
- Product summary
- Customer summary

---

# 5. Power Query

Power Query is useful for importing and transforming data.

### Topics

- Get Data
- Import Excel files
- Import CSV files
- Data type conversion
- Remove duplicates
- Remove errors
- Replace values
- Fill missing values
- Split columns
- Merge columns
- Append queries
- Filter rows
- Rename columns
- Transform text
- Transform dates
- Transform numbers

### Practice Workflow

**Get Data**

→ **Transform**

→ **Clean**

→ **Validate**

→ **Load**

---

# 6. Power BI

Power BI is used to build interactive analytical reports.

### Topics

- Power BI Desktop
- Get Data
- Power Query
- Data Model
- Relationships
- Measures
- DAX
- Visualisations
- Filters
- Slicers
- Tooltips
- Drillthrough
- Bookmarks
- Dashboard/report design

### Practice

Build a complete sales report using the Day 100 dataset.

---

# 7. Data Modelling

### Main Tables

**Fact Table**

- SalesData

**Dimension Tables**

- Dim_Customer
- Dim_Product
- Dim_Date

### Important Concepts

- Fact table
- Dimension table
- Primary key
- Foreign key
- Relationships
- One-to-many relationship
- Filter direction
- Star schema

### Suggested Search Topics

- Power BI data modelling
- Star schema Power BI
- Fact and dimension tables
- Power BI relationships

---

# 8. DAX

DAX is the calculation language used in Power BI.

### Core Topics

- Measures
- Calculated columns
- SUM
- AVERAGE
- COUNT
- DISTINCTCOUNT
- DIVIDE
- IF
- CALCULATE
- FILTER
- ALL
- Time intelligence

### Core Measures

**Total Revenue**

`SUM(SalesData[Revenue])`

**Total Cost**

`SUM(SalesData[Cost])`

**Total Profit**

`[Total Revenue] - [Total Cost]`

**Profit Margin %**

`DIVIDE([Total Profit], [Total Revenue], 0)`

**Total Orders**

`DISTINCTCOUNT(SalesData[Order_ID])`

**Total Quantity**

`SUM(SalesData[Quantity])`

**Average Order Value**

`DIVIDE([Total Revenue], [Total Orders], 0)`

**Customers**

`DISTINCTCOUNT(SalesData[Customer_ID])`

---

# 9. Time Intelligence

### Topics

- Date table
- Year
- Quarter
- Month
- Month-Year
- YTD
- MTD
- Previous period
- Year-over-year analysis

### Core Measures

**Revenue YTD**

`TOTALYTD([Total Revenue], Dim_Date[Date])`

**Revenue MTD**

`TOTALMTD([Total Revenue], Dim_Date[Date])`

### Suggested Search Topics

- Power BI time intelligence
- DAX YTD
- DAX MTD
- Power BI Date table

---

# 10. Power BI Visualisation

Study the purpose of each visual rather than simply learning how to create it.

### Core Visuals

- Card
- KPI
- Bar Chart
- Column Chart
- Stacked Column Chart
- 100% Stacked Chart
- Line Chart
- Area Chart
- Pie Chart
- Donut Chart
- Scatter Chart
- Combo Chart
- Treemap
- Waterfall
- Funnel
- Ribbon Chart
- Gauge
- Table
- Matrix

---

# 11. Visual Selection Guide

| Requirement | Suggested Visual |
|---|---|
| Single KPI | Card |
| Category comparison | Column Chart |
| Ranking | Bar Chart |
| Trend | Line Chart |
| Composition | Donut / Pie |
| Contribution | Treemap |
| Relationship | Scatter |
| Change analysis | Waterfall |
| Two measures | Combo Chart |
| Detailed values | Table |
| Hierarchical analysis | Matrix |
| Interactive filtering | Slicer |

---

# 12. Dashboard Design

### Study

- Visual hierarchy
- KPI placement
- Consistent formatting
- White space
- Titles
- Labels
- Filters
- User interaction
- Report navigation

### Suggested Layout

**Top**

- Revenue
- Profit
- Orders
- Profit Margin %

**Middle**

- Monthly Revenue
- Category Revenue
- Regional Revenue
- Segment Revenue

**Bottom**

- Product Analysis
- Detailed Matrix
- Additional analysis

**Side / Top**

- Slicers

---

# 13. Power BI Interactivity

### Topics

- Slicers
- Filters
- Cross-filtering
- Cross-highlighting
- Tooltips
- Drillthrough
- Bookmarks
- Buttons
- Page navigation
- Conditional formatting

### Practice

Create:

- Region slicer
- Category slicer
- Customer Segment slicer
- Channel slicer
- Date slicer

Then test whether the visuals respond correctly.

---

# 14. Tooltips

### Study

- Default tooltips
- Report page tooltips
- Additional KPI information
- Context-specific information

### Practice

Create a tooltip showing:

- Revenue
- Profit
- Orders
- Quantity
- Profit Margin %

---

# 15. Drillthrough

### Study

- Drillthrough page
- Drillthrough field
- Filter context
- Detail pages

### Practice

Create:

**Region Summary → Region Detail**

The detail page can contain:

- Revenue
- Profit
- Orders
- Products
- Customers
- Monthly Trend

---

# 16. Bookmarks

### Study

- Bookmark states
- Buttons
- Navigation
- Show/Hide visuals
- Alternate report views

### Practice

Create two report views:

**Overview**

and

**Detailed Analysis**

Use buttons/bookmarks to navigate between them.

---

# 17. Business Insights

### Learn

A useful insight should be:

- Data-based
- Specific
- Relevant
- Easy to understand
- Connected to the business question

### Insight Structure

**Observation**

→ **Evidence**

→ **Business Context**

→ **Possible Area for Investigation**

Avoid presenting assumptions as proven causes.

---

# 18. Data Storytelling

### Study

- Start with the business question
- Show important KPIs
- Explain trends
- Highlight meaningful differences
- Connect visuals
- End with key findings

### Basic Story

**What happened?**

→ **Where did it happen?**

→ **When did it happen?**

→ **Which segment/product/region was involved?**

→ **What should be investigated further?**

---

# 19. Python for Business Analytics

### Libraries

- Pandas
- NumPy
- Matplotlib

### Topics

- Data loading
- Data inspection
- Data cleaning
- GroupBy
- Aggregation
- Merge
- Date handling
- KPI calculation
- Visualisation
- CSV export

### Suggested Search Topics

- Pandas business analytics
- Pandas GroupBy
- Pandas data cleaning
- Matplotlib business charts

---

# 20. Pandas Practice

Practice these operations:

- `read_excel()`
- `read_csv()`
- `head()`
- `info()`
- `describe()`
- `isna()`
- `drop_duplicates()`
- `fillna()`
- `groupby()`
- `agg()`
- `sort_values()`
- `to_csv()`

### Practice Tasks

Calculate:

- Revenue by Category
- Revenue by Region
- Revenue by Segment
- Monthly Revenue
- Product Revenue
- Customer Revenue

---

# 21. Matplotlib

### Study

- Bar chart
- Column-style chart
- Line chart
- Pie chart
- Scatter plot
- Titles
- Axis labels
- Legends
- Figure size

### Practice

Create:

- Revenue by Category
- Revenue by Region
- Monthly Revenue Trend
- Revenue vs Quantity

---

# 22. Business KPIs Resource List

Important KPIs for this project:

- Total Revenue
- Total Cost
- Total Profit
- Profit Margin %
- Total Orders
- Total Quantity
- Average Order Value
- Customers

Additional KPIs can be added when the business question requires them.

---

# 23. Analysis Areas

The final project covers:

### Category

Revenue, Cost, Profit, Margin

### Region

Revenue, Orders, Profit, Margin

### Customer Segment

Revenue, Orders, Profit

### Product

Revenue, Quantity, Profit

### Channel

Revenue, Orders, Profit

### Customer

Revenue, Orders, Quantity, Profit

### Monthly

Revenue, Cost, Profit, Orders

---

# 24. Final Report Resources

Study how to structure:

- Executive Summary
- Business Problem
- Data Description
- Data Preparation
- Methodology
- KPI Analysis
- Detailed Analysis
- Visualisation
- Business Insights
- Limitations
- Conclusion

The report should explain the analysis in business language.

---

# 25. Recommended Learning Sequence

### Phase 1 — Data

1. Business Understanding
2. Data Understanding
3. Data Quality
4. Data Cleaning
5. Data Validation

### Phase 2 — Analysis

6. KPI Analysis
7. Category Analysis
8. Region Analysis
9. Segment Analysis
10. Product Analysis
11. Customer Analysis
12. Channel Analysis
13. Monthly Analysis

### Phase 3 — Power BI

14. Power Query
15. Data Model
16. Relationships
17. DAX
18. Time Intelligence
19. Visualisation
20. Slicers
21. Tooltips
22. Drillthrough
23. Bookmarks

### Phase 4 — Reporting

24. Dashboard
25. Business Insights
26. Final Report
27. Presentation

---

# 26. Practice Resources

Use the Day 100 workbook for hands-on practice.

### Main Workbook

`Day_100_Final_Business_Analytics_Project.xlsx`

### Main Power BI Resources

- Day 100 Power BI Build Guide
- DAX Reference
- Final Business Analytics Python Code

### Project Practice

Repeat the workflow without looking at the completed analysis:

**Raw Data**

→ **Clean**

→ **Validate**

→ **Analyse**

→ **Build KPIs**

→ **Create Dashboard**

→ **Write Insights**

---

# 27. Official Learning Resources

### Microsoft Power BI

:contentReference[oaicite:0]{index=0}

### Microsoft Learn — Power BI

:contentReference[oaicite:1]{index=1}

### Microsoft DAX Documentation

:contentReference[oaicite:2]{index=2}

### Microsoft Power Query Documentation

:contentReference[oaicite:3]{index=3}

### Pandas Documentation

:contentReference[oaicite:4]{index=4}

### NumPy Documentation

:contentReference[oaicite:5]{index=5}

### Matplotlib Documentation

:contentReference[oaicite:6]{index=6}

---

# 28. Suggested Search Topics

Search and study these topics one by one:

### Business Analytics

- Business analytics workflow
- KPI development
- Business data analysis
- Data storytelling

### Excel

- Excel Pivot Tables
- Excel business dashboard
- Excel data cleaning
- Excel lookup functions

### Power BI

- Power BI beginner tutorial
- Power BI data modelling
- Power BI relationships
- Power BI dashboard
- Power BI slicers
- Power BI drillthrough
- Power BI bookmarks
- Power BI tooltips

### DAX

- DAX measures
- DAX CALCULATE
- DAX DIVIDE
- DAX DISTINCTCOUNT
- DAX time intelligence
- DAX YTD
- DAX MTD

### Python

- Pandas data cleaning
- Pandas GroupBy
- Pandas aggregation
- Matplotlib charts

---

# 29. Final Project Study Checklist

## Business

- [ ] Business objective understood
- [ ] Business questions defined
- [ ] KPIs identified

## Data

- [ ] Dataset understood
- [ ] Data types checked
- [ ] Missing values checked
- [ ] Duplicates checked
- [ ] Invalid values checked

## Cleaning

- [ ] Text standardized
- [ ] Dates validated
- [ ] Numeric fields validated
- [ ] Missing values handled
- [ ] Duplicates reviewed

## Analysis

- [ ] KPI analysis
- [ ] Category analysis
- [ ] Region analysis
- [ ] Segment analysis
- [ ] Product analysis
- [ ] Customer analysis
- [ ] Channel analysis
- [ ] Monthly analysis

## Power BI

- [ ] Data imported
- [ ] Relationships created
- [ ] DAX measures created
- [ ] KPI cards created
- [ ] Charts created
- [ ] Slicers added
- [ ] Matrix created
- [ ] Tooltips added
- [ ] Drillthrough added
- [ ] Bookmarks added
- [ ] Dashboard formatted

## Reporting

- [ ] Insights written
- [ ] Evidence checked
- [ ] Limitations documented
- [ ] Final report prepared
- [ ] Dashboard validated
- [ ] Presentation prepared

---

# 🏆 Final Resource Map

**Business Analytics**

→ Business Understanding

→ Data Understanding

→ Data Cleaning

→ Data Analysis

→ KPI

→ Excel

→ Power BI

→ DAX

→ Visualisation

→ Dashboard

→ Business Insights

→ Reporting

---

# 🎓 Final Takeaway

The most important skill from the 100-day roadmap is not memorising individual tools.

It is learning how to take:

**Business Problem**

→ **Business Data**

→ **Clean Data**

→ **Analysis**

→ **KPI**

→ **Visualisation**

→ **Dashboard**

→ **Business Insight**

→ **Business Report**

This workflow can be reused for many different business datasets and analytics projects.