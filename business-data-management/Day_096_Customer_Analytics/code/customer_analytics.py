# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 096
# Topic: Customer Analytics

import os
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. FIND INPUT FILE
# ============================================================

def find_workbook():
    possible_paths = [
        Path("/mnt/data/Day_096_Customer_Analytics.xlsx"),
        Path("Day_096_Customer_Analytics.xlsx"),
        Path("data/Day_096_Customer_Analytics.xlsx"),
    ]

    for path in possible_paths:
        if path.exists():
            return path

    raise FileNotFoundError(
        "Day_096_Customer_Analytics.xlsx was not found."
    )


INPUT_FILE = find_workbook()

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD RAW CUSTOMER DATA
# ============================================================

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Raw_Customer_Data",
    header=3
)

print("\n========== RAW CUSTOMER DATA ==========")
print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 3. DATA INSPECTION
# ============================================================

print("\n========== DATA INFORMATION ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isna().sum())

print("\n========== DUPLICATE ROWS ==========")
print("Duplicate rows:", df.duplicated().sum())

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe(include="all"))


# ============================================================
# 4. DATA CLEANING
# ============================================================

clean_df = df.copy()

# ------------------------------------------------------------
# Text cleaning
# ------------------------------------------------------------

text_columns = [
    "Customer_ID",
    "Customer_Name",
    "Gender",
    "City",
    "Region",
    "Customer_Segment",
    "Product_Category",
    "Customer_Status",
    "Payment_Method",
]

for column in text_columns:
    if column in clean_df.columns:
        clean_df[column] = clean_df[column].astype("string").str.strip()


# ------------------------------------------------------------
# Standardise categorical values
# ------------------------------------------------------------

for column in [
    "Gender",
    "City",
    "Region",
    "Customer_Segment",
    "Product_Category",
    "Customer_Status",
]:
    if column in clean_df.columns:
        clean_df[column] = clean_df[column].str.title()

if "Payment_Method" in clean_df.columns:
    clean_df["Payment_Method"] = clean_df["Payment_Method"].str.title()

    clean_df["Payment_Method"] = clean_df["Payment_Method"].replace(
        {"Upi": "UPI"}
    )


# ------------------------------------------------------------
# Date cleaning
# ------------------------------------------------------------

clean_df["Date"] = pd.to_datetime(
    clean_df["Date"],
    errors="coerce"
)

median_date = clean_df["Date"].dropna().median()

clean_df["Date"] = clean_df["Date"].fillna(median_date)


# ------------------------------------------------------------
# Numeric conversion
# ------------------------------------------------------------

numeric_columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Revenue",
    "Customer_Satisfaction",
]

for column in numeric_columns:
    clean_df[column] = pd.to_numeric(
        clean_df[column],
        errors="coerce"
    )


# ============================================================
# 5. HANDLE MISSING VALUES
# ============================================================

# Age
median_age = clean_df["Age"].median()

clean_df["Age"] = clean_df["Age"].fillna(median_age)


# Quantity
clean_df["Quantity"] = clean_df["Quantity"].fillna(1)

clean_df.loc[
    clean_df["Quantity"] <= 0,
    "Quantity"
] = 1


# Unit Price
category_price = {
    "Electronics": 18000,
    "Furniture": 9500,
    "Stationery": 850,
    "Accessories": 2200,
}

for category, price in category_price.items():
    mask = (
        clean_df["Product_Category"].eq(category)
        & clean_df["Unit_Price"].isna()
    )

    clean_df.loc[mask, "Unit_Price"] = price


# Remaining missing Unit Price
clean_df["Unit_Price"] = clean_df["Unit_Price"].fillna(
    clean_df["Unit_Price"].median()
)


# Customer Satisfaction
median_satisfaction = clean_df[
    "Customer_Satisfaction"
].median()

clean_df["Customer_Satisfaction"] = (
    clean_df["Customer_Satisfaction"]
    .fillna(median_satisfaction)
)


# ============================================================
# 6. RECALCULATE REVENUE
# ============================================================

clean_df["Revenue"] = (
    clean_df["Quantity"]
    * clean_df["Unit_Price"]
)


# ============================================================
# 7. REMOVE DUPLICATES
# ============================================================

before_duplicates = len(clean_df)

