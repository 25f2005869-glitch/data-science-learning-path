from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 057
# Topic: Tutorial Assignment

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_057_W8_L10_Tutorial_Assignment.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Tutorial_Data",
    header=2
)

df["Average_Daily_Usage"] = df["Material_Usage"] / 30

df["Lead_Time_Demand_Calc"] = (
    df["Average_Daily_Usage"]
    * df["Lead_Time_Days"]
)

df["Safety_Stock_Calc"] = (
    df["Average_Daily_Usage"]
    * df["Safety_Stock_Days"]
)

df["Reorder_Point_Calc"] = (
    df["Lead_Time_Demand_Calc"]
    + df["Safety_Stock_Calc"]
)

df["Inventory_Gap_Calc"] = (
    df["Closing_Inventory"]
    - df["Reorder_Point_Calc"]
)

df["Stock_Status_Calc"] = (
    df["Inventory_Gap_Calc"]
    .apply(
        lambda x:
        "Below Reorder Point"
        if x < 0
        else "At/Above Reorder Point"
    )
)

material = (
    df.groupby(
        "Raw_Material",
        as_index=False
    )
    .agg(
        Total_Purchases=(
            "Purchases",
            "sum"
        ),
        Total_Usage=(
            "Material_Usage",
            "sum"
        ),
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
        Avg_Safety_Stock=(
            "Safety_Stock_Calc",
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
        Purchases=(
            "Purchases",
            "sum"
        ),
        Material_Usage=(
            "Material_Usage",
            "sum"
        ),
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

regional = (
    df.groupby(
        "Region",
        as_index=False
    )
    .agg(
        Purchases=(
            "Purchases",
            "sum"
        ),
        Material_Usage=(
            "Material_Usage",
            "sum"
        ),
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
    OUTPUT_DIR
    / "tutorial_material_analysis.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR
    / "tutorial_monthly_analysis.csv",
    index=False
)

regional.to_csv(
    OUTPUT_DIR
    / "tutorial_regional_analysis.csv",
    index=False
)

status.to_csv(
    OUTPUT_DIR
    / "tutorial_stock_status.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    material["Raw_Material"],
    material["Total_Usage"],
    color="#4472C4"
)

plt.title(
    "Total Material Usage by Raw Material"
)

plt.xlabel("Raw Material")

plt.ylabel(
    "Total Usage (Units)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR
    / "total_material_usage.png",
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

plt.title(
    "Monthly Material Usage"
)

plt.xlabel("Month")

plt.ylabel(
    "Material Usage (Units)"
)

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

plt.ylabel(
    "Average Inventory Value"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR
    / "inventory_value_by_material.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    regional["Region"],
    regional["Avg_Closing_Inventory"],
    color="#8064A2"
)

plt.title(
    "Regional Average Closing Inventory"
)

plt.xlabel("Region")

plt.ylabel(
    "Average Closing Inventory (Units)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR
    / "regional_average_closing_inventory.png",
    dpi=160
)

plt.close()

print("Day 057 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output folder: {OUTPUT_DIR}")