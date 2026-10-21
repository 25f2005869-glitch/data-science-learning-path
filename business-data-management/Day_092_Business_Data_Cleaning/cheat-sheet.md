# 🧹 Day 092 — Business Data Cleaning — Cheat Sheet

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Diploma Level](https://img.shields.io/badge/Level-Diploma-blue?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Subject-BDM-green?style=for-the-badge)
![Data Cleaning](https://img.shields.io/badge/Topic-Data%20Cleaning-orange?style=for-the-badge)
![Day 092](https://img.shields.io/badge/Day-092-purple?style=for-the-badge)

---

## 👤 Metadata

| Field | Details |
|---|---|
| **Author** | Saloni Tiwari |
| **Programme** | IIT Madras BS Degree — Diploma Level |
| **Day** | 092 |
| **Topic** | Business Data Cleaning |

---

# 📌 1. Data Cleaning Workflow

**Inspect → Identify → Clean → Validate → Analyse**

### Quick Flow

**Raw Data**

→ Check quality

→ Find problems

→ Clean data

→ Validate

→ Create analysis-ready data

→ Analyse

---

# 🔍 2. Data Quality Checklist

Check these before analysis:

- [ ] Missing values
- [ ] Duplicate records
- [ ] Duplicate rows
- [ ] Extra spaces
- [ ] Inconsistent text
- [ ] Invalid dates
- [ ] Incorrect data types
- [ ] Invalid numeric values
- [ ] Negative values
- [ ] Outliers
- [ ] Incorrect formats

---

# 🕳️ 3. Missing Values

### Common examples

- Blank Cost
- Blank Customer Satisfaction
- Blank Email
- Blank Date

### Possible actions

- Leave blank
- Replace with an appropriate value
- Calculate from other information
- Flag for review
- Remove when justified

**Remember:** Do not automatically replace every missing value.

---

# ♻️ 4. Duplicate Records

### Check

- Record ID
- Full row
- Relevant identifying columns

### Problems caused by duplicates

- Incorrect totals
- Double counting
- Incorrect averages
- Incorrect KPIs

**Rule:** Remove only genuine duplicates.

---

# 🧹 5. Text Cleaning

### Common problems

`Sales`

`sales`

` SALES `

These may represent the same category.

### Useful functions

| Function | Use |
|---|---|
| `TRIM()` | Remove unnecessary spaces |
| `UPPER()` | Convert to uppercase |
| `LOWER()` | Convert to lowercase |
| `LEFT()` | Extract from left |
| `RIGHT()` | Extract from right |
| `MID()` | Extract from middle |
| `LEN()` | Count characters |

---

# ✂️ 6. TRIM Function

Use:

`=TRIM(A2)`

Purpose:

- Removes unnecessary spaces
- Helps standardise text
- Improves grouping and filtering

Example:

`" Sales "` → `"Sales"`

---

# 🔤 7. Text Standardisation

### Business Function

Use consistent values such as:

- Sales
- Operations
- Customer Service
- Marketing

### Region

Use:

- North
- South
- East
- West

### Product Category

Use:

- Electronics
- Clothing
- Home
- Grocery

### Status

Use consistent values such as:

- Completed
- Pending
- Returned
- Cancelled

---

# 📅 8. Date Cleaning

### Check for

- Different date formats
- Invalid dates
- Blank dates
- Dates stored as text

### Useful functions

`=TODAY()`

`=YEAR(A2)`

`=MONTH(A2)`

`=DAY(A2)`

### Goal

Create consistent, valid dates for:

- Daily analysis
- Monthly analysis
- Yearly analysis
- Trend analysis

---

# 🔢 9. Numeric Data Cleaning

Check fields such as:

- Orders
- Revenue
- Cost
- Returned Orders
- Customer Satisfaction

### Look for

- Numbers stored as text
- Blank values
- Invalid text
- Negative values
- Incorrect formats

---

# 💰 10. Currency Cleaning

A value such as:

`1,25,000`

may need to be converted into a proper numeric value before calculations.

Correct numeric data is required for:

- SUM
- AVERAGE
- Sorting
- Charts
- KPI calculations

---

# ⚠️ 11. Negative Values

Investigate negative values in fields such as:

- Orders
- Returned Orders
- Cost

A negative value may be:

- Data-entry error
- Adjustment
- Refund
- Accounting value
- Business-specific value

**Never delete it automatically.**

---

# 📧 12. Email Cleaning

Check for:

- Extra spaces
- Inconsistent formatting
- Obvious spacing problems

Example:

`neha.verma @example.com`

Basic cleaning:

`neha.verma@example.com`

---

# 📊 13. Outlier Checklist

An outlier is an unusually high or low value.

### When an outlier is found:

1. Identify it.
2. Check the original record.
3. Check whether it is possible.
4. Look for data-entry errors.
5. Check formatting or units.
6. Investigate the business context.
7. Decide whether to retain, correct or flag it.

**Outlier ≠ automatically incorrect data**

---

# 📋 14. Cleaning Log

Record important cleaning decisions.

| Field | Purpose |
|---|---|
| Issue ID | Identify issue |
| Column | Location |
| Issue Found | Problem |
| Cleaning Action | Action taken |
| Reason | Why it was done |
| Result | Outcome |
| Notes | Additional information |

---

# ✅ 15. Validation

After cleaning, check:

- Record IDs are not blank
- Orders are not negative
- Cost is not negative
- Returned Orders are not negative
- Customer Satisfaction is within a reasonable range
- Text categories are standardised
- Dates are valid
- Duplicate records are handled

---

# 🧮 16. Useful Excel Checks

### Count blanks

`=COUNTBLANK(A2:A100)`

### Count duplicates

Use:

**Conditional Formatting → Duplicate Values**

or compare IDs using:

`COUNTIF()`

### Count negative values

`=COUNTIF(A2:A100,"<0")`

### Count values above a limit

`=COUNTIF(A2:A100,">100")`

---

# 🔎 17. Find and Replace

Useful for repeated text corrections.

Example:

`Customer service`

→

`Customer Service`

Use:

**Find and Replace**

Always review the replacement before applying it to the complete dataset.

---

# 🎨 18. Conditional Formatting for Cleaning

Useful for highlighting:

- Blank values
- Duplicate values
- Negative values
- High values
- Low values
- Unusual values

This makes data-quality problems easier to identify.

---

# 📊 19. Before vs After

| Area | Before | After |
|---|---|---|
| Text | Inconsistent | Standardised |
| Dates | Mixed / invalid | Consistent where possible |
| Numbers | Text / invalid | Cleaned or flagged |
| Duplicates | Present | Handled |
| Emails | Extra spaces | Cleaned |
| Status | Mixed formatting | Standardised |
| Outliers | Unusual values | Investigated |

---

# 📈 20. Analysis-Ready Data

A clean dataset should have:

- Consistent column names
- Consistent categories
- Valid dates
- Appropriate numeric values
- Duplicates handled
- Missing values identified or handled
- Unusual values investigated
- Correct formats

---

# 🛠️ 21. Excel Data Cleaning Tools

| Tool | Main Use |
|---|---|
| Sort | Arrange and inspect data |
| Filter | Display selected records |
| Remove Duplicates | Handle duplicate records |
| Find & Replace | Correct repeated text |
| TRIM | Remove extra spaces |
| Conditional Formatting | Highlight problems |
| Data Validation | Control allowed values |
| Excel Tables | Organise structured data |
| Formulas | Calculate and check values |

---

# 🧠 22. Important Functions

### Text

`TRIM()`

`UPPER()`

`LOWER()`

`LEFT()`

`RIGHT()`

`MID()`

`LEN()`

### Date

`TODAY()`

`YEAR()`

`MONTH()`

`DAY()`

### Checking

`COUNTBLANK()`

`COUNTIF()`

---

# 💼 23. Business Data Fields

Important Day 092 fields include:

- Record ID
- Date
- Customer Name
- Business Function
- Region
- Product Category
- Orders
- Revenue
- Cost
- Returned Orders
- Customer Satisfaction
- Email
- Status

---

# 📊 24. Cleaning Summary

Track:

- Raw record count
- Cleaned record count
- Rows removed
- Columns
- Missing values
- Duplicates
- Invalid values
- Outliers
- Validation results

---

# 🚨 25. Common Mistakes

### ❌ Do not:

- Delete all blanks
- Delete all outliers
- Change values without checking
- Remove records without understanding them
- Ignore inconsistent categories
- Analyse before checking data quality

### ✅ Do:

- Inspect first
- Document important changes
- Validate after cleaning
- Keep the original raw data
- Investigate unusual values

---

# 🗂️ 26. Day 092 Workbook

Main file:

`Day_092_Business_Data_Cleaning.xlsx`

Important sheets:

- `Instructions`
- `Raw_Business_Data`
- `Data_Quality_Check`
- `Cleaning_Practice`
- `Cleaning_Log`
- `Cleaned_Business_Data`
- `Before_After`
- `Validation`
- `Cleaning_Summary`
- `Cleaned_Analysis`
- `Cleaning_Charts`

---

# 🔄 27. Quick Cleaning Process

**1. Inspect**

↓

**2. Find Missing Values**

↓

**3. Find Duplicates**

↓

**4. Clean Text**

↓

**5. Clean Dates**

↓

**6. Clean Numbers**

↓

**7. Investigate Outliers**

↓

**8. Validate**

↓

**9. Create Clean Dataset**

↓

**10. Analyse**

---

# 🎯 28. One-Line Revision

**Data Cleaning = Identify Problems + Apply Appropriate Cleaning + Validate the Result**

---

# 📌 29. Must Remember

> **Never change data blindly. First understand the problem, then apply the appropriate cleaning action.**

**Raw Data → Clean Data → Reliable Analysis**