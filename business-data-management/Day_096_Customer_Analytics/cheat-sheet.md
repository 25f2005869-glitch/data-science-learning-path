# 📊 Day 096 — Customer Analytics — Cheat Sheet

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

# 1. Customer Analytics

Customer Analytics means analysing customer and transaction data to understand:

- Customer behaviour
- Customer spending
- Customer segments
- Product preferences
- Regional activity
- Customer activity over time

---

# 2. Main Customer Fields

| Field | Meaning |
|---|---|
| Order_ID | Identifies a transaction |
| Date | Transaction date |
| Customer_ID | Identifies a customer |
| Customer_Name | Customer name |
| Age | Customer age |
| Gender | Recorded gender category |
| City | Customer city |
| Region | Geographic region |
| Customer_Segment | Customer group |
| Product_Category | Product category |
| Quantity | Units purchased |
| Unit_Price | Price per unit |
| Revenue | Transaction revenue |
| Customer_Satisfaction | Satisfaction score |
| Customer_Status | Customer status |
| Payment_Method | Payment method |

---

# 3. Customer Segments

The dataset uses:

- **New**
- **Regular**
- **Loyal**
- **At Risk**

Use segmentation to compare customer activity and revenue.

---

# 4. Basic Revenue Formula

**Revenue = Quantity × Unit Price**

Example:

Quantity = 3  
Unit Price = ₹1,000

Revenue:

**3 × ₹1,000 = ₹3,000**

---

# 5. Key Customer Metrics

### Total Customers

**Count of Unique Customer IDs**

### Total Orders

**Number of Transaction Records**

### Total Revenue

**SUM(Revenue)**

### Average Customer Spend

**Total Revenue / Total Customers**

### Average Order Value

**Total Revenue / Total Orders**

### Average Orders per Customer

**Total Orders / Total Customers**

---

# 6. Repeat Customers

A repeat customer has more than one order.

Example:

C001 → 3 orders

Therefore:

**C001 = Repeat Customer**

---

# 7. Repeat Customer Rate

**Repeat Customer Rate = Repeat Customers / Total Customers**

To express as a percentage:

**Repeat Customer Rate × 100**

---

# 8. Active Customers

Active Customers are unique customers whose recorded status is:

**Active**

Count unique Customer IDs rather than transaction rows.

---

# 9. Customer Satisfaction

Use `Customer_Satisfaction` to calculate:

- Average satisfaction
- Satisfaction by segment
- Satisfaction by region
- Monthly satisfaction

---

# 10. Data Quality Checks

Check for:

- Missing values
- Extra spaces
- Inconsistent capitalization
- Invalid dates
- Negative quantities
- Invalid revenue
- Duplicate records

---

# 11. Cleaning Checklist

### Text

Remove extra spaces.

**Example:**

`" east "` → `East`

### Capitalization

Standardise labels.

`" electronics "` → `Electronics`

### Date

Convert to valid date format.

### Age

Missing Age → median age.

### Quantity

Missing or negative Quantity → `1`.

### Unit Price

Missing Unit Price → category reference price.

### Satisfaction

Missing Satisfaction → median satisfaction.

### Revenue

Recalculate:

**Revenue = Quantity × Unit Price**

### Duplicates

Remove exact duplicate records.

---

# 12. Customer Analysis

Analyse customers using:

- Customer ID
- Customer Segment
- Orders
- Quantity
- Revenue
- Satisfaction
- Repeat Customer

---

# 13. Segment Analysis

Compare:

| Metric | Use |
|---|---|
| Unique Customers | Customer base |
| Orders | Transaction activity |
| Revenue | Revenue contribution |
| Average Order Value | Average order size |
| Average Satisfaction | Customer experience measure |

---

# 14. Product Category Analysis

Categories in the dataset:

- Electronics
- Furniture
- Stationery
- Accessories

Analyse:

- Orders
- Quantity
- Revenue
- Average Order Value

---

# 15. Regional Analysis

Regions:

- North
- South
- East
- West

Analyse:

- Unique Customers
- Orders
- Revenue
- Average Order Value
- Average Satisfaction

---

# 16. Monthly Analysis

Analyse each month using:

- Unique Customers
- Orders
- Revenue
- Average Order Value
- Average Satisfaction

Monthly analysis helps identify changes over time.

---

# 17. Customer Spending Analysis

Customer-level analysis includes:

- Customer ID
- Customer Name
- Customer Segment
- Orders
- Quantity
- Revenue
- Average Satisfaction
- Repeat Customer

---

# 18. Customer KPIs

