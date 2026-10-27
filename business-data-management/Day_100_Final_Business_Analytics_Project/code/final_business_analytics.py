# Day 100 — Final Business Analytics Project
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 100
# Topic: Final Business Analytics Project

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WORKBOOK_PATH = DATA_DIR / "Day_100_Final_Business_Analytics_Project.xlsx"

# Fallback paths for easier execution from the working directory.
if not WORKBOOK_PATH.exists():
    fallback_paths = [
        Path("/mnt/data/Day_100_Final_Business_Analytics_Project.xlsx"),
        Path("Day_100_Final_Business_Analytics_Project.xlsx"),
    ]

    for path in fallback_paths:
        if path.exists():
            WORKBOOK_PATH = path
            break


# ============================================================
# 2. CHECK INPUT FILE
# ============================================================

if not WORKBOOK_PATH.exists():
    raise FileNotFoundError(
        "Day_100_Final_Business_Analytics_Project.xlsx was not found.\n"
        "Place the workbook inside the data folder or update WORKBOOK_PATH."
    )


# ============================================================
# 3. LOAD SALES DATA
# ============================================================

print("=" * 70)
print("DAY 100 — FINAL BUSINESS ANALYTICS PROJECT")
print("=" * 70)

print(f"\nWorkbook: {WORKBOOK_PATH}")

excel_file = pd.ExcelFile(WORKBOOK_PATH)

print("\nAvailable sheets:")
for sheet in excel_file.sheet_names:
    print(f"- {sheet}")

# The workbook contains a prepared Cleaned_Sales_Data sheet.
# This is used as the main analytical dataset.
sales = pd.read_excel(
    WORKBOOK_PATH,
    sheet_name="Cleaned_Sales_Data"
)


# ============================================================
# 4. BASIC DATA INSPECTION
# ============================================================

print("\n" + "=" * 70)
print("DATA INSPECTION")
print("=" * 70)

print("\nShape:")
print(sales.shape)

print("\nColumns:")
print(list(sales.columns))

print("\nFirst 5 rows:")
print(sales.head())

print("\nData types:")
print(sales.dtypes)

print("\nMissing values:")
print(sales.isna().sum())

print("\nDuplicate rows:")
print(sales.duplicated().sum())


# ============================================================
# 5. DATA CLEANING
# ============================================================

print("\n" + "=" * 70)
print("DATA CLEANING")
print("=" * 70)

# Work on a copy.
sales = sales.copy()

# Standardise column names.
sales.columns = (
    sales.columns
    .str.strip()
    .str.replace(" ", "_")
)

# Clean text columns.
text_columns = [
    "Order_ID",
    "Customer_ID",
    "Product",
    "Category",
    "Region",
    "City",
    "Customer_Segment",
    "Channel",
    "Payment_Method",
    "Sales_Rep",
]

for column in text_columns:
    if column in sales.columns:
        sales[column] = (
            sales[column]
            .astype("string")
            .str.strip()
        )


# Standardise commonly used categorical fields.
categorical_columns = [
    "Category",
    "Region",
    "Customer_Segment",
    "Channel",
    "Payment_Method",
]

for column in categorical_columns:
    if column in sales.columns:
        sales[column] = (
            sales[column]
            .str.title()
            .str.strip()
        )


# Convert Date.
if "Date" in sales.columns:
    sales["Date"] = pd.to_datetime(
        sales["Date"],
        errors="coerce"
    )

    if sales["Date"].notna().any():
        median_date = sales["Date"].dropna().sort_values().iloc[
            len(sales["Date"].dropna()) // 2
        ]
        sales["Date"] = sales["Date"].fillna(median_date)


# Convert numerical columns.
numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount_%",
    "Revenue",
    "Cost",
    "Profit",
    "Profit_Margin_%",
]

for column in numeric_columns:
    if column in sales.columns:
        sales[column] = pd.to_numeric(
            sales[column],
            errors="coerce"
        )


# Handle invalid Quantity.
if "Quantity" in sales.columns:
    sales.loc[
        sales["Quantity"].isna() | (sales["Quantity"] < 0),
        "Quantity"
    ] = 0


