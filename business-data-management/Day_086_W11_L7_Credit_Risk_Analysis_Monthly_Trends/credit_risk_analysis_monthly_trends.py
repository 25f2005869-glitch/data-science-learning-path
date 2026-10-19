from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Day 086 — Credit Risk Analysis: Monthly Trends
#
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 086
# Topic: Credit Risk Analysis — Monthly Trends
# ============================================================


# ------------------------------------------------------------
# 1. File Paths
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "Day_086_W11_L7_Credit_Risk_Analysis_Monthly_Trends.xlsx"
)

OUTPUT_DIR = BASE_DIR / "output"
CHART_DIR = OUTPUT_DIR / "charts"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. Load Excel Data
# ------------------------------------------------------------

SHEET_NAME = "Monthly_Trend_Data"

df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)

print("\n" + "=" * 70)
print("CREDIT RISK ANALYSIS — MONTHLY TRENDS")
print("=" * 70)

print("\nDataset loaded successfully.")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ------------------------------------------------------------
# 3. Basic Dataset Review
# ------------------------------------------------------------

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isna().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())


# ------------------------------------------------------------
# 4. Numeric Columns
# ------------------------------------------------------------

numeric_columns = [
    "Customers",
    "Loan_Exposure_Rupee",
    "Defaults",
    "Average_Credit_Score",
    "Average_DTI_%",
    "High_Risk_Customers",
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# ------------------------------------------------------------
# 5. Sort Monthly Data
# ------------------------------------------------------------

df["Month"] = pd.to_datetime(df["Month"])

df = df.sort_values("Month").reset_index(drop=True)


# ------------------------------------------------------------
# 6. Calculate Default Rate
# ------------------------------------------------------------

df["Default_Rate_%"] = (
    df["Defaults"] / df["Customers"] * 100
)


# ------------------------------------------------------------
# 7. Calculate High-Risk Share
# ------------------------------------------------------------

df["High_Risk_Share_%"] = (
    df["High_Risk_Customers"] / df["Customers"] * 100
)


# ------------------------------------------------------------
# 8. Month-to-Month Changes
# ------------------------------------------------------------

df["Customer_Change"] = df["Customers"].diff()

df["Exposure_Change_Rupee"] = (
    df["Loan_Exposure_Rupee"].diff()
)

df["Default_Change"] = df["Defaults"].diff()

df["Default_Rate_Change_pp"] = (
    df["Default_Rate_%"].diff()
)

df["Credit_Score_Change"] = (
    df["Average_Credit_Score"].diff()
)

df["DTI_Change_pp"] = (
    df["Average_DTI_%"].diff()
)

df["High_Risk_Customer_Change"] = (
    df["High_Risk_Customers"].diff()
)

df["High_Risk_Share_Change_pp"] = (
    df["High_Risk_Share_%"].diff()
)


# ------------------------------------------------------------
# 9. Display Monthly KPI Table
# ------------------------------------------------------------

monthly_kpis = df[
    [
        "Month",
        "Customers",
        "Loan_Exposure_Rupee",
        "Defaults",
        "Default_Rate_%",
        "Average_Credit_Score",
        "Average_DTI_%",
        "High_Risk_Customers",
        "High_Risk_Share_%",
    ]
].copy()

print("\n--- Monthly KPIs ---")
print(monthly_kpis.to_string(index=False))


# ------------------------------------------------------------
# 10. Display Month-to-Month Changes
# ------------------------------------------------------------

monthly_changes = df[
    [
        "Month",
        "Customer_Change",
        "Exposure_Change_Rupee",
        "Default_Change",
        "Default_Rate_Change_pp",
        "Credit_Score_Change",
        "DTI_Change_pp",
        "High_Risk_Customer_Change",
        "High_Risk_Share_Change_pp",
    ]
].copy()

print("\n--- Month-to-Month Changes ---")
print(monthly_changes.to_string(index=False))


# ------------------------------------------------------------
# 11. Create Summary Statistics
# ------------------------------------------------------------

summary = pd.DataFrame(
    {
        "Metric": [
            "Total Customers",
            "Total Loan Exposure",
            "Total Defaults",
            "Average Default Rate",
            "Average Credit Score",
            "Average DTI",
            "Total High-Risk Customers",
            "Average High-Risk Share",
        ],
        "Value": [
            df["Customers"].sum(),
            df["Loan_Exposure_Rupee"].sum(),
            df["Defaults"].sum(),
            df["Default_Rate_%"].mean(),
            df["Average_Credit_Score"].mean(),
            df["Average_DTI_%"].mean(),
            df["High_Risk_Customers"].sum(),
            df["High_Risk_Share_%"].mean(),
        ],
    }
)

print("\n--- Credit Risk Monthly Summary ---")
print(summary.to_string(index=False))


# ------------------------------------------------------------
# 12. Identify Highest and Lowest Months
# ------------------------------------------------------------

highest_customer_month = df.loc[
    df["Customers"].idxmax(), "Month"
]

lowest_customer_month = df.loc[
    df["Customers"].idxmin(), "Month"
]

highest_exposure_month = df.loc[
    df["Loan_Exposure_Rupee"].idxmax(), "Month"
]

lowest_exposure_month = df.loc[
    df["Loan_Exposure_Rupee"].idxmin(), "Month"
]

highest_default_month = df.loc[
    df["Defaults"].idxmax(), "Month"
]

highest_default_rate_month = df.loc[
    df["Default_Rate_%"].idxmax(), "Month"
]

highest_high_risk_share_month = df.loc[
    df["High_Risk_Share_%"].idxmax(), "Month"
]


print("\n--- Key Monthly Findings ---")

print(
    f"Highest customer count: "
    f"{highest_customer_month.strftime('%Y-%m')}"
)

print(
    f"Lowest customer count: "
    f"{lowest_customer_month.strftime('%Y-%m')}"
)

print(
    f"Highest loan exposure: "
    f"{highest_exposure_month.strftime('%Y-%m')}"
)

print(
    f"Lowest loan exposure: "
    f"{lowest_exposure_month.strftime('%Y-%m')}"
)

print(
    f"Highest default count: "
    f"{highest_default_month.strftime('%Y-%m')}"
)

print(
    f"Highest default rate: "
    f"{highest_default_rate_month.strftime('%Y-%m')}"
)

print(
    f"Highest high-risk share: "
    f"{highest_high_risk_share_month.strftime('%Y-%m')}"
)


# ------------------------------------------------------------
# 13. Export Monthly KPI Data
# ------------------------------------------------------------

monthly_kpis_output = OUTPUT_DIR / "monthly_kpis.csv"

monthly_kpis.to_csv(
    monthly_kpis_output,
    index=False
)


# ------------------------------------------------------------
# 14. Export Trend Analysis
# ------------------------------------------------------------

trend_analysis_output = (
    OUTPUT_DIR / "monthly_risk_trend_analysis.csv"
)

df.to_csv(
    trend_analysis_output,
    index=False
)


# ------------------------------------------------------------
# 15. Export Summary
# ------------------------------------------------------------

summary_output = (
    OUTPUT_DIR / "credit_risk_monthly_summary.csv"
)

summary.to_csv(
    summary_output,
    index=False
)


# ------------------------------------------------------------
# 16. Prepare Month Labels
# ------------------------------------------------------------

month_labels = df["Month"].dt.strftime("%b")


# ------------------------------------------------------------
# 17. Chart 1 — Monthly Customer Volume
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    month_labels,
    df["Customers"],
    marker="o"
)

