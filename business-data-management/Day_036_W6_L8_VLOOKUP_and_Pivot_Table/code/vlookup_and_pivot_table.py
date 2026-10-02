from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError("No Excel workbook found in the Day 036 folder.")

xlsx_path = files[0]

df = pd.read_excel(
    xlsx_path,
    sheet_name="Sales_Data"
)

master = pd.read_excel(
    xlsx_path,
    sheet_name="Product_Master"
)

# VLOOKUP equivalent in pandas
enriched = df.merge(
    master,
    on="Product",
    how="left",
    suffixes=("", "_Master")
)

enriched.to_csv(
    BASE_DIR / "vlookup_enriched_sales.csv",
    index=False
)

# Product pivot-style summary
product_summary = (
    df.groupby("Product", as_index=False)
      .agg(
          Total_Units=("Units", "sum"),
          Total_Revenue=("Revenue", "sum"),
          Average_Unit_Price=("Unit_Price", "mean")
      )
)

# Region pivot-style summary
region_summary = (
    df.groupby("Region", as_index=False)
      .agg(
          Total_Units=("Units", "sum"),
          Total_Revenue=("Revenue", "sum")
      )
)

# Channel pivot-style summary
channel_summary = (
    df.groupby("Channel", as_index=False)
      .agg(
          Total_Units=("Units", "sum"),
          Total_Revenue=("Revenue", "sum")
      )
)

product_summary.to_csv(
    BASE_DIR / "pivot_product_summary.csv",
    index=False
)

region_summary.to_csv(
    BASE_DIR / "pivot_region_summary.csv",
    index=False
)

channel_summary.to_csv(
    BASE_DIR / "pivot_channel_summary.csv",
    index=False
)

# Product revenue chart
plt.figure(figsize=(9, 5))

plt.bar(
    product_summary["Product"],
    product_summary["Total_Revenue"],
    color="#4472C4"
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    BASE_DIR / "revenue_by_product.png",
    dpi=160
)

plt.close()

# Region revenue chart
plt.figure(figsize=(8, 5))

plt.bar(
    region_summary["Region"],
    region_summary["Total_Revenue"],
    color="#ED7D31"
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "revenue_by_region.png",
    dpi=160
)

plt.close()

print("VLOOKUP enrichment and pivot-style summaries completed.")

print("\nProduct summary:")
print(product_summary)

print("\nRegion summary:")
print(region_summary)

print("\nChannel summary:")
print(channel_summary)