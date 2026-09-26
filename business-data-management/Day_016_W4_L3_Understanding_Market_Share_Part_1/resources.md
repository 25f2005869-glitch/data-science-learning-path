![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-016-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Market%20Share%20Part%201-orange?style=for-the-badge)

# 🔗 Resources — Day 016

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Business Data Management  
**Day:** 016  
**Lecture:** W4_L3  
**Topic:** Understanding Market Share — Part 1

---

## 🎯 01. Learning Purpose

This resource file is designed to support the Day 016 learning process.

The main topic is understanding market share.

The focus is on practical business-data analysis.

The learning process combines spreadsheets and Python.

The goal is to move from raw data to a meaningful comparison.

---

## 🎓 02. Course Context

**Course:** Business Data Management

**Lecture:** W4_L3

**Topic:** Understanding Market Share — Part 1

This day follows the BDM lecture sequence.

The work is organized around the market-share concept.

---

## 📚 03. Main Learning Areas

The Day 016 resources focus on:

- Market share
- Company comparison
- Market measure
- Company measure
- Percentage calculation
- Business data
- Summary tables
- Visualization
- Ranking
- Business insights

---

## 🧠 04. Concept Resources

Before practicing, understand these concepts:

### Market Share

Market share represents a company's portion of a defined market.

### Company Measure

The company measure is the value used for an individual company.

### Total Market Measure

The total market measure is the combined value used as the comparison base.

### Percentage Share

Percentage share expresses the relative value as a percentage.

---

## 🧮 05. Formula Resource

The primary formula is:

**Market Share = Company Measure / Total Market Measure**

Percentage form:

**Market Share % = Market Share × 100**

Equivalent form:

**Market Share % = (Company Measure / Total Market Measure) × 100**

---

## 📗 06. Excel Resources

The Day 016 workbook is the main practical resource.

Workbook:

`Day_016_W4_L3_Understanding_Market_Share_Part_1.xlsx`

Use the workbook to practice:

- Raw-data inspection
- Company summaries
- Market totals
- Market-share calculations
- Percentage formatting
- Ranking
- Charts
- Business interpretation

---

## 📊 07. Excel Sheet Resources

The workbook contains:

### `Market_Data`

Raw business data.

### `Company_Summary`

Company-wise totals.

### `Market_Share`

Market-share calculations.

### `Region_Summary`

Region-wise business summary.

### `Instructions`

Practical instructions.

---

## 🔧 08. Excel Functions

Important functions for this day include:

`SUM`

`SUMIF`

These functions help summarize the business data.

---

## 📊 09. Excel Visualization Resources

Prepared visualizations include:

- Total Loans by Company
- Market Share by Company
- Total Loans by Region

Use these charts to practice visual interpretation.

---

## 🧠 10. Excel Practice Method

Follow this sequence:

**Open Workbook**

↓

**Inspect Data**

↓

**Create Summary**

↓

**Calculate Total**

↓

**Calculate Market Share**

↓

**Format Percentage**

↓

**Create Chart**

↓

**Interpret**

↓

**Write Insight**

---

## 🐍 11. Python Resource

Python file:

`code/market_share_analysis.py`

This file provides a programming-based implementation of the Day 016 analysis.

---

## 🐼 12. Pandas Resource

Pandas is used for:

- Creating the DataFrame
- Storing business data
- Calculating market share
- Sorting companies
- Inspecting results

The DataFrame provides a structured representation of the dataset.

---

## 📈 13. Matplotlib Resource

Matplotlib is used for:

- Bar charts
- Pie charts
- Revenue comparison

These charts provide visual representations of the calculated values.

---

## 📊 14. Seaborn Resource

Seaborn is used for an additional bar visualization.

It works directly with the Pandas DataFrame.

---

## 🧮 15. Python Calculation Resource

The basic calculation follows:

`df["Market_Share"] = df["Loans"] / df["Loans"].sum()`

Percentage calculation follows:

`df["Market_Share_Percent"] = df["Market_Share"] * 100`

---

## 🏆 16. Ranking Resource

Ranking is useful for comparing companies.

Sort market share from highest to lowest.

The first company has the highest calculated share.

The last company has the lowest calculated share.

---

## 📊 17. Chart Selection Resource

Use a **bar chart** when comparing companies.

Use a **pie chart** when showing contribution to a meaningful total.

Always choose a visualization according to the analytical question.

---

