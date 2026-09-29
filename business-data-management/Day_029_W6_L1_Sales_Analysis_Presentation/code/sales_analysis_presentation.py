from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 029
# Topic: Sales Analysis Presentation

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))
if not files:
    raise FileNotFoundError("No Excel workbook found in the Day 029 folder.")

excel_file = files[0]

df = pd.read_excel(
    excel_file,
    sheet_name="Sales_Data"
)

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("\n=== SALES ANALYSIS PRESENTATION ===")
print("Workbook:", excel_file.name)
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n--- KPIs ---")

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
        Revenue_Lakh=("Revenue_Lakh", "sum")
    )
    .reset_index()
)

product = (
    df.groupby("Product")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum")
    )
    .reset_index()
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

channel = (
    df.groupby("Channel")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum")
    )
    .reset_index()
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

region = (
    df.groupby("Region")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum")
    )
    .reset_index()
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

print("\n--- Product Ranking ---")
print(product)

print("\n--- Channel Ranking ---")
print(channel)

print("\n--- Region Ranking ---")
print(region)

monthly.to_csv(
    BASE_DIR / "monthly_sales_summary.csv",
    index=False
)

product.to_csv(
    BASE_DIR / "product_sales_summary.csv",
    index=False
)

channel.to_csv(
    BASE_DIR / "channel_sales_summary.csv",
    index=False
)

region.to_csv(
    BASE_DIR / "region_sales_summary.csv",
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
    BASE_DIR / "monthly_revenue_trend.png",
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
    BASE_DIR / "product_revenue.png",
    dpi=150
)

plt.close()

plt.figure(
    figsize=(8, 5)
)

plt.bar(
    channel["Channel"],
    channel["Revenue_Lakh"]
)

plt.title(
    "Revenue by Channel"
)

plt.xlabel(
    "Channel"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    BASE_DIR / "channel_revenue.png",
    dpi=150
)

plt.close()

print("\n--- Presentation Insights ---")

print(
    "1. Revenue trend:",
    "increasing"
    if monthly["Revenue_Lakh"].iloc[-1]
    > monthly["Revenue_Lakh"].iloc[0]
    else "not increasing"
)

print(
    "2. Top product:",
    product.iloc[0]["Product"]
)

print(
    "3. Top channel:",
    channel.iloc[0]["Channel"]
)

print(
    "4. Top region:",
    region.iloc[0]["Region"]
)

print(
    "\nAnalysis complete. "
    "Use the Excel dashboard for the presentation."
)