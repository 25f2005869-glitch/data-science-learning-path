from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 049
# Topic: Scrap Analysis Working
# ============================================================


# ------------------------------------------------------------
# 1. Paths
# ------------------------------------------------------------

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_049_W8_L2_Scrap_Analysis_Working.xlsx"

OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


# ------------------------------------------------------------
# 2. Read Excel data
# ------------------------------------------------------------

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Scrap_Analysis_Data"
)


# ------------------------------------------------------------
# 3. Product-level analysis
# ------------------------------------------------------------

product = (
    df.groupby("Product", as_index=False)
    .agg(
        Production_Units=("Production_Units", "sum"),
        Scrap_Units=("Scrap_Units", "sum"),
        Good_Units=("Good_Units", "sum"),
        Scrap_Cost=("Scrap_Cost", "sum")
    )
)

product["Scrap_Rate"] = (
    product["Scrap_Units"]
    / product["Production_Units"]
)


# ------------------------------------------------------------
# 4. Monthly analysis
# ------------------------------------------------------------

monthly = (
    df.groupby("Month", as_index=False)
    .agg(
        Production_Units=("Production_Units", "sum"),
        Scrap_Units=("Scrap_Units", "sum"),
        Good_Units=("Good_Units", "sum"),
        Scrap_Cost=("Scrap_Cost", "sum")
    )
)

monthly["Scrap_Rate"] = (
    monthly["Scrap_Units"]
    / monthly["Production_Units"]
)


# ------------------------------------------------------------
# 5. Regional analysis
# ------------------------------------------------------------

region = (
    df.groupby("Region", as_index=False)
    .agg(
        Production_Units=("Production_Units", "sum"),
        Scrap_Units=("Scrap_Units", "sum"),
        Good_Units=("Good_Units", "sum"),
        Scrap_Cost=("Scrap_Cost", "sum")
    )
)

region["Scrap_Rate"] = (
    region["Scrap_Units"]
    / region["Production_Units"]
)


# ------------------------------------------------------------
# 6. Product-region analysis
# ------------------------------------------------------------

product_region = (
    df.groupby(
        ["Product", "Region"],
        as_index=False
    )
    .agg(
        Production_Units=("Production_Units", "sum"),
        Scrap_Units=("Scrap_Units", "sum"),
        Good_Units=("Good_Units", "sum"),
        Scrap_Cost=("Scrap_Cost", "sum")
    )
)

product_region["Scrap_Rate"] = (
    product_region["Scrap_Units"]
    / product_region["Production_Units"]
)


# ------------------------------------------------------------
# 7. Export CSV files
# ------------------------------------------------------------

product.to_csv(
    OUTPUT_DIR / "product_scrap_summary.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_scrap.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_scrap.csv",
    index=False
)

product_region.to_csv(
    OUTPUT_DIR / "product_region_scrap.csv",
    index=False
)


# ------------------------------------------------------------
# 8. Chart — Production vs Scrap by Product
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

x = range(len(product))
width = 0.35

plt.bar(
    [value - width / 2 for value in x],
    product["Production_Units"],
    width=width,
    label="Production",
    color="#4472C4"
)

plt.bar(
    [value + width / 2 for value in x],
    product["Scrap_Units"],
    width=width,
    label="Scrap",
    color="#ED7D31"
)

plt.xticks(
    list(x),
    product["Product"]
)

plt.title("Production vs Scrap by Product")
plt.xlabel("Product")
plt.ylabel("Units")
plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "production_vs_scrap_by_product.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 9. Chart — Monthly Scrap Rate
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    monthly["Month"],
    monthly["Scrap_Rate"],
    marker="o",
    color="#70AD47"
)

plt.title("Monthly Scrap Rate")
plt.xlabel("Month")
plt.ylabel("Scrap Rate")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_scrap_rate.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 10. Chart — Scrap Units by Product
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["Scrap_Units"],
    color="#8064A2"
)

plt.title("Scrap Units by Product")
plt.xlabel("Product")
plt.ylabel("Scrap Units")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "scrap_units_by_product.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 11. Chart — Scrap Rate by Region
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    region["Region"],
    region["Scrap_Rate"],
    color="#5B9BD5"
)

plt.title("Scrap Rate by Region")
plt.xlabel("Region")
plt.ylabel("Scrap Rate")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "scrap_rate_by_region.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 12. Overall metrics
# ------------------------------------------------------------

total_production = df["Production_Units"].sum()

total_scrap = df["Scrap_Units"].sum()

total_good = df["Good_Units"].sum()

overall_scrap_rate = (
    total_scrap
    / total_production
)

total_scrap_cost = df["Scrap_Cost"].sum()


# ------------------------------------------------------------
# 13. Console output
# ------------------------------------------------------------

print("=" * 60)
print("DAY 049 — SCRAP ANALYSIS WORKING")
print("=" * 60)

print(f"Total Production : {total_production:,.0f}")
print(f"Total Scrap      : {total_scrap:,.0f}")
print(f"Total Good Units : {total_good:,.0f}")
print(f"Scrap Rate       : {overall_scrap_rate:.2%}")
print(f"Scrap Cost       : ₹{total_scrap_cost:,.0f}")

print("\nPRODUCT SUMMARY")
print(product)

print("\nMONTHLY SUMMARY")
print(monthly)

print("\nREGION SUMMARY")
print(region)

print("\nPRODUCT-REGION SUMMARY")
print(product_region)

print("\nAnalysis completed successfully.")