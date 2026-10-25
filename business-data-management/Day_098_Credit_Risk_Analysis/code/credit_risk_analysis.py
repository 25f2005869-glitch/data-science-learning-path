# Day 098 — Credit Risk Analysis
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 098
# Topic: Credit Risk Analysis

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. PATH SETUP
# ============================================================

def find_workbook():
    """Find the Day 098 workbook from common project locations."""

    possible_paths = [
        Path("/mnt/data/Day_098_Credit_Risk_Analysis.xlsx"),
        Path("Day_098_Credit_Risk_Analysis.xlsx"),
        Path("../Day_098_Credit_Risk_Analysis.xlsx"),
    ]

    for path in possible_paths:
        if path.exists():
            return path.resolve()

    raise FileNotFoundError(
        "Day_098_Credit_Risk_Analysis.xlsx was not found."
    )


BASE_DIR = Path(__file__).resolve().parent.parent
WORKBOOK_PATH = find_workbook()
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD RAW DATA
# ============================================================

df = pd.read_excel(
    WORKBOOK_PATH,
    sheet_name="Raw_Credit_Risk_Data",
    header=3
)

print("\n" + "=" * 60)
print("DAY 098 — CREDIT RISK ANALYSIS")
print("=" * 60)

print("\nRaw Data Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())


# ============================================================
# 3. DATA INSPECTION
# ============================================================

print("\n" + "=" * 60)
print("DATA INFORMATION")
print("=" * 60)

print(df.info())

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nBasic Statistics:")
print(df.describe(include="all"))


# ============================================================
# 4. TEXT CLEANING
# ============================================================

text_columns = [
    "Customer_ID",
    "City",
    "Employment_Type",
    "Risk_Category",
    "Loan_Status",
]

for column in text_columns:
    if column in df.columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.title()
        )


# ============================================================
# 5. DATE CLEANING
# ============================================================

df["Loan_Date"] = pd.to_datetime(
    df["Loan_Date"],
    errors="coerce"
)

valid_dates = df["Loan_Date"].dropna()

