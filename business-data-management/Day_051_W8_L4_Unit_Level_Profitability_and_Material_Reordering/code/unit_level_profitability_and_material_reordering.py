from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 051
# Topic: Unit Level Profitability and Material Reordering
# ============================================================


CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

INPUT_FILE = (
    BASE_DIR
    / "Day_051_W8_L4_Unit_Level_Profitability_and_Material_Reordering.xlsx"
)


# ------------------------------------------------------------
# 1. Read data
# ------------------------------------------------------------

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Profitability_Data"
)


# ------------------------------------------------------------
# 2. Unit-level profitability
# ------------------------------------------------------------

df["Calculated_Revenue"] = (
    df["Sales_Units"]
    * df["Selling_Price_per_Unit"]
)

df["Calculated_Total_Cost"] = (
    df["Material_Cost"]
    + df["Labour_Cost"]
    + df["Overhead_Cost"]
)

df["Calculated_Gross_Profit"] = (
    df["Calculated_Revenue"]
    - df["Calculated_Total_Cost"]
)

df["Calculated_Unit_Profit"] = (
    df["Calculated_Gross_Profit"]
    / df["Sales_Units"]
)

df["Calculated_Margin"] = (
    df["Calculated_Gross_Profit"]
    / df["Calculated_Revenue"]
)


# ------------------------------------------------------------
# 3. Product profitability
# ------------------------------------------------------------

product = (
    df.groupby("Product", as_index=False)
    .agg(
        Sales_Units=("Sales_Units", "sum"),
        Revenue=("Calculated_Revenue", "sum"),
        Material_Cost=("Material_Cost", "sum"),
        Labour_Cost=("Labour_Cost", "sum"),
        Overhead_Cost=("Overhead_Cost", "sum"),
        Total_Cost=("Calculated_Total_Cost", "sum"),
        Gross_Profit=("Calculated_Gross_Profit", "sum"),
    )
)

product["Unit_Revenue"] = (
    product["Revenue"]
    / product["Sales_Units"]
)

product["Unit_Cost"] = (
    product["Total_Cost"]
    / product["Sales_Units"]
)

product["Unit_Profit"] = (
    product["Gross_Profit"]
    / product["Sales_Units"]
)

product["Margin_%"] = (
    product["Gross_Profit"]
    / product["Revenue"]
)


# ------------------------------------------------------------
# 4. Material reordering
# ------------------------------------------------------------

material = (
    df.groupby("Product", as_index=False)
    .agg(
        Avg_Daily_Usage=("Avg_Daily_Material_Usage", "mean"),
        Lead_Time_Days=("Lead_Time_Days", "first"),
        Safety_Stock=("Safety_Stock", "first"),
        Reorder_Point=("Reorder_Point", "first"),
        Closing_Material_Stock=(
            "Closing_Material_Stock",
            "mean"
        ),
    )
)

material["Lead_Time_Demand"] = (
    material["Avg_Daily_Usage"]
    * material["Lead_Time_Days"]
)

material["Reorder_Status"] = np.where(
    material["Closing_Material_Stock"]
    <= material["Reorder_Point"],
    "Reorder Now",
    "Monitor"
)


# ------------------------------------------------------------
# 5. Monthly profitability
# ------------------------------------------------------------

monthly = (
    df.groupby("Month", as_index=False)
    .agg(
        Revenue=("Calculated_Revenue", "sum"),
        Total_Cost=("Calculated_Total_Cost", "sum"),
        Gross_Profit=("Calculated_Gross_Profit", "sum"),
        Sales_Units=("Sales_Units", "sum"),
        Material_Demand=("Monthly_Material_Demand", "sum"),
    )
)

monthly["Margin_%"] = (
    monthly["Gross_Profit"]
    / monthly["Revenue"]
)


# ------------------------------------------------------------
# 6. Regional profitability
# ------------------------------------------------------------

region = (
    df.groupby("Region", as_index=False)
    .agg(
        Revenue=("Calculated_Revenue", "sum"),
        Total_Cost=("Calculated_Total_Cost", "sum"),
        Gross_Profit=("Calculated_Gross_Profit", "sum"),
        Sales_Units=("Sales_Units", "sum"),
    )
)

region["Margin_%"] = (
    region["Gross_Profit"]
    / region["Revenue"]
)


# ------------------------------------------------------------
# 7. Export summaries
# ------------------------------------------------------------

product.to_csv(
    OUTPUT_DIR / "unit_profitability_summary.csv",
    index=False
)

material.to_csv(
    OUTPUT_DIR / "material_reorder_analysis.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_profitability.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "regional_profitability.csv",
    index=False
)


# ------------------------------------------------------------
# 8. Chart — Unit Profit
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["Unit_Profit"],
    color="#4472C4"
)

plt.title("Unit Profit by Product")
plt.xlabel("Product")
plt.ylabel("Unit Profit")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "unit_profit_by_product.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 9. Chart — Monthly Gross Profit
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    monthly["Month"],
    monthly["Gross_Profit"],
    marker="o",
    color="#ED7D31"
)

plt.title("Monthly Gross Profit Trend")
plt.xlabel("Month")
plt.ylabel("Gross Profit")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_gross_profit.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 10. Chart — Reorder Point
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    material["Product"],
    material["Reorder_Point"],
    color="#70AD47"
)

plt.title("Reorder Point by Product")
plt.xlabel("Product")
plt.ylabel("Material Units")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "reorder_point_by_product.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 11. Chart — Unit Margin
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["Margin_%"],
    color="#8064A2"
)

plt.title("Unit Margin by Product")
plt.xlabel("Product")
plt.ylabel("Margin")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "unit_margin_by_product.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 12. Overall profitability
# ------------------------------------------------------------

overall_revenue = (
    df["Calculated_Revenue"].sum()
)

overall_cost = (
    df["Calculated_Total_Cost"].sum()
)

overall_profit = (
    df["Calculated_Gross_Profit"].sum()
)

overall_margin = (
    overall_profit
    / overall_revenue
)


# ------------------------------------------------------------
# 13. Console output
# ------------------------------------------------------------

print("=" * 65)
print(
    "DAY 051 — UNIT LEVEL PROFITABILITY "
    "AND MATERIAL REORDERING"
)
print("=" * 65)

print(f"Revenue      : {overall_revenue:,.2f}")
print(f"Total Cost   : {overall_cost:,.2f}")
print(f"Gross Profit : {overall_profit:,.2f}")
print(f"Margin       : {overall_margin:.2%}")

print("\nPRODUCT PROFITABILITY")
print(product)

print("\nMATERIAL REORDER ANALYSIS")
print(material)

print("\nMONTHLY PROFITABILITY")
print(monthly)

print("\nREGIONAL PROFITABILITY")
print(region)

print("\nAnalysis completed successfully.")