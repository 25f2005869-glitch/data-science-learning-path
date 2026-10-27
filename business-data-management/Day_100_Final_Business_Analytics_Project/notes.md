# 📘 Day 100 — Final Business Analytics Project Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 100  
**Topic:** Final Business Analytics Project

---

# 1. Introduction to the Final Project

Day 100 is the final project of the Business Data Management roadmap.

The purpose of this project is to bring together the concepts learned throughout the 100-day journey and apply them to a complete business analytics workflow.

The project starts with business data and ends with a structured analytical report and dashboard.

The complete workflow is:

**Business Understanding**

→ **Data Understanding**

→ **Data Cleaning**

→ **Data Validation**

→ **Data Analysis**

→ **KPI Development**

→ **Visualisation**

→ **Dashboard**

→ **Business Insights**

→ **Presentation**

---

# 2. Business Understanding

Before analysing data, the business problem should be clearly understood.

Business Understanding means identifying:

- What the business does
- What data is available
- What the business wants to understand
- Which questions need to be answered
- Which KPIs are important
- Who will use the analysis

The analysis should begin with business questions rather than charts.

---

# 3. Defining Business Questions

Business questions give direction to the analysis.

Examples:

- What is the total revenue?
- What is the total profit?
- How many orders were generated?
- Which categories contribute to revenue?
- How do regions compare?
- How do customer segments perform?
- Which products generate revenue?
- Which channels generate sales?
- How does revenue change over time?
- How does profitability change over time?

Good business questions should be clear and measurable.

---

# 4. Data Understanding

Data Understanding means examining the available dataset before performing analysis.

Important things to identify include:

- Number of rows
- Number of columns
- Column names
- Data types
- Business meaning of each field
- Dimensions
- Measures
- Missing values
- Duplicate records
- Invalid values

The main transaction table in this project is:

`SalesData`

---

# 5. Main Sales Data Fields

The sales dataset contains fields such as:

| Field | Meaning |
|---|---|
| Order_ID | Unique order identifier |
| Date | Transaction date |
| Customer_ID | Customer identifier |
| Product | Product purchased |
| Category | Product category |
| Region | Business region |
| City | Customer or transaction city |
| Customer_Segment | Customer segment |
| Channel | Sales channel |
| Payment_Method | Payment method |
| Sales_Rep | Sales representative |
| Quantity | Quantity sold |
| Unit_Price | Price per unit |
| Discount_% | Discount percentage |
| Revenue | Revenue generated |
| Cost | Business cost |

Additional calculated fields include:

- Profit
- Profit Margin %

---

# 6. Data Cleaning

Raw business data may contain issues that affect analysis.

Common issues include:

- Missing values
- Duplicate records
- Incorrect data types
- Invalid dates
- Inconsistent text
- Incorrect numeric values
- Blank fields

The purpose of data cleaning is to prepare the dataset for reliable analysis.

---

# 7. Data Validation

After cleaning, the data should be validated.

Validation checks whether:

- Required fields are available
- Numeric values are reasonable
- Dates are valid
- Duplicate records have been reviewed
- Calculated fields are correct
- Relationships between tables are appropriate

Cleaning and validation are separate steps.

**Cleaning** changes or prepares the data.

**Validation** checks whether the prepared data is suitable.

---

# 8. Data Model

The final project uses a simple business data model.

### Main Table

`SalesData`

### Dimension Tables

- `Dim_Customer`
- `Dim_Product`
- `Dim_Date`

The sales table contains transaction-level information.

The dimension tables provide additional descriptive information.

---

# 9. Customer Dimension

`Dim_Customer` contains customer-related information.

Important fields include:

- Customer_ID
- Customer_Name
- Age
- Gender
- Customer_Segment
- City
- Region

Customer dimensions can be used to analyse sales from a customer perspective.

---

# 10. Product Dimension

`Dim_Product` contains product information.

Important fields include:

- Product_ID
- Product
- Category
- Standard_Price

This dimension supports product and category analysis.

---

# 11. Date Dimension

`Dim_Date` supports time-based analysis.

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