## 🔎 18. Interpretation Resource

When reading a market-share chart:

1. Identify the companies.
2. Identify the measure.
3. Check the units.
4. Compare the values.
5. Identify the highest value.
6. Identify the lowest value.
7. Look for meaningful differences.
8. Write a data-supported insight.

---

## 💼 19. Business Analysis Resource

Market-share analysis can support:

- Competitive comparison
- Business reporting
- Performance discussions
- Market understanding
- Data presentations
- Decision-support analysis

Market share alone does not explain the reason behind a company's position.

---

## ⚠️ 20. Data Quality Resource

Before calculating market share, check:

- Company names
- Market names
- Numerical values
- Missing values
- Duplicate records
- Measurement consistency
- Market definition

Incorrect input data can produce incorrect market-share results.

---

## 🧠 21. Denominator Resource

The denominator is especially important.

It represents the total market measure.

All companies being compared should use the same comparison base.

A changed market definition can change the result.

---

## 📌 22. Market Definition Resource

A market can be defined using different dimensions.

Possible dimensions include:

- Geography
- Product
- Customer group
- Industry
- Business segment

The definition should be appropriate to the analysis.

---

## 📊 23. Visualization Practice Resource

Practice these questions:

Which company has the highest value?

Which company has the lowest value?

Which company has the highest share?

How different are the companies?

Which chart communicates the comparison most clearly?

---

## 🧪 24. Practical Resource

Complete the following:

Open the workbook.

Review the raw dataset.

Review the company summary.

Review the market-share table.

Check the calculations.

Study the prepared charts.

Run the Python code.

Compare Excel and Python results.

---

## 🐍 25. Python Practice Resource

After running the Python script:

Change one company's loan value.

Run the program again.

Observe the new market total.

Observe the new market shares.

Observe the ranking.

Observe the charts.

---

## ➕ 26. Extension Practice

Add a new company.

Give it a measured value.

Update the market total.

Calculate the new shares.

Check all percentages.

Update the visualization.

Write new insights.

---

## 📝 27. Insight-Writing Resource

Use this structure:

**Observation**

What does the data show?

**Evidence**

Which calculated value supports the observation?

**Meaning**

What does the observation mean in the context of the selected market measure?

---

## 🎯 28. Recommended Practice Order

### Step 1

Understand the concept.

### Step 2

Inspect the dataset.

### Step 3

Calculate totals.

### Step 4

Calculate shares.

### Step 5

Format percentages.

### Step 6

Create charts.

### Step 7

Rank companies.

### Step 8

Write insights.

### Step 9

Repeat the process in Python.

---

## 📋 29. Revision Questions

1. What is market share?

2. What is the market measure?

3. What is the company measure?

4. What is the denominator?

5. What is the numerator?

6. Why is consistency important?

7. How is market share converted into percentage?

8. Which chart is useful for comparison?

9. What does a higher share indicate?

10. Why should insights be data-supported?

---

## 📚 30. Repository Resources

The Day 016 repository contains:

- `README.md`
- `notes.md`
- `cheat-sheet.md`
- `practice.md`
- `resources.md`
- Excel workbook
- Python analysis file

Together, these files provide the complete learning and practice material for this day.

---

## 🛠️ 31. Tool Stack

### Spreadsheet

Microsoft Excel

### Spreadsheet Alternative

Google Sheets

### Programming

Python

### Data Analysis

Pandas

### Visualization

Matplotlib

### Statistical Visualization

Seaborn

### Repository

Git and GitHub

---

## 🔗 32. GitHub Practice

After completing the work:

Review all files.

Check the Excel workbook.

Check the Python script.

Check Markdown formatting.

Check badges.

Check file names.

Commit the changes.

Push the Day 016 folder to GitHub.

---

## 📸 33. Screenshot Practice

Useful screenshots can include:

- Raw dataset
- Company summary
- Market-share table
- Bar chart
- Pie chart
- Python output

Screenshots can document practical progress.

---

## 🧠 34. Study Tip

Do not memorize the formula alone.

Understand what each part represents.

**Company value** is the numerator.

**Total market value** is the denominator.

The result is the relative share.

Then convert it to a percentage.

---

## ⚠️ 35. Common Mistakes

Avoid:

- Wrong denominator
- Wrong numerator
- Mixed measures
- Incorrect percentage formatting
- Incorrect company grouping
- Misreading charts
- Unsupported business claims

