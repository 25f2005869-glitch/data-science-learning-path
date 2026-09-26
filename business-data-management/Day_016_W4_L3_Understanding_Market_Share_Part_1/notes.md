![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-016-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Market%20Share%20Part%201-orange?style=for-the-badge)

# 📝 Notes — Understanding Market Share — Part 1

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Business Data Management  
**Day:** 016  
**Lecture:** W4_L3  
**Topic:** Understanding Market Share — Part 1

---

## 🎯 1. Learning Objective

The main objective of this lecture is to understand the concept of **market share**.

Market share helps compare companies within a defined market.

It provides a relative view of a company's position.

Instead of looking only at the company's raw value, we compare it with the total market value.

---

## 🧠 2. What Is Market Share?

Market share represents the portion of a defined market associated with a company.

It is a relative measure.

For example, if four companies operate in the same market, their individual values can be compared with the combined market value.

This produces a percentage for each company.

The percentages can then be compared.

---

## 📌 3. Basic Formula

The basic formula is:

**Market Share = Company Measure / Total Market Measure**

For percentage representation:

**Market Share % = (Company Measure / Total Market Measure) × 100**

The same denominator should be used when comparing companies within the same market.

---

## 🔢 4. Simple Example

Suppose the market has a total measured value of:

**100 units**

Company A has:

**25 units**

Then:

**Market Share = 25 / 100**

Therefore:

**Market Share = 0.25**

As a percentage:

**Market Share = 25%**

---

## 📊 5. Company Measure

The company measure is the value associated with an individual company.

Depending on the business problem, different measures may be used.

In this Day 016 practice dataset, **Loans** are used as the primary market measure.

Therefore, the company loan value becomes the numerator.

---

## 🏢 6. Total Market Measure

The total market measure is the combined value of all companies included in the defined market.

For the Day 016 exercise:

**Total Market Loans = Sum of all company loan values**

This value becomes the denominator.

---

## ⚠️ 7. Why the Denominator Matters

The denominator defines the comparison base.

If the total market changes, the calculated market share can change.

Therefore, the market definition must be clear.

The companies should be compared using a consistent measure.

---

## 📋 8. Day 016 Dataset

The workbook contains the following business fields:

| Field | Meaning |
|---|---|
| Company | Company name |
| Market | Region or market |
| Loans | Loan measure |
| Customers | Customer count |
| Revenue_Lakh | Revenue measure |

The dataset is designed for practical market-share analysis.

---

## 📗 9. Excel Sheet — Market_Data

The `Market_Data` sheet contains the raw business information.

Each row represents a company-market observation.

The sheet can be used as the starting point for analysis.

Before calculating anything, inspect the data.

Check the company names.

Check the market names.

Check the numerical columns.

---

## 📊 10. Excel Sheet — Company_Summary

The `Company_Summary` sheet summarizes the business data by company.

It provides:

- Total Loans
- Total Customers
- Total Revenue

This summary makes company comparison easier.

---

## 🧮 11. Excel Sheet — Market_Share

The `Market_Share` sheet contains:

- Company
- Total Loans
- Market Share %

The market-share percentage is calculated using the company loan value divided by total market loans.

---

## 📐 12. Excel Calculation

The general calculation pattern is:

**Company Value ÷ Total Market Value**

For example:

`=B2/SUM($B$2:$B$5)`

The result can then be formatted as a percentage.

---

## 🔧 13. SUM Function

`SUM` can be used to calculate the total market measure.

Example:

`=SUM(B2:B5)`

This adds all company values.

The result becomes the market total.

---

## 🔧 14. SUMIF Function

`SUMIF` can be used when company-level totals need to be calculated from raw data.

General pattern:

`=SUMIF(criteria_range,criteria,sum_range)`

It allows a selected company's values to be summarized.

---

## 📊 15. Visualization

Market-share results can be represented visually.

The Day 016 workbook contains prepared charts.

These charts help compare the companies.

Visualization makes numerical comparison easier to communicate.

---

## 📊 16. Bar Chart

