# Day 099 — Power BI Extension Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 099  
**Topic:** Power BI Extension

## Workflow
Get Data → Power Query → Model → DAX → Visuals → Interaction → Dashboard

## Tables
- SalesData
- Dim_Customer
- Dim_Product
- Dim_Date

## Core DAX
Total Revenue = SUM(SalesData[Revenue])

Total Cost = SUM(SalesData[Cost])

Total Profit = [Total Revenue] - [Total Cost]

Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)

Total Orders = DISTINCTCOUNT(SalesData[Order_ID])

Total Quantity = SUM(SalesData[Quantity])

Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)

Customers = DISTINCTCOUNT(SalesData[Customer_ID])

## Visual Selection
- Card → KPI
- Column → Category comparison
- Bar → Ranking/comparison
- Line → Trend
- Pie/Donut → Composition
- Scatter → Relationship
- Treemap → Hierarchical composition
- Waterfall → Change
- Funnel → Stages
- Gauge → Target/progress
- Matrix → Detailed cross-tab
- Slicer → Interactive filter
- Decomposition Tree → Root-cause exploration

## Final Check
Data loaded, types checked, relationships checked, measures created, visuals formatted, slicers tested, drillthrough tested, tooltip tested, bookmarks tested, dashboard completed, insights written.
