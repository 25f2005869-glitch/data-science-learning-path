from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 033
# Topic: Days of Sales of Inventory

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError(
        "No Excel workbook found in the Day 033 folder."
    )

excel_file = files[0]

df = pd.read_excel(
    excel_file,
    sheet_name="Inventory_Data"
)

df["Date"] = pd.to_datetime(df["Date"])

observation_days = (
    df["Date"].max() -
    df["Date"].min()
).days + 1

print("\n=== W6_L5 DAYS OF SALES OF INVENTORY ===")

print("Workbook:", excel_file.name)
print("Rows:", len(df))
print("Observation Days:", observation_days)
print("Products:", df["Product"].nunique())
print("Total Sales Units:", df["Sales_Units"].sum())

product = (
    df.groupby("Product")
    .agg(
        Total_Purchases=("Purchases", "sum"),
        Total_Sales_Units=("Sales_Units", "sum"),
        Average_Inventory=("Closing_Stock", "mean"),
        Closing_Stock=("Closing_Stock", "last")
    )
    .reset_index()
)

product["Average_Daily_Sales"] = (
    product["Total_Sales_Units"] /
    observation_days
)

product["Days_of_Sales_of_Inventory"] = (
    product["Average_Inventory"] /
    product["Average_Daily_Sales"]
)

product["Inventory_Turnover"] = (
    product["Total_Sales_Units"] /
    product["Average_Inventory"]
)

monthly = (
    df.assign(
        Month=df["Date"]
        .dt.to_period("M")
        .astype(str)
    )
    .groupby("Month")
    .agg(
        Purchases=("Purchases", "sum"),
        Sales_Units=("Sales_Units", "sum"),
        Closing_Stock=("Closing_Stock", "sum")
    )
    .reset_index()
)

product.to_csv(
    BASE_DIR / "product_dsi_analysis.csv",
    index=False
)

monthly.to_csv(
    BASE_DIR / "monthly_inventory_summary.csv",
    index=False
)

print("\n--- Product DSI Analysis ---")
print(product)

print("\n--- Monthly Inventory ---")
print(monthly)

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["Days_of_Sales_of_Inventory"]
)

plt.title(
    "Days of Sales of Inventory by Product"
)

plt.xlabel("Product")
plt.ylabel("Days")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    BASE_DIR / "days_of_sales_inventory.png",
    dpi=150
)

plt.close()

plt.figure(figsize=(9, 5))

plt.plot(
    monthly["Month"],
    monthly["Closing_Stock"],
    marker="o"
)

plt.title(
    "Monthly Closing Inventory"
)

plt.xlabel("Month")
plt.ylabel("Closing Inventory (Units)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    BASE_DIR / "monthly_closing_inventory.png",
    dpi=150
)

plt.close()

print("\n--- Presentation Insights ---")

highest_dsi = product.loc[
    product["Days_of_Sales_of_Inventory"].idxmax()
]

lowest_dsi = product.loc[
    product["Days_of_Sales_of_Inventory"].idxmin()
]

print(
    "Highest DSI:",
    highest_dsi["Product"],
    round(
        highest_dsi["Days_of_Sales_of_Inventory"],
        2
    ),
    "days"
)

print(
    "Lowest DSI:",
    lowest_dsi["Product"],
    round(
        lowest_dsi["Days_of_Sales_of_Inventory"],
        2
    ),
    "days"
)

print(
    "\nInventory analysis completed successfully."
)