A date dimension is useful for trend analysis and time-intelligence calculations.

---

# 12. Relationships

The model uses relationships between the sales table and dimension tables.

Main relationships:

`Dim_Customer[Customer_ID]`

→

`SalesData[Customer_ID]`

---

`Dim_Product[Product]`

→

`SalesData[Product]`

---

`Dim_Date[Date]`

→

`SalesData[Date]`

These relationships allow dimension fields to filter the sales data.

---

# 13. Business Metrics

Business metrics convert raw data into useful measurements.

Important metrics in this project include:

- Revenue
- Cost
- Profit
- Profit Margin
- Orders
- Quantity
- Average Order Value
- Customers

---

# 14. Revenue

Revenue represents the sales value generated from transactions.

The basic calculation is:

**Revenue = Quantity × Unit Price**

When discounts are included, the final revenue can be lower than the gross sales value.

Revenue is one of the main KPIs used in the project.

---

# 15. Cost

Cost represents the business cost associated with the sales.

It can be used with revenue to understand profitability.

Basic relationship:

**Profit = Revenue − Cost**

---

# 16. Profit

Profit represents the difference between revenue and cost.

Formula:

**Profit = Total Revenue − Total Cost**

Profit is useful for understanding the financial result after considering the recorded cost.

---

# 17. Profit Margin

Profit Margin measures profit relative to revenue.

Formula:

**Profit Margin % = Profit ÷ Revenue × 100**

A percentage format is normally used for this KPI.

---

# 18. Total Orders

Total Orders measures the number of unique orders.

In Power BI, a distinct count can be used:

**Total Orders = DISTINCTCOUNT(SalesData[Order_ID])**

This avoids counting the same order more than once when the order identifier is repeated.

---

# 19. Total Quantity

Total Quantity represents the total number of units sold.

Formula:

**Total Quantity = SUM(SalesData[Quantity])**

This metric can be analysed by product, category, region, customer segment and time.

---

# 20. Average Order Value

Average Order Value measures the average revenue generated per order.

Formula:

**Average Order Value = Total Revenue ÷ Total Orders**

In Power BI:

**Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)**

---

# 21. Customers

Customers represents the number of unique customers.

Power BI measure:

**Customers = DISTINCTCOUNT(SalesData[Customer_ID])**

This can be used as a KPI or for customer analysis.

---

# 22. KPI Analysis

KPIs provide a quick summary of business performance.

The project includes:

- Total Revenue
- Total Cost
- Total Profit
- Profit Margin %
- Total Orders
- Total Quantity
- Average Order Value
- Customers

KPI cards can be used to display these values in Power BI.

---

# 23. Category Analysis

Category Analysis compares business performance across product categories.

Metrics include:

- Orders
- Quantity
- Revenue
- Cost
- Profit
- Profit Margin %

Category analysis can help identify differences in business performance between product groups.

---

# 24. Regional Analysis

Regional Analysis compares performance across business regions.

The project includes:

- North
- South
- East
- West

Important metrics include:

- Orders
- Quantity
- Revenue
- Cost
- Profit
- Profit Margin %

---

# 25. Customer Segment Analysis

Customers are grouped into segments:

- New
- Regular
- Loyal
- At Risk

Segment analysis can include:

- Orders
- Quantity
- Revenue
- Profit
- Profit Margin %

This provides a customer-segment view of business performance.

---

# 26. Product Analysis

Product Analysis focuses on individual products.

Important measures include:

- Orders
- Quantity
- Revenue
- Cost
- Profit
- Profit Margin %

Product-level analysis provides more detail than category-level analysis.

---

# 27. Channel Analysis

The project contains multiple sales channels.

Channel analysis can compare:

- Orders
- Revenue
- Profit

This helps understand how business performance differs across sales channels.

---

# 28. Customer Analysis

Customer Analysis focuses on individual customer performance.

Important measures include:

- Orders
- Quantity
- Revenue
- Profit
- Average Order Value

Customer attributes can also be used to understand performance by:

- Segment
- Region
- City
- Gender
- Age

---

