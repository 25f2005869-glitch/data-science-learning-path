# 🧹 Day 092 — Business Data Cleaning

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

## 📖 Overview

Day 092 focuses on **Business Data Cleaning**.

Business datasets often contain missing values, duplicate records, inconsistent text, invalid dates, incorrect numeric values and other quality problems.

Before performing business analysis, the data should be checked and prepared carefully.

The main workflow for Day 092 is:

**Inspect → Identify Issues → Clean → Validate → Compare → Analyse**

---

## 🎯 Learning Objectives

By the end of Day 092, the learner should be able to:

- Understand data quality.
- Inspect a raw business dataset.
- Identify common data-quality problems.
- Find missing values.
- Detect duplicate records.
- Standardise text values.
- Clean unnecessary spaces.
- Check date values.
- Check numeric values.
- Identify invalid values.
- Investigate outliers.
- Maintain a cleaning log.
- Validate cleaned data.
- Compare data before and after cleaning.
- Prepare an analysis-ready dataset.
- Perform basic analysis on cleaned business data.

---

## 🧠 Topics Covered

### 1. Understanding Raw Data

- Dataset structure
- Columns and rows
- Data types
- Business fields
- Data quality inspection

### 2. Missing Values

- Identifying blank values
- Understanding missing information
- Deciding whether to retain, replace or flag values

### 3. Duplicate Records

- Duplicate IDs
- Duplicate rows
- Identifying genuine duplicates
- Removing exact duplicate records

### 4. Text Cleaning

- Extra spaces
- Inconsistent capitalization
- Inconsistent category names
- Standardising labels

### 5. Date Cleaning

- Different date formats
- Invalid dates
- Converting dates into a consistent format

### 6. Numeric Cleaning

- Numbers stored as text
- Blank numeric values
- Invalid numeric values
- Negative values where inappropriate
- Currency values

### 7. Email Cleaning

- Extra spaces
- Inconsistent formatting
- Basic consistency checks

### 8. Status Cleaning

- Extra spaces
- Different capitalization
- Standardising status values

### 9. Outlier Investigation

An unusually high or low value should be investigated before changing or removing it.

Outliers should not automatically be deleted.

---

## 📊 Business Dataset

The workbook contains a deliberately messy **synthetic business dataset**.

Important fields include:

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

The dataset contains intentionally introduced data-quality issues for practice.

---

## ⚠️ Data Quality Issues Included

The raw dataset provides examples of:

- Missing values
- Duplicate records
- Duplicate rows
- Extra spaces
- Mixed capitalization
- Inconsistent category labels
- Invalid dates
- Numeric values stored as text
- Invalid numeric values
- Negative values
- Email spacing issues
- Status formatting issues
- Extreme revenue values

---

## 🧹 Cleaning Workflow

### Step 1 — Inspect

Understand the dataset before changing anything.

### Step 2 — Identify Issues

Find:

- Missing values
- Duplicates
- Incorrect formats
- Invalid values
- Inconsistent text
- Possible outliers

### Step 3 — Clean

Apply appropriate cleaning actions.

### Step 4 — Validate

Check whether the cleaned data satisfies basic quality rules.

### Step 5 — Compare

Compare the dataset before and after cleaning.

### Step 6 — Analyse

Use the cleaned dataset for business analysis.

---

## 📋 Cleaning Log

The `Cleaning_Log` sheet is used to document important cleaning decisions.

A cleaning log can contain:

- Issue ID
- Column
- Issue Found
- Cleaning Action
- Reason
- Result
- Notes

Maintaining a cleaning log makes the cleaning process easier to understand and reproduce.

---

## 🔍 Data Validation

The `Validation` sheet provides checks for conditions such as:

- Blank Record IDs
- Negative Orders
- Negative Cost
- Negative Returned Orders
- Customer Satisfaction below 0
- Customer Satisfaction above 100

Validation helps confirm that the cleaned dataset is suitable for further analysis.

---

## 📊 Before vs After Cleaning

The `Before_After` sheet compares common quality areas.

