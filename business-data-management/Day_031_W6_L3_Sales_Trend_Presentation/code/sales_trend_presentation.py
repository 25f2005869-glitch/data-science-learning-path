from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 031
# Topic: Sales Trend Presentation

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError(
        "No Excel workbook found in the Day 031 folder."
    )

excel_file = files[0]

df = pd.read_excel(
    excel_file,
    sheet_name="Sales_Data"
)

df["Date"] = pd.to_datetime(
    df["Date"]
)

df["Month"] = (
    df["Date"]
    .dt
    .to_period("M")
    .astype(str)
)

df["Weekday"] = (
    df["Date"]
    .dt
    .day_name()
)

print("\n=== W6_L3 SALES TREND PRESENTATION ===")

print(
    "Workbook:",
    excel_file.name
)

print(
    "Rows:",
    len(df)
)

print(
    "Total Orders:",
    df["Orders"].sum()
)

print(
    "Total Units:",
    df["Units"].sum()
)

print(
    "Total Revenue (Lakh):",
    round(
        df["Revenue_Lakh"].sum(),
        2
    )
)

monthly = (
    df.groupby("Month")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        )
    )
    .reset_index()
)

monthly[
    "MoM_Revenue_Growth_%"
] = (
    monthly["Revenue_Lakh"]
    .pct_change()
    * 100
)

product = (
    df.groupby("Product")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        )
    )
    .reset_index()
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

weekday = (
    df.groupby("Weekday")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        )
    )
    .reindex(
        weekday_order
    )
    .reset_index()
)

monthly.to_csv(
    BASE_DIR /
    "monthly_trend_summary.csv",
    index=False
)

product.to_csv(
    BASE_DIR /
    "product_trend_summary.csv",
    index=False
)

weekday.to_csv(
    BASE_DIR /
    "weekday_trend_summary.csv",
    index=False
)

plt.figure(
    figsize=(9, 5)
)

plt.plot(
    monthly["Month"],
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

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    BASE_DIR /
    "monthly_revenue_trend.png",
    dpi=150
)

plt.close()

plt.figure(
    figsize=(9, 5)
)

plt.plot(
    monthly["Month"],
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

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    BASE_DIR /
    "monthly_unit_trend.png",
    dpi=150
)

plt.close()

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
    BASE_DIR /
    "product_revenue_trend.png",
    dpi=150
)

plt.close()

print(
    "\n--- Monthly Trend ---"
)

print(
    monthly
)

print(
    "\n--- Product Trend ---"
)

print(
    product
)

print(
    "\n--- Weekday Trend ---"
)

print(
    weekday
)

print(
    "\n--- Presentation Insights ---"
)

print(
    "Revenue trend:",
    "increasing"
    if monthly[
        "Revenue_Lakh"
    ].iloc[-1]
    >
    monthly[
        "Revenue_Lakh"
    ].iloc[0]
    else
    "not increasing"
)

print(
    "Top product:",
    product.iloc[0]["Product"]
)

print(
    "Highest revenue weekday:",
    weekday.loc[
        weekday[
            "Revenue_Lakh"
        ].idxmax(),
        "Weekday"
    ]
)

print(
    "Analysis complete."
)