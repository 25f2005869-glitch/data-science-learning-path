# 🧹 Day 092 — Business Data Cleaning — Notes

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

# 1. Introduction

Business data is often collected from different sources and may contain errors or inconsistencies.

Examples include:

- Missing values
- Duplicate records
- Extra spaces
- Different spellings
- Different text cases
- Invalid dates
- Numbers stored as text
- Negative values
- Incorrect formats
- Unusual values

Before performing business analysis, the data should be checked and cleaned.

The main purpose of data cleaning is to make the dataset more consistent, reliable and suitable for analysis.

---

# 2. What Is Data Cleaning?

**Data cleaning** is the process of identifying and handling problems in a dataset.

A typical cleaning process is:

**Inspect → Identify Issues → Clean → Validate → Analyse**

Data cleaning does not mean changing every unusual value.

The goal is to understand the problem and apply an appropriate action.

---

# 3. Why Data Cleaning Is Important

Poor-quality data can produce incorrect analysis.

For example:

If one region is written as:

`North`

and another record contains:

`north`

Excel or another analysis tool may treat them as different categories.

Similarly, extra spaces can create incorrect groups.

Clean data helps improve:

- Calculations
- Reports
- KPIs
- Charts
- Dashboards
- Business analysis
- Business insights

---

# 4. Data Quality

Data quality refers to how suitable the data is for its intended use.

Important quality areas include:

- Accuracy
- Completeness
- Consistency
- Validity
- Uniqueness
- Reliability

During Day 092, the focus is mainly on identifying and handling common quality problems in a business dataset.

---

# 5. Understanding the Raw Dataset

Before cleaning, first understand the dataset.

The Day 092 workbook contains fields such as:

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

The dataset is deliberately messy for learning purposes.

---

# 6. First Step — Inspect the Data

Do not immediately start changing the data.

First inspect:

- Number of rows
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate records
- Text consistency
- Numeric values
- Date values
- Possible outliers

Inspection helps identify what needs to be cleaned.

---

# 7. Missing Values

A missing value means that information is not available in a particular cell.

Examples:

- Missing cost
- Missing customer satisfaction
- Missing email
- Missing date

### Common ways to handle missing values

Depending on the situation, a missing value may be:

- Left blank
- Replaced with an appropriate value
- Calculated from available information
- Flagged for review
- Removed when justified

The correct method depends on the meaning of the column and the purpose of the analysis.

---

# 8. Duplicate Records

A duplicate is a record that appears more than once.

Duplicates can cause problems because they may result in:

- Double counting
- Incorrect totals
- Incorrect averages
- Incorrect business KPIs

### Duplicate Checking

Check:

- Record ID
- Full rows
- Relevant identifying columns

Do not remove a record simply because two records look similar.

First determine whether it is a genuine duplicate.

---

# 9. Text Inconsistency

Text values may represent the same category in different ways.

Example:

`Sales`

`sales`

` SALES `

These may represent the same business function.

If they are not standardised, grouping and summary calculations may become incorrect.

---

# 10. Removing Extra Spaces

Extra spaces can appear at the beginning or end of text.

Example:

` Sales `

should become:

`Sales`

In Excel, the `TRIM()` function can help remove unnecessary spaces.

Example:

`=TRIM(A2)`

Text cleaning is especially useful for:

- Customer names
- Business functions
- Regions
- Product categories
- Status values

---

# 11. Standardising Text

Text values should follow a consistent format.

Example:

Before:

`Sales`

`sales`

`SALES`

After:

`Sales`

Similarly:

Before:

`WEST`

`West `

`west`

After:

`West`

Standardised categories make filtering and grouping more reliable.

---

# 12. Business Function Cleaning

The dataset contains business functions such as:

- Sales
- Operations
- Customer Service
- Marketing

These labels should be consistent.

For example:

`Customer service`

can be standardised to:

`Customer Service`

This prevents the same category from appearing as separate groups.

---

# 13. Region Cleaning

The main regions are:

- North
- South
- East
- West

Examples of inconsistent values:

`north`

`North`

`NORTH`

`WEST `

These should be standardised before regional analysis.

---

# 14. Product Category Cleaning

Product categories should also use consistent labels.

Examples include:

- Electronics
- Clothing
- Home
- Grocery

Values such as:

` Electronics `

or

`grocery`

should be standardised.

---

# 15. Date Cleaning