clean_df = clean_df.drop_duplicates().reset_index(drop=True)

after_duplicates = len(clean_df)

print("\n========== DUPLICATE CLEANING ==========")
print("Rows before:", before_duplicates)
print("Rows after :", after_duplicates)
print("Duplicates removed:", before_duplicates - after_duplicates)


# ============================================================
# 8. CUSTOMER-LEVEL INFORMATION
# ============================================================

customer_order_count = (
    clean_df
    .groupby("Customer_ID")["Order_ID"]
    .count()
)

clean_df["Repeat_Customer"] = (
    clean_df["Customer_ID"]
    .map(customer_order_count)
    .gt(1)
    .map({True: "Yes", False: "No"})
)


# Customer Spend Band
clean_df["Customer_Spend_Band"] = np.select(
    [
        clean_df["Revenue"] >= 30000,
        clean_df["Revenue"] >= 10000,
    ],
    [
        "High",
        "Medium",
    ],
    default="Low",
)


# ============================================================
# 9. CUSTOMER SUMMARY
# ============================================================

total_customers = clean_df["Customer_ID"].nunique()
total_orders = clean_df["Order_ID"].nunique()
total_revenue = clean_df["Revenue"].sum()

average_customer_spend = (
    total_revenue / total_customers
    if total_customers
    else 0
)

average_order_value = (
    total_revenue / total_orders
    if total_orders
    else 0
)

average_satisfaction = clean_df[
    "Customer_Satisfaction"
].mean()

repeat_customers = (
    customer_order_count
    .gt(1)
    .sum()
)

repeat_customer_rate = (
    repeat_customers / total_customers
    if total_customers
    else 0
)

active_customers = clean_df.loc[
    clean_df["Customer_Status"].eq("Active"),
    "Customer_ID"
].nunique()


customer_summary = pd.DataFrame(
    {
        "Metric": [
            "Total Customers",
            "Total Orders",
            "Total Revenue",
            "Average Customer Spend",
            "Average Order Value",
            "Average Customer Satisfaction",
            "Repeat Customers",
            "Repeat Customer Rate",
            "Active Customers",
        ],
        "Value": [
            total_customers,
            total_orders,
            total_revenue,
            average_customer_spend,
            average_order_value,
            average_satisfaction,
            repeat_customers,
            repeat_customer_rate,
            active_customers,
        ],
    }
)

customer_summary.to_csv(
    OUTPUT_DIR / "customer_summary.csv",
    index=False
)


# ============================================================
# 10. CUSTOMER SEGMENT ANALYSIS
# ============================================================

segment_analysis = (
    clean_df
    .groupby("Customer_Segment")
    .agg(
        Unique_Customers=("Customer_ID", "nunique"),
        Orders=("Order_ID", "nunique"),
        Revenue=("Revenue", "sum"),
        Avg_Order_Value=("Revenue", "mean"),
        Avg_Satisfaction=("Customer_Satisfaction", "mean"),
    )
    .reset_index()
)

segment_analysis.to_csv(
    OUTPUT_DIR / "customer_segment_analysis.csv",
    index=False
)


# ============================================================
# 11. PRODUCT CATEGORY ANALYSIS
# ============================================================

category_analysis = (
    clean_df
    .groupby("Product_Category")
    .agg(
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Avg_Order_Value=("Revenue", "mean"),
    )
    .reset_index()
)

category_analysis.to_csv(
    OUTPUT_DIR / "product_category_analysis.csv",
    index=False
)


# ============================================================
# 12. REGION ANALYSIS
# ============================================================

region_analysis = (
    clean_df
    .groupby("Region")
    .agg(
        Unique_Customers=("Customer_ID", "nunique"),
        Orders=("Order_ID", "nunique"),
        Revenue=("Revenue", "sum"),
        Avg_Order_Value=("Revenue", "mean"),
        Avg_Satisfaction=("Customer_Satisfaction", "mean"),
    )
    .reset_index()
)

region_analysis.to_csv(
    OUTPUT_DIR / "region_analysis.csv",
    index=False
)


# ============================================================
# 13. MONTHLY CUSTOMER ANALYSIS
# ============================================================

clean_df["Month"] = clean_df["Date"].dt.to_period("M").astype(str)

