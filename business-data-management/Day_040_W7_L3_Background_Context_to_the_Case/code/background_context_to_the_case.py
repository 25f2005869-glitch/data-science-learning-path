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

product_summary = (
    df.groupby("Product", as_index=False)
      .agg(
          Production_Units=("Production_Units", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Revenue=("Revenue", "sum"),
          Production_Cost=("Production_Cost", "sum"),
          Gross_Margin=("Gross_Margin", "sum")
      )
)

region_summary = (
    df.groupby("Region", as_index=False)
      .agg(
          Production_Units=("Production_Units", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Revenue=("Revenue", "sum"),
          Production_Cost=("Production_Cost", "sum"),
          Gross_Margin=("Gross_Margin", "sum")
      )
)

product_summary.to_csv(
    BASE_DIR / "background_product_summary.csv",
    index=False
)

region_summary.to_csv(
    BASE_DIR / "background_region_summary.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    product_summary["Product"],
    product_summary["Revenue"],
    color="#4472C4"
)

plt.title("Illustrative ACE Gears Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "background_revenue_by_product.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    region_summary["Region"],
    region_summary["Revenue"],
    color="#ED7D31"
)

plt.title("Illustrative ACE Gears Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "background_revenue_by_region.png",
    dpi=160
)

plt.close()

print("Background context analysis completed.")

print("\nProduct Context Summary:")
print(product_summary)

print("\nRegion Context Summary:")
print(region_summary)