Dates are important for time-based business analysis.

Common date problems include:

- Different date formats
- Invalid date text
- Missing dates
- Dates stored as text

Example:

`15/02/2026`

may need to be converted into a consistent date format.

An invalid value such as:

`invalid-date`

cannot be treated as a valid date without further information.

---

# 16. Why Date Cleaning Matters

Clean dates are required for analysis such as:

- Daily trends
- Monthly trends
- Yearly trends
- Time-based comparisons
- Period-based reporting

If dates are stored incorrectly, sorting and grouping may produce incorrect results.

---

# 17. Numeric Data Cleaning

Business datasets contain many numeric fields.

Examples:

- Orders
- Revenue
- Cost
- Returned Orders
- Customer Satisfaction

These values should be checked carefully.

Common problems include:

- Numbers stored as text
- Blank values
- Invalid text
- Negative values
- Incorrect formatting

---

# 18. Numbers Stored as Text

A value such as:

`1,25,000`

may be stored as text rather than as a numeric value.

Before analysis, the value should be converted into an appropriate numeric representation.

Numeric data must be recognised correctly for:

- SUM
- AVERAGE
- Sorting
- Charts
- KPI calculations

---

# 19. Negative Values

Some business fields should normally not contain negative values.

For example:

- Orders
- Returned Orders
- Cost

If a negative value appears, it should be investigated.

A negative value could represent:

- Data-entry error
- Adjustment
- Refund
- Accounting convention
- Other business-specific meaning

It should not automatically be deleted.

---

# 20. Email Cleaning

Email values should be checked for unnecessary spaces and obvious formatting problems.

Example:

`neha.verma @example.com`

contains an unnecessary space.

A basic cleaning operation can remove the extra space.

However, detailed email validation is beyond the main scope of this exercise.

---

# 21. Status Cleaning

Status values should use consistent labels.

Possible statuses in the dataset include:

- Completed
- Pending
- Returned
- Cancelled

Examples of inconsistent values:

` completed `

`Completed`

`COMPLETED`

These should be standardised.

---

# 22. Outliers

An **outlier** is a value that is unusually high or low compared with other observations.

Example:

Most revenue values may be within a normal business range, while one value is extremely high.

An unusual value does not automatically mean that it is wrong.

---

# 23. How to Handle an Outlier

When an outlier is found:

1. Identify the value.
2. Check the original record.
3. Check whether the value is possible.
4. Check for data-entry or formatting problems.
5. Understand the business context if available.
6. Decide whether it should be retained, corrected or flagged.

Do not remove outliers automatically.

---

# 24. Data Cleaning Log

A cleaning log records important cleaning decisions.

Useful fields include:

| Field | Purpose |
|---|---|
| Issue ID | Identifies the issue |
| Column | Shows where the issue occurred |
| Issue Found | Describes the problem |
| Cleaning Action | Describes what was done |
| Reason | Explains why |
| Result | Records the outcome |
| Notes | Additional information |

A cleaning log makes the process easier to review.

---

# 25. Cleaned Dataset

After cleaning, the dataset should be easier to use for analysis.

The cleaned dataset should have:

- Consistent labels
- Appropriate data types
- Valid dates where possible
- Valid numeric values
- Duplicates handled appropriately
- Missing values identified or handled
- Unusual values investigated

The cleaned dataset becomes the basis for further analysis.

---

# 26. Before vs After Cleaning

Comparing the data before and after cleaning helps understand the effect of cleaning.

| Area | Before | After |
|---|---|---|
| Text | Inconsistent | Standardised |
| Dates | Mixed / invalid values | Consistent valid values where possible |
| Numbers | Text / invalid values | Cleaned or flagged |
| Duplicates | Present | Genuine duplicates handled |
| Emails | Extra spaces | Cleaned |
| Status | Mixed formatting | Standardised |
| Outliers | Unusual value | Investigated / flagged |

---

# 27. Data Validation

Cleaning should be followed by validation.

Validation checks whether the cleaned dataset satisfies basic rules.

Examples:

- Record IDs should not be blank.
- Orders should not be negative.
- Cost should not be negative.
- Returned Orders should not be negative.
- Customer Satisfaction should be within an appropriate range.

Validation helps detect remaining problems.

---

# 28. Excel Tools for Data Cleaning

Useful Excel features include:

- Sort
- Filter
- Remove Duplicates
- Find and Replace
- Text functions
- Conditional Formatting
- Data Validation
- Tables
- Formulas

These tools can help identify and handle common data-quality issues.

---

# 29. Useful Excel Functions

### TRIM

Removes unnecessary spaces.

`=TRIM(A2)`

### UPPER

Converts text to uppercase.

`=UPPER(A2)`

### LOWER

Converts text to lowercase.

`=LOWER(A2)`

### LEFT

Extracts characters from the left.

`=LEFT(A2,3)`

### RIGHT

Extracts characters from the right.

`=RIGHT(A2,3)`

### LEN

Counts characters.

`=LEN(A2)`

These functions are useful for text inspection and standardisation.

---

# 30. Cleaning with Find and Replace

Find and Replace can be useful when the same incorrect value occurs many times.

For example, if a dataset contains:

`Customer service`

and the desired category is:

`Customer Service`

Find and Replace can help standardise the value.

Always review replacements carefully before applying them to the entire dataset.

---

# 31. Conditional Formatting for Data Quality

Conditional formatting can help highlight:

- Blank values
- Negative values
- High values
- Low values
- Duplicate values
- Unusual values

This provides a quick visual way to inspect the dataset.

---

# 32. Cleaning Summary

A cleaning summary can contain:

- Raw record count
- Cleaned record count
- Rows removed
- Number of columns
- Cleaning areas
- Validation results

This provides a simple overview of the cleaning process.

---

# 33. Analysis After Cleaning

Once the data has been cleaned, it can be analysed by:

- Business Function
- Region
- Product Category
- Status
- Orders
- Revenue
- Cost
- Profit
- Customer Satisfaction

Cleaning therefore acts as a preparation step for business analysis.

---

# 34. Business Data Cleaning Workflow

The complete workflow is:

**Raw Business Data**

↓

**Inspect Data**

↓

**Identify Quality Issues**

↓

**Handle Missing Values**

↓

**Remove Genuine Duplicates**

↓

**Standardise Text**

↓

**Clean Dates**

↓

**Clean Numeric Values**

↓

**Investigate Outliers**

↓

**Validate Data**

↓

**Create Cleaned Dataset**

↓

**Analyse Business Data**

---

# 35. Common Mistakes to Avoid

### Mistake 1 — Deleting all unusual values

An unusual value may be a genuine business event.

### Mistake 2 — Removing all blanks

A blank may have an important meaning.

### Mistake 3 — Treating similar text as identical without checking

Different labels may represent different categories.

### Mistake 4 — Changing values without recording the action

Important cleaning decisions should be documented.

### Mistake 5 — Analysing before cleaning

Poor-quality data can produce misleading results.

### Mistake 6 — Assuming every negative value is an error

The meaning depends on the business context.

---

# 36. Practical Day 092 Workbook

The main workbook is:

`Day_092_Business_Data_Cleaning.xlsx`

Important sheets include:

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

# 37. Practical Learning Sequence

Follow this order:

1. Open `Instructions`.
2. Inspect `Raw_Business_Data`.
3. Review `Data_Quality_Check`.
4. Complete `Cleaning_Practice`.
5. Record important actions in `Cleaning_Log`.
6. Review `Cleaned_Business_Data`.
7. Compare `Before_After`.
8. Check `Validation`.
9. Review `Cleaning_Summary`.
10. Analyse `Cleaned_Analysis`.
11. Review `Cleaning_Charts`.

---

# 38. Key Learning Points

- Always inspect data before changing it.
- Missing values require careful handling.
- Duplicate records can distort analysis.
- Text should be standardised.
- Dates should use consistent formats.
- Numeric fields should contain appropriate numeric values.
- Invalid values should be investigated.
- Outliers should not automatically be removed.
- Cleaning decisions should be documented.
- Validation should follow cleaning.
- Clean data is the foundation for reliable analysis.

---

# 39. Final Summary

Business Data Cleaning is an important step in the data-analysis workflow.

The complete process can be remembered as:

**Inspect → Identify → Clean → Validate → Analyse**

The objective is not simply to make the dataset look clean.

The objective is to create data that is:

**Consistent → Valid → Reliable → Analysis-Ready**

---

## 🎯 Key Takeaway

> **Good business analysis starts with good data. Before calculating KPIs or creating charts, make sure the underlying data has been properly checked and cleaned.**