if not valid_dates.empty:
    median_date = valid_dates.sort_values().iloc[len(valid_dates) // 2]
    df["Loan_Date"] = df["Loan_Date"].fillna(median_date)


# ============================================================
# 6. NUMERIC CONVERSION
# ============================================================

numeric_columns = [
    "Age",
    "Monthly_Income",
    "Credit_Score",
    "Loan_Amount",
    "Interest_Rate_%",
    "Loan_Tenure_Months",
    "Existing_Loans",
    "Debt_to_Income_Ratio_%",
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ============================================================
# 7. CLEAN AGE
# ============================================================

valid_age = df.loc[
    df["Age"].between(18, 100, inclusive="both"),
    "Age"
]

age_median = valid_age.median()

df.loc[
    ~df["Age"].between(18, 100, inclusive="both"),
    "Age"
] = np.nan

df["Age"] = df["Age"].fillna(age_median)


# ============================================================
# 8. CLEAN MONTHLY INCOME
# ============================================================

valid_income = df.loc[
    df["Monthly_Income"] > 0,
    "Monthly_Income"
]

income_median = valid_income.median()

df.loc[
    df["Monthly_Income"] <= 0,
    "Monthly_Income"
] = np.nan

df["Monthly_Income"] = df["Monthly_Income"].fillna(
    income_median
)


# ============================================================
# 9. CLEAN CREDIT SCORE
# ============================================================

valid_scores = df.loc[
    df["Credit_Score"].between(300, 850, inclusive="both"),
    "Credit_Score"
]

score_median = valid_scores.median()

df.loc[
    ~df["Credit_Score"].between(300, 850, inclusive="both"),
    "Credit_Score"
] = np.nan

df["Credit_Score"] = df["Credit_Score"].fillna(
    score_median
)


# ============================================================
# 10. CLEAN LOAN AMOUNT
# ============================================================

valid_loan_amount = df.loc[
    df["Loan_Amount"] >= 0,
    "Loan_Amount"
]

loan_amount_median = valid_loan_amount.median()

df.loc[
    df["Loan_Amount"] < 0,
    "Loan_Amount"
] = np.nan

df["Loan_Amount"] = df["Loan_Amount"].fillna(
    loan_amount_median
)


# ============================================================
# 11. CLEAN INTEREST RATE
# ============================================================

valid_interest = df.loc[
    df["Interest_Rate_%"].gt(0)
    & df["Interest_Rate_%"].le(30),
    "Interest_Rate_%"
]

interest_median = valid_interest.median()

invalid_interest = (
    df["Interest_Rate_%"].isna()
    | df["Interest_Rate_%"].le(0)
    | df["Interest_Rate_%"].gt(30)
)

df.loc[invalid_interest, "Interest_Rate_%"] = np.nan

df["Interest_Rate_%"] = df["Interest_Rate_%"].fillna(
    interest_median
)


# ============================================================
# 12. CLEAN LOAN TENURE
# ============================================================

valid_tenure = df.loc[
    df["Loan_Tenure_Months"] > 0,
    "Loan_Tenure_Months"
]

tenure_median = valid_tenure.median()

df.loc[
    df["Loan_Tenure_Months"] <= 0,
    "Loan_Tenure_Months"
] = np.nan

df["Loan_Tenure_Months"] = df[
    "Loan_Tenure_Months"
].fillna(tenure_median)


# ============================================================
# 13. CLEAN EXISTING LOANS
# ============================================================

df["Existing_Loans"] = df["Existing_Loans"].fillna(0)

df.loc[
    df["Existing_Loans"] < 0,
    "Existing_Loans"
] = 0


# ============================================================
# 14. CLEAN DTI
# ============================================================

valid_dti = df.loc[
    df["Debt_to_Income_Ratio_%"].between(
        0,
        100,
        inclusive="both"
    ),
    "Debt_to_Income_Ratio_%"
]

dti_median = valid_dti.median()

invalid_dti = (
    df["Debt_to_Income_Ratio_%"].isna()
    | df["Debt_to_Income_Ratio_%"].lt(0)
    | df["Debt_to_Income_Ratio_%"].gt(100)
)

df.loc[
    invalid_dti,
    "Debt_to_Income_Ratio_%"
] = np.nan

df["Debt_to_Income_Ratio_%"] = df[
    "Debt_to_Income_Ratio_%"
].fillna(dti_median)


# ============================================================
# 15. RECALCULATE RISK CATEGORY
# ============================================================

def calculate_risk(row):
    credit_score = row["Credit_Score"]
    dti = row["Debt_to_Income_Ratio_%"]

    if credit_score >= 740 and dti < 30:
        return "Low"

    elif credit_score >= 680 and dti < 40:
        return "Medium"

    elif credit_score >= 620 and dti < 50:
        return "High"

    else:
        return "Very High"


df["Risk_Category"] = df.apply(
    calculate_risk,
    axis=1
)


# ============================================================
# 16. CLEAN LOAN STATUS
# ============================================================

valid_statuses = [
    "Approved",
    "Active",
    "Closed",
    "Defaulted",
]

df["Loan_Status"] = df["Loan_Status"].where(
    df["Loan_Status"].isin(valid_statuses),
    "Active"
)


# ============================================================
# 17. REMOVE EXACT DUPLICATES
# ============================================================

before_duplicates = len(df)

df = df.drop_duplicates().reset_index(drop=True)

after_duplicates = len(df)

duplicates_removed = before_duplicates - after_duplicates


# ============================================================
# 18. DATA VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("VALIDATION")
print("=" * 60)

print(
    "Invalid Credit Scores:",
    (~df["Credit_Score"].between(300, 850)).sum()
)

print(
    "Negative Loan Amounts:",
    (df["Loan_Amount"] < 0).sum()
)

print(
    "Invalid Interest Rates:",
    (
        ~df["Interest_Rate_%"].gt(0)
        | ~df["Interest_Rate_%"].le(30)
    ).sum()
)

print(
    "Invalid Loan Tenure:",
    (df["Loan_Tenure_Months"] <= 0).sum()
)

print(
    "Negative Existing Loans:",
    (df["Existing_Loans"] < 0).sum()
)

print(
    "Invalid DTI:",
    (
        ~df["Debt_to_Income_Ratio_%"].between(
            0,
            100,
            inclusive="both"
        )
    ).sum()
)

print(
    "Remaining Duplicate Rows:",
    df.duplicated().sum()
)


# ============================================================
# 19. CREDIT RISK SUMMARY
# ============================================================

total_customers = df["Customer_ID"].nunique()

total_loan_amount = df["Loan_Amount"].sum()

average_credit_score = df["Credit_Score"].mean()

average_income = df["Monthly_Income"].mean()

average_dti = df["Debt_to_Income_Ratio_%"].mean()

high_risk_count = (
    df["Risk_Category"] == "High"
).sum()

very_high_risk_count = (
    df["Risk_Category"] == "Very High"
).sum()

high_very_high_count = (
    high_risk_count + very_high_risk_count
)

active_loan_count = (
    df["Loan_Status"] == "Active"
).sum()

default_count = (
    df["Loan_Status"] == "Defaulted"
).sum()

default_rate = (
    default_count / total_customers * 100
    if total_customers > 0
    else 0
)

risk_summary = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "Total Loan Amount",
        "Average Credit Score",
        "Average Monthly Income",
        "Average DTI %",
        "High Risk Customers",
        "Very High Risk Customers",
        "High / Very High Risk Customers",
        "Active Loans",
        "Defaulted Loans",
        "Default Rate %",
        "Duplicates Removed",
    ],
    "Value": [
        total_customers,
        total_loan_amount,
        average_credit_score,
        average_income,
        average_dti,
        high_risk_count,
        very_high_risk_count,
        high_very_high_count,
        active_loan_count,
        default_count,
        default_rate,
        duplicates_removed,
    ],
})


