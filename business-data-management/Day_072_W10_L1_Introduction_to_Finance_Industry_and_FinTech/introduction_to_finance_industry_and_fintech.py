from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 072
# Topic: Introduction to Finance Industry and FinTech

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_072_W10_L1_Introduction_to_Finance_Industry_and_FinTech.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Finance_FinTech_Data",
    header=2
)

numeric_cols = [
    "Employees",
    "Annual_Revenue_Crore",
    "Active_Customers",
    "Digital_Transactions_Lakh",
    "Transaction_Value_Crore",
    "Digital_Adoption_%"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["Revenue_per_Employee_Lakh"] = (
    df["Annual_Revenue_Crore"]
    * 100
    / df["Employees"]
)

df["Transactions_per_Customer"] = (
    df["Digital_Transactions_Lakh"]
    * 100000
    / df["Active_Customers"]
)

industry = df.groupby(
    "Institution_Type",
    as_index=False
).agg(
    Entities=("Entity_ID", "count"),
    Employees=("Employees", "sum"),
    Annual_Revenue_Crore=(
        "Annual_Revenue_Crore",
        "sum"
    ),
    Active_Customers=(
        "Active_Customers",
        "sum"
    ),
    Digital_Transactions_Lakh=(
        "Digital_Transactions_Lakh",
        "sum"
    )
)

fintech = df.groupby(
    "FinTech_Category",
    as_index=False
).agg(
    Entities=("Entity_ID", "count"),
    Annual_Revenue_Crore=(
        "Annual_Revenue_Crore",
        "sum"
    ),
    Active_Customers=(
        "Active_Customers",
        "sum"
    ),
    Digital_Transactions_Lakh=(
        "Digital_Transactions_Lakh",
        "sum"
    ),
    Average_Digital_Adoption=(
        "Digital_Adoption_%",
        "mean"
    )
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Entities=("Entity_ID", "count"),
    Employees=("Employees", "sum"),
    Annual_Revenue_Crore=(
        "Annual_Revenue_Crore",
        "sum"
    ),
    Active_Customers=(
        "Active_Customers",
        "sum"
    ),
    Average_Digital_Adoption=(
        "Digital_Adoption_%",
        "mean"
    )
)

service = df.groupby(
    "Primary_Service",
    as_index=False
).agg(
    Entities=("Entity_ID", "count"),
    Annual_Revenue_Crore=(
        "Annual_Revenue_Crore",
        "sum"
    ),
    Active_Customers=(
        "Active_Customers",
        "sum"
    ),
    Digital_Transactions_Lakh=(
        "Digital_Transactions_Lakh",
        "sum"
    )
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Entities",
        "Total Employees",
        "Total Annual Revenue (Crore)",
        "Total Active Customers",
        "Total Digital Transactions (Lakh)",
        "Average Digital Adoption %",
        "Average Revenue per Employee (Lakh)"
    ],
    "Value": [
        len(df),
        df["Employees"].sum(),
        df["Annual_Revenue_Crore"].sum(),
        df["Active_Customers"].sum(),
        df["Digital_Transactions_Lakh"].sum(),
        df["Digital_Adoption_%"].mean(),
        df["Revenue_per_Employee_Lakh"].mean()
    ]
})

df.to_csv(
    OUTPUT_DIR / "finance_fintech_data.csv",
    index=False
)

industry.to_csv(
    OUTPUT_DIR / "industry_summary.csv",
    index=False
)

fintech.to_csv(
    OUTPUT_DIR / "fintech_category_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_summary.csv",
    index=False
)

service.to_csv(
    OUTPUT_DIR / "service_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "finance_fintech_kpis.csv",
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
    industry["Institution_Type"],
    industry["Annual_Revenue_Crore"],
    "Annual Revenue by Institution Type",
    "Institution Type",
    "Revenue (Crore)",
    "revenue_by_institution_type.png",
    "#4472C4",
    25
)

save_bar(
    fintech["FinTech_Category"],
    fintech["Average_Digital_Adoption"],
    "Digital Adoption by FinTech Category",
    "FinTech Category",
    "Average Digital Adoption %",
    "digital_adoption_by_fintech_category.png",
    "#ED7D31",
    25
)

save_bar(
    region["Region"],
    region["Active_Customers"],
    "Active Customers by Region",
    "Region",
    "Active Customers",
    "active_customers_by_region.png",
    "#70AD47"
)

save_bar(
    service["Primary_Service"],
    service["Digital_Transactions_Lakh"],
    "Digital Transactions by Financial Service",
    "Financial Service",
    "Digital Transactions (Lakh)",
    "digital_transactions_by_service.png",
    "#8064A2",
    25
)

print("Day 072 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")