# Handle invalid Unit Price.
if "Unit_Price" in sales.columns:
    if sales["Unit_Price"].isna().any():
        median_unit_price = sales["Unit_Price"].median()
        sales["Unit_Price"] = sales["Unit_Price"].fillna(
            median_unit_price
        )


# Handle invalid Cost.
if "Cost" in sales.columns:
    if sales["Cost"].isna().any():
        median_cost = sales["Cost"].median()
        sales["Cost"] = sales["Cost"].fillna(median_cost)


# Recalculate Revenue where possible.
if {"Quantity", "Unit_Price"}.issubset(sales.columns):
    calculated_revenue = (
        sales["Quantity"] * sales["Unit_Price"]
    )

    sales["Revenue"] = sales["Revenue"].fillna(
        calculated_revenue
    )


# Recalculate Profit.
if {"Revenue", "Cost"}.issubset(sales.columns):
    sales["Profit"] = (
        sales["Revenue"] - sales["Cost"]
    )


# Recalculate Profit Margin.
if {"Profit", "Revenue"}.issubset(sales.columns):
    sales["Profit_Margin_%"] = np.where(
        sales["Revenue"] != 0,
        (sales["Profit"] / sales["Revenue"]) * 100,
        0
    )


# Remove exact duplicate rows.
before_duplicates = len(sales)

sales = sales.drop_duplicates().reset_index(drop=True)

after_duplicates = len(sales)

print(f"\nRows before duplicate removal: {before_duplicates}")
print(f"Rows after duplicate removal:  {after_duplicates}")
print(f"Duplicates removed:            {before_duplicates - after_duplicates}")


# ============================================================
# 6. VALIDATION
# ============================================================

print("\n" + "=" * 70)
print("DATA VALIDATION")
print("=" * 70)

print("\nRemaining missing values:")
print(sales.isna().sum())

print("\nRemaining duplicate rows:")
print(sales.duplicated().sum())

if "Quantity" in sales.columns:
    print(
        "\nNegative Quantity:",
        int((sales["Quantity"] < 0).sum())
    )

if "Revenue" in sales.columns:
    print(
        "Negative Revenue:",
        int((sales["Revenue"] < 0).sum())
    )

if "Cost" in sales.columns:
    print(
        "Negative Cost:",
        int((sales["Cost"] < 0).sum())
    )


# ============================================================
# 7. CREATE MONTH FIELD
# ============================================================

if "Date" in sales.columns:
    sales["Month"] = sales["Date"].dt.to_period("M").astype(str)


# ============================================================
# 8. KPI ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("KPI ANALYSIS")
print("=" * 70)

total_revenue = sales["Revenue"].sum()
total_cost = sales["Cost"].sum()
total_profit = sales["Profit"].sum()

profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue != 0
    else 0
)

total_orders = sales["Order_ID"].nunique()
total_quantity = sales["Quantity"].sum()
customers = sales["Customer_ID"].nunique()

average_order_value = (
    total_revenue / total_orders
    if total_orders != 0
    else 0
)

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Revenue",
        "Total Cost",
        "Total Profit",
        "Profit Margin %",
        "Total Orders",
        "Total Quantity",
        "Average Order Value",
        "Customers",
    ],
    "Value": [
        total_revenue,
        total_cost,
        total_profit,
        profit_margin,
        total_orders,
        total_quantity,
        average_order_value,
        customers,
    ],
})

print(kpi_summary.to_string(index=False))


# ============================================================
# 9. CATEGORY ANALYSIS
# ============================================================

category_analysis = (
    sales.groupby("Category")
    .agg(
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Profit=("Profit", "sum"),
    )
    .reset_index()
)

category_analysis["Profit_Margin_%"] = np.where(
    category_analysis["Revenue"] != 0,
    category_analysis["Profit"]
    / category_analysis["Revenue"] * 100,
    0
)


# ============================================================
# 10. REGION ANALYSIS
# ============================================================

region_analysis = (
    sales.groupby("Region")
    .agg(
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Profit=("Profit", "sum"),
    )
    .reset_index()
)

region_analysis["Profit_Margin_%"] = np.where(
    region_analysis["Revenue"] != 0,
    region_analysis["Profit"]
    / region_analysis["Revenue"] * 100,
    0
)


