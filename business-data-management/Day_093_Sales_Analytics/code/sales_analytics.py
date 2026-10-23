# ============================================================
# Day 093 — Sales Analytics
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 093
# Topic: Sales Analytics
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. FIND INPUT FILE
# ============================================================

possible_paths = [
    "data/Day_093_Sales_Analytics.xlsx",
    "Day_093_Sales_Analytics.xlsx",
    "../data/Day_093_Sales_Analytics.xlsx",
    "/mnt/data/Day_093_Sales_Analytics.xlsx"
]

input_file = None

for path in possible_paths:
    if os.path.exists(path):
        input_file = path
        break

if input_file is None:
    raise FileNotFoundError(
        "Day_093_Sales_Analytics.xlsx was not found. "
        "Please place the workbook inside the data folder."
    )

print("\nInput file:")
print(input_file)


# ============================================================
# 2. CREATE OUTPUT FOLDER
# ============================================================

output_dir = "outputs"

os.makedirs(output_dir, exist_ok=True)

print("\nOutput folder:")
print(output_dir)


# ============================================================
# 3. LOAD RAW SALES DATA
# ============================================================

# The workbook contains title/information rows above
# the actual table header.
# Therefore header=3 is used.

df = pd.read_excel(
    input_file,
    sheet_name="Raw_Sales_Data",
    header=3
)


# ============================================================
# 4. BASIC DATA INSPECTION
# ============================================================

print("\n" + "=" * 60)
print("DATA INSPECTION")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ============================================================
# 5. CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.replace(" ", "_", regex=False)
)

print("\nCleaned Column Names:")
print(df.columns.tolist())


# ============================================================
# 6. CHECK REQUIRED COLUMNS
# ============================================================

required_columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Name",
    "Region",
    "Salesperson",
    "Product_Category",
    "Product",
    "Quantity",
    "Unit_Price",
    "Revenue",
    "Cost",
    "Discount_%",
    "Profit",
    "Payment_Method",
    "Order_Status"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise KeyError(
        "The following required columns are missing: "
        + ", ".join(missing_columns)
    )


# ============================================================
# 7. CREATE CLEAN COPY
# ============================================================

clean_df = df.copy()


# ============================================================
# 8. CLEAN TEXT COLUMNS
# ============================================================

text_columns = [
    "Customer_Name",
    "Region",
    "Salesperson",
    "Product_Category",
    "Product",
    "Payment_Method",
    "Order_Status"
]

for column in text_columns:

    clean_df[column] = (
        clean_df[column]
        .astype("string")
        .str.strip()
    )


# ============================================================
# 9. STANDARDISE TEXT CAPITALISATION
# ============================================================

for column in text_columns:

    clean_df[column] = (
        clean_df[column]
        .str.title()
    )


# ============================================================
# 10. CLEAN DATE COLUMN
# ============================================================

clean_df["Order_Date"] = pd.to_datetime(
    clean_df["Order_Date"],
    errors="coerce"
)


# ============================================================
# 11. CLEAN NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Revenue",
    "Cost",
    "Discount_%",
    "Profit"
]

for column in numeric_columns:

    clean_df[column] = pd.to_numeric(
        clean_df[column],
        errors="coerce"
    )


# ============================================================
# 12. CHECK MISSING VALUES AFTER CONVERSION
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES AFTER CLEANING")
print("=" * 60)

print(clean_df.isna().sum())


# ============================================================
# 13. HANDLE MISSING QUANTITY
# ============================================================

clean_df["Quantity"] = clean_df["Quantity"].fillna(0)


# ============================================================
# 14. HANDLE MISSING UNIT PRICE
# ============================================================

clean_df["Unit_Price"] = clean_df["Unit_Price"].fillna(0)


# ============================================================
# 15. HANDLE MISSING COST
# ============================================================

clean_df["Cost"] = clean_df["Cost"].fillna(0)


# ============================================================
# 16. CALCULATE REVENUE
# ============================================================

clean_df["Calculated_Revenue"] = (
    clean_df["Quantity"] *
    clean_df["Unit_Price"]
)

# If Revenue is missing, use calculated revenue.
clean_df["Revenue"] = clean_df["Revenue"].fillna(
    clean_df["Calculated_Revenue"]
)


# ============================================================
# 17. CALCULATE PROFIT
# ============================================================

clean_df["Profit"] = (
    clean_df["Revenue"] -
    clean_df["Cost"]
)


# ============================================================
# 18. CALCULATE PROFIT MARGIN
# ============================================================

