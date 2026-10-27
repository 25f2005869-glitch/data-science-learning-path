# 📘 Day 100 — Power BI Build Guide

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 100  
**Topic:** Final Business Analytics Project — Power BI Build Guide

---

# 🎯 1. Purpose of This Guide

This guide explains how to build the Day 100 Final Business Analytics Project in Power BI.

The complete workflow is:

**Import Data**

→ **Clean Data**

→ **Create Data Model**

→ **Create Relationships**

→ **Create DAX Measures**

→ **Create Visuals**

→ **Add Slicers**

→ **Add Interactions**

→ **Build Dashboard**

→ **Generate Insights**

→ **Validate Report**

---

# 📁 2. Required Files

Use the Day 100 workbook:

`Day_100_Final_Business_Analytics_Project.xlsx`

The main tables are:

- `SalesData`
- `Dim_Customer`
- `Dim_Product`
- `Dim_Date`

---

# 🗂️ 3. Power BI Project Structure

The final Power BI report can contain pages such as:

1. Executive Dashboard
2. Category Analysis
3. Regional Analysis
4. Customer Analysis
5. Product Analysis
6. Monthly Analysis
7. Detailed Analysis

You can keep the report simple and add pages only when they provide useful information.

---

# 🚀 4. Step 1 — Open Power BI Desktop

Open **Power BI Desktop**.

Select:

**Home → Get Data → Excel Workbook**

Select:

`Day_100_Final_Business_Analytics_Project.xlsx`

---

# 📥 5. Step 2 — Select the Required Sheets

Load the required tables:

- `SalesData`
- `Dim_Customer`
- `Dim_Product`
- `Dim_Date`

Check the preview before loading.

Click:

**Load**

---

# 🧹 6. Step 3 — Check Data Types

Open the Data or Model view.

Check important fields.

### SalesData

- Order_ID → Text
- Date → Date
- Customer_ID → Text
- Product → Text
- Category → Text
- Region → Text
- Quantity → Whole Number
- Unit_Price → Decimal Number
- Discount_% → Decimal Number
- Revenue → Decimal Number
- Cost → Decimal Number

### Dim_Date

`Date` should be a Date data type.

Correct data types are important for calculations and visualisation.

---

# 🔄 7. Step 4 — Power Query

If additional transformation is required:

**Home → Transform Data**

Power Query can be used to:

- Remove duplicates
- Handle missing values
- Change data types
- Rename columns
- Remove unwanted columns
- Standardise text
- Transform dates
- Filter rows

After completing transformations:

**Home → Close & Apply**

---

# 🧩 8. Step 5 — Open Model View

Select the **Model** icon.

You should see:

`SalesData`

`Dim_Customer`

`Dim_Product`

`Dim_Date`

The goal is to connect the sales table with the relevant dimensions.

---

# 🔗 9. Step 6 — Create Relationships

Create these relationships:

### Customer

`Dim_Customer[Customer_ID]`

→

`SalesData[Customer_ID]`

### Product

`Dim_Product[Product]`

→

`SalesData[Product]`

### Date

`Dim_Date[Date]`

→

`SalesData[Date]`

The dimension side should provide unique values for the corresponding key.

---

# ⭐ 10. Step 7 — Check the Data Model

Verify:

- Relationships exist
- Correct columns are connected
- Key columns have compatible data types
- Dimension keys are unique
- Filters work correctly

A clean model makes the report easier to maintain.

---

# 🧮 11. Step 8 — Create DAX Measures

Go to:

**Modeling → New Measure**

Create the following measures.

---

# 💰 12. Total Revenue

`Total Revenue = SUM(SalesData[Revenue])`

This is the main revenue KPI.

---

# 💵 13. Total Cost

`Total Cost = SUM(SalesData[Cost])`

This calculates total recorded cost.

---

# 📈 14. Total Profit

`Total Profit = [Total Revenue] - [Total Cost]`

This calculates profit.

---

