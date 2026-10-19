from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 085
# Topic: Credit Risk Analysis — Review of Data

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_085_W11_L6_Credit_Risk_Analysis_Review_of_Data.xlsx"
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

# ---------------------------------------------------------
# Missing-value review
# ---------------------------------------------------------

missing = df.isna().sum().reset_index()

missing.columns = [
    "Field",
    "Missing_Count"
]

missing["Missing_%"] = (
    missing["Missing_Count"]
    / len(df)
    * 100
)

# ---------------------------------------------------------
# Duplicate review
# ---------------------------------------------------------

duplicates = pd.DataFrame({
    "Check": [
        "Duplicate Record_ID",
        "Duplicate Customer_ID",
        "Duplicate Rows"
    ],
    "Count": [
        int(
            df["Record_ID"]
            .duplicated()
            .sum()
        ),
        int(
            df["Customer_ID"]
            .duplicated()
            .sum()
        ),
        int(
            df.duplicated()
            .sum()
        )
    ]
})

# ---------------------------------------------------------
# Numeric review
# ---------------------------------------------------------

numeric_review = pd.DataFrame({
    "Field": numeric_cols,
    "Count": [
        df[col].count()
        for col in numeric_cols
    ],
    "Mean": [
        df[col].mean()
        for col in numeric_cols
    ],
    "Median": [
        df[col].median()
        for col in numeric_cols
    ],
    "Minimum": [
        df[col].min()
        for col in numeric_cols
    ],
    "Maximum": [
        df[col].max()
        for col in numeric_cols
    ],
    "Missing": [
        df[col].isna().sum()
        for col in numeric_cols
    ]
})

# ---------------------------------------------------------
# Category review
# ---------------------------------------------------------

category_records = []

for col in [
    "Employment_Type",
    "Region",
    "Loan_Product"
]:

    values = (
        df[col]
        .value_counts(
            dropna=False
        )
    )

    for category, count in values.items():

        category_records.append([
            col,
            category,
            int(count),
            round(
                count / len(df) * 100,
                2
            )
        ])

category_review = pd.DataFrame(
    category_records,
    columns=[
        "Field",
        "Category",
        "Count",
        "Share_%"
    ]
)

# ---------------------------------------------------------
# Product risk review
# ---------------------------------------------------------

product = (
    df.groupby(
        "Loan_Product",
        as_index=False
    )
    .agg(
        Customers=(
            "Customer_ID",
            "count"
        ),
        Total_Loan_Amount=(
            "Loan_Amount_Rupee",
            "sum"
        ),
        Avg_Credit_Score=(
            "Credit_Score",
            "mean"
        ),
        Avg_DTI=(
            "Debt_to_Income_%",
            "mean"
        ),
        Defaults=(
            "Default_Flag",
            "sum"
        ),
        High_Risk_Customers=(
            "High_Risk_Flag",
            "sum"
        )
    )
)

product["Default_Rate_%"] = (
    product["Defaults"]
    / product["Customers"]
    * 100
)

# ---------------------------------------------------------
# Region risk review
# ---------------------------------------------------------

region = (
    df.groupby(
        "Region",
        as_index=False
    )
    .agg(
        Customers=(
            "Customer_ID",
            "count"
        ),
        Total_Loan_Amount=(
            "Loan_Amount_Rupee",
            "sum"
        ),
        Avg_Credit_Score=(
            "Credit_Score",
            "mean"
        ),
        Avg_DTI=(
            "Debt_to_Income_%",
            "mean"
        ),
        Defaults=(
            "Default_Flag",
            "sum"
        ),
        High_Risk_Customers=(
            "High_Risk_Flag",
            "sum"
        )
    )
)

region["Default_Rate_%"] = (
    region["Defaults"]
    / region["Customers"]
    * 100
)

# ---------------------------------------------------------
# Employment review
# ---------------------------------------------------------

