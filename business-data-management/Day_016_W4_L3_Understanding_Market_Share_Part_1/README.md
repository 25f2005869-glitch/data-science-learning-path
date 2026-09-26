![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-016-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Market%20Share%20Part%201-orange?style=for-the-badge)

# 📊 Day 016 — W4_L3: Understanding Market Share — Part 1

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Business Data Management  
**Day:** 016  
**Lecture:** W4_L3  
**Topic:** Understanding Market Share — Part 1

---

## 🎯 Learning Objective

The objective of Day 016 is to understand the basic concept of **market share** and learn how business data can be used to compare companies within a defined market.

This day focuses on:

- Understanding market share
- Working with company-level business data
- Calculating a total market measure
- Calculating company-wise market share
- Converting market share into percentages
- Comparing companies
- Ranking companies
- Creating visual representations
- Interpreting market-share results
- Writing basic business insights

---

## 📚 Lecture Context

**Course:** Business Data Management

**Lecture:** W4_L3

**Lecture Title:** Understanding Market Share — Part 1

Market-share analysis is useful when a business wants to understand the relative position of different companies within a defined market.

The analysis in this repository uses a business dataset containing company, region, loan, customer and revenue information.

---

## 🧠 What Is Market Share?

Market share is a relative measure.

It represents the portion of a defined market associated with a particular company.

The company value is compared with the total market value.

The basic formula is:

**Market Share = Company Measure / Total Market Measure**

To express the result as a percentage:

**Market Share % = (Company Measure / Total Market Measure) × 100**

---

## 🧮 Example

Suppose a company has a measured value of:

**20**

And the total market value is:

**100**

Then:

**Market Share = 20 / 100**

Therefore:

**Market Share = 0.20**

As a percentage:

**Market Share = 20%**

The same calculation can be applied to multiple companies.

---

## 📊 Dataset

The Excel workbook contains business data with the following fields:

| Column | Description |
|---|---|
| Company | Company name |
| Market | Region/market |
| Loans | Number of loans |
| Customers | Number of customers |
| Revenue_Lakh | Revenue measured in lakh |

The dataset is designed for practicing market-share calculations.

---

## 🗂️ Excel Workbook

The workbook is:

`Day_016_W4_L3_Understanding_Market_Share_Part_1.xlsx`

It contains the following sheets:

### 1. `Market_Data`

Contains the raw business dataset.

### 2. `Company_Summary`

Contains company-wise totals.

### 3. `Market_Share`

Contains company-wise market-share calculations.

### 4. `Region_Summary`

Contains region-wise business summaries.

### 5. `Instructions`

Contains the practical instructions for Day 016.

---

## 📈 Excel Visualizations

The workbook already contains prepared charts.

### 📊 Chart 1 — Total Loans by Company

This chart compares the total loan measure of each company.

It helps identify the company with the highest measured loan value.

---

### 🥧 Chart 2 — Market Share by Company

This chart represents the relative contribution of each company to the measured market.

It helps visualize the distribution of the selected market measure.

---

### 📊 Chart 3 — Total Loans by Region

This chart compares the measured loan values across different regions.

It provides a regional view of the business data.

---

## 🔎 Market-Share Calculation Flow

The analysis follows this sequence:

**Raw Data**

↓

**Company Summary**

↓

**Total Market Measure**

↓

**Company Measure**

↓

**Market Share Calculation**

↓

**Percentage Conversion**

↓

**Visualization**

↓

**Business Insight**

---

## 🧮 Formula

The primary formula used in this project is:

**Market Share = Company Measure / Total Market Measure**

For percentage representation:

**Market Share % = Market Share × 100**

---

## 📗 Excel Skills Practiced

Day 016 uses practical Excel concepts such as:

- SUM
- SUMIF
- Division
- Percentage formatting
- Summary tables
- Data comparison
- Bar charts
- Pie charts
- Basic business interpretation

---

## 🔧 Excel Workflow

### Step 1

Open the workbook.

### Step 2

Go to `Market_Data`.

### Step 3

Understand the available columns.

### Step 4

Review company-level data.

### Step 5

Open `Company_Summary`.

### Step 6

Check total loans for each company.

### Step 7

Calculate the total market measure.

### Step 8

Open `Market_Share`.

### Step 9

Calculate company-wise market share.

### Step 10

Format the values as percentages.

### Step 11

Compare the companies.

### Step 12

Review the prepared charts.

### Step 13

Write business insights.

---

## 🏆 Market-Share Ranking

After calculating market share, companies can be ranked from highest to lowest.

The ranking helps identify:

