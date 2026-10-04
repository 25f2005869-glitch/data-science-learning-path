from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 041
# Topic: W7_L4 Introduction to the Dataset —
#        Sales, Production and Inventory
# ============================================================


CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


excel_files = list(BASE_DIR.glob("*.xlsx"))

if not excel_files:
    raise FileNotFoundError(
        "Excel workbook not found in the Day_041 folder."
    )

excel_file = excel_files[0]


# ============================================================
# Load Dataset
# ============================================================

df = pd.read_excel(
    excel_file,
    sheet_name="ACE_Gears_Dataset"
)


print("\n================ DATASET INFORMATION ================\n")

print("Excel File:")
print(excel_file.name)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())


# ============================================================
# Product Summary
# ============================================================

product_summary = (
    df.groupby("Product")
      .agg(
          Production_Units=("Production_Units", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Scrap_Units=("Scrap_Units", "sum"),
          Closing_Inventory=("Closing_Inventory", "sum"),
          Revenue=("Revenue", "sum"),
          Production_Cost=("Production_Cost", "sum")
      )
      .reset_index()
)

product_summary["Gross_Margin"] = (
    product_summary["Revenue"]
    - product_summary["Production_Cost"]
)

product_summary["Scrap_Rate"] = (
    product_summary["Scrap_Units"]
    / product_summary["Production_Units"]
)


product_summary.to_csv(
    OUTPUT_DIR / "product_summary.csv",
    index=False
)


# ============================================================
# Region Summary
# ============================================================

region_summary = (
    df.groupby("Region")
      .agg(
          Production_Units=("Production_Units", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Closing_Inventory=("Closing_Inventory", "sum"),
          Revenue=("Revenue", "sum")
      )
      .reset_index()
)


region_summary.to_csv(
    OUTPUT_DIR / "region_summary.csv",
    index=False
)


# ============================================================
# Monthly Summary
# ============================================================

month_order = [
    "Jan-2023",
    "Feb-2023",
    "Mar-2023"
]

monthly_summary = (
    df.groupby("Month", sort=False)
      .agg(
          Production_Units=("Production_Units", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Scrap_Units=("Scrap_Units", "sum"),
          Closing_Inventory=("Closing_Inventory", "sum"),
          Revenue=("Revenue", "sum"),
          Production_Cost=("Production_Cost", "sum")
      )
      .reindex(month_order)
      .reset_index()
)

monthly_summary["Gross_Margin"] = (
    monthly_summary["Revenue"]
    - monthly_summary["Production_Cost"]
)


monthly_summary.to_csv(
    OUTPUT_DIR / "monthly_summary.csv",
    index=False
)


# ============================================================
# Sales View
# ============================================================

sales_view = (
    df.groupby(
        ["Product", "Region", "Customer_Type"],
        as_index=False
    )
    .agg(
        Sales_Units=("Sales_Units", "sum"),
        Revenue=("Revenue", "sum")
    )
)

sales_view.to_csv(
    OUTPUT_DIR / "sales_view.csv",
    index=False
)


# ============================================================
# Production View
# ============================================================

production_view = (
    df.groupby(
        ["Product", "Region"],
        as_index=False
    )
    .agg(
        Production_Units=("Production_Units", "sum"),
        Scrap_Units=("Scrap_Units", "sum"),
        Production_Cost=("Production_Cost", "sum")
    )
)

production_view["Scrap_Rate"] = (
    production_view["Scrap_Units"]
    / production_view["Production_Units"]
)

production_view.to_csv(
    OUTPUT_DIR / "production_view.csv",
    index=False
)


# ============================================================
# Inventory View
# ============================================================

inventory_view = (
    df.groupby(
        ["Product", "Region"],
        as_index=False
    )
    .agg(
        Closing_Inventory=("Closing_Inventory", "sum")
    )
)

inventory_view.to_csv(
    OUTPUT_DIR / "inventory_view.csv",
    index=False
)


# ============================================================
# Chart 1 — Sales vs Production by Product
# ============================================================

plt.figure(figsize=(9, 5))

x = range(len(product_summary))

plt.bar(
    [i - 0.2 for i in x],
    product_summary["Sales_Units"],
    width=0.4,
    label="Sales Units",
    color="#4472C4"
)

plt.bar(
    [i + 0.2 for i in x],
    product_summary["Production_Units"],
    width=0.4,
    label="Production Units",
    color="#70AD47"
)

plt.xticks(
    list(x),
    product_summary["Product"]
)

plt.title("Sales vs Production by Product")
plt.xlabel("Product")
plt.ylabel("Units")
plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "sales_vs_production_by_product.png",
    dpi=160
)

plt.close()


# ============================================================
# Chart 2 — Closing Inventory by Product
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    product_summary["Product"],
    product_summary["Closing_Inventory"],
    color="#ED7D31"
)

plt.title("Closing Inventory by Product")
plt.xlabel("Product")
plt.ylabel("Closing Inventory")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "closing_inventory_by_product.png",
    dpi=160
)

plt.close()


# ============================================================
# Chart 3 — Monthly Revenue
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    monthly_summary["Month"],
    monthly_summary["Revenue"],
    marker="o",
    linewidth=2.5,
    color="#8064A2"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(alpha=0.25)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_revenue.png",
    dpi=160
)

plt.close()


# ============================================================
# Key Results
# ============================================================

highest_revenue_product = product_summary.loc[
    product_summary["Revenue"].idxmax(),
    "Product"
]

highest_revenue_region = region_summary.loc[
    region_summary["Revenue"].idxmax(),
    "Region"
]

highest_revenue_month = monthly_summary.loc[
    monthly_summary["Revenue"].idxmax(),
    "Month"
]


print("\n================ KEY RESULTS ================\n")

print(
    f"Total Revenue: "
    f"{df['Revenue'].sum():,.0f}"
)

print(
    f"Total Sales Units: "
    f"{df['Sales_Units'].sum():,.0f}"
)

print(
    f"Total Production Units: "
    f"{df['Production_Units'].sum():,.0f}"
)

print(
    f"Total Closing Inventory: "
    f"{df['Closing_Inventory'].sum():,.0f}"
)

print(
    f"Highest Revenue Product: "
    f"{highest_revenue_product}"
)

print(
    f"Highest Revenue Region: "
    f"{highest_revenue_region}"
)

print(
    f"Highest Revenue Month: "
    f"{highest_revenue_month}"
)

print("\nAnalysis completed successfully.")

print(
    f"\nOutput files are available in:\n"
    f"{OUTPUT_DIR}"
)