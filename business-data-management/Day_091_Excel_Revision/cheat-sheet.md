# 🧾 Day 091 — Excel Revision — Cheat Sheet

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

# 📌 1. Excel Basics

| Concept | Meaning |
|---|---|
| Workbook | Complete Excel file |
| Worksheet | Individual sheet |
| Cell | Single data location |
| Row | Horizontal collection of cells |
| Column | Vertical collection of cells |
| Range | Group of cells |
| Formula | Calculation written by the user |
| Function | Predefined Excel calculation |

Example cell:

`A1`

Example range:

`A1:C10`

---

# ➕ 2. Basic Operators

| Operator | Operation |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `()` | Controls calculation order |

Examples:

`=A2+B2`

`=A2-B2`

`=A2*B2`

`=A2/B2`

`=(A2+B2)*C2`

---

# 🔗 3. Cell References

### Relative Reference

`A1`

Changes when the formula is copied.

### Absolute Reference

`$A$1`

Remains fixed when the formula is copied.

### Mixed Reference

`$A1`

`A$1`

One part remains fixed.

---

# 🧮 4. Common Functions

| Function | Purpose | Example |
|---|---|---|
| `SUM()` | Total | `=SUM(A2:A10)` |
| `AVERAGE()` | Average | `=AVERAGE(A2:A10)` |
| `COUNT()` | Count numbers | `=COUNT(A2:A10)` |
| `COUNTA()` | Count non-empty cells | `=COUNTA(A2:A10)` |
| `MIN()` | Smallest value | `=MIN(A2:A10)` |
| `MAX()` | Largest value | `=MAX(A2:A10)` |

---

# 🧠 5. Logical Functions

### IF

`=IF(A2>=50,"Pass","Fail")`

### AND

`=AND(A2>=50,B2>=50)`

### OR

`=OR(A2>=50,B2>=50)`

### NOT

`=NOT(A2>50)`

---

# 📊 6. Conditional Functions

| Function | Purpose |
|---|---|
| `COUNTIF()` | Count values matching a condition |
| `SUMIF()` | Sum values matching a condition |
| `AVERAGEIF()` | Average values matching a condition |

Examples:

`=COUNTIF(A2:A20,"Sales")`

`=SUMIF(A2:A20,"Sales",B2:B20)`

`=AVERAGEIF(A2:A20,"Sales",B2:B20)`

---

# 🔤 7. Text Functions

| Function | Purpose |
|---|---|
| `LEFT()` | Characters from left |
| `RIGHT()` | Characters from right |
| `MID()` | Characters from middle |
| `LEN()` | Number of characters |
| `TRIM()` | Removes extra spaces |
| `UPPER()` | Converts to uppercase |
| `LOWER()` | Converts to lowercase |

Examples:

`=LEFT(A2,3)`

`=RIGHT(A2,3)`

`=MID(A2,2,4)`

`=LEN(A2)`

`=TRIM(A2)`

`=UPPER(A2)`

`=LOWER(A2)`

---

# 📅 8. Date Functions

| Function | Purpose |
|---|---|
| `TODAY()` | Current date |
| `YEAR()` | Extract year |
| `MONTH()` | Extract month |
| `DAY()` | Extract day |

Examples:

`=TODAY()`

`=YEAR(A2)`

`=MONTH(A2)`

`=DAY(A2)`

---

# 🔎 9. Lookup Functions

### VLOOKUP

Used to search for a value in a table and return related information.

Common uses:

- Product lookup
- Customer lookup
- Price lookup
- Category lookup

### XLOOKUP

Used to search for a value and return the corresponding result.

Useful for structured business datasets.

---

# 🔃 10. Sorting

Use sorting to arrange data.

Common options:

- Smallest to Largest
- Largest to Smallest
- A to Z
- Z to A
- Oldest to Newest
- Newest to Oldest

Useful for finding:

- Highest revenue
- Lowest profit
- Best-performing category
- Recent records

---

# 🔍 11. Filtering

Filtering displays only records matching selected conditions.

Examples:

- Business Function = Sales
- Region = North
- Orders > 100
- Customer Satisfaction > 80%

---

# 🧹 12. Data Cleaning Checklist

Before analysis:

- Remove duplicates
- Check blank values
- Remove unnecessary spaces
- Standardise text
- Check dates
- Check numeric values
- Check percentage formats
- Check inconsistent categories
- Verify calculations

---

# 📋 13. Excel Tables

Excel Tables provide:

- Structured data
- Automatic filtering
- Automatic expansion
- Better formatting
- Structured references

Tables are useful for business datasets that grow over time.

---

# 🎨 14. Conditional Formatting

Useful rules include:

- Highlight cells greater than a value
- Highlight cells less than a value
- Duplicate values
- Data bars
- Colour scales
- Top/bottom values

