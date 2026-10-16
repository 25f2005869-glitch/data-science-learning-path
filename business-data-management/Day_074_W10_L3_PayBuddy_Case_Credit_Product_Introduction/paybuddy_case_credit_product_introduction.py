from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 074
# Topic: PayBuddy Case — Credit Product Introduction

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_074_W10_L3_PayBuddy_Case_Credit_Product_Introduction.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="PayBuddy_Credit_Data", header=2)

numeric_cols = [
    "Credit_Limit_Rupee",
    "Credit_Utilised_Rupee",
    "Transactions_Lakh",
    "Repayment_Score",
    "Annual_Credit_Cost_Rupee",
    "Customer_Activity_Score"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Utilisation_%"] = (
    df["Credit_Utilised_Rupee"]
    / df["Credit_Limit_Rupee"]
    * 100
)

df["Available_Credit_Rupee"] = (
    df["Credit_Limit_Rupee"]
    - df["Credit_Utilised_Rupee"]
)

df["Credit_Activity_Index"] = (
    df["Transactions_Lakh"]
    * df["Customer_Activity_Score"]
    / 100
)

product = df.groupby(
    "Credit_Product",
    as_index=False
).agg(
    Customers=("Customer_ID", "count"),
    Total_Credit_Limit=("Credit_Limit_Rupee", "sum"),
    Total_Credit_Utilised=("Credit_Utilised_Rupee", "sum"),
    Average_Utilisation=("Utilisation_%", "mean"),
    Total_Transactions_Lakh=("Transactions_Lakh", "sum"),
    Average_Repayment_Score=("Repayment_Score", "mean")
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Customers=("Customer_ID", "count"),
    Total_Credit_Limit=("Credit_Limit_Rupee", "sum"),
    Total_Credit_Utilised=("Credit_Utilised_Rupee", "sum"),
    Average_Utilisation=("Utilisation_%", "mean"),
    Total_Transactions_Lakh=("Transactions_Lakh", "sum"),
    Average_Activity_Score=("Customer_Activity_Score", "mean")
)

segment = df.groupby(
    "Customer_Segment",
    as_index=False
).agg(
    Customers=("Customer_ID", "count"),
    Average_Credit_Limit=("Credit_Limit_Rupee", "mean"),
    Average_Credit_Utilised=("Credit_Utilised_Rupee", "mean"),
    Average_Utilisation=("Utilisation_%", "mean"),
    Average_Repayment_Score=("Repayment_Score", "mean"),
    Average_Activity_Score=("Customer_Activity_Score", "mean")
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Customers",
        "Total Credit Limit (Rupee)",
        "Total Credit Utilised (Rupee)",
        "Overall Credit Utilisation %",
        "Total Transactions (Lakh)",
        "Average Repayment Score",
        "Average Customer Activity Score"
    ],
    "Value": [
        len(df),
        df["Credit_Limit_Rupee"].sum(),
        df["Credit_Utilised_Rupee"].sum(),
        (
            df["Credit_Utilised_Rupee"].sum()
            / df["Credit_Limit_Rupee"].sum()
            * 100
        ),
        df["Transactions_Lakh"].sum(),
        df["Repayment_Score"].mean(),
        df["Customer_Activity_Score"].mean()
    ]
})

df.to_csv(
    OUTPUT_DIR / "paybuddy_credit_data.csv",
    index=False
)

product.to_csv(
    OUTPUT_DIR / "credit_product_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_credit_summary.csv",
    index=False
)

segment.to_csv(
    OUTPUT_DIR / "customer_segment_credit_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "credit_product_kpis.csv",
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
    product["Credit_Product"],
    product["Customers"],
    "Customers by Credit Product",
    "Credit Product",
    "Customers",
    "customers_by_credit_product.png",
    "#4472C4",
    20
)

save_bar(
    product["Credit_Product"],
    product["Total_Credit_Utilised"],
    "Credit Utilised by Product",
    "Credit Product",
    "Credit Utilised (Rupee)",
    "credit_utilised_by_product.png",
    "#ED7D31",
    20
)

save_bar(
    region["Region"],
    region["Total_Transactions_Lakh"],
    "Transaction Volume by Region",
    "Region",
    "Transactions (Lakh)",
    "transaction_volume_by_region.png",
    "#70AD47"
)

save_bar(
    segment["Customer_Segment"],
    segment["Average_Credit_Utilised"],
    "Average Credit Utilised by Customer Segment",
    "Customer Segment",
    "Average Credit Utilised (Rupee)",
    "average_credit_utilised_by_segment.png",
    "#8064A2",
    20
)

print("Day 074 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")