clean_df["Profit_Margin_%"] = np.where(
    clean_df["Revenue"] != 0,
    (
        clean_df["Profit"] /
        clean_df["Revenue"]
    ) * 100,
    0
)


# ============================================================
# 19. CREATE MONTH COLUMN
# ============================================================

clean_df["Month"] = (
    clean_df["Order_Date"]
    .dt.to_period("M")
    .astype("string")
)


# ============================================================
# 20. REMOVE EXACT DUPLICATE ROWS
# ============================================================

before_duplicates = len(clean_df)

clean_df = clean_df.drop_duplicates()

after_duplicates = len(clean_df)

duplicates_removed = (
    before_duplicates -
    after_duplicates
)

print("\nDuplicate rows removed:")
print(duplicates_removed)


# ============================================================
# 21. SAVE CLEANED DATA
# ============================================================

cleaned_file = (
    f"{output_dir}/cleaned_sales_data.csv"
)

clean_df.to_csv(
    cleaned_file,
    index=False
)

print("\nCleaned data saved:")
print(cleaned_file)


# ============================================================
# 22. SALES SUMMARY
# ============================================================

total_revenue = clean_df["Revenue"].sum()

total_cost = clean_df["Cost"].sum()

total_profit = clean_df["Profit"].sum()

total_orders = clean_df["Order_ID"].nunique()

total_quantity = clean_df["Quantity"].sum()

profit_margin = (
    (total_profit / total_revenue) * 100
    if total_revenue != 0
    else 0
)

average_order_value = (
    total_revenue / total_orders
    if total_orders != 0
    else 0
)


sales_summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Cost",
        "Total Profit",
        "Profit Margin (%)",
        "Total Orders",
        "Total Quantity Sold",
        "Average Order Value"
    ],
    "Value": [
        total_revenue,
        total_cost,
        total_profit,
        profit_margin,
        total_orders,
        total_quantity,
        average_order_value
    ]
})


# ============================================================
# 23. SAVE SALES SUMMARY
# ============================================================

sales_summary.to_csv(
    f"{output_dir}/sales_summary.csv",
    index=False
)

print("\n" + "=" * 60)
print("SALES SUMMARY")
print("=" * 60)

print(sales_summary)


# ============================================================
# 24. PRODUCT ANALYSIS
# ============================================================

