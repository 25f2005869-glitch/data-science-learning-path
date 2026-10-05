from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 043
# Topic: W7_L6 Revenue Analysis Presentation

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError(
        "No Excel workbook found in the Day_043 folder."
    )

xlsx_file = files[0]

df = pd.read_excel(
    xlsx_file,
    sheet_name="Revenue_Data"
)

df["Gross_Margin"] = (
    df["Revenue"] - df["Production_Cost"]
)

df["Margin_%"] = (
    df["Gross_Margin"] / df["Revenue"]
)

months = [
    "Jan-2023",
    "Feb-2023",
    "Mar-2023",
    "Apr-2023",
    "May-2023",
    "Jun-2023"
]

monthly = (
    df.groupby("Month", sort=False)
      .agg(
          Revenue=("Revenue", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Production_Units=("Production_Units", "sum"),
          Gross_Margin=("Gross_Margin", "sum")
      )
      .reindex(months)
      .reset_index()
)

monthly["MoM_Growth"] = (
    monthly["Revenue"].pct_change()
)

product = (
    df.groupby("Product")
      .agg(
          Revenue=("Revenue", "sum"),
          Sales_Units=("Sales_Units", "sum"),
          Production_Units=("Production_Units", "sum"),
          Gross_Margin=("Gross_Margin", "sum")
      )
      .reset_index()
)

product["Margin_%"] = (
    product["Gross_Margin"] / product["Revenue"]
)

product["Revenue_Share"] = (
    product["Revenue"] / product["Revenue"].sum()
)

product = product.sort_values(
    "Revenue",
    ascending=False
).reset_index(drop=True)

region = (
    df.groupby("Region")
      .agg(
          Revenue=("Revenue", "sum"),
          Sales_Units=("Sales_Units", "sum")
      )
      .reset_index()
)

region["Revenue_Share"] = (
    region["Revenue"] / region["Revenue"].sum()
)

region = region.sort_values(
    "Revenue",
    ascending=False
).reset_index(drop=True)

output = BASE_DIR / "outputs"
output.mkdir(exist_ok=True)

monthly.to_csv(
    output / "monthly_revenue.csv",
    index=False
)

product.to_csv(
    output / "product_revenue.csv",
    index=False
)

region.to_csv(
    output / "region_revenue.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.plot(
    monthly["Month"],
    monthly["Revenue"],
    marker="o",
    color="#4472C4"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(alpha=0.25)

plt.tight_layout()

plt.savefig(
    output / "monthly_revenue_trend.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    product["Product"],
    product["Revenue"],
    color="#ED7D31"
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    output / "revenue_by_product.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    region["Region"],
    region["Revenue"],
    color="#70AD47"
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    output / "revenue_by_region.png",
    dpi=160
)

plt.close()

print("Revenue Analysis Presentation completed.")

print(
    f"Total Revenue: "
    f"{df['Revenue'].sum():,.0f}"
)

print(
    "Highest Revenue Month: "
    f"{monthly.loc[monthly['Revenue'].idxmax(), 'Month']}"
)

print(
    "Top Product: "
    f"{product.iloc[0]['Product']}"
)

print(
    "Top Region: "
    f"{region.iloc[0]['Region']}"
)