# ============================================================
# 11. CUSTOMER SEGMENT ANALYSIS
# ============================================================

segment_analysis = (
    sales.groupby("Customer_Segment")
    .agg(
        Customers=("Customer_ID", "nunique"),
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Profit=("Profit", "sum"),
    )
    .reset_index()
)

segment_analysis["Profit_Margin_%"] = np.where(
    segment_analysis["Revenue"] != 0,
    segment_analysis["Profit"]
    / segment_analysis["Revenue"] * 100,
    0
)


# ============================================================
# 12. PRODUCT ANALYSIS
# ============================================================

product_analysis = (
    sales.groupby("Product")
    .agg(
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Profit=("Profit", "sum"),
    )
    .reset_index()
)

product_analysis["Profit_Margin_%"] = np.where(
    product_analysis["Revenue"] != 0,
    product_analysis["Profit"]
    / product_analysis["Revenue"] * 100,
    0
)

product_analysis = product_analysis.sort_values(
    "Revenue",
    ascending=False
)


# ============================================================
# 13. CHANNEL ANALYSIS
# ============================================================

channel_analysis = (
    sales.groupby("Channel")
    .agg(
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Profit=("Profit", "sum"),
    )
    .reset_index()
)

channel_analysis["Profit_Margin_%"] = np.where(
    channel_analysis["Revenue"] != 0,
    channel_analysis["Profit"]
    / channel_analysis["Revenue"] * 100,
    0
)


# ============================================================
# 14. MONTHLY ANALYSIS
# ============================================================

monthly_analysis = (
    sales.groupby("Month")
    .agg(
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Profit=("Profit", "sum"),
    )
    .reset_index()
)

monthly_analysis["Profit_Margin_%"] = np.where(
    monthly_analysis["Revenue"] != 0,
    monthly_analysis["Profit"]
    / monthly_analysis["Revenue"] * 100,
    0
)

monthly_analysis = monthly_analysis.sort_values("Month")


# ============================================================
# 15. CUSTOMER ANALYSIS
# ============================================================

customer_analysis = (
    sales.groupby(
        ["Customer_ID"],
        as_index=False
    )
    .agg(
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Profit=("Profit", "sum"),
    )
)

customer_analysis["Average_Order_Value"] = np.where(
    customer_analysis["Orders"] != 0,
    customer_analysis["Revenue"]
    / customer_analysis["Orders"],
    0
)

customer_analysis["Profit_Margin_%"] = np.where(
    customer_analysis["Revenue"] != 0,
    customer_analysis["Profit"]
    / customer_analysis["Revenue"] * 100,
    0
)

customer_analysis = customer_analysis.sort_values(
    "Revenue",
    ascending=False
)


# ============================================================
# 16. EXPORT CSV OUTPUTS
# ============================================================

print("\n" + "=" * 70)
print("EXPORTING ANALYSIS")
print("=" * 70)

sales.to_csv(
    OUTPUT_DIR / "cleaned_sales_data.csv",
    index=False
)

kpi_summary.to_csv(
    OUTPUT_DIR / "kpi_summary.csv",
    index=False
)

category_analysis.to_csv(
    OUTPUT_DIR / "category_analysis.csv",
    index=False
)

region_analysis.to_csv(
    OUTPUT_DIR / "region_analysis.csv",
    index=False
)

segment_analysis.to_csv(
    OUTPUT_DIR / "segment_analysis.csv",
    index=False
)

product_analysis.to_csv(
    OUTPUT_DIR / "product_analysis.csv",
    index=False
)

channel_analysis.to_csv(
    OUTPUT_DIR / "channel_analysis.csv",
    index=False
)

monthly_analysis.to_csv(
    OUTPUT_DIR / "monthly_analysis.csv",
    index=False
)

customer_analysis.to_csv(
    OUTPUT_DIR / "customer_analysis.csv",
    index=False
)


# ============================================================
# 17. CREATE CHARTS
# ============================================================

print("\nCreating charts...")


# ------------------------------------------------------------
# Chart 1 — Monthly Revenue
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_analysis["Month"],
    monthly_analysis["Revenue"],
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_revenue_trend.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 2 — Revenue by Category
# ------------------------------------------------------------

category_chart = category_analysis.sort_values(
    "Revenue",
    ascending=False
)