A bar chart is useful for comparing companies.

The company names appear as categories.

The market-share percentage becomes the measure.

The height of each bar represents the relative value.

This makes ranking easier to see.

---

## 🥧 17. Pie Chart

A pie chart can represent the contribution of companies to a meaningful total.

In the workbook, the company loan values are used to show the distribution.

The slices represent the relative contribution of the companies.

---

## 📊 18. Region Summary

The workbook also contains a `Region_Summary` sheet.

It summarizes:

- Total Loans
- Total Customers
- Revenue

The regional summary provides another perspective on the business dataset.

---

## 🏆 19. Market-Share Ranking

After calculating market share, companies can be ranked.

The company with the highest percentage has the largest share of the selected measured market.

The company with the lowest percentage has the smallest share.

Ranking helps communicate relative position.

---

## 🔎 20. Business Interpretation

Market share should be interpreted carefully.

A higher market share means a larger portion of the measured market.

It does not automatically explain why the company has that share.

Additional business analysis may be needed to understand causes.

---

## 💼 21. Business Use

Market-share analysis can help businesses:

- Compare competitors
- Understand relative position
- Monitor business measures
- Communicate performance
- Support business discussions
- Prepare analytical reports

The usefulness depends on having a clearly defined market and consistent measure.

---

## 🐍 22. Python Analysis

The repository contains:

`code/market_share_analysis.py`

The script performs the same basic analysis programmatically.

Python is useful when the dataset becomes larger or the analysis needs to be repeated.

---

## 🐼 23. Pandas

Pandas is used to create the DataFrame.

It allows the business data to be stored in rows and columns.

It also supports calculations and sorting.

The market-share calculation can be performed directly on DataFrame columns.

---

## 📈 24. Matplotlib

Matplotlib is used for visualization.

The Python file includes:

- Bar chart
- Pie chart
- Revenue comparison

These visualizations help communicate the calculated results.

---

## 📊 25. Seaborn

Seaborn is used for an additional bar visualization.

It works with Pandas DataFrames.

It provides a convenient way to create statistical-style charts.

---

## 🧮 26. Python Calculation

The basic calculation is:

`df["Market_Share"] = df["Loans"] / df["Loans"].sum()`

This calculates the relative share of each company.

The percentage can be obtained by multiplying the share by 100.

---

## 📈 27. Percentage Conversion

The Python calculation can use:

`df["Market_Share_Percent"] = df["Market_Share"] * 100`

This creates a percentage representation.

The percentage makes comparison easier to communicate.

---

## 🏅 28. Ranking in Python

Companies can be sorted using market share.

A descending sort places the company with the highest market share first.

This creates a simple market-share ranking.

---

## 🔍 29. Reading a Market-Share Chart

When reading a chart, first identify:

- The categories
- The measure
- The units
- The title
- The relative values

Then compare the companies.

Finally, convert the observation into a business statement.

---

## ⚠️ 30. Common Mistakes

Common mistakes include:

- Using the wrong denominator
- Mixing different measures
- Using inconsistent market definitions
- Forgetting percentage conversion
- Misreading chart values
- Making unsupported conclusions

Always verify the calculation before interpreting it.

---

## 🧠 31. Important Distinction

A raw value is not the same as market share.

For example:

**Company A Loans = 14,900**

is a raw value.

But:

**Company A Market Share = Company A Loans / Total Market Loans**

is a relative measure.

This distinction is important.

---

## 📌 32. Market Definition

A market should have a clear boundary.

The boundary may be based on factors such as:

- Geography
- Product
- Customer group
- Industry
- Business segment

The exact definition depends on the business analysis.

---

## 📊 33. Consistent Measure

If one company is measured using loans, the comparison should use loans for the other companies as well.

Do not compare one company's loans with another company's revenue when calculating market share.

The numerator and denominator must represent the same measure.

---

## 🎯 34. Interpretation Rule

A simple interpretation rule is:

**Higher company measure relative to the total → Higher market share**

and:

**Lower company measure relative to the total → Lower market share**