# 29. Monthly Analysis

Monthly analysis helps understand business movement over time.

Important measures include:

- Orders
- Revenue
- Cost
- Profit
- Quantity
- Profit Margin %

A line chart is useful for showing monthly trends.

---

# 30. Visualisation

Visualisation converts analytical results into graphical form.

The visual should be selected according to the business question.

Examples:

- KPI → Card
- Comparison → Bar or Column Chart
- Trend → Line Chart
- Composition → Pie or Donut
- Relationship → Scatter Chart
- Hierarchical contribution → Treemap
- Change → Waterfall
- Detailed comparison → Matrix

---

# 31. KPI Card

A Card visual is useful for displaying a single important metric.

Examples:

- Total Revenue
- Total Profit
- Total Orders
- Profit Margin %

A dashboard can place these cards at the top.

---

# 32. Column Chart

A column chart is useful for comparing categories.

Example:

**Revenue by Category**

The category is placed on the axis and revenue is used as the value.

---

# 33. Bar Chart

A bar chart can be used for regional or product comparisons.

Example:

**Revenue by Region**

Regions are displayed as categories and revenue is displayed as the measure.

---

# 34. Line Chart

A line chart is useful for time-series analysis.

Example:

**Monthly Revenue Trend**

The date or month is placed on the X-axis and revenue is placed on the Y-axis.

---

# 35. Donut Chart

A donut chart can be used to show composition.

Example:

**Revenue by Customer Segment**

Each segment represents a portion of the total.

---

# 36. Treemap

A treemap displays hierarchical or contribution-based information using differently sized rectangles.

Example:

**Revenue by Product**

It can help visually compare product contribution.

---

# 37. Scatter Chart

A scatter chart can show relationships between two numerical measures.

Example:

**Revenue vs Quantity**

Each point can represent a product, customer or other business entity.

---

# 38. Combo Chart

A combo chart combines two chart types.

For example:

- Revenue as columns
- Cost as a line

This can allow two related measures to be viewed together.

---

# 39. Waterfall Chart

A waterfall chart is useful for showing how a starting value changes through increases and decreases.

It can be used when the business question involves movement from one value to another.

---

# 40. Matrix

A Matrix visual is useful for detailed cross-tab analysis.

Example:

**Region → Category → Revenue → Profit**

Matrix visuals can provide hierarchical business detail.

---

# 41. Slicers

Slicers allow users to filter a report interactively.

Useful slicers include:

- Region
- Category
- Customer Segment
- Channel
- Date

When a slicer is changed, connected visuals can update according to the filter context.

---

# 42. Filter Context

Filter context is important in Power BI.

A measure can return different results depending on:

- Slicers
- Filters
- Visual selections
- Page filters
- Cross-filtering

For example, Total Revenue can display overall revenue or revenue for a selected region.

---

# 43. DAX Measures

DAX is used to create calculations in Power BI.

Important measures include:

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

# 44. Time Intelligence

The Date dimension supports time-based calculations.

Examples include:

- Year
- Quarter
- Month
- Month-Year
- Week
- Day

Additional DAX measures can be created for:

- YTD
- MTD

Example:

**Revenue YTD**

`TOTALYTD([Total Revenue], Dim_Date[Date])`

**Revenue MTD**

`TOTALMTD([Total Revenue], Dim_Date[Date])`

---

# 45. Dashboard Design

A dashboard should present important information clearly.

A possible layout is:

**Top**

- Total Revenue
- Total Profit
- Total Orders
- Profit Margin %

**Middle**

- Monthly Revenue Trend
- Revenue by Category
- Revenue by Region
- Revenue by Segment

**Bottom**

- Product Analysis
- Revenue vs Cost
- Detailed Matrix
- Slicers

---

# 46. Interactive Reporting

Power BI allows users to interact with the report.

Important interactive features include:

- Slicers
- Filters
- Cross-filtering
- Tooltips
- Drillthrough
- Bookmarks
- Buttons
- Conditional formatting

These features make the report more useful for exploration.

---

# 47. Tooltips

