from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError("No Excel workbook found.")

xlsx_path = files[0]

df = pd.read_excel(
    xlsx_path,
    sheet_name="ACE_Gears_Data"
)

df["Gross_Margin"] = (
    df["Revenue"] -
    df["Production_Cost"]
)

df["Scrap_Rate"] = (
    df["Scrap_Units"] /
    df["Production_Units"]
)

product_summary = (
    df.groupby("Product", as_index=False)
      .agg(
          Production_Units=("Production_Units", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Scrap_Units=("Scrap_Units", "sum"),
          Revenue=("Revenue", "sum"),
          Production_Cost=("Production_Cost", "sum"),
          Gross_Margin=("Gross_Margin", "sum")
      )
)

product_summary["Scrap_Rate"] = (
    product_summary["Scrap_Units"] /
    product_summary["Production_Units"]
)

region_summary = (
    df.groupby("Region", as_index=False)
      .agg(
          Production_Units=("Production_Units", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Scrap_Units=("Scrap_Units", "sum"),
          Revenue=("Revenue", "sum"),
          Production_Cost=("Production_Cost", "sum"),
          Gross_Margin=("Gross_Margin", "sum")
      )
)

region_summary["Scrap_Rate"] = (
    region_summary["Scrap_Units"] /
    region_summary["Production_Units"]
)

customer_summary = (
    df.groupby("Customer_Type", as_index=False)
      .agg(
          Production_Units=("Production_Units", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Revenue=("Revenue", "sum"),
          Production_Cost=("Production_Cost", "sum")
      )
)

customer_summary["Gross_Margin"] = (
    customer_summary["Revenue"] -
    customer_summary["Production_Cost"]
)

product_summary.to_csv(
    BASE_DIR / "ace_gears_product_summary.csv",
    index=False
)

region_summary.to_csv(
    BASE_DIR / "ace_gears_region_summary.csv",
    index=False
)

customer_summary.to_csv(
    BASE_DIR / "ace_gears_customer_summary.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    product_summary["Product"],
    product_summary["Revenue"],
    color="#4472C4"
)

plt.title("ACE Gears Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "ace_gears_revenue_by_product.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    region_summary["Region"],
    region_summary["Revenue"],
    color="#ED7D31"
)

plt.title("ACE Gears Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "ace_gears_revenue_by_region.png",
    dpi=160
)

plt.close()

print("ACE Gears case introduction analysis completed.")

print("\nProduct Summary:")
print(product_summary)

print("\nRegion Summary:")
print(region_summary)

print("\nCustomer Summary:")
print(customer_summary)