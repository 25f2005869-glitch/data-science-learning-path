from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 052
# Topic: Unit Level Profitability Working

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_052_W8_L5_Unit_Level_Profitability_Working.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Profitability_Working_Data"
)

# ---------------------------------------
# Core Unit-Level Profitability Calculations
# ---------------------------------------

df["Revenue_Calc"] = (
    df["Sales_Units"]
    * df["Selling_Price_per_Unit"]
)

df["Material_Cost_Calc"] = (
    df["Sales_Units"]
    * df["Material_Cost_per_Unit"]
)

df["Labour_Cost_Calc"] = (
    df["Sales_Units"]
    * df["Labour_Cost_per_Unit"]
)

df["Overhead_Cost_Calc"] = (
    df["Sales_Units"]
    * df["Overhead_per_Unit"]
)

df["Total_Cost_Calc"] = (
    df["Material_Cost_Calc"]
    + df["Labour_Cost_Calc"]
    + df["Overhead_Cost_Calc"]
)

df["Unit_Cost_Calc"] = (
    df["Total_Cost_Calc"]
    / df["Sales_Units"]
)

df["Gross_Profit_Calc"] = (
    df["Revenue_Calc"]
    - df["Total_Cost_Calc"]
)

df["Unit_Profit_Calc"] = (
    df["Gross_Profit_Calc"]
    / df["Sales_Units"]
)

df["Margin_%_Calc"] = (
    df["Gross_Profit_Calc"]
    / df["Revenue_Calc"]
)

# ---------------------------------------
# Product-Level Profitability
# ---------------------------------------

product = (
    df.groupby("Product", as_index=False)
      .agg(
          Sales_Units=("Sales_Units", "sum"),
          Revenue=("Revenue_Calc", "sum"),
          Material_Cost=("Material_Cost_Calc", "sum"),
          Labour_Cost=("Labour_Cost_Calc", "sum"),
          Overhead_Cost=("Overhead_Cost_Calc", "sum"),
          Total_Cost=("Total_Cost_Calc", "sum"),
          Gross_Profit=("Gross_Profit_Calc", "sum"),
      )
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

# ---------------------------------------
# Monthly Profitability
# ---------------------------------------

monthly = (
    df.groupby(
        "Month",
        sort=False,
        as_index=False
    )
    .agg(
        Sales_Units=("Sales_Units", "sum"),
        Revenue=("Revenue_Calc", "sum"),
        Total_Cost=("Total_Cost_Calc", "sum"),
        Gross_Profit=("Gross_Profit_Calc", "sum"),
    )
)

monthly["Unit_Cost"] = (
    monthly["Total_Cost"]
    / monthly["Sales_Units"]
)

monthly["Unit_Profit"] = (
    monthly["Gross_Profit"]
    / monthly["Sales_Units"]
)

monthly["Margin_%"] = (
    monthly["Gross_Profit"]
    / monthly["Revenue"]
)

# ---------------------------------------
# Regional Profitability
# ---------------------------------------

region = (
    df.groupby(
        "Region",
        as_index=False
    )
    .agg(
        Sales_Units=("Sales_Units", "sum"),
        Revenue=("Revenue_Calc", "sum"),
        Total_Cost=("Total_Cost_Calc", "sum"),
        Gross_Profit=("Gross_Profit_Calc", "sum"),
    )
)

region["Unit_Cost"] = (
    region["Total_Cost"]
    / region["Sales_Units"]
)

region["Unit_Profit"] = (
    region["Gross_Profit"]
    / region["Sales_Units"]
)

region["Margin_%"] = (
    region["Gross_Profit"]
    / region["Revenue"]
)

# ---------------------------------------
# Cost Component Analysis
# ---------------------------------------

cost = (
    df.groupby(
        "Product",
        as_index=False
    )[
        [
            "Material_Cost_Calc",
            "Labour_Cost_Calc",
            "Overhead_Cost_Calc",
            "Total_Cost_Calc",
        ]
    ]
    .sum()
    .rename(
        columns={
            "Material_Cost_Calc": "Material_Cost",
            "Labour_Cost_Calc": "Labour_Cost",
            "Overhead_Cost_Calc": "Overhead_Cost",
            "Total_Cost_Calc": "Total_Cost",
        }
    )
)

# ---------------------------------------
# Export CSV Outputs
# ---------------------------------------

product.to_csv(
    OUTPUT_DIR / "product_profitability.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_profitability.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_profitability.csv",
    index=False
)

cost.to_csv(
    OUTPUT_DIR / "cost_component_analysis.csv",
    index=False
)

# ---------------------------------------
# Chart 1 — Unit Profit by Product
# ---------------------------------------

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

# ---------------------------------------
# Chart 2 — Monthly Gross Profit Trend
# ---------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    monthly["Month"],
    monthly["Gross_Profit"],
    marker="o",
    color="#ED7D31"
)

plt.title("Monthly Gross Profit Trend")
plt.xlabel("Month")
plt.ylabel("Gross Profit")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_gross_profit_trend.png",
    dpi=160
)

plt.close()

# ---------------------------------------
# Chart 3 — Cost Components
# ---------------------------------------

ax = product.set_index("Product")[
    [
        "Material_Cost",
        "Labour_Cost",
        "Overhead_Cost"
    ]
].plot(
    kind="bar",
    figsize=(9, 5),
    color=[
        "#70AD47",
        "#ED7D31",
        "#8064A2"
    ]
)

ax.set_title(
    "Cost Components by Product"
)

ax.set_xlabel("Product")
ax.set_ylabel("Cost")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "cost_components_by_product.png",
    dpi=160
)

plt.close()

# ---------------------------------------
# Chart 4 — Margin by Product
# ---------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["Margin_%"] * 100,
    color="#5B9BD5"
)

plt.title("Margin % by Product")
plt.xlabel("Product")
plt.ylabel("Margin (%)")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "margin_by_product.png",
    dpi=160
)

plt.close()

print("Day 052 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output folder: {OUTPUT_DIR}")