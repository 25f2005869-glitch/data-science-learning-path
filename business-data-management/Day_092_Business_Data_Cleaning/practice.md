# 📝 Day 092 — Business Data Cleaning — Practice

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

# 🎯 Practice Objective

The objective of Day 092 practice is to learn how to inspect, clean and validate a business dataset before using it for analysis.

Use the workbook:

`Day_092_Business_Data_Cleaning.xlsx`

Main workflow:

**Inspect → Identify Issues → Clean → Validate → Compare → Analyse**

---

# 1. Raw Data Inspection

Open the `Raw_Business_Data` sheet.

### Tasks

1. Check the number of rows.
2. Check the number of columns.
3. Read all column names.
4. Identify text columns.
5. Identify numeric columns.
6. Identify date columns.
7. Identify columns containing possible missing values.
8. Look for unusual values.

### Questions

- What types of data are present?
- Which columns may require cleaning?
- Which values look inconsistent?

---

# 2. Find Missing Values

Inspect the raw dataset for blank values.

Focus on:

- `Cost_Rupee`
- `Customer_Satisfaction_%`
- `Email`
- Other columns where blanks appear

### Tasks

1. Locate missing values.
2. Record them in `Cleaning_Log`.
3. Decide whether each value should be retained, replaced or flagged.
4. Explain the reason for your action.

---

# 3. Find Duplicate Records

Check the `Record_ID` column and the complete dataset.

### Tasks

1. Search for duplicate Record IDs.
2. Check whether any complete rows are duplicated.
3. Determine whether the repeated record is a genuine duplicate.
4. Record the finding in `Cleaning_Log`.
5. Remove genuine duplicate rows.

### Questions

- Why can duplicates affect business analysis?
- What happens to total revenue if a transaction is counted twice?

---

# 4. Clean Business Function

Inspect:

`Business_Function`

Look for values such as:

- `Sales`
- `sales`
- `SALES`
- ` sales `
- `Customer service`

### Tasks

1. Identify inconsistent values.
2. Remove unnecessary spaces.
3. Standardise capitalization.
4. Make sure the categories are consistent.
5. Verify the cleaned values.

---

# 5. Clean Region

Inspect:

`Region`

Expected categories:

- North
- South
- East
- West

### Tasks

1. Find inconsistent capitalization.
2. Find unnecessary spaces.
3. Standardise all region names.
4. Check the result using filtering.

---

# 6. Clean Product Category

Inspect:

`Product_Category`

Expected categories:

- Electronics
- Clothing
- Home
- Grocery

### Tasks

1. Find values with extra spaces.
2. Find inconsistent capitalization.
3. Standardise the category names.
4. Check the final categories.

---

# 7. Clean Customer Names

Inspect:

`Customer_Name`

### Tasks

1. Find names with unnecessary spaces.
2. Use `TRIM()` where appropriate.
3. Compare the values before and after cleaning.
4. Check that the customer names are consistent.

---

# 8. Clean Dates

Inspect:

`Date`

### Tasks

1. Identify different date formats.
2. Identify invalid date values.
3. Convert valid dates into a consistent format.
4. Flag dates that cannot be interpreted reliably.
5. Verify the final date column.

### Questions

- Why are consistent dates important?
- What problems can invalid dates cause in monthly analysis?

---

# 9. Clean Numeric Values

Inspect:

- `Orders`
- `Revenue_Rupee`
- `Cost_Rupee`
- `Returned_Orders`
- `Customer_Satisfaction_%`

### Tasks

1. Find numbers stored as text.
2. Find blank numeric values.
3. Find invalid numeric values.
4. Find negative values.
5. Check whether the values are within reasonable ranges.
6. Record important issues in `Cleaning_Log`.

---

# 10. Revenue Cleaning

Inspect:

`Revenue_Rupee`

### Tasks

1. Find values stored as text.
2. Convert valid text-based numbers into numeric values.
3. Identify unusually high revenue.
4. Investigate the extreme value.
5. Do not automatically delete the outlier.

### Question

Is an unusually high revenue value necessarily an error?

Explain your answer.

---

# 11. Returned Orders Cleaning

Inspect:

`Returned_Orders`

### Tasks

