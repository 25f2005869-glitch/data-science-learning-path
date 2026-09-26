![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-016-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Market%20Share%20Part%201-orange?style=for-the-badge)

# ⚡ Cheat Sheet — Understanding Market Share — Part 1

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 016  
**Topic:** W4_L3 — Understanding Market Share — Part 1

## 📌 01. Market Share

Market share is a relative measure.

It shows the portion of a defined market represented by a company.

It is used for comparison.

The market must be clearly defined.

The measure must be consistent.

## 🧮 02. Basic Formula

Market Share = Company Measure / Total Market Measure

## 📊 03. Percentage Formula

Market Share % = (Company Measure / Total Market Measure) × 100

## 🔢 04. Simple Example

Company value = 20

Total market value = 100

Market Share = 20 / 100

Market Share = 0.20

Market Share % = 20%

## 🧠 05. Important Terms

Company Measure → value belonging to one company.

Total Market Measure → combined value of the defined market.

Market Share → company's relative portion.

Percentage Share → market share expressed as percentage.

## 📗 06. Excel Workflow

Step 1 → Enter raw data.

Step 2 → Check column names.

Step 3 → Summarize company values.

Step 4 → Calculate total market value.

Step 5 → Calculate company share.

Step 6 → Convert share into percentage.

Step 7 → Format percentage.

Step 8 → Create chart.

Step 9 → Interpret chart.

Step 10 → Write insight.

## 🔧 07. Useful Excel Functions

SUM

SUMIF

COUNT

COUNTA

## 🧮 08. Excel Formula Pattern

=Company_Value/Total_Market_Value

## 📊 09. Bar Chart

Use a bar chart for category comparison.

Company versus market share is a suitable comparison.

Higher bars indicate larger values.

## 🥧 10. Pie Chart

A pie chart can show contribution to a meaningful total.

Use a small number of meaningful categories.

## 🐍 11. Python Libraries

Pandas

Matplotlib

Seaborn

## 🐼 12. Pandas Calculation

df["Market_Share"] = df["Loans"] / df["Loans"].sum()

## 📈 13. Percentage Conversion

df["Market_Share_Percent"] = df["Market_Share"] * 100

## 📊 14. Matplotlib Bar

plt.bar(df["Company"], df["Market_Share_Percent"])

## 🥧 15. Matplotlib Pie

plt.pie(df["Loans"], labels=df["Company"])

## 📉 16. Seaborn

sns.barplot(data=df, x="Company", y="Market_Share_Percent")

## 🏆 17. Ranking

Sort market share from highest to lowest.

Highest value → first position.

Lowest value → last position.

## 🔎 18. Interpretation

Higher market share means a larger portion of the measured market.

Lower market share means a smaller portion.

The comparison is meaningful only when the measure and market definition are consistent.

## ⚠️ 19. Common Mistakes

Wrong denominator.

Mixing different measures.

Incorrect percentage calculation.

Using inconsistent data.

Misreading a chart.

Making unsupported explanations.

## 🎯 20. Five-Step Method

1. Define the market.
2. Select the measure.
3. Calculate total.
4. Calculate company shares.
5. Visualize and interpret.

## 📋 21. Quick Checklist

☐ Market defined

☐ Measure selected

☐ Total calculated

☐ Share calculated

☐ Percentage formatted

☐ Chart created

☐ Ranking checked

☐ Insight written

## 💡 22. Key Reminder

Market share is a relative measure.

Raw value alone is not market share.

The denominator is important.

The same denominator should be used for comparison.

Charts help communicate the result.

Business insights must be data-supported.

## 🔁 23. Revision

Define.

Measure.

Total.

Divide.

Convert.

Visualize.

Compare.

Interpret.

Communicate.

## 🚀 24. Final Formula

Business Data → Total Market → Company Share → Percentage → Visualization → Insight