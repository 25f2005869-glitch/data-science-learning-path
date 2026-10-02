![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-036-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 036 Notes — VLOOKUP & Pivot Table

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 036  
**Topic:** VLOOKUP & Pivot Table

## 1. Why Data Retrieval Matters

Business datasets are often split across tables.

One table may contain transactions.

Another table may contain product attributes.

A lookup connects related information.

## 2. Lookup Structure

The lookup value is the value being searched.

The lookup table contains reference information.

The column index identifies the return column.

FALSE requests an exact match.

## 3. VLOOKUP Pattern

The practical pattern is:

VLOOKUP(lookup_value, table_array, col_index_num, FALSE)

The first column of the table array must contain the lookup value.

## 4. Product Example

Product is used as the lookup key.

Product_Master stores Category, Unit_Price and Value_Segment.

VLOOKUP retrieves these attributes into the sales analysis.

## 5. Pivot Table Thinking

A Pivot Table groups records by selected dimensions.

Revenue can be summed by Product.

Units can be summed by Region.

Revenue can be compared by Channel.

## 6. Measures

Sum of Units measures volume.

Sum of Revenue measures monetary value.

Average Unit Price measures the average listed price in a group.

## 7. Product Summary

The Product summary compares four products.

This makes product-level performance easier to inspect than raw rows.

## 8. Region Summary

The Region summary compares North, South and West.

Regional aggregation can support sales planning.

## 9. Channel Summary

The Channel summary compares Online and Retail.

Channel analysis can support distribution analysis.

## 10. Dashboard

The dashboard converts summaries into visual business information.

Charts are used for product revenue, regional revenue and product units.

## 11. Excel Workflow

First inspect the source data.

Then inspect the master table.

Next verify the lookup formulas.

Finally review grouped summaries.

## 12. Python Workflow

pandas merge performs lookup-style enrichment.

groupby and agg create pivot-style summaries.

CSV outputs preserve the calculated summaries.

## 13. Common Errors

A wrong lookup range can return incorrect attributes.

A wrong column index can return the wrong field.

Missing product keys can produce errors or missing values.

## 14. Key Learning

VLOOKUP connects information.

Pivot Tables summarize information.

Both are useful for spreadsheet-based business analytics.

## 🎯 Learning Objectives

- Understand VLOOKUP.
- Understand lookup tables.
- Understand exact matching.
- Understand Pivot Table logic.
- Analyze grouped business data.

## 🔎 Lookup Checklist

Identify the key.

Check the lookup table.

Check the return column.

Use exact match when required.

Verify the returned value.

## 📊 Pivot Checklist

Choose a dimension.

Choose a measure.

Aggregate the measure.

Compare groups.

Interpret the result.

## 🏅 Badges

![VLOOKUP](https://img.shields.io/badge/VLOOKUP-Data%20Retrieval-blue?style=flat-square)
![Pivot](https://img.shields.io/badge/Pivot-Analysis-green?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-BDM-orange?style=flat-square)

## 🔄 Revision Notes

Review the workbook after completing the exercises.

Repeat the lookup from memory.

Repeat the grouped summary without looking at the formulas.

Explain the difference between retrieval and aggregation.

Check the dashboard against the source data.

Record formula errors and their causes.

Keep the lookup table consistent.

Interpret numbers before writing conclusions.