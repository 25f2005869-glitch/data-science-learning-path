"""
Day 091 — Excel Revision
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Day: 091
Topic: Excel Revision

This script supports the Excel revision workflow by:
- Loading business data from the Day 091 workbook
- Checking and cleaning data
- Calculating business metrics
- Creating KPI summaries
- Creating business-function, process, region and monthly summaries
- Creating visualisations
- Exporting analysis results

Required packages:
pandas
matplotlib
openpyxl
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. FILE PATHS
# ============================================================

WORKBOOK = Path("Day_091_Excel_Revision.xlsx")
OUTPUT_DIR = Path("day_091_outputs")

OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD BUSINESS DATA
# ============================================================

print("Loading Day 091 business data...")

df = pd.read_excel(
    WORKBOOK,
    sheet_name="Business_Data",
    header=1
)

df.columns = df.columns.str.strip()


# ============================================================
# 3. BASIC DATA CHECK
# ============================================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ============================================================
# 4. DATA CLEANING
# ============================================================

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

text_columns = [
    "Business_Function",
    "Process",
    "Region"
]

for column in text_columns:
    if column in df.columns:
        df[column] = df[column].astype(str).str.strip()

numeric_columns = [
    "Orders",
    "Revenue_Rupee",
    "Cost_Rupee",
    "Delivery_Days",
    "Deliveries",
    "On_Time_Deliveries",
    "Returned_Orders",
    "Customer_Satisfaction_%",
    "Customers",
    "New_Customers",
    "Ad_Spend_Rupee"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")


# Remove duplicate rows
df = df.drop_duplicates().reset_index(drop=True)


# ============================================================
# 5. CALCULATE BUSINESS METRICS
# ============================================================

df["Profit_Rupee_Calculated"] = (
    df["Revenue_Rupee"] - df["Cost_Rupee"]
)

df["Profit_Margin_%_Calculated"] = (
    df["Profit_Rupee_Calculated"]
    / df["Revenue_Rupee"]
    * 100
)

df["Return_Rate_%_Calculated"] = (
    df["Returned_Orders"]
    / df["Orders"]
    * 100
)

df["On_Time_Rate_%_Calculated"] = (
    df["On_Time_Deliveries"]
    / df["Deliveries"]
    * 100
)

df["Average_Order_Value_Rupee"] = (
    df["Revenue_Rupee"]
    / df["Orders"]
)

df["Cost_Per_Order_Rupee"] = (
    df["Cost_Rupee"]
    / df["Orders"]
)


# ============================================================
# 6. KPI SUMMARY
# ============================================================

total_orders = df["Orders"].sum()
total_revenue = df["Revenue_Rupee"].sum()
total_cost = df["Cost_Rupee"].sum()
total_profit = df["Profit_Rupee_Calculated"].sum()

average_order_value = (
    total_revenue / total_orders
)

profit_margin = (
    total_profit / total_revenue * 100
)

return_rate = (
    df["Returned_Orders"].sum()
    / total_orders
    * 100
)

on_time_rate = (
    df["On_Time_Deliveries"].sum()
    / df["Deliveries"].sum()
    * 100
)

average_customer_satisfaction = (
    df["Customer_Satisfaction_%"].mean()
)

kpi_summary = pd.DataFrame(
    {
        "KPI": [
            "Total Orders",
            "Total Revenue",
            "Total Cost",
            "Total Profit",
            "Average Order Value",
            "Profit Margin",
            "Return Rate",
            "On-Time Delivery Rate",
            "Average Customer Satisfaction"
        ],
        "Value": [
            total_orders,
            total_revenue,
            total_cost,
            total_profit,
            average_order_value,
            profit_margin,
            return_rate,
            on_time_rate,
            average_customer_satisfaction
        ]
    }
)

print("\nKPI Summary:")
print(kpi_summary)


# ============================================================
# 7. BUSINESS FUNCTION SUMMARY
# ============================================================

function_summary = (
    df.groupby("Business_Function")
    .agg(
        Orders=("Orders", "sum"),
        Revenue_Rupee=("Revenue_Rupee", "sum"),
        Cost_Rupee=("Cost_Rupee", "sum"),
        Profit_Rupee=("Profit_Rupee_Calculated", "sum"),
        Average_Customer_Satisfaction=(
            "Customer_Satisfaction_%",
            "mean"
        )
    )
    .reset_index()
)

function_summary["Profit_Margin_%"] = (
    function_summary["Profit_Rupee"]
    / function_summary["Revenue_Rupee"]
    * 100
)

print("\nBusiness Function Summary:")
print(function_summary)


# ============================================================
# 8. PROCESS SUMMARY
# ============================================================

process_summary = (
    df.groupby("Process")
    .agg(
        Orders=("Orders", "sum"),
        Revenue_Rupee=("Revenue_Rupee", "sum"),
        Cost_Rupee=("Cost_Rupee", "sum"),
        Profit_Rupee=("Profit_Rupee_Calculated", "sum"),
        Deliveries=("Deliveries", "sum"),
        On_Time_Deliveries=("On_Time_Deliveries", "sum"),
        Returned_Orders=("Returned_Orders", "sum")
    )
    .reset_index()
)

process_summary["On_Time_Rate_%"] = (
    process_summary["On_Time_Deliveries"]
    / process_summary["Deliveries"]
    * 100
)

process_summary["Return_Rate_%"] = (
    process_summary["Returned_Orders"]
    / process_summary["Orders"]
    * 100
)

print("\nProcess Summary:")
print(process_summary)


# ============================================================
# 9. REGION SUMMARY
# ============================================================

region_summary = (
    df.groupby("Region")
    .agg(
        Orders=("Orders", "sum"),
        Revenue_Rupee=("Revenue_Rupee", "sum"),
        Cost_Rupee=("Cost_Rupee", "sum"),
        Profit_Rupee=("Profit_Rupee_Calculated", "sum"),
        Customer_Satisfaction=(
            "Customer_Satisfaction_%",
            "mean"
        )
    )
    .reset_index()
)

region_summary["Profit_Margin_%"] = (
    region_summary["Profit_Rupee"]
    / region_summary["Revenue_Rupee"]
    * 100
)

print("\nRegion Summary:")
print(region_summary)


# ============================================================
# 10. MONTHLY SUMMARY
# ============================================================

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_summary = (
    df.groupby("Month")
    .agg(
        Orders=("Orders", "sum"),
        Revenue_Rupee=("Revenue_Rupee", "sum"),
        Cost_Rupee=("Cost_Rupee", "sum"),
        Profit_Rupee=("Profit_Rupee_Calculated", "sum")
    )
    .reset_index()
)

monthly_summary["Profit_Margin_%"] = (
    monthly_summary["Profit_Rupee"]
    / monthly_summary["Revenue_Rupee"]
    * 100
)

print("\nMonthly Summary:")
print(monthly_summary)


# ============================================================
# 11. EXPORT ANALYSIS RESULTS
# ============================================================

df.to_csv(
    OUTPUT_DIR / "cleaned_business_data.csv",
    index=False
)

kpi_summary.to_csv(
    OUTPUT_DIR / "kpi_summary.csv",
    index=False
)

function_summary.to_csv(
    OUTPUT_DIR / "business_function_summary.csv",
    index=False
)

process_summary.to_csv(
    OUTPUT_DIR / "process_summary.csv",
    index=False
)

region_summary.to_csv(
    OUTPUT_DIR / "region_summary.csv",
    index=False
)

monthly_summary.to_csv(
    OUTPUT_DIR / "monthly_summary.csv",
    index=False
)


# ============================================================
# 12. CHART 1 — REVENUE BY BUSINESS FUNCTION
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    function_summary["Business_Function"],
    function_summary["Revenue_Rupee"]
)

plt.title("Revenue by Business Function")
plt.xlabel("Business Function")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_business_function.png",
    dpi=300
)

plt.close()


# ============================================================
# 13. CHART 2 — MONTHLY REVENUE TREND
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_summary["Month"],
    monthly_summary["Revenue_Rupee"],
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_revenue_trend.png",
    dpi=300
)

plt.close()


# ============================================================
# 14. CHART 3 — ORDERS BY PROCESS
# ============================================================

plt.figure(figsize=(10, 6))

plt.barh(
    process_summary["Process"],
    process_summary["Orders"]
)

plt.title("Orders by Process")
plt.xlabel("Orders")
plt.ylabel("Process")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "orders_by_process.png",
    dpi=300
)

plt.close()


# ============================================================
# 15. CHART 4 — PROFIT BY REGION
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    region_summary["Region"],
    region_summary["Profit_Rupee"]
)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit (₹)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "profit_by_region.png",
    dpi=300
)

plt.close()


# ============================================================
# 16. CHART 5 — AD SPEND VS REVENUE
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Ad_Spend_Rupee"],
    df["Revenue_Rupee"]
)

plt.title("Ad Spend vs Revenue")
plt.xlabel("Ad Spend (₹)")
plt.ylabel("Revenue (₹)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "ad_spend_vs_revenue.png",
    dpi=300
)

plt.close()


# ============================================================
# 17. BUSINESS INSIGHTS
# ============================================================

highest_revenue_function = function_summary.loc[
    function_summary["Revenue_Rupee"].idxmax(),
    "Business_Function"
]

highest_profit_function = function_summary.loc[
    function_summary["Profit_Rupee"].idxmax(),
    "Business_Function"
]

highest_revenue_region = region_summary.loc[
    region_summary["Revenue_Rupee"].idxmax(),
    "Region"
]

highest_order_process = process_summary.loc[
    process_summary["Orders"].idxmax(),
    "Process"
]

insights = [
    f"Highest revenue business function: {highest_revenue_function}",
    f"Highest profit business function: {highest_profit_function}",
    f"Highest revenue region: {highest_revenue_region}",
    f"Highest order-volume process: {highest_order_process}",
    f"Overall profit margin: {profit_margin:.2f}%",
    f"Overall return rate: {return_rate:.2f}%",
    f"Overall on-time delivery rate: {on_time_rate:.2f}%"
]

insights_df = pd.DataFrame(
    {"Business_Insight": insights}
)

insights_df.to_csv(
    OUTPUT_DIR / "business_insights.csv",
    index=False
)


# ============================================================
# 18. FINAL MESSAGE
# ============================================================

print("\nDay 091 Excel Revision analysis completed.")

print(f"Output folder: {OUTPUT_DIR.resolve()}")

print("\nGenerated files:")
for file in sorted(OUTPUT_DIR.iterdir()):
    print(f"- {file.name}")