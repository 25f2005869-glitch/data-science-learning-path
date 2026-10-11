from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 056
# Topic: Raw Material Inventory Analysis Presentation

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_056_W8_L9_Raw_Material_Inventory_Analysis_Presentation.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Raw_Material_Data",
    header=2
)

df["Lead_Time_Demand_Calc"] = (
    df["Material_Usage"] / 30
) * df["Lead_Time_Days"]

df["Reorder_Point_Calc"] = (
    df["Lead_Time_Demand_Calc"]
    + (df["Material_Usage"] / 30)
    * df["Safety_Stock_Days"]
)

df["Inventory_Gap_Calc"] = (
    df["Closing_Inventory"]
    - df["Reorder_Point_Calc"]
)

df["Stock_Status_Calc"] = df[
    "Inventory_Gap_Calc"
].apply(
    lambda x:
        "Below Reorder Point"
        if x < 0
        else "At/Above Reorder Point"
)

material = (
    df.groupby(
        "Raw_Material",
        as_index=False
    )
    .agg(
        Purchases=("Purchases", "sum"),
        Material_Usage=("Material_Usage", "sum"),
        Avg_Closing_Inventory=(
            "Closing_Inventory",
            "mean"
        ),
        Avg_Inventory_Value=(
            "Inventory_Value",
            "mean"
        ),
        Avg_Lead_Time_Days=(
            "Lead_Time_Days",
            "mean"
        ),
        Avg_Lead_Time_Demand=(
            "Lead_Time_Demand_Calc",
            "mean"
        ),
        Avg_Reorder_Point=(
            "Reorder_Point_Calc",
            "mean"
        ),
        Avg_Inventory_Gap=(
            "Inventory_Gap_Calc",
            "mean"
        )
    )
)

monthly = (
    df.groupby(
        "Month",
        sort=False,
        as_index=False
    )
    .agg(
        Purchases=("Purchases", "sum"),
        Material_Usage=("Material_Usage", "sum"),
        Closing_Inventory=(
            "Closing_Inventory",
            "sum"
        ),
        Inventory_Value=(
            "Inventory_Value",
            "sum"
        ),
        Lead_Time_Demand=(
            "Lead_Time_Demand_Calc",
            "sum"
        ),
        Reorder_Point=(
            "Reorder_Point_Calc",
            "sum"
        )
    )
)

region = (
    df.groupby(
        "Region",
        as_index=False
    )
    .agg(
        Purchases=("Purchases", "sum"),
        Material_Usage=("Material_Usage", "sum"),
        Avg_Closing_Inventory=(
            "Closing_Inventory",
            "mean"
        ),
        Avg_Inventory_Value=(
            "Inventory_Value",
            "mean"
        ),
        Avg_Lead_Time_Demand=(
            "Lead_Time_Demand_Calc",
            "mean"
        ),
        Avg_Reorder_Point=(
            "Reorder_Point_Calc",
            "mean"
        ),
        Avg_Inventory_Gap=(
            "Inventory_Gap_Calc",
            "mean"
        )
    )
)

status = (
    df["Stock_Status_Calc"]
    .value_counts()
    .rename_axis("Stock_Status")
    .reset_index(name="Records")
)

material.to_csv(
    OUTPUT_DIR / "raw_material_summary.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "raw_material_monthly_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "raw_material_region_summary.csv",
    index=False
)

status.to_csv(
    OUTPUT_DIR / "raw_material_stock_status.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    material["Raw_Material"],
    material["Avg_Closing_Inventory"],
    color="#4472C4"
)

plt.title(
    "Average Closing Inventory by Raw Material"
)

plt.xlabel("Raw Material")

plt.ylabel(
    "Average Closing Inventory (Units)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR
    / "average_closing_inventory_by_material.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.plot(
    monthly["Month"],
    monthly["Material_Usage"],
    marker="o",
    color="#ED7D31"
)

plt.title("Monthly Material Usage")

plt.xlabel("Month")

plt.ylabel("Material Usage (Units)")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR
    / "monthly_material_usage.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    material["Raw_Material"],
    material["Avg_Inventory_Value"],
    color="#70AD47"
)

plt.title(
    "Average Inventory Value by Raw Material"
)

plt.xlabel("Raw Material")

plt.ylabel("Average Inventory Value")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR
    / "inventory_value_by_material.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    region["Region"],
    region["Avg_Closing_Inventory"],
    color="#8064A2"
)

plt.title(
    "Average Closing Inventory by Region"
)

plt.xlabel("Region")

plt.ylabel(
    "Average Closing Inventory (Units)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR
    / "regional_closing_inventory.png",
    dpi=160
)

plt.close()

print("Day 056 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output folder: {OUTPUT_DIR}")