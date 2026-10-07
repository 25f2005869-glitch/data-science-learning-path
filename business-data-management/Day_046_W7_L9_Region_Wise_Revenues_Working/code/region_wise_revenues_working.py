from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 046
# Topic: Region-wise Revenues Working

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_046_W7_L9_Region_Wise_Revenues_Working.xlsx"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Revenue_Data"
)

# Regional revenue summary
region = (
    df.groupby("Region", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Production_Units=("Production_Units", "sum"),
        Sales_Units=("Sales_Units", "sum"),
        Scrap_Units=("Scrap_Units", "sum"),
        Gross_Margin=("Gross_Margin", "sum"),
    )
)

region["Revenue_Share_%"] = (
    region["Revenue"] / region["Revenue"].sum()
)

region["Margin_%"] = (
    region["Gross_Margin"] / region["Revenue"]
)

region["Sales_Conversion_%"] = (
    region["Sales_Units"] / region["Production_Units"]
)

region["Scrap_Rate_%"] = (
    region["Scrap_Units"] / region["Production_Units"]
)

region = (
    region
    .sort_values("Revenue", ascending=False)
    .reset_index(drop=True)
)

region["Revenue_Rank"] = (
    region["Revenue"]
    .rank(method="dense", ascending=False)
    .astype(int)
)

# Monthly regional revenue
monthly_region = (
    df.pivot_table(
        index="Month",
        columns="Region",
        values="Revenue",
        aggfunc="sum"
    )
    .reset_index()
)

# Product-region revenue
product_region = (
    df.pivot_table(
        index="Product",
        columns="Region",
        values="Revenue",
        aggfunc="sum"
    )
    .reset_index()
)

# Export analysis tables
region.to_csv(
    OUTPUT_DIR / "region_revenue_summary.csv",
    index=False
)

monthly_region.to_csv(
    OUTPUT_DIR / "monthly_region_revenue.csv",
    index=False
)

product_region.to_csv(
    OUTPUT_DIR / "product_region_revenue.csv",
    index=False
)

# Revenue by Region
plt.figure(figsize=(9, 5))

plt.bar(
    region["Region"],
    region["Revenue"],
    color="#4472C4"
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_region.png",
    dpi=160
)

plt.close()

# Monthly Revenue by Region
plt.figure(figsize=(10, 5))

for region_name, color in zip(
    ["North", "South", "West"],
    ["#4472C4", "#ED7D31", "#70AD47"]
):
    plt.plot(
        monthly_region["Month"],
        monthly_region[region_name],
        marker="o",
        label=region_name,
        color=color
    )

plt.title("Monthly Revenue by Region")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_revenue_by_region.png",
    dpi=160
)

plt.close()

# Product-region revenue
plt.figure(figsize=(9, 5))

x = range(len(product_region))
width = 0.25

for i, (region_name, color) in enumerate(
    zip(
        ["North", "South", "West"],
        ["#4472C4", "#ED7D31", "#70AD47"]
    )
):
    plt.bar(
        [
            value + (i - 1) * width
            for value in x
        ],
        product_region[region_name],
        width=width,
        label=region_name,
        color=color
    )

plt.xticks(
    list(x),
    product_region["Product"]
)

plt.title("Revenue by Product and Region")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "product_region_revenue.png",
    dpi=160
)

plt.close()

# Regional Revenue Share
plt.figure(figsize=(8, 5))

plt.barh(
    region["Region"],
    region["Revenue_Share_%"],
    color="#8064A2"
)

plt.title("Regional Revenue Share")
plt.xlabel("Revenue Share")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "regional_revenue_share.png",
    dpi=160
)

plt.close()

print("Region-wise revenue analysis completed.")

print(
    region[
        [
            "Region",
            "Revenue",
            "Revenue_Share_%",
            "Margin_%",
            "Revenue_Rank"
        ]
    ]
)