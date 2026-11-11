from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 055
# Topic: Safety Stock and Reorder

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_055_W8_L8_Safety_Stock_and_Reorder.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Safety_Stock_Reorder_Data"
)

df["Lead_Time_Demand_Calc"] = (
    df["Avg_Daily_Demand"] *
    df["Avg_Lead_Time_Days"]
)

df["Reorder_Point_Calc"] = (
    df["Lead_Time_Demand_Calc"] +
    df["Safety_Stock"]
)

df["Reorder_Coverage_Days"] = (
    df["Reorder_Point"] /
    df["Avg_Daily_Demand"]
)

df["Inventory_Gap_to_Reorder"] = (
    df["Closing_Inventory"] -
    df["Reorder_Point"]
)

df["Stock_Status"] = df.apply(
    lambda row:
    "Below Reorder Point"
    if row["Closing_Inventory"] < row["Reorder_Point"]
    else "At/Above Reorder Point",
    axis=1
)

product = (
    df.groupby("Product", as_index=False)
    .agg(
        Avg_Daily_Demand=("Avg_Daily_Demand", "mean"),
        Avg_Lead_Time_Days=("Avg_Lead_Time_Days", "mean"),
        Safety_Stock=("Safety_Stock", "mean"),
        Lead_Time_Demand=("Lead_Time_Demand", "mean"),
        Reorder_Point=("Reorder_Point", "mean"),
        Closing_Inventory=("Closing_Inventory", "mean"),
        Sales_Units=("Sales_Units", "sum")
    )
)

product["Reorder_Coverage_Days"] = (
    product["Reorder_Point"] /
    product["Avg_Daily_Demand"]
)

monthly = (
    df.groupby("Month", sort=False, as_index=False)
    .agg(
        Avg_Daily_Demand=("Avg_Daily_Demand", "mean"),
        Safety_Stock=("Safety_Stock", "mean"),
        Lead_Time_Demand=("Lead_Time_Demand", "mean"),
        Reorder_Point=("Reorder_Point", "mean"),
        Closing_Inventory=("Closing_Inventory", "mean")
    )
)

region = (
    df.groupby("Region", as_index=False)
    .agg(
        Avg_Daily_Demand=("Avg_Daily_Demand", "mean"),
        Avg_Lead_Time_Days=("Avg_Lead_Time_Days", "mean"),
        Safety_Stock=("Safety_Stock", "mean"),
        Lead_Time_Demand=("Lead_Time_Demand", "mean"),
        Reorder_Point=("Reorder_Point", "mean"),
        Closing_Inventory=("Closing_Inventory", "mean")
    )
)

status = (
    df["Stock_Status"]
    .value_counts()
    .rename_axis("Stock_Status")
    .reset_index(name="Records")
)

product.to_csv(
    OUTPUT_DIR / "product_safety_stock_reorder.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_safety_stock_reorder.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_safety_stock_reorder.csv",
    index=False
)

status.to_csv(
    OUTPUT_DIR / "stock_status.csv",
    index=False
)

plt.figure(figsize=(9, 5))
plt.bar(
    product["Product"],
    product["Reorder_Point"],
    color="#4472C4"
)
plt.title("Reorder Point by Product")
plt.xlabel("Product")
plt.ylabel("Reorder Point (Units)")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "reorder_point_by_product.png",
    dpi=160
)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(
    product["Product"],
    product["Safety_Stock"],
    color="#ED7D31"
)
plt.title("Safety Stock by Product")
plt.xlabel("Product")
plt.ylabel("Safety Stock (Units)")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "safety_stock_by_product.png",
    dpi=160
)
plt.close()

plt.figure(figsize=(9, 5))
plt.plot(
    monthly["Month"],
    monthly["Lead_Time_Demand"],
    marker="o",
    color="#70AD47"
)
plt.title("Monthly Lead-Time Demand")
plt.xlabel("Month")
plt.ylabel("Lead-Time Demand (Units)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "monthly_lead_time_demand.png",
    dpi=160
)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(
    region["Region"],
    region["Closing_Inventory"],
    color="#8064A2"
)
plt.title("Closing Inventory by Region")
plt.xlabel("Region")
plt.ylabel("Closing Inventory (Units)")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "closing_inventory_by_region.png",
    dpi=160
)
plt.close()

print("Day 055 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output folder: {OUTPUT_DIR}")