from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 030
# Topic: Scatter Chart Presentation

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError(
        "No Excel workbook found in the Day 030 folder."
    )

excel_file = files[0]

df = pd.read_excel(
    excel_file,
    sheet_name="Sales_Data"
)

print("\n=== W6_L2 SCATTER CHART PRESENTATION ===")
print("Workbook:", excel_file.name)
print("Rows:", len(df))

x = df["Ad_Spend_Thousand"]
y = df["Revenue_Lakh"]

correlation = x.corr(y)

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

print(
    "Total Ad Spend (Thousand):",
    df["Ad_Spend_Thousand"].sum()
)

print("\n--- Correlation ---")

print(
    "Ad Spend vs Revenue:",
    round(
        correlation,
        3
    )
)

print(
    "Orders vs Revenue:",
    round(
        df["Orders"].corr(
            df["Revenue_Lakh"]
        ),
        3
    )
)

print(
    "Units vs Revenue:",
    round(
        df["Units"].corr(
            df["Revenue_Lakh"]
        ),
        3
    )
)

product_summary = (
    df.groupby("Product")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum"),
        Ad_Spend_Thousand=(
            "Ad_Spend_Thousand",
            "sum"
        )
    )
    .reset_index()
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

channel_summary = (
    df.groupby("Channel")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum")
    )
    .reset_index()
)

region_summary = (
    df.groupby("Region")
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=("Revenue_Lakh", "sum")
    )
    .reset_index()
)

product_summary.to_csv(
    BASE_DIR / "product_summary.csv",
    index=False
)

channel_summary.to_csv(
    BASE_DIR / "channel_summary.csv",
    index=False
)

region_summary.to_csv(
    BASE_DIR / "region_summary.csv",
    index=False
)

plt.figure(
    figsize=(8, 5)
)

plt.scatter(
    x,
    y
)

plt.title(
    "Ad Spend vs Revenue"
)

plt.xlabel(
    "Ad Spend (Thousand)"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    BASE_DIR / "ad_spend_vs_revenue.png",
    dpi=150
)

plt.close()

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    product_summary["Product"],
    product_summary["Revenue_Lakh"]
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
    BASE_DIR / "revenue_by_product.png",
    dpi=150
)

plt.close()

print("\n--- Presentation Insights ---")

print(
    "1. The scatter chart shows a broadly positive "
    "relationship between ad spend and revenue."
)

print(
    "2. Correlation describes association; "
    "it does not prove that ad spend caused revenue."
)

print(
    "3. Product-level revenue can provide "
    "context for the relationship."
)

print("\nAnalysis complete.")