plt.figure(figsize=(10, 6))

plt.bar(
    category_chart["Category"],
    category_chart["Revenue"]
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_category.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 3 — Revenue by Region
# ------------------------------------------------------------

region_chart = region_analysis.sort_values(
    "Revenue",
    ascending=False
)

plt.figure(figsize=(10, 6))

plt.bar(
    region_chart["Region"],
    region_chart["Revenue"]
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_region.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 4 — Revenue by Customer Segment
# ------------------------------------------------------------

segment_chart = segment_analysis.sort_values(
    "Revenue",
    ascending=False
)

plt.figure(figsize=(8, 6))

plt.bar(
    segment_chart["Customer_Segment"],
    segment_chart["Revenue"]
)

plt.title("Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_customer_segment.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 5 — Revenue by Product
# ------------------------------------------------------------

top_products = (
    product_analysis
    .sort_values("Revenue", ascending=False)
    .head(12)
    .sort_values("Revenue")
)

plt.figure(figsize=(10, 7))

plt.barh(
    top_products["Product"],
    top_products["Revenue"]
)

plt.title("Revenue by Product")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_product.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 6 — Revenue vs Quantity
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

plt.scatter(
    product_analysis["Quantity"],
    product_analysis["Revenue"]
)

plt.title("Revenue vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_vs_quantity.png",
    dpi=150
)

plt.close()


# ============================================================
# 18. BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 70)
print("BUSINESS INSIGHTS")
print("=" * 70)

highest_revenue_category = (
    category_analysis.loc[
        category_analysis["Revenue"].idxmax()
    ]
)

highest_revenue_region = (
    region_analysis.loc[
        region_analysis["Revenue"].idxmax()
    ]
)

highest_revenue_segment = (
    segment_analysis.loc[
        segment_analysis["Revenue"].idxmax()
    ]
)

highest_revenue_product = (
    product_analysis.loc[
        product_analysis["Revenue"].idxmax()
    ]
)

highest_revenue_channel = (
    channel_analysis.loc[
        channel_analysis["Revenue"].idxmax()
    ]
)

highest_revenue_month = (
    monthly_analysis.loc[
        monthly_analysis["Revenue"].idxmax()
    ]
)

insights = pd.DataFrame({
    "Area": [
        "Category",
        "Region",
        "Customer Segment",
        "Product",
        "Channel",
        "Month",
    ],
    "Observation": [
        (
            f"{highest_revenue_category['Category']} "
            f"has the highest recorded revenue among categories."
        ),
        (
            f"{highest_revenue_region['Region']} "
            f"has the highest recorded revenue among regions."
        ),
        (
            f"{highest_revenue_segment['Customer_Segment']} "
            f"has the highest recorded revenue among customer segments."
        ),
        (
            f"{highest_revenue_product['Product']} "
            f"has the highest recorded revenue among products."
        ),
        (
            f"{highest_revenue_channel['Channel']} "
            f"has the highest recorded revenue among channels."
        ),
        (
            f"{highest_revenue_month['Month']} "
            f"has the highest recorded monthly revenue."
        ),
    ],
})

insights.to_csv(
    OUTPUT_DIR / "business_insights.csv",
    index=False
)

print(insights.to_string(index=False))


# ============================================================
# 19. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("FINAL PROJECT SUMMARY")
print("=" * 70)

print(f"Total Customers     : {customers:,.0f}")
print(f"Total Orders        : {total_orders:,.0f}")
print(f"Total Quantity      : {total_quantity:,.0f}")
print(f"Total Revenue       : {total_revenue:,.2f}")
print(f"Total Cost          : {total_cost:,.2f}")
print(f"Total Profit        : {total_profit:,.2f}")
print(f"Profit Margin       : {profit_margin:,.2f}%")
print(f"Average Order Value : {average_order_value:,.2f}")

print("\nOutput folder:")
print(OUTPUT_DIR)

print("\nGenerated files:")

for output_file in sorted(OUTPUT_DIR.iterdir()):
    if output_file.is_file():
        print(f"- {output_file.name}")

print("\n" + "=" * 70)
print("FINAL BUSINESS ANALYTICS PROJECT COMPLETED")
print("=" * 70)