monthly_analysis = (
    clean_df
    .groupby("Month")
    .agg(
        Unique_Customers=("Customer_ID", "nunique"),
        Orders=("Order_ID", "nunique"),
        Revenue=("Revenue", "sum"),
        Avg_Order_Value=("Revenue", "mean"),
        Avg_Satisfaction=("Customer_Satisfaction", "mean"),
    )
    .reset_index()
)

monthly_analysis.to_csv(
    OUTPUT_DIR / "monthly_customer_analysis.csv",
    index=False
)


# ============================================================
# 14. CUSTOMER SPENDING ANALYSIS
# ============================================================

customer_spending = (
    clean_df
    .groupby("Customer_ID")
    .agg(
        Customer_Name=("Customer_Name", "first"),
        Customer_Segment=("Customer_Segment", "first"),
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Avg_Satisfaction=("Customer_Satisfaction", "mean"),
    )
    .reset_index()
)

customer_spending["Repeat_Customer"] = np.where(
    customer_spending["Orders"] > 1,
    "Yes",
    "No",
)

customer_spending.to_csv(
    OUTPUT_DIR / "customer_spending_analysis.csv",
    index=False
)


# ============================================================
# 15. CUSTOMER KPI ANALYSIS
# ============================================================

average_orders_per_customer = (
    total_orders / total_customers
    if total_customers
    else 0
)

customer_kpi = pd.DataFrame(
    {
        "KPI": [
            "Total Customers",
            "Active Customers",
            "Total Revenue",
            "Average Customer Spend",
            "Average Order Value",
            "Total Orders",
            "Average Orders per Customer",
            "Repeat Customers",
            "Repeat Customer Rate",
            "Average Satisfaction",
        ],
        "Value": [
            total_customers,
            active_customers,
            total_revenue,
            average_customer_spend,
            average_order_value,
            total_orders,
            average_orders_per_customer,
            repeat_customers,
            repeat_customer_rate,
            average_satisfaction,
        ],
    }
)

customer_kpi.to_csv(
    OUTPUT_DIR / "customer_kpi_summary.csv",
    index=False
)


# ============================================================
# 16. CLEANED DATA OUTPUT
# ============================================================

cleaned_output = clean_df.copy()

cleaned_output.to_csv(
    OUTPUT_DIR / "cleaned_customer_data.csv",
    index=False
)


# ============================================================
# 17. CHART 1 — CUSTOMER COUNT BY SEGMENT
# ============================================================

plt.figure(figsize=(9, 6))

plt.bar(
    segment_analysis["Customer_Segment"],
    segment_analysis["Unique_Customers"]
)

plt.title("Customer Count by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Unique Customers")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "customer_count_by_segment.png",
    dpi=150
)

plt.close()


# ============================================================
# 18. CHART 2 — REVENUE BY SEGMENT
# ============================================================

plt.figure(figsize=(9, 6))

plt.bar(
    segment_analysis["Customer_Segment"],
    segment_analysis["Revenue"]
)

plt.title("Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Revenue")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_segment.png",
    dpi=150
)

plt.close()


# ============================================================
# 19. CHART 3 — REVENUE BY REGION
# ============================================================

plt.figure(figsize=(9, 6))

plt.bar(
    region_analysis["Region"],
    region_analysis["Revenue"]
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_region.png",
    dpi=150
)

plt.close()


# ============================================================
# 20. CHART 4 — MONTHLY CUSTOMER REVENUE TREND
# ============================================================

plt.figure(figsize=(11, 6))

plt.plot(
    monthly_analysis["Month"],
    monthly_analysis["Revenue"],
    marker="o"
)

plt.title("Monthly Customer Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_customer_trend.png",
    dpi=150
)

plt.close()


# ============================================================
# 21. PRINT FINAL SUMMARY
# ============================================================

print("\n========================================")
print("DAY 096 — CUSTOMER ANALYTICS COMPLETE")
print("========================================")

print("\nInput file:")
print(INPUT_FILE)

print("\nCleaned data shape:")
print(clean_df.shape)

print("\nCustomer Summary:")
print(customer_summary.to_string(index=False))

print("\nOutput directory:")
print(OUTPUT_DIR)

print("\nGenerated files:")

for file in sorted(OUTPUT_DIR.iterdir()):
    print(" -", file.name)

print("\nCustomer Analytics analysis completed successfully.")