- Market leader
- Second-largest company
- Smaller participants
- Relative differences

Ranking should be performed using the same market measure.

---

## 📊 Why Visualization Matters

A table contains the numerical values.

A chart makes comparison easier.

For example:

A bar chart can quickly show which company has the highest value.

A pie chart can show how the total is distributed among companies.

Visualization therefore supports communication of business analysis.

---

## 🐍 Python Component

The repository also contains Python code.

File:

`code/market_share_analysis.py`

The Python implementation uses:

- Pandas
- Matplotlib
- Seaborn

---

## 🐼 Pandas

Pandas is used to create and manipulate the business dataset.

A DataFrame is used to organize the company-level information.

The market-share calculation is performed using DataFrame operations.

---

## 📊 Matplotlib

Matplotlib is used to create visualizations.

The Python file contains:

- Bar chart
- Pie chart
- Revenue comparison chart

---

## 📈 Seaborn

Seaborn is used for an additional bar-chart visualization.

It provides a convenient interface for creating statistical visualizations.

---

## 🧮 Python Market-Share Logic

The Python analysis follows:

**Company Data**

↓

**Total Loans**

↓

**Market Share**

↓

**Market Share Percentage**

↓

**Ranking**

↓

**Visualization**

↓

**Business Insights**

---

## 🔎 Business Interpretation

Suppose one company has a higher market share than another company.

The higher percentage means that the first company represents a larger portion of the selected market measure.

The interpretation should remain connected to the measure being analyzed.

---

## ⚠️ Important Point

Market share depends on how the market is defined.

The denominator is therefore extremely important.

If the total market measure changes, the calculated market share can also change.

The companies should be compared using the same definition and the same measure.

---

## 💼 Business Analysis Perspective

Market-share analysis can help businesses understand relative competitive position.

It can be used to compare companies.

It can also help organize business data for presentations and decision-making.

However, market share alone does not explain why a company has a particular position.

Additional business analysis may be required to understand causes.

---

## 🧪 Practical Tasks

### Task 1

Open the Excel workbook.

### Task 2

Review the raw data.

### Task 3

Calculate company-wise total loans.

### Task 4

Calculate total market loans.

### Task 5

Calculate market share.

### Task 6

Convert market share into percentage.

### Task 7

Rank the companies.

### Task 8

Review the prepared bar chart.

### Task 9

Review the prepared pie chart.

### Task 10

Create one additional visualization.

### Task 11

Write three business insights.

---

## 🐍 Python Practice

Run:

`code/market_share_analysis.py`

Observe:

- Original dataset
- Total market loans
- Market-share values
- Market-share percentages
- Ranking
- Visualizations
- Business insights

---

## 🔧 Python Modification Practice

Modify the loan value of one company.

Run the program again.

Observe the change in:

- Total market value
- Market share
- Ranking
- Visualization

This helps understand how market-share calculations respond to changes in the underlying data.

---

## 🎯 Mini Challenge

Add another company to the dataset.

Give the company a loan value.

Calculate the new total market value.

Calculate the new market shares.

Rank all companies.

Create an updated chart.

Write three insights.

---

## 📝 Business Insight Format

Use the following structure:

**Insight 1:** The company with the highest measured market share is __________.

**Insight 2:** The company with the lowest measured market share is __________.

**Insight 3:** The market-share distribution indicates __________.

Insights should be based on the calculated data.

---

## 📋 Questions for Revision

1. What is market share?

2. What is the basic market-share formula?

3. What is the numerator?

4. What is the denominator?

5. Why is the denominator important?

6. Why should the same measure be used?

7. How is market share converted into a percentage?

8. Which chart is useful for company comparison?

9. Which chart can represent contribution to a total?

10. Why should business insights be based on data?

---

## 🧠 Key Concepts

### Concept 1 — Relative Measure

Market share is relative rather than simply a raw value.

### Concept 2 — Total Market

The total market measure provides the denominator.

### Concept 3 — Company Measure

The company measure provides the numerator.

### Concept 4 — Percentage

Percentage makes relative comparison easier to communicate.

### Concept 5 — Visualization

Charts provide a visual representation of the calculated result.

### Concept 6 — Insight

An insight explains what the data shows.

---

## 📁 Repository Structure

```text
Day_016_W4_L3_Understanding_Market_Share_Part_1/
│
├── README.md
├── notes.md
├── cheat-sheet.md
├── practice.md
├── resources.md
│
├── Day_016_W4_L3_Understanding_Market_Share_Part_1.xlsx
│
└── code/
    └── market_share_analysis.py