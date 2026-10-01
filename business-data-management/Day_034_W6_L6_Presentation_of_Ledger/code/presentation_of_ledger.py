from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 034
# Topic: Presentation of Ledger

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError(
        "No Excel workbook found in the Day 034 folder."
    )

excel_file = files[0]

df = pd.read_excel(
    excel_file,
    sheet_name="Inventory_Ledger"
)

df["Date"] = pd.to_datetime(df["Date"])

print("\n=== W6_L6 PRESENTATION OF LEDGER ===")
print("Workbook:", excel_file.name)
print("Rows:", len(df))
print("Products:", df["Product"].nunique())
print("Total Purchases:", df["Purchases"].sum())
print("Total Sales Units:", df["Sales_Units"].sum())

product_summary = (
    df.groupby("Product")
    .agg(
        Total_Purchases=("Purchases", "sum"),
        Total_Sales_Units=("Sales_Units", "sum"),
        Average_Inventory=("Closing_Stock", "mean"),
        Closing_Stock=("Closing_Stock", "last")
    )
    .reset_index()
)

monthly_summary = (
    df.assign(
        Month=df["Date"]
        .dt.to_period("M")
        .astype(str)
    )
    .groupby("Month")
    .agg(
        Purchases=("Purchases", "sum"),
        Sales_Units=("Sales_Units", "sum"),
        Closing_Stock=("Closing_Stock", "sum")
    )
    .reset_index()
)

transaction_summary = (
    df.groupby("Transaction_Type")
    .agg(
        Records=("Transaction_Type", "size"),
        Purchases=("Purchases", "sum"),
        Sales_Units=("Sales_Units", "sum")
    )
    .reset_index()
)

product_summary.to_csv(
    BASE_DIR / "product_ledger_summary.csv",
    index=False
)

monthly_summary.to_csv(
    BASE_DIR / "monthly_ledger_summary.csv",
    index=False
)

transaction_summary.to_csv(
    BASE_DIR / "transaction_summary.csv",
    index=False
)

print("\n--- Product Ledger Summary ---")
print(product_summary)

print("\n--- Monthly Ledger Summary ---")
print(monthly_summary)

print("\n--- Transaction Summary ---")
print(transaction_summary)

plt.figure(figsize=(9, 5))

plt.bar(
    product_summary["Product"],
    product_summary["Total_Sales_Units"]
)

plt.title("Sales Units by Product")
plt.xlabel("Product")
plt.ylabel("Sales Units")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    BASE_DIR / "sales_units_by_product.png",
    dpi=150
)

plt.close()

plt.figure(figsize=(9, 5))

plt.plot(
    monthly_summary["Month"],
    monthly_summary["Closing_Stock"],
    marker="o"
)

plt.title("Monthly Closing Stock")
plt.xlabel("Month")
plt.ylabel("Closing Stock")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    BASE_DIR / "monthly_closing_stock.png",
    dpi=150
)

plt.close()

highest_sales = product_summary.loc[
    product_summary["Total_Sales_Units"].idxmax()
]

highest_purchase = product_summary.loc[
    product_summary["Total_Purchases"].idxmax()
]

print("\n--- Presentation Insights ---")

print(
    "Highest sales product:",
    highest_sales["Product"],
    int(highest_sales["Total_Sales_Units"])
)

print(
    "Highest purchase product:",
    highest_purchase["Product"],
    int(highest_purchase["Total_Purchases"])
)

print("\nLedger presentation analysis completed.")