Tooltips display additional information when the user moves the pointer over a visual.

A tooltip can contain:

- Revenue
- Profit
- Orders
- Quantity
- Margin

This allows additional information to be available without overcrowding the main dashboard.

---

# 48. Drillthrough

Drillthrough allows users to move from a summary visual to a detailed report page.

For example:

A user can select a region from a regional visual and open a detailed regional analysis page.

The drillthrough page can contain:

- Revenue
- Profit
- Orders
- Products
- Customers
- Trends

---

# 49. Bookmarks

Bookmarks save a particular report state.

They can be used to create:

- Alternate report views
- Navigation experiences
- Show/hide sections
- Button-based interactions

Bookmarks can be combined with buttons.

---

# 50. Conditional Formatting

Conditional formatting helps highlight values in tables and matrices.

Possible methods include:

- Background formatting
- Font formatting
- Data bars
- Rules

The purpose is to make important values easier to identify.

---

# 51. Business Insights

Business insights should come from the data.

An insight can describe:

- A high-revenue category
- A high-revenue region
- A strong customer segment
- A high-performing product
- A monthly change
- A profitability pattern

An observation should be clearly separated from an assumption about why it happened.

---

# 52. Business Recommendations

Possible business actions should be connected to evidence.

For example:

- Investigate categories with strong revenue contribution.
- Review products with unusual profitability.
- Examine regional differences.
- Study customer-segment behaviour.
- Investigate significant monthly changes.

Recommendations should not claim causality unless the available analysis supports it.

---

# 53. Final Business Report

The final report should contain:

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

# 54. Limitations

Every analysis has limitations.

For this educational project, limitations can include:

- The dataset is synthetic.
- The project uses predefined business fields.
- The analysis describes the available data.
- Observed relationships do not automatically establish causation.
- Additional business context may be required for real-world decisions.

---

# 55. Excel and Power BI Connection

Excel can be used for:

- Data preparation
- Formula calculations
- Summary tables
- Charts
- Initial analysis

Power BI can be used for:

- Power Query
- Data modelling
- DAX
- Interactive visuals
- Slicers
- Drillthrough
- Tooltips
- Dashboard development

Together they provide a practical business analytics workflow.

---

# 56. Python Connection

Python can reproduce parts of the analytical workflow.

Useful libraries include:

- Pandas
- NumPy
- Matplotlib

Python can be used for:

- Data loading
- Data cleaning
- Data transformation
- Aggregation
- KPI calculation
- Exporting analytical outputs

The project code is available in:

`code/final_business_analytics.py`

---

# 57. Final Project Workflow

The complete project can be summarised as:

**1. Understand the Business**

↓

**2. Understand the Data**

↓

**3. Check Data Quality**

↓

**4. Clean the Data**

↓

**5. Validate the Data**

↓

**6. Analyse the Data**

↓

**7. Create KPIs**

↓

**8. Create Visualisations**

↓

**9. Build Dashboard**

↓

**10. Generate Business Insights**

↓

**11. Prepare Final Report**

↓

**12. Present the Findings**

---

# 58. Final Learning Points

The major concepts brought together in Day 100 are:

- Business understanding
- Data understanding
- Data cleaning
- Data validation
- Exploratory analysis
- KPI development
- Business metrics
- Excel analysis
- Power BI
- Power Query
- Data modelling
- DAX
- Visualisation
- Dashboard design
- Interactive reporting
- Business insights
- Final reporting

---

# 59. Final Outcome

After completing the project, the learner should be able to take a business dataset and follow a complete analytical workflow.

The final output should contain:

- Clean data
- Structured analysis
- KPIs
- Charts
- Interactive dashboard
- Business insights
- Final report

---

# 🎓 Final Takeaway

Business Analytics is not only about creating charts.

The complete process is:

**Understand the business**

→ **Prepare the data**

→ **Analyse the data**

→ **Create meaningful KPIs**

→ **Visualise the results**

→ **Identify evidence-based insights**

→ **Communicate the findings clearly**

Day 100 brings together the major concepts practiced throughout the 100-day Business Data Management roadmap.