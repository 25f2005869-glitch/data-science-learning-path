from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 053
# Topic: Scrap Costs and Margin Analysis Presentation

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_053_W8_L6_Scrap_Costs_and_Margin_Analysis_Presentation.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="Scrap_Margin_Data")

df["Unit_Production_Cost"] = (
    df["Material_Cost_per_Unit"]
    + df["Labour_Cost_per_Unit"]
    + df["Overhead_per_Unit"]
)

df["Scrap_Rate_Calc"] = (
    df["Scrap_Units"]
    / df["Production_Units"]
)

df["Scrap_Cost_Calc"] = (
    df["Scrap_Units"]
    * df["Unit_Production_Cost"]
)

df["Revenue_Calc"] = (
    df["Sales_Units"]
    * df["Selling_Price_per_Unit"]
)

df["Cost_of_Sales_Calc"] = (
    df["Sales_Units"]
    * df["Unit_Production_Cost"]
)

df["Gross_Profit_Calc"] = (
    df["Revenue_Calc"]
    - df["Cost_of_Sales_Calc"]
)

df["Margin_Calc"] = (
    df["Gross_Profit_Calc"]
    / df["Revenue_Calc"]
)

df["Margin_After_Scrap_Calc"] = (
    df["Revenue_Calc"]
    - df["Total_Production_Cost"]
) / df["Revenue_Calc"]

product = df.groupby(
    "Product",
    as_index=False
).agg(
    Production_Units=("Production_Units", "sum"),
    Scrap_Units=("Scrap_Units", "sum"),
    Sales_Units=("Sales_Units", "sum"),
    Revenue=("Revenue_Calc", "sum"),
    Scrap_Cost=("Scrap_Cost_Calc", "sum"),
    Gross_Profit=("Gross_Profit_Calc", "sum"),
)

product["Scrap_Rate_%"] = (
    product["Scrap_Units"]
    / product["Production_Units"]
)

product["Margin_%"] = (
    product["Gross_Profit"]
    / product["Revenue"]
)

monthly = df.groupby(
    "Month",
    sort=False,
    as_index=False
).agg(
    Production_Units=("Production_Units", "sum"),
    Scrap_Units=("Scrap_Units", "sum"),
    Revenue=("Revenue_Calc", "sum"),
    Scrap_Cost=("Scrap_Cost_Calc", "sum"),
    Gross_Profit=("Gross_Profit_Calc", "sum"),
)

monthly["Scrap_Rate_%"] = (
    monthly["Scrap_Units"]
    / monthly["Production_Units"]
)

monthly["Margin_%"] = (
    monthly["Gross_Profit"]
    / monthly["Revenue"]
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Production_Units=("Production_Units", "sum"),
    Scrap_Units=("Scrap_Units", "sum"),
    Revenue=("Revenue_Calc", "sum"),
    Scrap_Cost=("Scrap_Cost_Calc", "sum"),
    Gross_Profit=("Gross_Profit_Calc", "sum"),
)

region["Scrap_Rate_%"] = (
    region["Scrap_Units"]
    / region["Production_Units"]
)

region["Margin_%"] = (
    region["Gross_Profit"]
    / region["Revenue"]
)

cost = df.groupby(
    "Product",
    as_index=False
)[
    [
        "Material_Cost",
        "Labour_Cost",
        "Overhead_Cost",
        "Scrap_Cost_Calc"
    ]
].sum().rename(
    columns={
        "Scrap_Cost_Calc": "Scrap_Cost"
    }
)

product.to_csv(
    OUTPUT_DIR / "product_scrap_margin.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_scrap_margin.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_scrap_margin.csv",
    index=False
)

cost.to_csv(
    OUTPUT_DIR / "cost_analysis.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["Scrap_Cost"],
    color="#4472C4"
)

plt.title("Scrap Cost by Product")
plt.xlabel("Product")
plt.ylabel("Scrap Cost")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "scrap_cost_by_product.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.plot(
    monthly["Month"],
    monthly["Scrap_Cost"],
    marker="o",
    color="#ED7D31"
)

plt.title("Monthly Scrap Cost")
plt.xlabel("Month")
plt.ylabel("Scrap Cost")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_scrap_cost.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["Scrap_Rate_%"] * 100,
    color="#70AD47"
)

plt.title("Scrap Rate by Product")
plt.xlabel("Product")
plt.ylabel("Scrap Rate (%)")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "scrap_rate_by_product.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["Margin_%"] * 100,
    color="#8064A2"
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

print("Day 053 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output folder: {OUTPUT_DIR}")