| KPI | Formula / Meaning |
|---|---|
| Total Customers | Unique Customer IDs |
| Active Customers | Unique active customers |
| Total Revenue | SUM(Revenue) |
| Average Customer Spend | Revenue ÷ Customers |
| Average Order Value | Revenue ÷ Orders |
| Total Orders | Transaction records |
| Average Orders per Customer | Orders ÷ Customers |
| Repeat Customers | Customers with >1 order |
| Repeat Customer Rate | Repeat Customers ÷ Customers |
| Average Satisfaction | AVERAGE(Satisfaction) |

---

# 19. Important Excel Functions

### SUM

`=SUM(range)`

Total revenue or quantity.

### AVERAGE

`=AVERAGE(range)`

Average satisfaction or price.

### COUNT

`=COUNT(range)`

Counts numerical values.

### COUNTA

`=COUNTA(range)`

Counts non-empty cells.

### COUNTIF

`=COUNTIF(range,criteria)`

Counts values matching one condition.

### COUNTIFS

`=COUNTIFS(range1,criteria1,range2,criteria2)`

Counts using multiple conditions.

### SUMIF

`=SUMIF(range,criteria,sum_range)`

Adds values matching a condition.

### SUMIFS

`=SUMIFS(sum_range,range1,criteria1)`

Adds values using conditions.

### AVERAGEIF

`=AVERAGEIF(range,criteria,average_range)`

Calculates a conditional average.

### IF

`=IF(condition,value_if_true,value_if_false)`

Creates conditional results.

---

# 20. Pivot-Style Analysis

Useful grouping dimensions:

- Customer Segment
- Product Category
- Region

Useful values:

- Customer Count
- Orders
- Quantity
- Revenue
- Average Satisfaction

---

# 21. Charts

Day 096 includes:

### Customer Count by Segment

Shows customer distribution across segments.

### Revenue by Customer Segment

Compares revenue across segments.

### Revenue by Region

Compares regional revenue.

### Monthly Customer Revenue Trend

Shows revenue changes over time.

---

# 22. Business Questions

Ask:

- How many unique customers are there?
- How many customers are active?
- How many are repeat customers?
- What is the average customer spend?
- What is the average order value?
- Which segment has higher revenue?
- Which category has higher revenue?
- Which region has higher revenue?
- How does revenue change monthly?
- What is the average satisfaction?

---

# 23. Customer Analytics Workflow

**Raw Data**

↓

**Inspect**

↓

**Data Quality Check**

↓

**Clean**

↓

**Validate**

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

**KPI Analysis**

↓

**Visualisation**

↓

**Business Insights**

---

# 24. Important Distinctions

### Customer vs Order

One customer can have multiple orders.

**Unique Customers ≠ Total Orders**

### Customer Spend vs AOV

**Customer Spend**

Revenue per unique customer.

**AOV**

Revenue per order.

### Raw vs Cleaned Data

**Raw Data**

May contain errors and inconsistencies.

**Cleaned Data**

Prepared for analysis after applying cleaning rules.

---

# 25. Quick Formula Revision

**Revenue**

`Quantity × Unit Price`

**Average Customer Spend**

`Total Revenue ÷ Total Customers`

**Average Order Value**

`Total Revenue ÷ Total Orders`

**Average Orders per Customer**

`Total Orders ÷ Total Customers`

**Repeat Customer Rate**

`Repeat Customers ÷ Total Customers`

---

# 26. Workbook Sheets

- `Instructions`
- `Raw_Customer_Data`
- `Data_Quality_Check`
- `Customer_Cleaning`
- `Cleaned_Customer_Data`
- `Customer_Summary`
- `Customer_Segment_Analysis`
- `Product_Category_Analysis`
- `Region_Analysis`
- `Monthly_Customer`
- `Customer_Spending_Analysis`
- `Customer_KPI`
- `Pivot_Segment`
- `Pivot_Category`
- `Pivot_Region`
- `Chart_Data`
- `Charts`
- `Customer_Insights`
- `Final_Customer_Analysis`

---

# 27. Quick Revision

### Remember:

**Customer Analytics = Customer Data + Cleaning + Segmentation + Spending + KPIs + Visualisation**

**Revenue = Quantity × Unit Price**

**AOV = Revenue ÷ Orders**

**Average Customer Spend = Revenue ÷ Customers**

**Repeat Rate = Repeat Customers ÷ Customers**

**Customer Analysis → Segment → KPI → Chart → Insight**

---

## 🔑 Key Takeaway

> **Customer Analytics helps analyse customer behaviour, spending, segments, products, regions, and activity over time using structured business data.**

---

**Day 096 — Customer Analytics**  
**IIT Madras BS Degree — Diploma Level**  
**Author: Saloni Tiwari**