This is the foundation of the calculation.

---

## 🧪 35. Practical Exercise

Open the Day 016 Excel workbook.

Go to `Market_Data`.

Review the raw data.

Open `Company_Summary`.

Review company-level totals.

Open `Market_Share`.

Check the calculated percentages.

Review the prepared charts.

Write three observations.

---

## 🔧 36. Modification Exercise

Change one company's loan value.

Recalculate the total market value.

Recalculate market shares.

Check whether the ranking changes.

Observe how the chart changes.

This demonstrates that market share depends on the underlying values.

---

## ➕ 37. Add a Company

Add a new company.

Assign a loan value.

Add the company to the summary.

Recalculate the market total.

Recalculate every market share.

Check whether the existing percentages change.

This is a useful practical exercise.

---

## 🐍 38. Python Practice

Run the Python file.

Observe the original DataFrame.

Observe the total market loans.

Observe market-share percentages.

Observe the ranking.

Observe the charts.

Then modify the data.

Run the script again.

Compare the results.

---

## 💡 39. Business Insight

A business insight should describe an important pattern found in the data.

For example:

**The company with the highest market share represents the largest portion of the selected market measure.**

The insight should be supported by the calculated values.

---

## 📝 40. Insight Writing Format

Use:

**Observation → Evidence → Meaning**

Example:

**Observation:** Company A has the highest market share.

**Evidence:** Its calculated percentage is the highest among the companies.

**Meaning:** Company A represents the largest portion of the measured market in this dataset.

---

## 📊 41. Chart Selection

Use a bar chart when comparison is the primary question.

Use a pie chart when composition of a meaningful whole is the primary question.

The chart should match the analytical purpose.

---

## 🧠 42. Key Learning

The main learning of Day 016 is not just the formula.

The important workflow is:

**Define → Measure → Calculate → Visualize → Interpret**

This workflow can be reused for many business-data problems.

---

## 🔁 43. Revision Questions

1. What is market share?

2. What is the market-share formula?

3. What is the numerator?

4. What is the denominator?

5. Why is the denominator important?

6. Why should the measure be consistent?

7. How is market share converted into percentage?

8. Which chart is useful for comparison?

9. What does a higher market share indicate?

10. Why should insights be data-supported?

---

## 📋 44. Quick Revision Table

| Concept | Meaning |
|---|---|
| Market Share | Relative market portion |
| Company Measure | Individual company value |
| Market Measure | Total comparison value |
| Numerator | Company value |
| Denominator | Total market value |
| Percentage | Share × 100 |
| Bar Chart | Category comparison |
| Pie Chart | Composition |
| Ranking | Ordered comparison |
| Insight | Data-supported interpretation |

---

## 🚀 45. Final Learning Flow

**Raw Data**

↓

**Company Summary**

↓

**Total Market Measure**

↓

**Company Measure**

↓

**Market Share**

↓

**Percentage**

↓

**Ranking**

↓

**Visualization**

↓

**Business Insight**

---

## ✅ 46. Completion Checklist

- [ ] W4_L3 studied
- [ ] Market share understood
- [ ] Market definition understood
- [ ] Company measure identified
- [ ] Total market measure calculated
- [ ] Market share calculated
- [ ] Percentage calculated
- [ ] Company ranking checked
- [ ] Bar chart reviewed
- [ ] Pie chart reviewed
- [ ] Region summary reviewed
- [ ] Python code executed
- [ ] Python visualization reviewed
- [ ] Data modification practiced
- [ ] Business insights written

---

## 🏁 47. Final Takeaway

Market share provides a relative view of a company's position within a defined market.

The calculation depends on a company measure and a total market measure.

The formula is simple:

**Market Share = Company Measure / Total Market Measure**

The result can be converted into a percentage.

Excel can be used to calculate and visualize the result.

Python can be used to automate the analysis.

Charts make comparison easier.

The final objective is to move from numbers to meaningful business understanding.

**Day 016 complete: Data → Market Share → Visualization → Insight.**