plt.title("Monthly Customer Volume")
plt.xlabel("Month")
plt.ylabel("Customers")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "monthly_customer_volume.png",
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 18. Chart 2 — Monthly Loan Exposure
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    month_labels,
    df["Loan_Exposure_Rupee"],
    marker="o"
)

plt.title("Monthly Loan Exposure")
plt.xlabel("Month")
plt.ylabel("Loan Exposure (Rupee)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "monthly_loan_exposure.png",
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 19. Chart 3 — Monthly Default Rate
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    month_labels,
    df["Default_Rate_%"],
    marker="o"
)

plt.title("Monthly Default Rate")
plt.xlabel("Month")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "monthly_default_rate.png",
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 20. Chart 4 — Average Credit Score
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    month_labels,
    df["Average_Credit_Score"],
    marker="o"
)

plt.title("Average Credit Score by Month")
plt.xlabel("Month")
plt.ylabel("Average Credit Score")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "average_credit_score.png",
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 21. Chart 5 — Average DTI
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    month_labels,
    df["Average_DTI_%"],
    marker="o"
)

plt.title("Average DTI by Month")
plt.xlabel("Month")
plt.ylabel("Average DTI (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "average_dti.png",
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 22. Chart 6 — High-Risk Share
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    month_labels,
    df["High_Risk_Share_%"],
    marker="o"
)

plt.title("Monthly High-Risk Customer Share")
plt.xlabel("Month")
plt.ylabel("High-Risk Share (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    CHART_DIR / "high_risk_share.png",
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 23. Final Output
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("ANALYSIS COMPLETED")
print("=" * 70)

print(f"\nInput file:")
print(INPUT_FILE)

print("\nOutput directory:")
print(OUTPUT_DIR)

print("\nGenerated files:")
print("- monthly_kpis.csv")
print("- monthly_risk_trend_analysis.csv")
print("- credit_risk_monthly_summary.csv")

print("\nGenerated charts:")
print("- monthly_customer_volume.png")
print("- monthly_loan_exposure.png")
print("- monthly_default_rate.png")
print("- average_credit_score.png")
print("- average_dti.png")
print("- high_risk_share.png")

print("\nDay 086 monthly credit-risk analysis completed successfully.")