from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 076
# Topic: PayBuddy Case — Main Players and Dataset

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_076_W10_L5_PayBuddy_Case_Main_Players_and_Dataset.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="PayBuddy_Main_Dataset",
    header=2
)

numeric_cols = [
    "Active_Customers_Lakh",
    "Transactions_Lakh",
    "Transaction_Value_Crore",
    "Digital_Adoption_%",
    "Satisfaction_Score"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["Transaction_Value_per_Customer_Lakh"] = (
    df["Transaction_Value_Crore"]
    * 100
    / df["Active_Customers_Lakh"]
)

df["Transactions_per_Customer"] = (
    df["Transactions_Lakh"]
    * 100000
    / (
        df["Active_Customers_Lakh"]
        * 100000
    )
)

df["Engagement_Index"] = (
    df["Digital_Adoption_%"]
    * df["Satisfaction_Score"]
    / 100
)

player = df.groupby(
    "Player_Type",
    as_index=False
).agg(
    Players=("Player_ID", "count"),
    Active_Customers_Lakh=(
        "Active_Customers_Lakh",
        "sum"
    ),
    Transactions_Lakh=(
        "Transactions_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
    Average_Digital_Adoption=(
        "Digital_Adoption_%",
        "mean"
    ),
    Average_Satisfaction=(
        "Satisfaction_Score",
        "mean"
    )
)

industry = df.groupby(
    "Industry",
    as_index=False
).agg(
    Players=("Player_ID", "count"),
    Active_Customers_Lakh=(
        "Active_Customers_Lakh",
        "sum"
    ),
    Transactions_Lakh=(
        "Transactions_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
    Average_Digital_Adoption=(
        "Digital_Adoption_%",
        "mean"
    ),
    Average_Satisfaction=(
        "Satisfaction_Score",
        "mean"
    )
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Players=("Player_ID", "count"),
    Active_Customers_Lakh=(
        "Active_Customers_Lakh",
        "sum"
    ),
    Transactions_Lakh=(
        "Transactions_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
    Average_Digital_Adoption=(
        "Digital_Adoption_%",
        "mean"
    )
)

product = df.groupby(
    "Primary_Product",
    as_index=False
).agg(
    Players=("Player_ID", "count"),
    Active_Customers_Lakh=(
        "Active_Customers_Lakh",
        "sum"
    ),
    Transactions_Lakh=(
        "Transactions_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
    Average_Satisfaction=(
        "Satisfaction_Score",
        "mean"
    )
)

segment = df.groupby(
    "Customer_Segment",
    as_index=False
).agg(
    Players=("Player_ID", "count"),
    Active_Customers_Lakh=(
        "Active_Customers_Lakh",
        "sum"
    ),
    Transactions_Lakh=(
        "Transactions_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
    Average_Digital_Adoption=(
        "Digital_Adoption_%",
        "mean"
    ),
    Average_Satisfaction=(
        "Satisfaction_Score",
        "mean"
    )
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Players",
        "Total Active Customers (Lakh)",
        "Total Transactions (Lakh)",
        "Total Transaction Value (Crore)",
        "Average Digital Adoption %",
        "Average Satisfaction Score"
    ],
    "Value": [
        len(df),
        df["Active_Customers_Lakh"].sum(),
        df["Transactions_Lakh"].sum(),
        df["Transaction_Value_Crore"].sum(),
        df["Digital_Adoption_%"].mean(),
        df["Satisfaction_Score"].mean()
    ]
})

df.to_csv(
    OUTPUT_DIR / "paybuddy_main_dataset.csv",
    index=False
)

player.to_csv(
    OUTPUT_DIR / "player_type_summary.csv",
    index=False
)

industry.to_csv(
    OUTPUT_DIR / "industry_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_summary.csv",
    index=False
)

product.to_csv(
    OUTPUT_DIR / "product_summary.csv",
    index=False
)

segment.to_csv(
    OUTPUT_DIR / "customer_segment_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "paybuddy_case_kpis.csv",
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
    player["Player_Type"],
    player["Players"],
    "Players by Player Type",
    "Player Type",
    "Players",
    "players_by_type.png",
    "#4472C4",
    20
)

save_bar(
    industry["Industry"],
    industry["Transaction_Value_Crore"],
    "Transaction Value by Industry",
    "Industry",
    "Transaction Value (Crore)",
    "transaction_value_by_industry.png",
    "#ED7D31",
    25
)

save_bar(
    region["Region"],
    region["Transaction_Value_Crore"],
    "Transaction Value by Region",
    "Region",
    "Transaction Value (Crore)",
    "transaction_value_by_region.png",
    "#70AD47"
)

save_bar(
    segment["Customer_Segment"],
    segment["Active_Customers_Lakh"],
    "Active Customers by Customer Segment",
    "Customer Segment",
    "Active Customers (Lakh)",
    "active_customers_by_segment.png",
    "#8064A2",
    20
)

print("Day 076 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")