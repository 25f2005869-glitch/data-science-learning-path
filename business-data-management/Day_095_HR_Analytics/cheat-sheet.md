# 🧾 Day 095 — HR Analytics Cheat Sheet

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

# 📌 HR Analytics

**HR Analytics** = Using employee data to understand workforce patterns, salaries, experience, departments, job roles, and attrition.

---

# 👥 Important HR Fields

| Field | Meaning |
|---|---|
| Employee ID | Unique employee identifier |
| Joining Date | Date the employee joined |
| Employee Name | Employee name |
| Age | Employee age |
| Department | Functional department |
| Job Role | Employee's role |
| Education | Educational qualification |
| Location | Work location |
| Experience Years | Professional experience |
| Monthly Salary | Monthly salary |
| Employment Type | Full-Time / Part-Time |
| Employee Status | Active / On Leave / Resigned |
| Attrition | Whether employee is marked for attrition |

---

# 🧹 Data Cleaning Checklist

Check for:

- Missing values
- Duplicate records
- Extra spaces
- Inconsistent capitalization
- Invalid numeric values
- Negative experience
- Missing salary
- Missing department
- Invalid dates

### Cleaning Workflow

**Inspect → Identify Issues → Clean → Validate → Analyse**

---

# 📊 Employee Analysis

Important metrics:

- Total Employees
- Average Age
- Average Experience
- Average Monthly Salary
- Total Monthly Salary Cost
- Active Employees
- Attrition Count

---

# 🏢 Department Analysis

Analyse each department using:

- Employee Count
- Average Salary
- Total Salary
- Average Experience
- Attrition Count
- Attrition Rate

Departments in the practice dataset:

- Sales
- Finance
- HR
- IT
- Marketing
- Operations

---

# 💼 Job Role Analysis

Important measures:

- Employee Count
- Average Salary
- Total Salary
- Average Experience

Example roles:

- Sales Executive
- Financial Analyst
- HR Executive
- Software Analyst
- Marketing Executive
- Operations Executive

---

# 💰 Salary Analysis

### Average Salary

**Average Salary = Total Salary ÷ Number of Employees**

### Total Salary

**Total Salary = Sum of Employee Salaries**

### Minimum Salary

Lowest salary in the selected group.

### Maximum Salary

Highest salary in the selected group.

---

# 📤 Attrition

**Attrition** = Employees marked as having left the organisation.

- `Yes` → Attrition
- `No` → No Attrition

### Attrition Count

**Attrition Count = Number of employees with Attrition = Yes**

### Attrition Rate

**Attrition Rate = Attrition Count ÷ Total Employees × 100**

---

# 📅 Monthly HR Analysis

Monthly analysis can examine:

- Employee records
- New joining records
- Attrition information
- Monthly salary information

Useful for identifying changes over time.

---

# 🎯 HR KPIs

| KPI | Meaning |
|---|---|
| Total Employees | Number of employees |
| Average Age | Average employee age |
| Average Experience | Average experience |
| Average Monthly Salary | Average salary |
| Total Monthly Salary Cost | Total salary cost |
| Attrition Count | Number of attrition records |
| Attrition Rate | Attrition as a percentage of employees |

---

# 📑 Pivot Analysis

### Department Pivot

**Rows:** Department

**Values:**
- Employee Count
- Average Salary
- Total Salary
- Average Experience
- Attrition Count

### Role Pivot

**Rows:** Job Role

**Values:**
- Employee Count
- Average Salary
- Total Salary
- Average Experience

---

# 📈 Visualisation

### Bar Chart

Useful for:

- Employee Count by Department
- Average Salary by Department
- Attrition Count by Department

### Line Chart

Useful for:

- Monthly HR trends

---

# 📗 Useful Excel Functions

### Counting

`COUNT()`

`COUNTA()`

`COUNTIF()`

`COUNTIFS()`

### Calculations

`SUM()`

`SUMIF()`

`SUMIFS()`

`AVERAGE()`

`AVERAGEIF()`

### Conditional Logic

`IF()`

### Minimum / Maximum

`MINIFS()`

`MAXIFS()`

---

# 🐍 Python Tools

### Pandas

Used for:

- Reading Excel
- Cleaning data
- Grouping data
- Aggregation
- KPI calculations
- Exporting results

Useful functions:

`pd.read_excel()`

`df.head()`

`df.shape`

`df.columns`

`df.dtypes`

`df.isna().sum()`

`df.duplicated().sum()`

`df.groupby()`

`df.sum()`

`df.mean()`

`df.to_csv()`

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

# 💡 Business Questions

1. How many employees are in the dataset?
2. How are employees distributed across departments?
3. What is the average monthly salary?
4. How does salary vary by department?
5. What is the average experience?
6. How many employees are marked for attrition?
7. What is the attrition rate?
8. How does attrition vary across departments?
9. How does the workforce change over time?
10. What patterns can be identified from the cleaned HR data?

---

# 🔄 Complete Workflow

**Raw HR Data**

→ **Data Quality Check**

→ **Data Cleaning**

→ **Employee Summary**

→ **Department Analysis**

→ **Job Role Analysis**

→ **Salary Analysis**

→ **Attrition Analysis**

→ **Monthly Analysis**

→ **HR KPIs**

→ **Pivot Analysis**

→ **Visualisation**

→ **Business Insights**

---

# ⚡ Quick Revision

**HR Analytics**

= Employee Data + Analysis

**Average Salary**

= Total Salary ÷ Employees

**Attrition Rate**

= Attrition Count ÷ Total Employees × 100

**Data Cleaning**

= Inspect → Clean → Validate

**Department Analysis**

= Employees + Salary + Experience + Attrition

**KPI**

= Key measure used to summarise HR data

**Pivot Table**

= Summarise HR data by dimensions such as Department or Job Role

**Visualisation**

= Convert HR data into charts for easier interpretation

---

# 🧠 Key Takeaway

**HR Analytics = Clean Employee Data → Analyse Workforce → Calculate HR KPIs → Visualise Results → Generate Business Insights**