1. Check for blank values.
2. Check for text values.
3. Check for negative values.
4. Investigate invalid values.
5. Make the column suitable for analysis.

---

# 12. Customer Satisfaction Cleaning

Inspect:

`Customer_Satisfaction_%`

### Tasks

1. Find blank values.
2. Check the minimum value.
3. Check the maximum value.
4. Identify values below 0.
5. Identify values above 100.
6. Record any issue found.

---

# 13. Email Cleaning

Inspect:

`Email`

### Tasks

1. Look for extra spaces.
2. Identify inconsistent formatting.
3. Remove unnecessary spaces.
4. Check the cleaned values.

Example problem:

`neha.verma @example.com`

Expected cleaned form:

`neha.verma@example.com`

---

# 14. Status Cleaning

Inspect:

`Status`

Expected categories include:

- Completed
- Pending
- Returned
- Cancelled

### Tasks

1. Identify extra spaces.
2. Identify inconsistent capitalization.
3. Standardise the status values.
4. Filter each status to verify the result.

---

# 15. Use TRIM()

Practise the `TRIM()` function.

### Task

Use `TRIM()` on text containing unnecessary spaces.

Example:

`=TRIM(A2)`

### Goal

Convert:

` Sales `

into:

`Sales`

---

# 16. Use UPPER() and LOWER()

Practise:

`UPPER()`

and

`LOWER()`

### Tasks

1. Convert a business category to uppercase.
2. Convert the same value to lowercase.
3. Compare the results.
4. Decide which standard format is appropriate for the dataset.

---

# 17. Find and Replace Practice

Use Excel's **Find and Replace** feature.

### Tasks

1. Find inconsistent category names.
2. Replace them with the standard category.
3. Review the changes.
4. Verify that unrelated values were not changed.

---

# 18. Conditional Formatting Practice

Apply conditional formatting to the raw data.

### Tasks

1. Highlight blank cells.
2. Highlight duplicate Record IDs.
3. Highlight negative values.
4. Highlight unusually high revenue.
5. Highlight low customer satisfaction.

### Goal

Use visual formatting to identify possible data-quality issues quickly.

---

# 19. Data Quality Check

Open the `Data_Quality_Check` sheet.

### Tasks

Review each issue category:

- Missing Values
- Duplicate Records
- Text Consistency
- Date Quality
- Numeric Quality
- Email Quality
- Outliers
- Status Consistency

For every issue, identify:

1. Where the problem occurs.
2. Why it is a problem.
3. What action should be taken.

---

# 20. Cleaning Log Practice

Open:

`Cleaning_Log`

For each important issue, record:

- Issue ID
- Column
- Issue Found
- Cleaning Action
- Reason
- Result
- Notes

### Example Structure

**Issue Found:** Extra spaces in category

**Cleaning Action:** Trimmed and standardised text

**Reason:** Prevent incorrect category grouping

**Result:** Category labels became consistent

---

# 21. Cleaned Dataset Practice

Open:

`Cleaned_Business_Data`

### Tasks

1. Check the cleaned Record IDs.
2. Check the dates.
3. Check business functions.
4. Check regions.
5. Check product categories.
6. Check numeric columns.
7. Check customer satisfaction.
8. Check emails.
9. Check status values.
10. Review calculated metrics.

---

# 22. Before vs After Practice

Open:

`Before_After`

Compare the raw and cleaned datasets.

Review:

- Text labels
- Dates
- Numeric values
- Duplicates
- Emails
- Status
- Outliers

### Question

Write three examples showing how cleaning improved the dataset.

---

# 23. Validation Practice

Open:

`Validation`

Check:

1. Blank Record IDs.
2. Negative Orders.
3. Negative Cost.
4. Negative Returned Orders.
5. Customer Satisfaction below 0.
6. Customer Satisfaction above 100.

### Goal

Identify whether any invalid values remain.

---

# 24. Cleaning Summary

Open:

`Cleaning_Summary`.

Review:

- Raw Records
- Cleaned Records
- Rows Removed
- Raw Columns
- Final Columns
- Cleaning Focus

### Questions

1. How many records were present before cleaning?
2. How many records remain after cleaning?
3. Were any duplicate rows removed?
4. Which types of cleaning were performed?

---

# 25. Analysis After Cleaning

Open:

`Cleaned_Analysis`.

Analyse the cleaned data by Business Function.

### Tasks

Compare:

- Orders
- Revenue
- Cost
- Profit
- Average Customer Satisfaction

Write at least three observations.

---

# 26. Chart Practice

Open:

`Cleaning_Charts`.

Review the charts based on the cleaned dataset.

### Tasks

1. Understand the revenue comparison.
2. Understand the profit comparison.
3. Identify differences between business functions.
4. Write two observations from the charts.

---

# 27. Business Cleaning Challenge

Complete the following without looking at the notes.

### Challenge 1

Find every inconsistent Business Function value.

### Challenge 2

Find every inconsistent Region value.

### Challenge 3

Find the duplicate record.

### Challenge 4

Find the invalid date.

### Challenge 5

Find the numeric value stored as text.

### Challenge 6

Find the negative Returned Orders value.

### Challenge 7

Find the missing Customer Satisfaction value.

### Challenge 8

Find the unusual Revenue value.

### Challenge 9

Clean the Email spacing issue.

### Challenge 10

Standardise the Status values.

---

# 28. Data Cleaning Decision Practice

For each problem, decide the appropriate action.

| Situation | Possible Action |
|---|---|
| Extra spaces | Trim |
| Different capitalization | Standardise |
| Genuine duplicate row | Remove |
| Missing value | Investigate / handle appropriately |
| Invalid date | Convert or flag |
| Number stored as text | Convert |
| Negative value | Investigate |
| Extreme value | Investigate |
| Valid unusual transaction | Retain |
| Incorrect repeated label | Standardise |

---

# 29. Final Mini Project

Use the Day 092 dataset to complete a complete cleaning workflow.

### Step 1

Inspect the raw dataset.

### Step 2

List all data-quality issues.

### Step 3

Clean the text fields.

### Step 4

Clean the dates.

### Step 5

Clean numeric values.

### Step 6

Handle genuine duplicates.

### Step 7

Investigate missing values.

### Step 8

Investigate the outlier.

### Step 9

Record important actions in the Cleaning Log.

### Step 10

Validate the cleaned dataset.

### Step 11

Compare before and after cleaning.

### Step 12

Perform basic business analysis.

### Step 13

Review the charts.

---

# 30. Business Insight Practice

After cleaning and analysing the data, write five observations.

Your observations should be based on the cleaned data.

Examples of areas to discuss:

- Revenue
- Profit
- Orders
- Business Function
- Customer Satisfaction

Do not make claims that are not supported by the dataset.

---

# 31. Final Questions

Answer these questions after completing the practical work.

### Q1

Why should data be cleaned before analysis?

### Q2

How can duplicate records affect revenue calculations?

### Q3

Why is text standardisation important?

### Q4

Why should invalid dates be identified before time-based analysis?

### Q5

Why should an outlier not automatically be removed?

### Q6

What is the purpose of a Cleaning Log?

### Q7

Why is validation required after cleaning?

### Q8

What is the difference between a missing value and an invalid value?

### Q9

How can conditional formatting help during data cleaning?

### Q10

What makes a dataset analysis-ready?

---

# 32. Final Practice Checklist

- [ ] Raw data inspected
- [ ] Data types reviewed
- [ ] Missing values identified
- [ ] Duplicates identified
- [ ] Business Function cleaned
- [ ] Region cleaned
- [ ] Product Category cleaned
- [ ] Customer Names cleaned
- [ ] Dates checked
- [ ] Numeric values checked
- [ ] Negative values investigated
- [ ] Email values cleaned
- [ ] Status values standardised
- [ ] Outlier investigated
- [ ] Cleaning Log completed
- [ ] Cleaned dataset reviewed
- [ ] Before/After comparison completed
- [ ] Validation completed
- [ ] Cleaning Summary reviewed
- [ ] Cleaned data analysed
- [ ] Charts reviewed
- [ ] Business insights written
- [ ] Final questions answered

---

# 🎯 Final Goal

The goal of Day 092 is to develop the ability to take a messy business dataset and prepare it for reliable analysis.

**Raw Data → Inspect → Clean → Validate → Analysis-Ready Data → Analyse**

---

## 📌 Key Takeaway

> **Clean the data before trusting the analysis.**