employment = (
    df.groupby(
        "Employment_Type",
        as_index=False
    )
    .agg(
        Customers=(
            "Customer_ID",
            "count"
        ),
        Avg_Income=(
            "Monthly_Income_Rupee",
            "mean"
        ),
        Avg_Loan_Amount=(
            "Loan_Amount_Rupee",
            "mean"
        ),
        Avg_Credit_Score=(
            "Credit_Score",
            "mean"
        ),
        Avg_DTI=(
            "Debt_to_Income_%",
            "mean"
        ),
        Defaults=(
            "Default_Flag",
            "sum"
        ),
        High_Risk_Customers=(
            "High_Risk_Flag",
            "sum"
        )
    )
)

# ---------------------------------------------------------
# Outcome review
# ---------------------------------------------------------

outcome = pd.DataFrame({
    "Outcome": [
        "Default",
        "Non-Default",
        "High Risk",
        "Not High Risk"
    ],
    "Count": [
        int(
            df["Default_Flag"]
            .sum()
        ),
        int(
            (
                df["Default_Flag"] == 0
            ).sum()
        ),
        int(
            df["High_Risk_Flag"]
            .sum()
        ),
        int(
            (
                df["High_Risk_Flag"] == 0
            ).sum()
        )
    ]
})

outcome["Share_%"] = (
    outcome["Count"]
    / len(df)
    * 100
)

# ---------------------------------------------------------
# KPI review
# ---------------------------------------------------------

kpis = pd.DataFrame({
    "KPI": [
        "Total Records",
        "Unique Customers",
        "Missing Cells",
        "Duplicate Record IDs",
        "Duplicate Customer IDs",
        "Total Loan Exposure",
        "Average Credit Score",
        "Average DTI %",
        "Total Defaults",
        "Default Rate %",
        "High Risk Customers",
        "High Risk Share %"
    ],
    "Value": [
        len(df),
        df["Customer_ID"].nunique(),
        int(
            df.isna()
            .sum()
            .sum()
        ),
        int(
            df["Record_ID"]
            .duplicated()
            .sum()
        ),
        int(
            df["Customer_ID"]
            .duplicated()
            .sum()
        ),
        df["Loan_Amount_Rupee"]
        .sum(),
        df["Credit_Score"]
        .mean(),
        df["Debt_to_Income_%"]
        .mean(),
        df["Default_Flag"]
        .sum(),
        df["Default_Flag"]
        .mean()
        * 100,
        df["High_Risk_Flag"]
        .sum(),
        df["High_Risk_Flag"]
        .mean()
        * 100
    ]
})

# ---------------------------------------------------------
# Export CSV files
# ---------------------------------------------------------

exports = [
    (
        df,
        "credit_risk_data_review.csv"
    ),
    (
        missing,
        "missing_value_review.csv"
    ),
    (
        duplicates,
        "duplicate_check.csv"
    ),
    (
        numeric_review,
        "numeric_data_review.csv"
    ),
    (
        category_review,
        "category_data_review.csv"
    ),
    (
        product,
        "product_risk_review.csv"
    ),
    (
        region,
        "region_risk_review.csv"
    ),
    (
        employment,
        "employment_risk_review.csv"
    ),
    (
        outcome,
        "outcome_review.csv"
    ),
    (
        kpis,
        "credit_risk_review_kpis.csv"
    )
]

for data, filename in exports:

    data.to_csv(
        OUTPUT_DIR / filename,
        index=False
    )

# ---------------------------------------------------------
# Chart function
# ---------------------------------------------------------

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

    plt.figure(
        figsize=(9, 5)
    )

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

# ---------------------------------------------------------
# Charts
# ---------------------------------------------------------

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
    region["Avg_Credit_Score"],
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

plt.figure(
    figsize=(9, 5)
)

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
    OUTPUT_DIR
    / "credit_score_vs_dti.png",
    dpi=160
)

plt.close()

print(
    "Day 085 analysis complete."
)

print(
    f"Input: {INPUT_FILE}"
)

print(
    f"Output: {OUTPUT_DIR}"
)