# ============================================================
# 20. RISK CATEGORY ANALYSIS
# ============================================================

risk_analysis = (
    df.groupby("Risk_Category")
    .agg(
        Customers=("Customer_ID", "nunique"),
        Total_Loan_Amount=("Loan_Amount", "sum"),
        Average_Credit_Score=("Credit_Score", "mean"),
        Average_Income=("Monthly_Income", "mean"),
        Average_DTI=("Debt_to_Income_Ratio_%", "mean"),
        Default_Count=(
            "Loan_Status",
            lambda x: (x == "Defaulted").sum()
        ),
    )
    .reset_index()
)

risk_analysis["Default_Rate_%"] = np.where(
    risk_analysis["Customers"] > 0,
    risk_analysis["Default_Count"]
    / risk_analysis["Customers"]
    * 100,
    0,
)


# ============================================================
# 21. LOAN ANALYSIS
# ============================================================

loan_analysis = (
    df.groupby("Loan_Status")
    .agg(
        Customers=("Customer_ID", "nunique"),
        Total_Loan_Amount=("Loan_Amount", "sum"),
        Average_Loan_Amount=("Loan_Amount", "mean"),
        Average_Interest_Rate=(
            "Interest_Rate_%",
            "mean"
        ),
        Average_Tenure_Months=(
            "Loan_Tenure_Months",
            "mean"
        ),
    )
    .reset_index()
)


# ============================================================
# 22. CUSTOMER ANALYSIS
# ============================================================

customer_analysis = df[
    [
        "Customer_ID",
        "Age",
        "City",
        "Employment_Type",
        "Monthly_Income",
        "Credit_Score",
        "Loan_Amount",
        "Interest_Rate_%",
        "Loan_Tenure_Months",
        "Existing_Loans",
        "Debt_to_Income_Ratio_%",
        "Risk_Category",
        "Loan_Status",
    ]
].copy()


# ============================================================
# 23. MONTHLY CREDIT RISK ANALYSIS
# ============================================================

df["Month"] = df["Loan_Date"].dt.to_period("M").astype(str)

monthly_risk = (
    df.groupby("Month")
    .agg(
        Customers=("Customer_ID", "nunique"),
        Total_Loan_Amount=("Loan_Amount", "sum"),
        Average_Credit_Score=("Credit_Score", "mean"),
        Average_DTI=("Debt_to_Income_Ratio_%", "mean"),
        High_Very_High_Risk_Customers=(
            "Risk_Category",
            lambda x: x.isin(
                ["High", "Very High"]
            ).sum()
        ),
        Default_Count=(
            "Loan_Status",
            lambda x: (x == "Defaulted").sum()
        ),
    )
    .reset_index()
)


# ============================================================
# 24. CREDIT RISK KPI
# ============================================================

credit_risk_kpi = pd.DataFrame({
    "KPI": [
        "Total Customers",
        "Total Loan Exposure",
        "Average Credit Score",
        "Average Monthly Income",
        "Average DTI %",
        "High / Very High Risk Rate %",
        "Default Count",
        "Default Rate %",
        "Active Loan Count",
    ],
    "Value": [
        total_customers,
        total_loan_amount,
        average_credit_score,
        average_income,
        average_dti,
        (
            high_very_high_count
            / total_customers
            * 100
            if total_customers > 0
            else 0
        ),
        default_count,
        default_rate,
        active_loan_count,
    ],
})


# ============================================================
# 25. PIVOT-STYLE RISK ANALYSIS
# ============================================================