# 📊 15. Profit Margin %

`Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)`

Format this measure as:

**Percentage**

---

# 🧾 16. Total Orders

`Total Orders = DISTINCTCOUNT(SalesData[Order_ID])`

This counts unique orders.

---

# 📦 17. Total Quantity

`Total Quantity = SUM(SalesData[Quantity])`

This calculates the total number of units sold.

---

# 🛒 18. Average Order Value

`Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)`

This calculates average revenue per order.

---

# 👥 19. Customers

`Customers = DISTINCTCOUNT(SalesData[Customer_ID])`

This calculates the number of unique customers.

---

# 📅 20. Revenue YTD

`Revenue YTD = TOTALYTD([Total Revenue], Dim_Date[Date])`

This calculates year-to-date revenue.

---

# 🗓️ 21. Revenue MTD

`Revenue MTD = TOTALMTD([Total Revenue], Dim_Date[Date])`

This calculates month-to-date revenue.

---

# 🃏 22. Step 9 — Create KPI Cards

Go to **Report View**.

Add a **Card** visual.

Create four main KPI cards:

### Card 1

**Total Revenue**

### Card 2

**Total Profit**

### Card 3

**Total Orders**

### Card 4

**Profit Margin %**

Additional cards can show:

- Customers
- Average Order Value
- Total Quantity

---

# 📈 23. Step 10 — Monthly Revenue Chart

Add a **Line Chart**.

### X-axis

`Dim_Date[Month-Year]`

### Y-axis

`[Total Revenue]`

Title:

**Monthly Revenue Trend**

Make sure months appear in chronological order.

---

# 🏷️ 24. Step 11 — Revenue by Category

Add a **Clustered Column Chart**.

### X-axis

`SalesData[Category]`

### Y-axis

`[Total Revenue]`

Title:

**Revenue by Category**

This provides a category comparison.

---

# 🌍 25. Step 12 — Revenue by Region

Add a **Bar Chart**.

### Y-axis / Category

`SalesData[Region]`

### X-axis / Values

`[Total Revenue]`

Title:

**Revenue by Region**

---

# 👥 26. Step 13 — Revenue by Customer Segment

Add a **Donut Chart**.

### Legend

`Dim_Customer[Customer_Segment]`

### Values

`[Total Revenue]`

Title:

**Revenue by Customer Segment**

Use this visual when the number of categories is manageable.

---

# 📦 27. Step 14 — Product Analysis

Add a **Bar Chart**.

### Category

`SalesData[Product]`

### Values

`[Total Revenue]`

Title:

**Revenue by Product**

Sort the visual by Revenue if a ranking view is useful.

---

# 🔵 28. Step 15 — Revenue vs Quantity

Add a **Scatter Chart**.

### X-axis

`[Total Quantity]`

### Y-axis

`[Total Revenue]`

### Details

`SalesData[Product]`

Title:

**Revenue vs Quantity**

This can be used to explore the relationship between units sold and revenue.

---

# 📣 29. Step 16 — Channel Analysis

Add a **Column Chart**.

### X-axis

`SalesData[Channel]`

### Y-axis

`[Total Revenue]`

Title:

**Revenue by Channel**

You can also create another visual using:

`[Total Profit]`

---

# 📋 30. Step 17 — Create a Matrix

Add a **Matrix** visual.

### Rows

`Region`

`Category`

### Values

- `[Total Revenue]`
- `[Total Profit]`
- `[Total Orders]`
- `[Profit Margin %]`

Title:

**Regional and Category Performance**

---

# 🎛️ 31. Step 18 — Add Region Slicer

Add a **Slicer**.

Field:

`SalesData[Region]`

Title:

**Region**

Test the slicer by selecting different regions.

The connected visuals should respond.

---

# 🏷️ 32. Step 19 — Add Category Slicer

Add another Slicer.

Field:

`SalesData[Category]`

Title:

**Category**

Use it to filter the report interactively.

---

# 👥 33. Step 20 — Add Customer Segment Slicer

