"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Day: 028
Topic: W5_L7 — Trend Analysis: Sales and Revenue Trends

This script reads the Day 028 Excel workbook and performs:
1. Data quality checks
2. Monthly sales and revenue trend analysis
3. Weekday analysis
4. Product, channel and regional summaries
5. Trend visualisation
6. CSV exports
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# PATH SETUP
# ---------------------------------------------------------

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError(
        "No Excel workbook found in the Day 028 folder."
    )

excel_file = files[0]

output_dir = BASE_DIR / "outputs"
output_dir.mkdir(exist_ok=True)


# ---------------------------------------------------------
# READ EXCEL
# ---------------------------------------------------------

df = pd.read_excel(
    excel_file,
    sheet_name="Ecommerce_Data"
)


# ---------------------------------------------------------
# REQUIRED COLUMNS
# ---------------------------------------------------------

required_columns = [
    "Order_ID",
    "Date",
    "Month",
    "Weekday",
    "Product",
    "Category",
    "Channel",
    "Region",
    "Orders",
    "Units",
    "Revenue_Lakh",
]

missing = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing:
    raise ValueError(
        f"Missing columns: {missing}"
    )


# ---------------------------------------------------------
# DATE CONVERSION
# ---------------------------------------------------------

df["Date"] = pd.to_datetime(
    df["Date"]
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

print("=" * 72)
print("DAY 028 — TREND ANALYSIS")
print("SALES AND REVENUE TRENDS")
print("=" * 72)


# ---------------------------------------------------------
# DATA PREVIEW
# ---------------------------------------------------------

print("\n1. DATA PREVIEW")

print(
    df.head()
)


# ---------------------------------------------------------
# DATA SHAPE
# ---------------------------------------------------------

print("\n2. DATA SHAPE")

print(
    df.shape
)


# ---------------------------------------------------------
# MISSING VALUES
# ---------------------------------------------------------

print("\n3. MISSING VALUES")

print(
    df.isna().sum()
)


# ---------------------------------------------------------
# DUPLICATES
# ---------------------------------------------------------

print("\n4. DUPLICATE ROWS")

print(
    df.duplicated().sum()
)


# ---------------------------------------------------------
# MONTHLY TREND
# ---------------------------------------------------------

month_order = [
    "Jan-2023",
    "Feb-2023",
    "Mar-2023",
    "Apr-2023",
    "May-2023",
    "Jun-2023",
]

monthly = (
    df.groupby(
        "Month",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum"),
    )
)

monthly["Month"] = pd.Categorical(
    monthly["Month"],
    categories=month_order,
    ordered=True,
)

monthly = monthly.sort_values(
    "Month"
)


# ---------------------------------------------------------
# REVENUE GROWTH
# ---------------------------------------------------------

monthly["Revenue_Growth_%"] = (
    monthly["Revenue_Lakh"]
    .pct_change()
    .mul(100)
)


# ---------------------------------------------------------
# UNIT GROWTH
# ---------------------------------------------------------

monthly["Units_Growth_%"] = (
    monthly["Units"]
    .pct_change()
    .mul(100)
)


print("\n5. MONTHLY TREND")

print(
    monthly
)


# ---------------------------------------------------------
# WEEKDAY TREND
# ---------------------------------------------------------

weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

weekday = (
    df.groupby(
        "Weekday",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum"),
    )
)

weekday["Weekday"] = pd.Categorical(
    weekday["Weekday"],
    categories=weekday_order,
    ordered=True,
)

weekday = weekday.sort_values(
    "Weekday"
)


print("\n6. WEEKDAY ANALYSIS")

print(
    weekday
)


# ---------------------------------------------------------
# PRODUCT SUMMARY
# ---------------------------------------------------------

product = (
    df.groupby(
        "Product",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum"),
    )
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)


print("\n7. PRODUCT SUMMARY")

print(
    product
)


# ---------------------------------------------------------
# CHANNEL SUMMARY
# ---------------------------------------------------------

channel = (
    df.groupby(
        "Channel",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum"),
    )
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)


print("\n8. CHANNEL SUMMARY")

print(
    channel
)


# ---------------------------------------------------------
# REGION SUMMARY
# ---------------------------------------------------------

region = (
    df.groupby(
        "Region",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum"),
    )
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)


print("\n9. REGION SUMMARY")

print(
    region
)


# ---------------------------------------------------------
# FIRST AND LAST MONTH
# ---------------------------------------------------------

first_month = monthly.iloc[0]

last_month = monthly.iloc[-1]


# ---------------------------------------------------------
# OVERALL REVENUE CHANGE
# ---------------------------------------------------------

revenue_change = (
    (
        last_month["Revenue_Lakh"]
        - first_month["Revenue_Lakh"]
    )
    /
    first_month["Revenue_Lakh"]
    *
    100
)


# ---------------------------------------------------------
# OVERALL UNIT CHANGE
# ---------------------------------------------------------

units_change = (
    (
        last_month["Units"]
        - first_month["Units"]
    )
    /
    first_month["Units"]
    *
    100
)


print("\n10. OVERALL TREND")

print(
    f"Revenue change from "
    f"{first_month['Month']} to "
    f"{last_month['Month']}: "
    f"{revenue_change:.2f}%"
)

print(
    f"Unit change from "
    f"{first_month['Month']} to "
    f"{last_month['Month']}: "
    f"{units_change:.2f}%"
)


# ---------------------------------------------------------
# KEY RESULTS
# ---------------------------------------------------------

top_revenue_month = monthly.loc[
    monthly["Revenue_Lakh"].idxmax()
]

top_units_month = monthly.loc[
    monthly["Units"].idxmax()
]

top_orders_month = monthly.loc[
    monthly["Orders"].idxmax()
]

top_product = product.iloc[0]

top_channel = channel.iloc[0]

top_region = region.iloc[0]

top_weekday = weekday.loc[
    weekday["Revenue_Lakh"].idxmax()
]


print("\n11. KEY RESULTS")

print(
    f"Highest revenue month: "
    f"{top_revenue_month['Month']} "
    f"({top_revenue_month['Revenue_Lakh']:.2f} lakh)"
)

print(
    f"Highest unit month: "
    f"{top_units_month['Month']} "
    f"({top_units_month['Units']} units)"
)

print(
    f"Highest order month: "
    f"{top_orders_month['Month']} "
    f"({top_orders_month['Orders']} orders)"
)

print(
    f"Highest revenue product: "
    f"{top_product['Product']} "
    f"({top_product['Revenue_Lakh']:.2f} lakh)"
)

print(
    f"Highest revenue channel: "
    f"{top_channel['Channel']} "
    f"({top_channel['Revenue_Lakh']:.2f} lakh)"
)

print(
    f"Highest revenue region: "
    f"{top_region['Region']} "
    f"({top_region['Revenue_Lakh']:.2f} lakh)"
)

print(
    f"Highest revenue weekday: "
    f"{top_weekday['Weekday']} "
    f"({top_weekday['Revenue_Lakh']:.2f} lakh)"
)


# ---------------------------------------------------------
# EXPORT CSV FILES
# ---------------------------------------------------------

monthly.to_csv(
    output_dir / "monthly_trend.csv",
    index=False
)

weekday.to_csv(
    output_dir / "weekday_trend.csv",
    index=False
)

product.to_csv(
    output_dir / "product_trend.csv",
    index=False
)

channel.to_csv(
    output_dir / "channel_trend.csv",
    index=False
)

region.to_csv(
    output_dir / "region_trend.csv",
    index=False
)


# ---------------------------------------------------------
# MONTHLY REVENUE CHART
# ---------------------------------------------------------

plt.figure(
    figsize=(9, 5)
)

plt.plot(
    monthly["Month"].astype(str),
    monthly["Revenue_Lakh"],
    marker="o"
)

plt.title(
    "Monthly Revenue Trend"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    output_dir / "monthly_revenue_trend.png",
    dpi=150
)

plt.close()


# ---------------------------------------------------------
# MONTHLY UNIT CHART
# ---------------------------------------------------------

plt.figure(
    figsize=(9, 5)
)

plt.plot(
    monthly["Month"].astype(str),
    monthly["Units"],
    marker="o"
)

plt.title(
    "Monthly Unit Trend"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Units"
)

plt.tight_layout()

plt.savefig(
    output_dir / "monthly_units_trend.png",
    dpi=150
)

plt.close()


# ---------------------------------------------------------
# WEEKDAY REVENUE CHART
# ---------------------------------------------------------

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    weekday["Weekday"].astype(str),
    weekday["Revenue_Lakh"]
)

