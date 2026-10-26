# Day 099 — Power BI Extension Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 099  
**Topic:** Power BI Extension

## 1. Power BI
Power BI is used to connect, transform, model, analyse and visualise business data.

## 2. Workflow
Get Data → Power Query → Data Model → DAX → Visuals → Interactions → Dashboard → Insights

## 3. Power Query
Power Query handles data transformation such as changing data types, removing duplicates, cleaning text, handling missing values and creating transformation steps.

## 4. Data Model
SalesData is the main transaction table. Dim_Customer, Dim_Product and Dim_Date provide descriptive fields for analysis.

## 5. Relationships
Relationships allow dimension fields to filter transaction data. A common design is one dimension record to many transaction records.

## 6. Measures
Measures are dynamic calculations evaluated in the current filter context.

Core measures:
- Total Revenue = SUM(SalesData[Revenue])
- Total Cost = SUM(SalesData[Cost])
- Total Profit = [Total Revenue] - [Total Cost]
- Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
- Total Orders = DISTINCTCOUNT(SalesData[Order_ID])
- Total Quantity = SUM(SalesData[Quantity])
- Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
- Customers = DISTINCTCOUNT(SalesData[Customer_ID])

## 7. Visuals
Use cards for KPIs, bar/column charts for comparisons, line charts for trends, composition charts for simple shares, scatter charts for relationships, and matrices for detailed cross-tab analysis.

## 8. Interactivity
Slicers, filters, tooltips, drillthrough, bookmarks and buttons make a report interactive.

## 9. Time Analysis
Dim_Date supports Year, Quarter, Month, Month-Year, Week and Day analysis. YTD and MTD measures can be added with DAX.

## 10. Dashboard
A practical sales dashboard can contain KPI cards, monthly revenue trend, category analysis, regional analysis, segment analysis, product analysis, a matrix and slicers.

## 11. Business Questions
- What is total revenue?
- What is total profit?
- Which category generates the most revenue?
- Which region generates the most revenue?
- How does revenue change over time?
- How do customer segments compare?

## Key Learning
Power BI connects data preparation, modelling, calculation, visualisation and interactive reporting in one workflow.
