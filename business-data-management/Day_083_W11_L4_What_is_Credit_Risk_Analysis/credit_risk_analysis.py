from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 083
# Topic: What is Credit Risk Analysis

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR /
    "Day_083_W11_L4_What_is_Credit_Risk_Analysis.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Credit_Risk_Data",
    header=3
)

numeric_cols = [
    "Age",
    "Monthly_Income_Rupee",
    "Loan_Amount_Rupee",
    "Tenure_Months",
    "Debt_to_Income_%",
    "Credit_Score",
    "Past_Delinquencies",
    "Default_Flag",
    "High_Risk_Flag"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["Annual_Income_Rupee"] = (
    df["Monthly_Income_Rupee"] * 12
)

df["Loan_to_Annual_Income_%"] = (
    df["Loan_Amount_Rupee"]
    / df["Annual_Income_Rupee"]
    * 100
)

df["Monthly_Installment_Estimate"] = (
    df["Loan_Amount_Rupee"]
    / df["Tenure_Months"]
)

df["Risk_Score"] = (
    (750 - df["Credit_Score"]).clip(lower=0)
    * 0.45
    + df["Debt_to_Income_%"] * 2.0
    + df["Past_Delinquencies"] * 4.0
    + df["Default_Flag"] * 30
)

product = df.groupby(
    "Loan_Product",
    as_index=False
).agg(
    Customers=("Customer_ID", "count"),
    Total_Loan_Amount=(
        "Loan_Amount_Rupee",
        "sum"
    ),
    Average_Credit_Score=(
        "Credit_Score",
        "mean"
    ),
    Average_DTI=(
        "Debt_to_Income_%",
        "mean"
    ),
    Defaults=(
        "Default_Flag",
        "sum"
    )
)

product["Default_Rate_%"] = (
    product["Defaults"]
    / product["Customers"]
    * 100
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Customers=("Customer_ID", "count"),
    Total_Loan_Amount=(
        "Loan_Amount_Rupee",
        "sum"
    ),
    Average_Credit_Score=(
        "Credit_Score",
        "mean"
    ),
    Average_DTI=(
        "Debt_to_Income_%",
        "mean"
    ),
    Defaults=(
        "Default_Flag",
        "sum"
    )
)

region["Default_Rate_%"] = (
    region["Defaults"]
    / region["Customers"]
    * 100
)

risk = df.groupby(
    "Risk_Level",
    observed=False,
    as_index=False
).agg(
    Customers=("Customer_ID", "count"),
    Average_Credit_Score=(
        "Credit_Score",
        "mean"
    ),
    Average_DTI=(
        "Debt_to_Income_%",
        "mean"
    ),
    Defaults=(
        "Default_Flag",
        "sum"
    )
)

risk["Default_Rate_%"] = (
    risk["Defaults"]
    / risk["Customers"].replace(0, 1)
    * 100
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Customers",
        "Total Loan Exposure",
        "Average Credit Score",
        "Average DTI %",
        "Total Defaults",
        "Default Rate %",
        "High Risk Customers"
    ],
    "Value": [
        len(df),
        df["Loan_Amount_Rupee"].sum(),
        df["Credit_Score"].mean(),
        df["Debt_to_Income_%"].mean(),
        df["Default_Flag"].sum(),
        df["Default_Flag"].mean() * 100,
        df["High_Risk_Flag"].sum()
    ]
})

df.to_csv(
    OUTPUT_DIR / "credit_risk_data.csv",
    index=False
)

product.to_csv(
    OUTPUT_DIR / "product_risk_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_risk_summary.csv",
    index=False
)

risk.to_csv(
    OUTPUT_DIR / "risk_level_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "credit_risk_kpis.csv",
    index=False
)


def save_bar(
    x,
    y,
    title,
    xlabel,
    ylabel,
    filename,
    color,
    rotation=0
):
    plt.figure(figsize=(9, 5))

    plt.bar(
        x,
        y,
        color=color
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(
        rotation=rotation
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=160
    )

    plt.close()


save_bar(
    product["Loan_Product"],
    product["Default_Rate_%"],
    "Default Rate by Loan Product",
    "Loan Product",
    "Default Rate (%)",
    "default_rate_by_product.png",
    "#4472C4",
    20
)

save_bar(
    region["Region"],
    region["Average_Credit_Score"],
    "Average Credit Score by Region",
    "Region",
    "Average Credit Score",
    "credit_score_by_region.png",
    "#ED7D31"
)

save_bar(
    product["Loan_Product"],
    product["Total_Loan_Amount"],
    "Loan Exposure by Product",
    "Loan Product",
    "Loan Amount (Rupee)",
    "loan_exposure_by_product.png",
    "#70AD47",
    20
)

plt.figure(figsize=(9, 5))

plt.scatter(
    df["Credit_Score"],
    df["Debt_to_Income_%"],
    color="#8064A2"
)

plt.title(
    "Credit Score vs Debt-to-Income"
)

plt.xlabel(
    "Credit Score"
)

plt.ylabel(
    "Debt-to-Income (%)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR /
    "credit_score_vs_dti.png",
    dpi=160
)

plt.close()

print(
    "Day 083 credit risk analysis complete."
)

print(
    f"Input: {INPUT_FILE}"
)

print(
    f"Output: {OUTPUT_DIR}"
)