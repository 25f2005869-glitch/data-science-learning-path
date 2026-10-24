# 📊 Day 096 — Customer Analytics — Notes

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-BDM-blue?style=for-the-badge)
![Customer Analytics](https://img.shields.io/badge/Topic-Customer%20Analytics-green?style=for-the-badge)
![Day 096](https://img.shields.io/badge/Day-096-orange?style=for-the-badge)

---

## 👤 Course Information

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 096  
**Topic:** Customer Analytics

---

# 1. Introduction to Customer Analytics

Customer Analytics is the process of analysing customer-related data to understand:

- Who the customers are
- How customers purchase
- How much customers spend
- Which customer segments are active
- Which products customers purchase
- Which regions generate customer activity
- How customer behaviour changes over time

Customer Analytics converts raw customer data into useful business information.

---

# 2. Customer Data

Customer data can contain information about both customers and their transactions.

The Day 096 dataset contains fields such as:

- Order ID
- Date
- Customer ID
- Customer Name
- Age
- Gender
- City
- Region
- Customer Segment
- Product Category
- Quantity
- Unit Price
- Revenue
- Customer Satisfaction
- Customer Status
- Payment Method

Each field provides a different type of information for analysis.

---

# 3. Order ID

`Order_ID` identifies an individual transaction.

Example:

- O001
- O002
- O003

Order IDs help count transactions and distinguish one order from another.

---

# 4. Customer ID

`Customer_ID` identifies a customer.

Example:

- C001
- C002
- C003

A customer can have more than one order.

Therefore:

**Customer Count ≠ Order Count**

For example:

If C001 has 3 orders, it is still counted as one unique customer.

---

# 5. Customer Name

`Customer_Name` contains the name associated with a customer.

Names are useful for customer-level analysis.

However, names may contain data-quality problems such as:

- Extra spaces
- Inconsistent formatting
- Missing values

Text cleaning should be performed before analysis.

---

# 6. Date

The `Date` field records when a transaction occurred.

Dates can be used for:

- Monthly analysis
- Trend analysis
- Customer activity analysis
- Revenue trend analysis

For example:

January 2026  
February 2026  
March 2026

---

# 7. Age

`Age` represents the customer's age.

Age can be used to understand customer demographics.

Possible analysis:

- Average customer age
- Age distribution
- Customer behaviour by age group

Missing age values should be handled during data cleaning.

---

# 8. Gender

`Gender` identifies the recorded gender category of the customer.

It can be used for descriptive demographic analysis.

Examples:

- Male
- Female

The analysis should be based on the values actually available in the dataset.

---

# 9. City

`City` represents the customer's city.

Examples in the dataset include:

- Patna
- Delhi
- Mumbai
- Bengaluru
- Kolkata

City-level information can be used to understand geographic customer activity.

---

# 10. Region

`Region` groups customers geographically.

The dataset contains:

- North
- South
- East
- West

Regional analysis can compare:

- Customer count
- Orders
- Revenue
- Average Order Value
- Customer Satisfaction

---

# 11. Customer Segment

Customer segmentation groups customers into meaningful categories.

The Day 096 dataset contains:

- New
- Regular
- Loyal
- At Risk

### New

Customers who are relatively new to the business.

### Regular

Customers who show regular purchasing activity.

### Loyal

Customers who have an established relationship with the business.

### At Risk

Customers identified in the dataset as an At Risk segment.

These categories are used for analysis and comparison.

---

# 12. Product Category

`Product_Category` identifies the category associated with an order.

The dataset includes:

- Electronics
- Furniture
- Stationery
- Accessories

Product category analysis helps compare revenue, quantity, and orders across categories.

---

# 13. Quantity

`Quantity` represents the number of units purchased in an order.

Example:

If:

Quantity = 3

the transaction contains three units.

A negative quantity is treated as a data-quality issue.

---

# 14. Unit Price

`Unit_Price` represents the price associated with one unit.

Revenue can be calculated using:

**Revenue = Quantity × Unit Price**

Missing unit prices are handled during the cleaning stage using the category reference values documented in the workbook.

---

# 15. Revenue

Revenue represents the amount generated from an order.

The main formula used in this project is:

**Revenue = Quantity × Unit Price**

Revenue is one of the most important measures in customer analytics.

It can be analysed by:

- Customer
- Segment
- Product Category
- Region
- Month

---

# 16. Customer Satisfaction

`Customer_Satisfaction` represents the recorded satisfaction score.

It can be used to calculate:

- Average satisfaction
- Satisfaction by segment
- Satisfaction by region
- Satisfaction over time

Missing satisfaction values are handled during data cleaning.

---

# 17. Customer Status

`Customer_Status` describes the recorded status of the customer.

Examples include:

- Active
- Inactive

Active customer counts can be used as a customer activity KPI.

---

# 18. Payment Method

`Payment_Method` records how the transaction was paid.

Examples include:

- UPI
- Card
- Cash
- Net Banking

Payment methods can be analysed to understand transaction preferences.

---

# 19. Customer Data Inspection

Before analysing data, the dataset should be inspected.

Important checks include:

- Number of records
- Column names
- Data types
- Missing values
- Duplicate records
- Invalid values
- Inconsistent text
- Negative quantities
- Invalid dates

Inspection helps identify problems before calculations are performed.

---

# 20. Data Quality Issues

The raw customer dataset intentionally contains several issues for practice.

Examples include:

- Extra spaces
- Inconsistent capitalization
- Missing Unit Price
- Missing Quantity
- Missing Customer Satisfaction
- Missing Age
- Invalid Date
- Negative Quantity
- Invalid Revenue
- Duplicate records

These issues should be identified before analysis.

---

# 21. Data Cleaning

Data cleaning prepares the dataset for reliable analysis.

The Day 096 cleaning workflow includes:

1. Remove extra spaces
2. Standardise text values
3. Convert dates
4. Handle missing Age
5. Handle missing Quantity
6. Handle missing Unit Price
7. Correct negative Quantity
8. Handle missing Customer Satisfaction
9. Recalculate Revenue
10. Remove duplicate rows
11. Validate the cleaned data

---

# 22. Text Cleaning

Text fields may contain unnecessary spaces or inconsistent capitalization.

For example:

`" east "`  

can be cleaned to:

`"East"`

Similarly:

`" electronics "`  

can become:

`"Electronics"`

Standard text values make grouping and analysis more reliable.

---

# 23. Date Cleaning

Dates should be stored as valid date values.

The dataset contains an invalid date entry for practice.

The cleaning rule documented in the workbook is:

**Invalid date → median valid date**

This keeps the educational dataset usable for analysis.

---

# 24. Missing Value Handling

Missing values need to be handled before analysis.

The workbook uses documented practice rules.

Examples:

- Missing Age → median age
- Missing Quantity → 1
- Missing Unit Price → category reference price
- Missing Satisfaction → median satisfaction

The purpose is to demonstrate practical data-cleaning techniques.

---

# 25. Revenue Recalculation

Revenue is recalculated after cleaning.

Formula:

**Revenue = Quantity × Unit Price**

This ensures that Revenue is consistent with the cleaned Quantity and Unit Price values.

---

# 26. Duplicate Records

Duplicate records can result in double-counting.

The dataset contains an exact duplicate row for practice.

The cleaning process removes exact duplicate records.

This helps prevent incorrect:

- Order counts
- Revenue totals
- Customer analysis

---

# 27. Customer Summary

The `Customer_Summary` sheet provides an overall view of the customer dataset.

Important measures include:

- Total Customers
- Total Orders
- Total Revenue
- Average Customer Spend
- Average Order Value
- Average Customer Satisfaction
- Repeat Customers
- Repeat Customer Rate
- Active Customers

---

# 28. Total Customers

Total Customers means the number of unique customers.

Formula:

**Total Customers = Count of Unique Customer IDs**

A customer with multiple orders is still counted once.

---

# 29. Total Orders

Total Orders represents the number of cleaned transaction records.

Formula:

**Total Orders = Number of Transaction Records**

Orders and customers should not be treated as the same metric.

---

# 30. Total Revenue

Total Revenue is the sum of revenue across all cleaned transactions.

Formula:

**Total Revenue = SUM(Revenue)**

It represents the total revenue contained in the analysed dataset.

---

# 31. Average Customer Spend

Average Customer Spend measures the average revenue associated with each unique customer.

Formula:

**Average Customer Spend = Total Revenue / Total Customers**

This is different from Average Order Value.

---

# 32. Average Order Value

Average Order Value, or AOV, measures the average revenue generated per order.

Formula:

**AOV = Total Revenue / Total Orders**

Example:

If total revenue is ₹100,000 and there are 50 orders:

**AOV = ₹100,000 / 50 = ₹2,000**

---

# 33. Repeat Customers

A repeat customer is a customer with more than one order in the cleaned dataset.

For example:

Customer C001:

- Order 1
- Order 2
- Order 3

C001 is a repeat customer.

---

# 34. Repeat Customer Rate

Repeat Customer Rate measures the proportion of customers who have more than one order.

Formula:

**Repeat Customer Rate = Repeat Customers / Total Customers**

It can be expressed as a percentage.

---

# 35. Active Customers

Active Customers are customers associated with transactions whose recorded status is `Active`.

The metric is calculated using unique Customer IDs.

---

# 36. Customer Segment Analysis

The `Customer_Segment_Analysis` sheet compares customer groups.

Metrics include:

- Unique Customers
- Orders
- Revenue
- Average Order Value
- Average Satisfaction

Segments:

- New
- Regular
- Loyal
- At Risk

This helps identify differences in customer activity across segments.

---

# 37. Product Category Analysis

The `Product_Category_Analysis` sheet compares product categories.

Important measures include:

- Orders
- Quantity
- Revenue
- Average Order Value

Categories:

- Electronics
- Furniture
- Stationery
- Accessories

---

# 38. Region Analysis

The `Region_Analysis` sheet compares geographic customer activity.

Metrics include:

- Unique Customers
- Orders
- Revenue
- Average Order Value
- Average Satisfaction

Regions:

- North
- South
- East
- West

---

# 39. Monthly Customer Analysis

The `Monthly_Customer` sheet is used to study customer activity over time.

Metrics include:

- Unique Customers
- Orders
- Revenue
- Average Order Value
- Average Satisfaction

Monthly analysis can reveal changes and patterns over the available period.

---

# 40. Customer Spending Analysis

The `Customer_Spending_Analysis` sheet aggregates transactions at the customer level.

It contains:

- Customer ID
- Customer Name
- Customer Segment
- Orders
- Quantity
- Revenue
- Average Satisfaction
- Repeat Customer

This sheet is useful for understanding individual customer behaviour.

---

# 41. Customer KPIs

Key Customer Analytics KPIs include:

| KPI | Meaning |
|---|---|
| Total Customers | Number of unique customers |
| Active Customers | Unique customers with Active status |
| Total Revenue | Total customer revenue |
| Average Customer Spend | Revenue per customer |
| Average Order Value | Revenue per order |
| Total Orders | Number of transactions |
| Average Orders per Customer | Orders divided by customers |
| Repeat Customers | Customers with more than one order |
| Repeat Customer Rate | Repeat customers as a share of customers |
| Average Satisfaction | Average satisfaction score |

---

# 42. Pivot-Style Analysis

Pivot-style analysis summarises customer data into groups.

The workbook contains:

- `Pivot_Segment`
- `Pivot_Category`
- `Pivot_Region`

These summaries make it easier to compare groups without examining every transaction individually.

---

# 43. Customer Visualisation

Charts help communicate customer analytics results.

The workbook includes:

### Customer Count by Segment

Shows the number of customers associated with each segment.

### Revenue by Customer Segment

Compares revenue across customer segments.

### Revenue by Region

Compares revenue across geographic regions.

### Monthly Customer Revenue Trend

Shows how revenue changes over the available months.

---

# 44. Business Insights

Business insights are observations derived from analysed data.

Examples of questions:

- Which customer segment has more revenue?
- Which region has more revenue?
- Which product category has more orders?
- How many customers are repeat customers?
- What is the average customer spend?
- How does revenue change month by month?
- How does satisfaction differ across regions or segments?

Insights should be based on the calculated data.

---

# 45. Excel Functions for Customer Analytics

Useful Excel functions include:

### SUM

Used to calculate total revenue or quantity.

### AVERAGE

Used to calculate average satisfaction or price.

### COUNT

Used to count numerical records.

### COUNTA

Used to count non-empty records.

### COUNTIF

Used to count records matching a condition.

### COUNTIFS

Used for multiple conditions.

### SUMIF

Used to calculate totals based on a condition.

### SUMIFS

Used to calculate totals using multiple conditions.

### AVERAGEIF

Used to calculate averages based on a condition.

### IF

Used to create conditional classifications.

---

# 46. Useful Customer Analytics Formulas

### Revenue

**Quantity × Unit Price**

### Average Customer Spend

**Total Revenue / Total Customers**

### Average Order Value

**Total Revenue / Total Orders**

### Repeat Customer Rate

**Repeat Customers / Total Customers**

### Average Orders per Customer

**Total Orders / Total Customers**

---

# 47. Customer Analytics Workflow

The complete workflow is:

**Raw Customer Data**

↓

**Data Inspection**

↓

**Data Quality Check**

↓

**Data Cleaning**

↓

**Validation**

↓

**Customer Analysis**

↓

**Segmentation**

↓

**Spending Analysis**

↓

**Category Analysis**

↓

**Regional Analysis**

↓

**Monthly Analysis**

↓

**KPI Calculation**

↓

**Visualisation**

↓

**Business Insights**

---

# 48. Important Distinctions

### Customer vs Order

A customer can place multiple orders.

Therefore:

**Unique Customers ≠ Total Orders**

### Customer Spend vs Order Value

Customer Spend is calculated per unique customer.

Order Value is calculated per order.

### Raw Data vs Cleaned Data

Raw data may contain errors.

Cleaned data is prepared for analysis after applying documented cleaning rules.

---

# 49. Questions for Revision

1. What is Customer Analytics?
2. What is the difference between a customer and an order?
3. Why is Customer ID important?
4. What is customer segmentation?
5. What are the four segments used in this dataset?
6. What is Total Revenue?
7. What is Average Customer Spend?
8. What is Average Order Value?
9. What is a repeat customer?
10. How is Repeat Customer Rate calculated?
11. Why should duplicate records be removed?
12. Why should text values be standardised?
13. How can missing values be handled?
14. Why is Revenue recalculated after cleaning?
15. What is regional customer analysis?
16. What is monthly customer analysis?
17. What are Customer KPIs?
18. Why are Pivot-style summaries useful?
19. Why are charts useful in customer analytics?
20. How can customer data be converted into business insights?

---

# 50. Key Learning Points

- Customer Analytics focuses on understanding customer behaviour.
- Customer ID is useful for unique customer analysis.
- One customer can have multiple orders.
- Data quality should be checked before analysis.
- Missing and invalid values need documented cleaning rules.
- Revenue can be calculated from Quantity and Unit Price.
- Customer segmentation helps compare customer groups.
- Spending analysis can be performed at customer level.
- Product category analysis compares customer purchases across categories.
- Regional analysis helps understand geographic patterns.
- Monthly analysis helps identify changes over time.
- KPIs provide a concise summary of customer activity.
- Pivot-style summaries simplify group-level analysis.
- Charts make customer patterns easier to communicate.
- Business insights should be supported by the analysed data.

---

# 51. Summary

Day 096 focuses on **Customer Analytics** using Excel.

The main process is:

**Understand → Inspect → Clean → Validate → Analyse → Segment → Calculate KPIs → Visualise → Interpret**

The goal is to understand how customer data can be transformed into structured business information and useful analytical insights.

---

# 🔑 Final Takeaway

> **Customer Analytics uses customer and transaction data to understand customer behaviour, spending, segments, products, regions, and activity over time.**

---

**Day 096 — Customer Analytics**  
**IIT Madras BS Degree — Diploma Level**  
**Author: Saloni Tiwari**