Add a Slicer.

Field:

`Dim_Customer[Customer_Segment]`

Title:

**Customer Segment**

---

# 📣 34. Step 21 — Add Channel Slicer

Add a Slicer.

Field:

`SalesData[Channel]`

Title:

**Channel**

---

# 📅 35. Step 22 — Add Date Slicer

Add a Slicer using:

`Dim_Date[Date]`

This allows the user to analyse a selected date range.

---

# 🔍 36. Step 23 — Test Cross-Filtering

Select a category in:

**Revenue by Category**

Check whether:

- KPI cards update
- Regional analysis updates
- Segment analysis updates
- Monthly trend updates

Repeat with:

- Region
- Segment
- Channel

This verifies report interactivity.

---

# 💬 37. Step 24 — Add Tooltips

Tooltips can display additional information.

Useful tooltip measures:

- Total Revenue
- Total Profit
- Total Orders
- Total Quantity
- Profit Margin %

Use tooltips to provide extra context without overcrowding the main visual.

---

# 🔎 38. Step 25 — Create Drillthrough

Create a detailed page for a selected business dimension.

Example:

**Region Detail**

Add the appropriate field to the Drillthrough filters.

The page can contain:

- Revenue
- Profit
- Orders
- Quantity
- Product analysis
- Monthly trend

Users can move from a summary visual to the detailed page.

---

# 🔖 39. Step 26 — Create Bookmarks

Bookmarks can be used for:

- Page navigation
- Alternate views
- Show/hide visuals
- Dashboard interactions

Example:

**Overview → Detailed Analysis**

Create buttons and assign bookmarks when required.

---

# 🎨 40. Step 27 — Formatting

Check:

- Titles
- Font sizes
- Number formats
- Percentage formats
- Alignment
- Spacing
- Visual size
- Slicer placement
- Axis titles
- Data labels

Keep formatting consistent throughout the report.

---

# 💰 41. Number Formatting

Recommended formats:

### Revenue

Currency or appropriate numeric format.

### Cost

Currency or appropriate numeric format.

### Profit

Currency or appropriate numeric format.

### Profit Margin

Percentage.

### Orders

Whole number.

### Quantity

Whole number.

### Average Order Value

Currency or appropriate numeric format.

---

# 🖥️ 42. Recommended Dashboard Layout

## Top Row

**Total Revenue | Total Profit | Total Orders | Profit Margin %**

---

## Middle Row

**Monthly Revenue Trend**

**Revenue by Category**

---

## Lower Row

**Revenue by Region**

**Revenue by Customer Segment**

---

## Bottom Row

**Revenue by Product**

**Revenue vs Quantity**

**Detailed Matrix**

---

## Filter Area

- Region
- Category
- Customer Segment
- Channel
- Date

---

# 📊 43. Suggested Report Pages

## Page 1 — Executive Dashboard

Include:

- KPI Cards
- Monthly Revenue
- Category Revenue
- Regional Revenue
- Segment Revenue
- Slicers

---

## Page 2 — Category Analysis

Include:

- Category Revenue
- Category Profit
- Orders
- Quantity
- Profit Margin
- Category slicer

---

## Page 3 — Regional Analysis

Include:

- Revenue by Region
- Profit by Region
- Orders by Region
- Regional Matrix
- Region slicer

---

## Page 4 — Customer Analysis

Include:

- Customers
- Revenue
- Orders
- Customer Segment
- Customer-level analysis

---

## Page 5 — Product Analysis

Include:

- Product Revenue
- Product Profit
- Quantity
- Product ranking
- Revenue vs Quantity

---

## Page 6 — Monthly Analysis

Include:

- Monthly Revenue
- Monthly Profit
- Monthly Orders
- Monthly Quantity
- Date slicer

---

# 💡 44. Step 28 — Write Business Insights

After completing the dashboard, review the visuals.

Look for:

- Revenue patterns
- Profit patterns
- Category differences
- Regional differences
- Segment differences
- Product performance
- Channel performance
- Monthly changes

Write observations based on the displayed data.

---

# ⚠️ 45. Separate Observation from Assumption

Example:

### Observation

Revenue increased in a particular month.

### Assumption

Customers increased their purchases because of a particular reason.

The second statement needs additional evidence.

Do not present assumptions as confirmed causes.

---

# 🔍 46. Step 29 — Validate the Dashboard

Before finalising the report, check:

### Numbers

- [ ] Revenue matches the source
- [ ] Cost matches the source
- [ ] Profit is correct
- [ ] Orders are unique
- [ ] Quantity is correct
- [ ] Customer count is correct

### Filters

- [ ] Region slicer works
- [ ] Category slicer works
- [ ] Segment slicer works
- [ ] Channel slicer works
- [ ] Date slicer works

### Visuals

- [ ] Titles are clear
- [ ] Labels are readable
- [ ] Numbers are formatted correctly
- [ ] Charts display the correct fields

---

# 🧪 47. Final Power BI Testing

Test the report using different selections.

### Test 1

Select one region.

Check all KPI cards.

### Test 2

Select one category.

Check the monthly trend.

### Test 3

Select one customer segment.

Check revenue and profit.

### Test 4

Select a date range.

Check all time-based visuals.

### Test 5

Clear all filters.

Confirm the dashboard returns to the overall view.

---

# 💾 48. Step 30 — Save the Power BI File

Save the completed report as:

`Day_100_Final_Business_Analytics_Project.pbix`

Keep the Excel workbook separately as the source/practice dataset.

---

# 📦 49. Final Project Files

Recommended project structure:

`Day_100_Final_Business_Analytics_Project/`

- README.md
- notes.md
- cheat-sheet.md
- practice.md
- resources.md
- DAX_REFERENCE.md
- POWER_BI_BUILD_GUIDE.md
- code/
- data/
- outputs/
- Power BI `.pbix` report

---

# 🏆 50. Final Dashboard Checklist

## Data

- [ ] SalesData imported
- [ ] Customer Dimension imported
- [ ] Product Dimension imported
- [ ] Date Dimension imported
- [ ] Data types checked
- [ ] Data quality checked

## Model

- [ ] Customer relationship created
- [ ] Product relationship created
- [ ] Date relationship created
- [ ] Relationships validated

## DAX

- [ ] Total Revenue
- [ ] Total Cost
- [ ] Total Profit
- [ ] Profit Margin %
- [ ] Total Orders
- [ ] Total Quantity
- [ ] Average Order Value
- [ ] Customers
- [ ] Revenue YTD
- [ ] Revenue MTD

## Visuals

- [ ] Revenue Card
- [ ] Profit Card
- [ ] Orders Card
- [ ] Margin Card
- [ ] Monthly Revenue
- [ ] Category Revenue
- [ ] Regional Revenue
- [ ] Segment Revenue
- [ ] Product Revenue
- [ ] Revenue vs Quantity
- [ ] Matrix

## Interactivity

- [ ] Region Slicer
- [ ] Category Slicer
- [ ] Segment Slicer
- [ ] Channel Slicer
- [ ] Date Slicer
- [ ] Cross-filtering tested
- [ ] Tooltip added
- [ ] Drillthrough tested
- [ ] Bookmark tested

## Final Report

- [ ] Dashboard formatted
- [ ] Insights written
- [ ] Numbers validated
- [ ] Limitations documented
- [ ] PBIX saved

---

# 🎓 Final Takeaway

The Day 100 Power BI report should demonstrate the complete Business Analytics workflow:

**Data**

→ **Power Query**

→ **Data Model**

→ **Relationships**

→ **DAX**

→ **KPIs**

→ **Visuals**

→ **Slicers**

→ **Interactive Report**

→ **Business Insights**

→ **Final Dashboard**

The objective is to build a report that converts business data into clear, interactive and evidence-based analytical information.