| Quality Area | Before Cleaning | After Cleaning |
|---|---|---|
| Text labels | Mixed casing and spaces | Standardised |
| Dates | Mixed formats / invalid text | Consistent valid dates where possible |
| Numeric values | Text, blanks or invalid values | Cleaned or flagged |
| Duplicates | Repeated records | Exact duplicate rows removed |
| Emails | Extra spaces | Spaces removed |
| Status | Mixed formatting | Standardised |
| Outliers | Extreme value present | Flagged for investigation |

---

## 📈 Analysis After Cleaning

Once the data has been cleaned, it can be used for business analysis.

The workbook includes analysis by:

- Business Function
- Orders
- Revenue
- Cost
- Profit
- Customer Satisfaction

The cleaned data can therefore be used as the foundation for later business analysis.

---

## 📊 Charts

The `Cleaning_Charts` sheet contains charts based on the cleaned business data.

Charts include:

- Revenue by Business Function
- Profit by Business Function

These charts demonstrate how cleaned data can be converted into visual business information.

---

## 🗂️ Workbook Structure

The Day 092 Excel workbook contains:

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

## 📚 Practical Exercise

Use the workbook to practise the following:

1. Inspect the raw dataset.
2. Identify data-quality issues.
3. Find duplicates.
4. Find missing values.
5. Clean text values.
6. Standardise categories.
7. Clean dates.
8. Clean numeric fields.
9. Clean email values.
10. Standardise status values.
11. Investigate the revenue outlier.
12. Record cleaning actions.
13. Validate the cleaned dataset.
14. Compare before and after cleaning.
15. Analyse the cleaned dataset.
16. Review the charts.

---

## 🚀 Business Data Cleaning Workflow

**Raw Business Data**

↓

**Data Quality Check**

↓

**Cleaning Practice**

↓

**Cleaning Log**

↓

**Cleaned Business Data**

↓

**Validation**

↓

**Before vs After**

↓

**Business Analysis**

↓

**Charts**

---

## 🧮 Analysis-Ready Data

A dataset should generally be checked for:

- Correct column names
- Consistent categories
- Valid dates
- Valid numeric values
- Appropriate missing-value handling
- Duplicate removal
- Reasonable ranges
- Consistent formatting

Only after these checks should the dataset be used for further analysis.

---

## ⚠️ Important Note About Outliers

An outlier is not automatically an error.

For example, an unusually high revenue value may represent:

- A genuine large transaction
- A special business event
- A data-entry mistake
- A unit or formatting problem

Therefore, an outlier should be **investigated before deciding what to do with it**.

---

## 💼 Business Importance

Clean business data helps improve:

- Reporting
- KPI calculations
- Business summaries
- Charts
- Dashboards
- Data analysis
- Business insights

Poor-quality data can lead to incorrect calculations and misleading conclusions.

---

## 📁 Main Excel File

`Day_092_Business_Data_Cleaning.xlsx`

This workbook is the main practical resource for Day 092.

---

## 📝 Supporting Files

The Day 092 learning package contains:

- `README.md`
- `notes.md`
- `cheat-sheet.md`
- `practice.md`
- `resources.md`
- `code/business_data_cleaning.py`
- `Day_092_Business_Data_Cleaning.xlsx`

---

## 📌 Data Note

The dataset used in this workbook is **synthetic educational data** created for learning and practice.

It does not represent real company data or actual business performance.

---

## 🔗 Day Progress

| Day | Topic |
|---|---|
| Day 090 | Processing Business Process Data Using Spreadsheets |
| Day 091 | Excel Revision |
| **Day 092** | **Business Data Cleaning** |
| Day 093 | Sales Analytics |

---

## ✅ Completion Checklist

- [ ] Raw data inspected
- [ ] Data-quality issues identified
- [ ] Missing values checked
- [ ] Duplicate records checked
- [ ] Text cleaned
- [ ] Categories standardised
- [ ] Dates checked
- [ ] Numeric values checked
- [ ] Email values cleaned
- [ ] Status values standardised
- [ ] Outlier investigated
- [ ] Cleaning log completed
- [ ] Cleaned dataset reviewed
- [ ] Validation completed
- [ ] Before/after comparison reviewed
- [ ] Cleaned data analysed
- [ ] Charts reviewed

---

## 🎯 Key Takeaway

> **Data cleaning is the process of identifying and handling data-quality problems so that business data becomes consistent, reliable and ready for analysis.**

**Raw Data → Clean Data → Reliable Analysis**