---

## 📊 36. Visualization Reminder

A visualization is useful only when it communicates information clearly.

A chart should have:

- Meaningful title
- Correct data
- Appropriate chart type
- Readable labels
- Correct units

---

## 💼 37. Business Insight Reminder

Do not write:

“The company is successful because of advertising.”

unless the dataset actually contains evidence about advertising.

Instead write:

“The company has the highest measured market share in the dataset.”

This keeps the insight data-supported.

---

## 🔄 38. Excel vs Python

Excel is useful for interactive spreadsheet-based analysis.

Python is useful for repeatable and programmable analysis.

Both can perform calculations.

Both can create visualizations.

The underlying business logic should remain consistent.

---

## 🧮 39. Verification

After calculating market share:

Add all company shares.

The total should be approximately:

**100%**

Small differences can occur because of rounding.

This is a useful validation check.

---

## 🔎 40. Quality Check

Before finalizing the analysis:

Check the source data.

Check totals.

Check formulas.

Check percentages.

Check charts.

Check ranking.

Check insights.

---

## 🎯 41. Mini Project Resource

Create a small market-share analysis using your own dataset.

Use at least five companies.

Include:

- Raw data
- Summary
- Total market
- Market share
- Ranking
- Bar chart
- Pie chart
- Three insights

---

## 📁 42. Suggested Mini-Project Structure

`market-share-project/`

Inside:

`data/`

`analysis/`

`charts/`

`README.md`

`insights.md`

This can be used as an extension exercise.

---

## 📝 43. Documentation Practice

Document:

- Dataset source
- Selected measure
- Market definition
- Calculation method
- Visualization choice
- Main insights

Clear documentation makes analysis easier to understand.

---

## 🚀 44. Learning Progression

The Day 016 learning process moves through:

**Business Data**

→

**Summary**

→

**Market Measure**

→

**Market Share**

→

**Percentage**

→

**Ranking**

→

**Visualization**

→

**Insight**

---

## 🧠 45. Core Knowledge

Remember these five ideas:

1. Market share is relative.
2. The market must be defined.
3. The measure must be consistent.
4. The denominator matters.
5. Insights must be supported by data.

---

## 📌 46. Quick Reference

| Item | Resource |
|---|---|
| Raw data | `Market_Data` |
| Company totals | `Company_Summary` |
| Market share | `Market_Share` |
| Regional totals | `Region_Summary` |
| Instructions | `Instructions` |
| Python analysis | `market_share_analysis.py` |
| Main formula | Company ÷ Total Market |
| Comparison chart | Bar chart |
| Composition chart | Pie chart |

---

## 🧪 47. Completion Checklist

- [ ] Lecture studied
- [ ] Concept understood
- [ ] Dataset inspected
- [ ] Company summary reviewed
- [ ] Market total calculated
- [ ] Market share calculated
- [ ] Percentages checked
- [ ] Ranking completed
- [ ] Bar chart reviewed
- [ ] Pie chart reviewed
- [ ] Python script run
- [ ] Python visualization reviewed
- [ ] Data modified
- [ ] New company practice completed
- [ ] Insights written
- [ ] Files committed to GitHub

---

## 🏁 48. Final Resource Summary

The most important resources for Day 016 are the practical Excel workbook and Python script.

The Markdown files provide conceptual support.

The Excel workbook provides spreadsheet practice.

The Python script provides programming practice.

The charts provide visualization practice.

The practice tasks provide hands-on reinforcement.

The final objective is to understand the complete workflow rather than only memorize a formula.

---

## 💡 49. Final Takeaway

Market share provides a relative comparison.

The calculation depends on a clearly defined market.

The selected measure must remain consistent.

The total market value is the denominator.

The company value is the numerator.

The result can be expressed as a percentage.

Visualization makes comparison easier.

Python can automate the calculation.

Excel can provide an interactive analysis environment.

The final result should be communicated through clear, data-supported insights.

---

## 🎓 50. Day 016 Completion

**Course:** Business Data Management

**Lecture:** W4_L3

**Topic:** Understanding Market Share — Part 1

**Practical Areas:** Excel + Python + Visualization

**Status:** 📚 Learning + 🧪 Practice + 📊 Analysis

**Repository Goal:** Build a clear and reproducible market-share analysis.

**Final Flow:**

**Data → Summary → Market Total → Market Share → Percentage → Ranking → Visualization → Insight**