product_analysis = (
    clean_df
    .groupby(
        "Product",
        dropna=False
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Quantity=("Quantity", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .reset_index()
    .sort_values(
        "Revenue",
        ascending=False
    )
)


# ============================================================
# 25. SAVE PRODUCT ANALYSIS
# ============================================================

product_analysis.to_csv(
    f"{output_dir}/product_analysis.csv",
    index=False
)

print("\n" + "=" * 60)
print("PRODUCT ANALYSIS")
print("=" * 60)

print(product_analysis)


# ============================================================
# 26. REGION ANALYSIS
# ============================================================

region_analysis = (
    clean_df
    .groupby(
        "Region",
        dropna=False
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Quantity=("Quantity", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .reset_index()
    .sort_values(
        "Revenue",
        ascending=False
    )
)


# ============================================================
# 27. SAVE REGION ANALYSIS
# ============================================================

region_analysis.to_csv(
    f"{output_dir}/region_analysis.csv",
    index=False
)

print("\n" + "=" * 60)
print("REGION ANALYSIS")
print("=" * 60)

print(region_analysis)


# ============================================================
# 28. MONTHLY SALES ANALYSIS
# ============================================================

monthly_sales = (
    clean_df
    .groupby(
        "Month",
        dropna=False
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .reset_index()
    .sort_values("Month")
)


# ============================================================
# 29. SAVE MONTHLY SALES ANALYSIS
# ============================================================

monthly_sales.to_csv(
    f"{output_dir}/monthly_sales_analysis.csv",
    index=False
)

print("\n" + "=" * 60)
print("MONTHLY SALES ANALYSIS")
print("=" * 60)

print(monthly_sales)


# ============================================================
# 30. CUSTOMER ANALYSIS
# ============================================================

customer_analysis = (
    clean_df
    .groupby(
        [
            "Customer_ID",
            "Customer_Name"
        ],
        dropna=False
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .reset_index()
    .sort_values(
        "Revenue",
        ascending=False
    )
)


# ============================================================
# 31. SAVE CUSTOMER ANALYSIS
# ============================================================

customer_analysis.to_csv(
    f"{output_dir}/customer_analysis.csv",
    index=False
)

print("\n" + "=" * 60)
print("CUSTOMER ANALYSIS")
print("=" * 60)

print(customer_analysis)


# ============================================================
# 32. SALES KPI SUMMARY
# ============================================================

sales_kpi = pd.DataFrame({
    "KPI": [
        "Total Revenue",
        "Total Cost",
        "Total Profit",
        "Profit Margin (%)",
        "Total Orders",
        "Total Quantity Sold",
        "Average Order Value"
    ],
    "Value": [
        total_revenue,
        total_cost,
        total_profit,
        profit_margin,
        total_orders,
        total_quantity,
        average_order_value
    ]
})


# ============================================================
# 33. SAVE KPI SUMMARY
# ============================================================

sales_kpi.to_csv(
    f"{output_dir}/sales_kpi_summary.csv",
    index=False
)

print("\n" + "=" * 60)
print("SALES KPIs")
print("=" * 60)

print(sales_kpi)


# ============================================================
# 34. REVENUE BY PRODUCT CHART
# ============================================================

if not product_analysis.empty:

    plt.figure(figsize=(10, 6))

    plt.bar(
        product_analysis["Product"],
        product_analysis["Revenue"]
    )

    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    plt.savefig(
        f"{output_dir}/sales_by_product.png",
        dpi=300
    )

    plt.close()


# ============================================================
# 35. REVENUE BY REGION CHART
# ============================================================

if not region_analysis.empty:

    plt.figure(figsize=(8, 6))

    plt.bar(
        region_analysis["Region"],
        region_analysis["Revenue"]
    )

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    plt.savefig(
        f"{output_dir}/sales_by_region.png",
        dpi=300
    )

    plt.close()


# ============================================================
# 36. MONTHLY REVENUE TREND
# ============================================================

if not monthly_sales.empty:

    plt.figure(figsize=(10, 6))

    plt.plot(
        monthly_sales["Month"],
        monthly_sales["Revenue"],
        marker="o"
    )

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(
        f"{output_dir}/monthly_sales_trend.png",
        dpi=300
    )

    plt.close()


# ============================================================
# 37. KEY BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 60)
print("KEY BUSINESS INSIGHTS")
print("=" * 60)


# Top Product

if not product_analysis.empty:

    top_product = product_analysis.iloc[0]

    print(
        "\nTop Revenue Product:"
    )

    print(
        f"{top_product['Product']} "
        f"→ Revenue = "
        f"{top_product['Revenue']:.2f}"
    )


# Top Region

if not region_analysis.empty:

    top_region = region_analysis.iloc[0]

    print(
        "\nTop Revenue Region:"
    )

    print(
        f"{top_region['Region']} "
        f"→ Revenue = "
        f"{top_region['Revenue']:.2f}"
    )


# Highest Revenue Month

if not monthly_sales.empty:

    valid_months = monthly_sales[
        monthly_sales["Month"].notna()
    ]

    if not valid_months.empty:

        highest_month_index = (
            valid_months["Revenue"].idxmax()
        )

        highest_month = (
            valid_months.loc[
                highest_month_index
            ]
        )

        print(
            "\nHighest Revenue Month:"
        )

        print(
            f"{highest_month['Month']} "
            f"→ Revenue = "
            f"{highest_month['Revenue']:.2f}"
        )


# Top Customer

if not customer_analysis.empty:

    top_customer = customer_analysis.iloc[0]

    print(
        "\nTop Revenue Customer:"
    )

    print(
        f"{top_customer['Customer_Name']} "
        f"→ Revenue = "
        f"{top_customer['Revenue']:.2f}"
    )


# Overall KPIs

print("\nOverall Sales Performance:")

print(
    f"Total Revenue: "
    f"{total_revenue:.2f}"
)

print(
    f"Total Cost: "
    f"{total_cost:.2f}"
)

print(
    f"Total Profit: "
    f"{total_profit:.2f}"
)

print(
    f"Profit Margin: "
    f"{profit_margin:.2f}%"
)

print(
    f"Total Orders: "
    f"{total_orders}"
)

print(
    f"Total Quantity Sold: "
    f"{total_quantity:.0f}"
)

print(
    f"Average Order Value: "
    f"{average_order_value:.2f}"
)


# ============================================================
# 38. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("SALES ANALYTICS COMPLETED SUCCESSFULLY")
print("=" * 60)

print(
    "\nGenerated files are available inside:"
)

print(
    f"{output_dir}/"
)

print("\nGenerated outputs:")

print("- cleaned_sales_data.csv")
print("- sales_summary.csv")
print("- product_analysis.csv")
print("- region_analysis.csv")
print("- monthly_sales_analysis.csv")
print("- customer_analysis.csv")
print("- sales_kpi_summary.csv")
print("- sales_by_product.png")
print("- sales_by_region.png")
print("- monthly_sales_trend.png")