Use conditional formatting to quickly identify important patterns.

---

# 💰 15. Business KPI Formulas

### Profit

`Profit = Revenue - Cost`

### Average Order Value

`AOV = Revenue / Orders`

### Cost per Order

`Cost per Order = Cost / Orders`

### Profit Margin

`Profit Margin = Profit / Revenue × 100`

### Return Rate

`Return Rate = Returned Orders / Orders × 100`

### On-Time Delivery Rate

`On-Time Delivery Rate = On-Time Deliveries / Deliveries × 100`

---

# 📊 16. Important Business Metrics

| Metric | What It Shows |
|---|---|
| Orders | Sales/order volume |
| Revenue | Money generated |
| Cost | Business expenditure |
| Profit | Revenue after cost |
| AOV | Average revenue per order |
| Profit Margin | Profit percentage |
| Return Rate | Returned-order proportion |
| On-Time Rate | Delivery performance |
| Customer Satisfaction | Customer experience |

---

# 🔄 17. Business Analysis Workflow

**Raw Data**

↓

**Data Review**

↓

**Data Cleaning**

↓

**Calculations**

↓

**KPI Analysis**

↓

**Summary**

↓

**Charts**

↓

**Dashboard**

↓

**Business Insights**

---

# 📑 18. Summary Analysis

Useful summary dimensions:

- Business Function
- Process
- Region
- Month

Useful summary metrics:

- Total Orders
- Total Revenue
- Total Cost
- Total Profit
- Average Order Value
- Return Rate
- On-Time Delivery Rate
- Customer Satisfaction

---

# 📈 19. Chart Selection

| Chart | Best Use |
|---|---|
| Column | Category comparison |
| Bar | Category comparison/ranking |
| Line | Time trends |
| Pie | Part-to-whole |
| Doughnut | Part-to-whole |
| Area | Trend + volume |
| Scatter | Relationship between variables |
| Radar | Multiple metric comparison |

---

# 📊 20. Dashboard Checklist

A business dashboard can contain:

- KPI cards
- Revenue summary
- Profit summary
- Trend charts
- Category comparisons
- Regional analysis
- Business observations

Keep the dashboard:

- Clear
- Simple
- Relevant
- Easy to read

---

# ⚠️ 21. Common Excel Mistakes

Check for:

- Wrong cell reference
- Wrong range
- Missing parentheses
- Incorrect data type
- Duplicate records
- Extra spaces
- Incorrect date format
- Incorrect lookup range
- Wrong percentage calculation
- Misleading chart selection

---

# 🚀 22. Quick Revision Workflow

**Step 1:** Open the workbook

**Step 2:** Review the data

**Step 3:** Clean the data

**Step 4:** Practise formulas

**Step 5:** Practise functions

**Step 6:** Apply logical and conditional functions

**Step 7:** Sort and filter

**Step 8:** Practise lookups

**Step 9:** Calculate KPIs

**Step 10:** Create summaries

**Step 11:** Create charts

**Step 12:** Build the dashboard

**Step 13:** Write business observations

---

# 🧠 23. Must-Remember Functions

`SUM()`

`AVERAGE()`

`COUNT()`

`COUNTA()`

`MIN()`

`MAX()`

`IF()`

`AND()`

`OR()`

`NOT()`

`COUNTIF()`

`SUMIF()`

`AVERAGEIF()`

`LEFT()`

`RIGHT()`

`MID()`

`LEN()`

`TRIM()`

`UPPER()`

`LOWER()`

`TODAY()`

`YEAR()`

`MONTH()`

`DAY()`

`VLOOKUP()`

`XLOOKUP()`

---

# 🎯 24. Final Revision Formula

**Excel Analysis = Clean Data + Correct Formulas + Useful Functions + KPIs + Summaries + Visualisation**

---

## ✅ Day 091 Quick Checklist

- [ ] Excel Basics
- [ ] Formulas
- [ ] Cell References
- [ ] Common Functions
- [ ] Logical Functions
- [ ] Conditional Functions
- [ ] Sorting
- [ ] Filtering
- [ ] Data Cleaning
- [ ] Text Functions
- [ ] Date Functions
- [ ] Lookup Functions
- [ ] Excel Tables
- [ ] Conditional Formatting
- [ ] Business KPIs
- [ ] Summary Analysis
- [ ] Column Chart
- [ ] Bar Chart
- [ ] Line Chart
- [ ] Pie Chart
- [ ] Doughnut Chart
- [ ] Area Chart
- [ ] Scatter Chart
- [ ] Radar Chart
- [ ] Dashboard
- [ ] Final Excel Project

---

## 📌 Key Takeaway

**Use Excel to move from raw business data to meaningful analysis:**

**Data → Clean → Calculate → Summarise → Visualise → Understand**