plt.title(
    "Revenue by Weekday"
)

plt.xlabel(
    "Weekday"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    output_dir / "weekday_revenue.png",
    dpi=150
)

plt.close()


# ---------------------------------------------------------
# PRODUCT REVENUE CHART
# ---------------------------------------------------------

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    product["Product"],
    product["Revenue_Lakh"]
)

plt.title(
    "Revenue by Product"
)

plt.xlabel(
    "Product"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    output_dir / "product_revenue.png",
    dpi=150
)

plt.close()


# ---------------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------------

print("\n12. BUSINESS INSIGHTS")

print(
    "• Trend analysis compares ordered periods "
    "rather than relying on one isolated observation."
)

print(
    "• Revenue and units should be reviewed together "
    "to understand sales performance."
)

print(
    "• Weekday analysis can reveal operational "
    "patterns in the sample data."
)

print(
    "• Product, channel and region summaries add "
    "context to the overall trend."
)

print(
    "• A trend should be interpreted with business "
    "context and data-quality checks."
)

print(
    "• A descriptive trend does not by itself prove "
    "the reason behind the movement."
)


# ---------------------------------------------------------
# OUTPUT FILES
# ---------------------------------------------------------

print("\n13. OUTPUT FILES")

for file in sorted(
    output_dir.iterdir()
):
    print(
        file.name
    )


# ---------------------------------------------------------
# COMPLETION
# ---------------------------------------------------------

print(
    "\nTrend analysis completed successfully."
)