pivot_risk = (
    df.groupby("Risk_Category")
    .agg(
        Customers=("Customer_ID", "nunique"),
        Loan_Amount=("Loan_Amount", "sum"),
        Default_Count=(
            "Loan_Status",
            lambda x: (x == "Defaulted").sum()
        ),
    )
    .reset_index()
)


# ============================================================
# 26. PIVOT-STYLE LOAN STATUS ANALYSIS
# ============================================================

pivot_loan_status = (
    df.groupby("Loan_Status")
    .agg(
        Customers=("Customer_ID", "nunique"),
        Loan_Amount=("Loan_Amount", "sum"),
        Average_Credit_Score=(
            "Credit_Score",
            "mean"
        ),
    )
    .reset_index()
)


# ============================================================
# 27. EXPORT CSV FILES
# ============================================================

df.to_csv(
    OUTPUT_DIR / "cleaned_credit_risk_data.csv",
    index=False
)

risk_summary.to_csv(
    OUTPUT_DIR / "credit_risk_summary.csv",
    index=False
)

risk_analysis.to_csv(
    OUTPUT_DIR / "risk_category_analysis.csv",
    index=False
)

loan_analysis.to_csv(
    OUTPUT_DIR / "loan_analysis.csv",
    index=False
)

customer_analysis.to_csv(
    OUTPUT_DIR / "customer_analysis.csv",
    index=False
)

monthly_risk.to_csv(
    OUTPUT_DIR / "monthly_credit_risk.csv",
    index=False
)

credit_risk_kpi.to_csv(
    OUTPUT_DIR / "credit_risk_kpi_summary.csv",
    index=False
)

pivot_risk.to_csv(
    OUTPUT_DIR / "pivot_risk.csv",
    index=False
)

pivot_loan_status.to_csv(
    OUTPUT_DIR / "pivot_loan_status.csv",
    index=False
)


# ============================================================
# 28. CHART 1 — CUSTOMERS BY RISK CATEGORY
# ============================================================

risk_order = [
    "Low",
    "Medium",
    "High",
    "Very High",
]

risk_chart_data = (
    risk_analysis
    .set_index("Risk_Category")
    .reindex(risk_order)
    .reset_index()
)

plt.figure(figsize=(9, 5))

plt.bar(
    risk_chart_data["Risk_Category"],
    risk_chart_data["Customers"]
)

plt.title("Customers by Risk Category")
plt.xlabel("Risk Category")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "risk_distribution.png",
    dpi=300
)

plt.close()


# ============================================================
# 29. CHART 2 — LOAN AMOUNT BY RISK CATEGORY
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    risk_chart_data["Risk_Category"],
    risk_chart_data["Total_Loan_Amount"]
)

plt.title("Loan Amount by Risk Category")
plt.xlabel("Risk Category")
plt.ylabel("Total Loan Amount")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "loan_amount_by_risk.png",
    dpi=300
)

plt.close()


# ============================================================
# 30. CHART 3 — MONTHLY LOAN EXPOSURE TREND
# ============================================================

monthly_chart = monthly_risk.sort_values("Month")

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_chart["Month"],
    monthly_chart["Total_Loan_Amount"],
    marker="o"
)

plt.title("Monthly Loan Exposure Trend")
plt.xlabel("Month")
plt.ylabel("Total Loan Amount")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_risk_trend.png",
    dpi=300
)

plt.close()


# ============================================================
# 31. FINAL OUTPUT
# ============================================================

print("\n" + "=" * 60)
print("CREDIT RISK ANALYSIS COMPLETED")
print("=" * 60)

print("\nCleaned Data Shape:")
print(df.shape)

print("\nTotal Customers:")
print(total_customers)

print("\nTotal Loan Exposure:")
print(round(total_loan_amount, 2))

print("\nAverage Credit Score:")
print(round(average_credit_score, 2))

print("\nAverage Monthly Income:")
print(round(average_income, 2))

print("\nAverage DTI:")
print(round(average_dti, 2))

print("\nHigh / Very High Risk Customers:")
print(high_very_high_count)

print("\nDefault Count:")
print(default_count)

print("\nDefault Rate:")
print(round(default_rate, 2), "%")

print("\nOutputs saved to:")
print(OUTPUT_DIR)

print("\nGenerated Files:")

for file in sorted(OUTPUT_DIR.iterdir()):
    print("-", file.name)

print("\n" + "=" * 60)
print("Day 098 — Credit Risk Analysis Complete")
print("=" * 60)