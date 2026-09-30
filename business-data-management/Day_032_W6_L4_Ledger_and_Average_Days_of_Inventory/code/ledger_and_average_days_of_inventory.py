from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 032
# Topic: Ledger and Average Days of Inventory

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError(
        "No Excel workbook found in the Day 032 folder."
    )

excel_file = files[0]

df = pd.read_excel(
    excel_file,
    sheet_name="Inventory_Ledger"
)

df["Date"] = pd.to_datetime(
    df["Date"]
)

print("\n=== W6_L4 LEDGER & AVERAGE DAYS OF INVENTORY ===")

print(
    "Workbook:",
    excel_file.name
)

print(
    "Rows:",
    len(df)
)

print("\n--- Basic KPIs ---")

print(
    "Products:",
    df["Product"].nunique()
)

print(
    "Total Purchases:",
    df["Purchases"].sum()
)

print(
    "Total Sales Units:",
    df["Sales_Units"].sum()
)

period_days = (
    df["Date"].max()
    - df["Date"].min()
).days + 1

product = (
    df.groupby("Product")
    .agg(
        Total_Purchases=(
            "Purchases",
            "sum"
        ),
        Total_Sales_Units=(
            "Sales_Units",
            "sum"
        ),
        Closing_Stock=(
            "Closing_Stock",
            "last"
        ),
        Average_Stock=(
            "Closing_Stock",
            "mean"
        )
    )
    .reset_index()
)

product["Average_Daily_Sales"] = (
    product["Total_Sales_Units"]
    / period_days
)

product[
    "Average_Days_of_Inventory"
] = (
    product["Average_Stock"]
    /
    product["Average_Daily_Sales"]
)

monthly = (
    df.assign(
        Month=df["Date"]
        .dt
        .to_period("M")
        .astype(str)
    )
    .groupby("Month")
    .agg(
        Purchases=(
            "Purchases",
            "sum"
        ),
        Sales_Units=(
            "Sales_Units",
            "sum"
        ),
        Closing_Stock=(
            "Closing_Stock",
            "sum"
        )
    )
    .reset_index()
)

product.to_csv(
    BASE_DIR /
    "product_inventory_summary.csv",
    index=False
)

monthly.to_csv(
    BASE_DIR /
    "monthly_inventory_summary.csv",
    index=False
)

print(
    "\n--- Product Inventory Summary ---"
)

print(product)

print(
    "\n--- Monthly Inventory Summary ---"
)

print(monthly)

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    product["Product"],
    product["Average_Days_of_Inventory"]
)

plt.title(
    "Average Days of Inventory by Product"
)

plt.xlabel(
    "Product"
)

plt.ylabel(
    "Average Days of Inventory"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    BASE_DIR /
    "average_days_inventory.png",
    dpi=150
)

plt.close()

plt.figure(
    figsize=(9, 5)
)

plt.plot(
    monthly["Month"],
    monthly["Closing_Stock"],
    marker="o"
)

plt.title(
    "Monthly Closing Stock"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Closing Stock (Units)"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    BASE_DIR /
    "monthly_closing_stock.png",
    dpi=150
)

plt.close()

print(
    "\n--- Presentation Insight ---"
)

top = product.loc[
    product[
        "Average_Days_of_Inventory"
    ].idxmax()
]

print(
    "Highest average inventory days:",
    top["Product"],
    round(
        top[
            "Average_Days_of_Inventory"
        ],
        2
    )
)

print(
    "\nInventory ledger analysis completed."
)