# Day 099 — Power BI Extension

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 099  
**Topic:** Power BI Extension

## Overview
Day 099 extends business analytics from Excel into Power BI. The practical goal is to import business data, build a model, create DAX measures, build visuals, add interactivity, and prepare a business dashboard.

## Learning Objectives
- Import Excel data into Power BI
- Understand Power Query
- Build a data model
- Understand relationships
- Create DAX measures
- Build KPI cards and charts
- Use slicers, tables and matrices
- Use tooltips, drillthrough, bookmarks and buttons
- Create a business dashboard
- Write business insights

## Tables
- SalesData
- Dim_Customer
- Dim_Product
- Dim_Date

## Main Relationships
- Dim_Customer[Customer_ID] → SalesData[Customer_ID]
- Dim_Product[Product] → SalesData[Product]
- Dim_Date[Date] → SalesData[Date]

## DAX Measures
- Total Revenue
- Total Cost
- Total Profit
- Profit Margin %
- Total Orders
- Total Quantity
- Average Order Value
- Customers
- Revenue YTD
- Revenue MTD

## Visuals
Card, KPI, Column, Bar, Stacked Column, 100% Stacked, Line, Area, Pie, Donut, Scatter, Combo, Treemap, Waterfall, Funnel, Ribbon, Gauge, Table, Matrix, Slicer and Decomposition Tree.

## Interactive Features
Slicers, cross-filtering, tooltips, drillthrough, bookmarks, buttons and conditional formatting.

## Project Structure
- README.md
- notes.md
- cheat-sheet.md
- practice.md
- resources.md
- POWER_BI_BUILD_GUIDE.md
- code/power_bi_extension.py
- data/Day_099_Power_BI_Extension.xlsx

## Practical Outcome
The final interactive Power BI report is saved from Power BI Desktop as `Day_099_Power_BI_Extension.pbix`.

> The Excel workbook is the practice/source workbook. The `.pbix` file is the actual Power BI report.
