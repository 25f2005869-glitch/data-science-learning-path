"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Day: 027
Topic: Revenue Pareto and Scatter Plot

This script reads the Day 027 Excel workbook, calculates revenue Pareto
analysis and creates a Units vs Revenue scatter plot.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))
if not files:
    raise FileNotFoundError("No Excel workbook found in the Day 027 folder.")

excel_file = files[0]
output_dir = BASE_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

df = pd.read_excel(excel_file, sheet_name="Ecommerce_Data")

required = [
    "Order_ID", "Month", "Product", "Category", "Channel",
    "Region", "Orders", "Units", "Revenue_Lakh"
]

missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns: {missing}")

print("=" * 70)
print("DAY 027 — REVENUE PARETO & SCATTER PLOT")
print("=" * 70)

print("\n1. DATA PREVIEW")
print(df.head())

print("\n2. DATA SHAPE")
print(df.shape)

print("\n3. MISSING VALUES")
print(df.isna().sum())

print("\n4. DUPLICATE ROWS")
print(df.duplicated().sum())

product_summary = (
    df.groupby("Product", as_index=False)
      .agg(
          Orders=("Orders", "sum"),
          Units=("Units", "sum"),
          Revenue_Lakh=("Revenue_Lakh", "sum")
      )
      .sort_values("Revenue_Lakh", ascending=False)
)

total_revenue = product_summary["Revenue_Lakh"].sum()

product_summary["Revenue_Share_%"] = (
    product_summary["Revenue_Lakh"] / total_revenue * 100
)

product_summary["Cumulative_Revenue_Share_%"] = (
    product_summary["Revenue_Share_%"].cumsum()
)

product_summary["Pareto_Group"] = product_summary[
    "Cumulative_Revenue_Share_%"
].apply(
    lambda x: "Core Revenue Group" if x <= 80 else "Remaining"
)

product_summary["Average_Revenue_per_Unit"] = (
    product_summary["Revenue_Lakh"] / product_summary["Units"]
)

print("\n5. PRODUCT REVENUE RANKING")
print(product_summary)

core = product_summary[
    product_summary["Cumulative_Revenue_Share_%"] <= 80
]

if core.empty:
    core = product_summary.head(1)

print("\n6. CORE REVENUE GROUP")
print(
    core[
        [
            "Product",
            "Revenue_Lakh",
            "Cumulative_Revenue_Share_%"
        ]
    ]
)

monthly = (
    df.groupby("Month", as_index=False)
      .agg(
          Orders=("Orders", "sum"),
          Units=("Units", "sum"),
          Revenue_Lakh=("Revenue_Lakh", "sum")
      )
)

channel = (
    df.groupby("Channel", as_index=False)
      .agg(
          Orders=("Orders", "sum"),
          Units=("Units", "sum"),
          Revenue_Lakh=("Revenue_Lakh", "sum")
      )
      .sort_values("Revenue_Lakh", ascending=False)
)

region = (
    df.groupby("Region", as_index=False)
      .agg(
          Orders=("Orders", "sum"),
          Units=("Units", "sum"),
          Revenue_Lakh=("Revenue_Lakh", "sum")
      )
      .sort_values("Revenue_Lakh", ascending=False)
)

print("\n7. MONTHLY SUMMARY")
print(monthly)

print("\n8. CHANNEL SUMMARY")
print(channel)

print("\n9. REGION SUMMARY")
print(region)

correlation = product_summary["Units"].corr(
    product_summary["Revenue_Lakh"]
)

print("\n10. UNITS VS REVENUE CORRELATION")
print(round(correlation, 3))

product_summary.to_csv(
    output_dir / "revenue_pareto_analysis.csv",
    index=False
)

monthly.to_csv(
    output_dir / "monthly_revenue_summary.csv",
    index=False
)

channel.to_csv(
    output_dir / "channel_revenue_summary.csv",
    index=False
)

region.to_csv(
    output_dir / "region_revenue_summary.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    product_summary["Product"],
    product_summary["Revenue_Lakh"]
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Lakh)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    output_dir / "revenue_by_product.png",
    dpi=150
)

plt.close()

plt.figure(figsize=(9, 5))

plt.plot(
    product_summary["Product"],
    product_summary["Cumulative_Revenue_Share_%"],
    marker="o"
)

plt.axhline(
    80,
    linestyle="--"
)

plt.title(
    "Cumulative Revenue Share — Pareto Analysis"
)

plt.xlabel("Product")
plt.ylabel(
    "Cumulative Revenue Share (%)"
)

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    output_dir / "revenue_pareto_curve.png",
    dpi=150
)

plt.close()

plt.figure(figsize=(8, 5))

plt.scatter(
    product_summary["Units"],
    product_summary["Revenue_Lakh"],
    s=100
)

for _, row in product_summary.iterrows():

    plt.annotate(
        row["Product"],
        (
            row["Units"],
            row["Revenue_Lakh"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.title("Units vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue (Lakh)")
plt.tight_layout()

plt.savefig(
    output_dir / "units_vs_revenue_scatter.png",
    dpi=150
)

plt.close()

print("\n11. BUSINESS INSIGHTS")

top_product = product_summary.iloc[0]
top_channel = channel.iloc[0]
top_region = region.iloc[0]

print(
    f"- Highest revenue product: "
    f"{top_product['Product']} "
    f"({top_product['Revenue_Lakh']:.2f} lakh)."
)

print(
    f"- Highest revenue channel: "
    f"{top_channel['Channel']} "
    f"({top_channel['Revenue_Lakh']:.2f} lakh)."
)

print(
    f"- Highest revenue region: "
    f"{top_region['Region']} "
    f"({top_region['Revenue_Lakh']:.2f} lakh)."
)

print(
    f"- Units-to-revenue correlation across products: "
    f"{correlation:.3f}."
)

print(
    "- Pareto analysis helps management focus on "
    "the products responsible for the largest "
    "revenue contribution."
)

print("\n12. OUTPUT FILES")

for path in sorted(output_dir.iterdir()):
    print(path.name)

print("\nAnalysis completed successfully.")