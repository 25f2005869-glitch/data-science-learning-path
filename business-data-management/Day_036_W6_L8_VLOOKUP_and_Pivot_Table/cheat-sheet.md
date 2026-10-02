![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-036-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 036 Cheat Sheet — VLOOKUP & Pivot Table

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 036  
**Topic:** VLOOKUP & Pivot Table

## 🔎 VLOOKUP Syntax

VLOOKUP(lookup_value, table_array, col_index_num, FALSE)

## 🧱 Arguments

- lookup_value → value to find
- table_array → lookup table
- col_index_num → return column number
- FALSE → exact match

## 🎯 Example

=VLOOKUP(B2,Product_Master!$A$2:$D$5,2,FALSE)

## 💰 Price Retrieval

=VLOOKUP(B2,Product_Master!$A$2:$D$5,3,FALSE)

## 🏷️ Segment Retrieval

=VLOOKUP(B2,Product_Master!$A$2:$D$5,4,FALSE)

## 📊 Summary Functions

SUMIF can reproduce a simple grouped total.

AVERAGEIF can reproduce a grouped average.

## 📌 SUMIF Pattern

=SUMIF(criteria_range,criteria,sum_range)

## 📌 AVERAGEIF Pattern

=AVERAGEIF(criteria_range,criteria,average_range)

## 🧮 Revenue

Revenue = Units × Unit Price

## 🗂️ Pivot Dimensions

- Product
- Region
- Channel

## 📈 Pivot Measures

- Total Units
- Total Revenue
- Average Unit Price

## 🧠 Remember

VLOOKUP = retrieve.

Pivot Table = summarize.

Lookup key = matching field.

Exact match = FALSE.

First lookup-table column = lookup key.

## 🛠️ Troubleshooting

Check spelling.

Check lookup range.

Check column index.

Check exact-match argument.

Check missing keys.

## 🐍 Python Equivalent

pandas.merge is the lookup-style operation.

groupby plus agg is the pivot-style operation.

## 🏅 Quick Reference

Use VLOOKUP when information must be retrieved from another table.

Use Pivot Tables when information must be grouped and summarized.

## 🔄 Revision Notes

Review the workbook after completing the exercises.

Repeat the lookup from memory.

Repeat the grouped summary without looking at the formulas.

Explain retrieval versus aggregation.

Check the dashboard against the source data.

Record formula errors and their causes.

Keep the lookup table clean.

Interpret numbers before conclusions.

Use absolute references for reusable lookup ranges.