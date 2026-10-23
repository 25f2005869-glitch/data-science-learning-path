# 📘 Day 095 — HR Analytics Notes

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Programme](https://img.shields.io/badge/Programme-Diploma%20Level-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-095-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-HR%20Analytics-orange?style=for-the-badge)

## 👩‍💻 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 095
- **Topic:** HR Analytics

---

# 1. Introduction to HR Analytics

HR Analytics is the process of using employee and workforce data to understand patterns related to employees, departments, salaries, experience, and attrition.

The purpose is to convert HR data into useful information that can support business analysis.

---

# 2. HR Data

HR data contains information about employees and their employment details.

The Day 095 dataset contains fields such as:

- Employee ID
- Joining Date
- Employee Name
- Age
- Department
- Job Role
- Education
- Location
- Experience Years
- Monthly Salary
- Employment Type
- Employee Status
- Attrition

---

# 3. Employee ID

Employee ID is a unique identifier assigned to an employee.

Example:

- E001
- E002
- E003

A unique Employee ID helps identify individual employee records.

---

# 4. Joining Date

Joining Date represents the date on which an employee joined the organisation.

It can be used for:

- New-joiner analysis
- Monthly HR analysis
- Workforce trends
- Experience-related analysis

---

# 5. Employee Age

Age represents the employee's age.

Age can be analysed to understand the distribution of employees across different age groups.

Important checks include:

- Missing age
- Invalid age
- Unusual values

---

# 6. Department

A department represents the functional area in which an employee works.

The Day 095 dataset contains:

- Sales
- Finance
- HR
- IT
- Marketing
- Operations

Department analysis helps understand how employees and salary costs are distributed.

---

# 7. Job Role

Job Role represents the employee's position or role within the organisation.

Examples include:

- Sales Executive
- Financial Analyst
- HR Executive
- Software Analyst
- Marketing Executive
- Operations Executive

Job-role analysis can be used to compare employee counts, salary, and experience.

---

# 8. Education

Education represents the employee's educational qualification.

The practice dataset includes:

- Graduate
- Postgraduate

Education can be used as one of the dimensions for employee analysis.

---

# 9. Location

Location represents the employee's work location.

Example locations in the dataset include:

- Patna
- Delhi
- Mumbai
- Bengaluru
- Kolkata

Location can be used to understand the geographic distribution of employees.

---

# 10. Experience

Experience Years represents the employee's years of professional experience.

Experience can be used to calculate:

- Average experience
- Experience by department
- Experience by job role

An experience value should not be negative.

---

# 11. Monthly Salary

Monthly Salary represents the employee's salary for a month.

Salary analysis can include:

- Average salary
- Minimum salary
- Maximum salary
- Total salary cost
- Department-wise salary

---

# 12. Employment Type

Employment Type describes the employee's work arrangement.

The practice dataset contains:

- Full-Time
- Part-Time

---

# 13. Employee Status

Employee Status represents the current status of an employee.

Examples include:

- Active
- On Leave
- Resigned

Status can be used to understand the current workforce and employee movement.

---

# 14. Attrition

Attrition represents employees who have left the organisation or are marked as having left.

In the practice dataset:

- `Yes` indicates attrition
- `No` indicates no attrition

Attrition analysis helps understand employee exits within the dataset.

---

# 15. Attrition Count

Attrition Count is the number of employees marked with attrition.

Formula:

**Attrition Count = Number of Employees with Attrition = Yes**

---

# 16. Attrition Rate

Attrition Rate represents attrition relative to the total number of employees.

Formula:

**Attrition Rate = Attrition Count / Total Employees × 100**

Example:

If there are 5 attrition records among 100 employees:

**Attrition Rate = 5 / 100 × 100 = 5%**

---

# 17. HR Data Inspection

Before analysing HR data, the dataset should be inspected.

Important checks include:

- Number of rows
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate records
- Inconsistent text
- Invalid numeric values

---

# 18. HR Data Quality

Common HR data-quality issues include:

### Missing Values

Examples:

- Missing Age
- Missing Department
- Missing Salary
- Missing Experience

### Duplicate Records

The same employee record may appear more than once.

### Extra Spaces

Example:

`" Sales "` instead of `"Sales"`

### Inconsistent Case

Example:

`"software analyst"` instead of `"Software Analyst"`

### Invalid Numeric Values

Example:

`"N/A"` in a salary column.

### Negative Values

Experience cannot logically be negative.

---

# 19. HR Data Cleaning

A basic cleaning workflow is:

**Inspect → Identify Issues → Clean → Validate → Analyse**

Common cleaning actions include:

- Trim unnecessary spaces
- Standardise text
- Convert values to the correct data type
- Handle missing values
- Validate numeric values
- Remove exact duplicate records

---

# 20. Employee Summary

The Employee Summary provides an overall view of the workforce.

Important measures include:

- Total Employees
- Average Age
- Average Experience
- Average Monthly Salary
- Total Monthly Salary Cost
- Active Employees
- Attrition Count

---

# 21. Department Analysis

Department analysis groups employees by department.

Important measures include:

- Employee Count
- Average Salary
- Total Salary
- Average Experience
- Attrition Count
- Attrition Rate

This helps understand workforce distribution across departments.

---

# 22. Job Role Analysis

Job Role Analysis groups employees according to their roles.

Important measures include:

- Employee Count
- Average Salary
- Total Salary
- Average Experience

This allows different roles to be compared using the available HR data.

---

# 23. Salary Analysis

Salary Analysis examines salary distribution.

Important measures include:

### Average Salary

**Average Salary = Total Salary / Number of Employees**

### Minimum Salary

The lowest salary value in the selected group.

### Maximum Salary

The highest salary value in the selected group.

### Total Salary

The sum of salaries for the selected employees.

---

# 24. Experience Analysis

Experience analysis helps understand the workforce experience level.

Important measures include:

- Average Experience
- Experience by Department
- Experience by Job Role

Experience should be validated before performing calculations.

---

# 25. Attrition Analysis

Attrition Analysis examines employee exits.

Important measures include:

- Employee Count
- Attrition Count
- Attrition Rate

Department-level attrition can also be compared.

---

# 26. Monthly HR Analysis

Monthly analysis groups HR records by month.

It can be used to examine:

- Employee records
- New joining records
- Attrition information
- Monthly salary information

Date-based analysis helps identify changes over time.

---

# 27. HR KPIs

Key HR KPIs in Day 095 include:

- Total Employees
- Average Age
- Average Experience
- Average Monthly Salary
- Total Monthly Salary Cost
- Attrition Count
- Attrition Rate

KPIs provide a quick summary of important HR measures.

---

# 28. Pivot Analysis

Pivot analysis is useful for summarising large datasets.

### Department Pivot

Rows:

**Department**

Values:

- Employee Count
- Average Salary
- Total Salary
- Average Experience
- Attrition Count

### Role Pivot

Rows:

**Job Role**

Values:

- Employee Count
- Average Salary
- Total Salary
- Average Experience

---

# 29. HR Visualisation

Charts help communicate HR information clearly.

The Day 095 workbook contains charts for:

### Employee Count by Department

Used to compare workforce size across departments.

### Average Salary by Department

Used to compare average monthly salary across departments.

### Attrition Count by Department

Used to compare attrition counts across departments.

---

# 30. Business Insights

HR Analytics is not only about calculating numbers.

The final step is interpreting the results.

Useful questions include:

- How is the workforce distributed across departments?
- Which departments have more employees?
- How does salary vary across departments?
- What is the average employee experience?
- How many employees are marked for attrition?
- How does attrition vary across departments?
- How does the workforce change over time?

Insights should be based on the cleaned data.

---

# 31. Excel Functions for HR Analytics

Useful Excel functions include:

- `COUNT`
- `COUNTA`
- `COUNTIF`
- `COUNTIFS`
- `SUM`
- `SUMIF`
- `SUMIFS`
- `AVERAGE`
- `AVERAGEIF`
- `MINIFS`
- `MAXIFS`
- `IF`

These functions can be used to calculate HR metrics and department-level summaries.

---

# 32. Python and HR Analytics

Python can automate the HR analysis workflow.

Important libraries:

- Pandas
- NumPy
- Matplotlib

### Pandas

Used for:

- Reading Excel files
- Cleaning data
- Grouping data
- Calculating metrics
- Exporting results

### NumPy

Used for:

- Numerical calculations
- Conditional operations

### Matplotlib

Used for:

- Bar charts
- Line charts
- HR visualisation

---

# 33. Useful Pandas Operations

### Read Excel

`pd.read_excel()`

### View Data

`df.head()`

### Check Shape

`df.shape`

### Check Columns

`df.columns`

### Check Data Types

`df.dtypes`

### Check Missing Values

`df.isna().sum()`

### Check Duplicates

`df.duplicated().sum()`

### Group Data

`df.groupby()`

### Calculate Average

`df["Monthly_Salary"].mean()`

### Calculate Total

`df["Monthly_Salary"].sum()`

---

# 34. HR Analytics Workflow

The complete Day 095 workflow is:

**Raw HR Data**

↓

**Data Quality Check**

↓

**Data Cleaning**

↓

**Cleaned HR Data**

↓

**Employee Summary**

↓

**Department Analysis**

↓

**Job Role Analysis**

↓

**Salary Analysis**

↓

**Attrition Analysis**

↓

**Monthly HR Analysis**

↓

**HR KPIs**

↓

**Pivot Analysis**

↓

**Visualisation**

↓

**Business Insights**

↓

**Final HR Analysis**

---

# 35. Important Questions for Revision

1. What is HR Analytics?
2. What type of data is used in HR Analytics?
3. What is Employee ID?
4. What is Attrition?
5. How is Attrition Rate calculated?
6. Why is data cleaning important in HR Analytics?
7. What is Department Analysis?
8. What is Job Role Analysis?
9. What is Salary Analysis?
10. What are HR KPIs?
11. Why are Pivot Tables useful?
12. Which charts can be used for HR analysis?
13. How can Python be used for HR Analytics?
14. Why should HR data be validated before analysis?

---

# 36. Key Learning Points

- HR Analytics uses employee data for structured analysis.
- Data quality should be checked before analysis.
- Missing and inconsistent values can affect results.
- Employee data can be analysed by department and job role.
- Salary can be analysed using average, minimum, maximum, and total values.
- Attrition can be measured using count and rate.
- KPIs provide a quick summary of HR data.
- Pivot analysis helps summarise employee information.
- Charts make HR analysis easier to understand.
- Business insights should be based on the cleaned dataset.

---

# 37. Day 095 Summary

Day 095 focuses on analysing employee and workforce data.

The main process is:

**Understand → Inspect → Clean → Analyse → Calculate KPIs → Visualise → Interpret**

The goal is to develop practical experience in converting HR data into structured analysis and business insights.

---

# 🔑 Key Takeaway

**HR Analytics = Employee Data → Data Cleaning → Workforce Analysis → HR KPIs → Visualisation → Business Insights**