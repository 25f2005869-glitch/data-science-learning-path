from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

EXCEL_FILE = BASE_DIR / "Day_087_W11_L8_Credit_Risk_Analysis_Presentation.xlsx"

# --------------------------------------------------
# Read credit-risk dataset
# --------------------------------------------------

df = pd.read_excel(
    EXCEL_FILE,
    sheet_name="Credit_Risk_Data",
    header=2
)

# --------------------------------------------------
# Monthly portfolio analysis
# --------------------------------------------------

monthly = (
    df.groupby("Month")
      .agg(
          Customers=("Customer_ID", "count"),
          Loan_Exposure=("Loan_Exposure_Rupee", "sum"),
          Avg_Credit_Score=("Credit_Score", "mean"),
          Avg_DTI=("Debt_to_Income_%", "mean"),
          Defaults=("Default_Flag", "sum"),
          High_Risk=("High_Risk_Flag", "sum")
      )
      .reset_index()
)

monthly["Default_Rate_%"] = (
    monthly["Defaults"] /
    monthly["Customers"] *
    100
)

monthly["High_Risk_Share_%"] = (
    monthly["High_Risk"] /
    monthly["Customers"] *
    100
)

monthly["Exposure_Growth_%"] = (
    monthly["Loan_Exposure"]
    .pct_change() *
    100
)

monthly["Default_Rate_Change_pp"] = (
    monthly["Default_Rate_%"]
    .diff()
)

# --------------------------------------------------
# Product-month analysis
# --------------------------------------------------

product = (
    df.groupby(
        ["Month", "Loan_Product"]
    )
    .agg(
        Customers=("Customer_ID", "count"),
        Exposure=("Loan_Exposure_Rupee", "sum"),
        Avg_Credit_Score=("Credit_Score", "mean"),
        Defaults=("Default_Flag", "sum"),
        High_Risk=("High_Risk_Flag", "sum")
    )
    .reset_index()
)

product["Default_Rate_%"] = (
    product["Defaults"] /
    product["Customers"] *
    100
)

# --------------------------------------------------
# Region-month analysis
# --------------------------------------------------

region = (
    df.groupby(
        ["Month", "Region"]
    )
    .agg(
        Customers=("Customer_ID", "count"),
        Exposure=("Loan_Exposure_Rupee", "sum"),
        Avg_Credit_Score=("Credit_Score", "mean"),
        Defaults=("Default_Flag", "sum"),
        High_Risk=("High_Risk_Flag", "sum")
    )
    .reset_index()
)

region["Default_Rate_%"] = (
    region["Defaults"] /
    region["Customers"] *
    100
)

# --------------------------------------------------
# Export summary files
# --------------------------------------------------

monthly.to_csv(
    OUTPUT_DIR / "monthly_trend.csv",
    index=False
)

product.to_csv(
    OUTPUT_DIR / "product_monthly_trend.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_monthly_trend.csv",
    index=False
)

# --------------------------------------------------
# Chart 1 — Monthly Default Rate
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    monthly["Month"],
    monthly["Default_Rate_%"],
    marker="o"
)

plt.title("Monthly Default Rate")
plt.xlabel("Month")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_default_rate.png",
    dpi=160
)

plt.close()

# --------------------------------------------------
# Chart 2 — Monthly Loan Exposure
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    monthly["Month"],
    monthly["Loan_Exposure"]
)

plt.title("Monthly Loan Exposure")
plt.xlabel("Month")
plt.ylabel("Loan Exposure (₹)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_loan_exposure.png",
    dpi=160
)

plt.close()

# --------------------------------------------------
# Chart 3 — Average Credit Score
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    monthly["Month"],
    monthly["Avg_Credit_Score"],
    marker="o"
)

plt.title("Average Credit Score by Month")
plt.xlabel("Month")
plt.ylabel("Average Credit Score")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_credit_score.png",
    dpi=160
)

plt.close()

# --------------------------------------------------
# Chart 4 — High-Risk Customer Share
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    monthly["Month"],
    monthly["High_Risk_Share_%"],
    marker="o"
)

plt.title("High-Risk Customer Share")
plt.xlabel("Month")
plt.ylabel("High-Risk Share (%)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "high_risk_share.png",
    dpi=160
)

plt.close()

# --------------------------------------------------
# Completion message
# --------------------------------------------------

print("Day 087 credit-risk presentation analysis completed.")
print("Output directory:", OUTPUT_DIR)
print("Monthly rows:", len(monthly))
print("Product-month rows:", len(product))
print("Region-month rows:", len(region))