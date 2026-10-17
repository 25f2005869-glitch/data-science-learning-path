from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 078
# Topic: Segment Analysis

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_078_W10_L7_Segment_Analysis.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Segment_Data",
    header=6
)

numeric_cols = [
    "Active_Customers_Lakh",
    "Transactions_Lakh",
    "Transaction_Value_Crore",
    "Digital_Adoption_%",
    "Satisfaction_Score",
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
    / df["Active_Customers_Lakh"]
)

df["Engagement_Index"] = (
    df["Digital_Adoption_%"]
    * df["Satisfaction_Score"]
    / 100
)

df["Customer_Value_Index"] = (
    df["Transaction_Value_per_Customer_Lakh"]
    * df["Satisfaction_Score"]
)

df["Segment_Activity_Level"] = pd.cut(
    df["Transactions_per_Customer"],
    bins=[
        -float("inf"),
        1.5,
        2.5,
        float("inf")
    ],
    labels=[
        "Low Activity",
        "Medium Activity",
        "High Activity"
    ]
)

segment_summary = df.groupby(
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
    ),
    Average_Engagement_Index=(
        "Engagement_Index",
        "mean"
    ),
    Average_Transactions_per_Customer=(
        "Transactions_per_Customer",
        "mean"
    ),
    Average_Customer_Value_Index=(
        "Customer_Value_Index",
        "mean"
    ),
)

segment_summary["Customer_Share_%"] = (
    segment_summary["Active_Customers_Lakh"]
    / segment_summary["Active_Customers_Lakh"].sum()
    * 100
)

segment_summary["Transaction_Value_Share_%"] = (
    segment_summary["Transaction_Value_Crore"]
    / segment_summary["Transaction_Value_Crore"].sum()
    * 100
)

player_segment = pd.pivot_table(
    df,
    index="Player_Type",
    columns="Customer_Segment",
    values="Player_ID",
    aggfunc="count",
    fill_value=0
).reset_index()

region_segment = df.groupby(
    [
        "Region",
        "Customer_Segment"
    ],
    as_index=False
).agg(
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
)

industry_segment = df.groupby(
    [
        "Industry",
        "Customer_Segment"
    ],
    as_index=False
).agg(
    Players=("Player_ID", "count"),
    Active_Customers_Lakh=(
        "Active_Customers_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
)

product_segment = df.groupby(
    [
        "Primary_Product",
        "Customer_Segment"
    ],
    as_index=False
).agg(
    Players=("Player_ID", "count"),
    Active_Customers_Lakh=(
        "Active_Customers_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
)

activity_summary = df.groupby(
    "Segment_Activity_Level",
    as_index=False,
    observed=False
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
    ),
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Customer Segments",
        "Total Player Records",
        "Total Active Customers (Lakh)",
        "Total Transactions (Lakh)",
        "Total Transaction Value (Crore)",
        "Average Digital Adoption %",
        "Average Satisfaction Score",
        "Average Engagement Index",
    ],
    "Value": [
        df["Customer_Segment"].nunique(),
        len(df),
        df["Active_Customers_Lakh"].sum(),
        df["Transactions_Lakh"].sum(),
        df["Transaction_Value_Crore"].sum(),
        df["Digital_Adoption_%"].mean(),
        df["Satisfaction_Score"].mean(),
        df["Engagement_Index"].mean(),
    ],
})

df.to_csv(
    OUTPUT_DIR / "segment_data.csv",
    index=False
)

segment_summary.to_csv(
    OUTPUT_DIR / "segment_summary.csv",
    index=False
)

player_segment.to_csv(
    OUTPUT_DIR / "player_segment_analysis.csv",
    index=False
)

region_segment.to_csv(
    OUTPUT_DIR / "region_segment_analysis.csv",
    index=False
)

industry_segment.to_csv(
    OUTPUT_DIR / "industry_segment_analysis.csv",
    index=False
)

product_segment.to_csv(
    OUTPUT_DIR / "product_segment_analysis.csv",
    index=False
)

activity_summary.to_csv(
    OUTPUT_DIR / "segment_activity_analysis.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "segment_kpis.csv",
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
    segment_summary["Customer_Segment"],
    segment_summary["Active_Customers_Lakh"],
    "Active Customers by Customer Segment",
    "Customer Segment",
    "Active Customers (Lakh)",
    "active_customers_by_segment.png",
    "#4472C4",
    15,
)

save_bar(
    segment_summary["Customer_Segment"],
    segment_summary["Transaction_Value_Crore"],
    "Transaction Value by Customer Segment",
    "Customer Segment",
    "Transaction Value (Crore)",
    "transaction_value_by_segment.png",
    "#ED7D31",
    15,
)

save_bar(
    segment_summary["Customer_Segment"],
    segment_summary["Average_Digital_Adoption"],
    "Digital Adoption by Customer Segment",
    "Customer Segment",
    "Average Digital Adoption (%)",
    "digital_adoption_by_segment.png",
    "#70AD47",
    15,
)

save_bar(
    segment_summary["Customer_Segment"],
    segment_summary["Average_Satisfaction"],
    "Satisfaction by Customer Segment",
    "Customer Segment",
    "Average Satisfaction Score",
    "satisfaction_by_segment.png",
    "#8064A2",
    15,
)

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Active_Customers_Lakh"],
    df["Transaction_Value_Crore"],
    color="#5B9BD5"
)

plt.title(
    "Transaction Value vs Active Customers"
)

plt.xlabel(
    "Active Customers (Lakh)"
)

plt.ylabel(
    "Transaction Value (Crore)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "transaction_value_vs_active_customers.png",
    dpi=160
)

plt.close()

print("Day 078 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")