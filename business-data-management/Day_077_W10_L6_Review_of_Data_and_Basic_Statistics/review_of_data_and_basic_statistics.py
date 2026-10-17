from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 077
# Topic: Review of Data and Basic Statistics

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_077_W10_L6_Review_of_Data_and_Basic_Statistics.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="PayBuddy_Data",
    header=5
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


def grouped_summary(group_col):
    return df.groupby(
        group_col,
        as_index=False
    ).agg(
        Records=("Player_ID", "count"),
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
    )


player_summary = grouped_summary("Player_Type")
industry_summary = grouped_summary("Industry")
region_summary = grouped_summary("Region")
product_summary = grouped_summary("Primary_Product")
segment_summary = grouped_summary("Customer_Segment")


stats_rows = []

for col in [
    "Active_Customers_Lakh",
    "Transactions_Lakh",
    "Transaction_Value_Crore",
    "Digital_Adoption_%",
    "Satisfaction_Score",
    "Transaction_Value_per_Customer_Lakh",
    "Transactions_per_Customer",
    "Engagement_Index",
]:
    s = df[col].dropna()

    stats_rows.append([
        col,
        len(s),
        s.mean(),
        s.median(),
        s.std(ddof=1),
        s.min(),
        s.max(),
        s.max() - s.min(),
        s.quantile(0.25),
        s.quantile(0.75),
        s.quantile(0.75) - s.quantile(0.25),
        s.sum()
    ])


basic_stats = pd.DataFrame(
    stats_rows,
    columns=[
        "Metric",
        "Count",
        "Mean",
        "Median",
        "Std_Dev",
        "Minimum",
        "Maximum",
        "Range",
        "Q1",
        "Q3",
        "IQR",
        "Sum",
    ]
)


quality = pd.DataFrame({
    "Check": [
        "Total Records",
        "Duplicate Player IDs",
        "Missing Player IDs",
        "Missing Player Names",
        "Missing Numeric Values",
        "Minimum Digital Adoption %",
        "Maximum Digital Adoption %",
        "Minimum Satisfaction Score",
        "Maximum Satisfaction Score",
    ],
    "Value": [
        len(df),
        df["Player_ID"].duplicated().sum(),
        df["Player_ID"].isna().sum(),
        df["Player_Name"].isna().sum(),
        int(
            df[
                [
                    "Active_Customers_Lakh",
                    "Transactions_Lakh",
                    "Transaction_Value_Crore",
                    "Digital_Adoption_%",
                    "Satisfaction_Score",
                ]
            ].isna().sum().sum()
        ),
        df["Digital_Adoption_%"].min(),
        df["Digital_Adoption_%"].max(),
        df["Satisfaction_Score"].min(),
        df["Satisfaction_Score"].max(),
    ],
})


player_frequency = (
    df["Player_Type"]
    .value_counts()
    .rename_axis("Player_Type")
    .reset_index(name="Frequency")
)

industry_frequency = (
    df["Industry"]
    .value_counts()
    .rename_axis("Industry")
    .reset_index(name="Frequency")
)

region_frequency = (
    df["Region"]
    .value_counts()
    .rename_axis("Region")
    .reset_index(name="Frequency")
)

product_frequency = (
    df["Primary_Product"]
    .value_counts()
    .rename_axis("Primary_Product")
    .reset_index(name="Frequency")
)


corr = df[
    [
        "Active_Customers_Lakh",
        "Transactions_Lakh",
        "Transaction_Value_Crore",
        "Digital_Adoption_%",
        "Satisfaction_Score",
        "Transaction_Value_per_Customer_Lakh",
        "Transactions_per_Customer",
        "Engagement_Index",
    ]
].corr()


kpis = pd.DataFrame({
    "KPI": [
        "Total Players",
        "Average Transaction Value (Crore)",
        "Median Transaction Value (Crore)",
        "Average Active Customers (Lakh)",
        "Average Transactions (Lakh)",
        "Average Digital Adoption %",
        "Average Satisfaction Score",
        "Average Engagement Index",
    ],
    "Value": [
        len(df),
        df["Transaction_Value_Crore"].mean(),
        df["Transaction_Value_Crore"].median(),
        df["Active_Customers_Lakh"].mean(),
        df["Transactions_Lakh"].mean(),
        df["Digital_Adoption_%"].mean(),
        df["Satisfaction_Score"].mean(),
        df["Engagement_Index"].mean(),
    ],
})


df.to_csv(
    OUTPUT_DIR / "paybuddy_data_reviewed.csv",
    index=False
)

quality.to_csv(
    OUTPUT_DIR / "data_quality_review.csv",
    index=False
)

basic_stats.to_csv(
    OUTPUT_DIR / "basic_statistics.csv",
    index=False
)

player_summary.to_csv(
    OUTPUT_DIR / "player_type_statistics.csv",
    index=False
)

industry_summary.to_csv(
    OUTPUT_DIR / "industry_statistics.csv",
    index=False
)

region_summary.to_csv(
    OUTPUT_DIR / "region_statistics.csv",
    index=False
)

product_summary.to_csv(
    OUTPUT_DIR / "product_statistics.csv",
    index=False
)

segment_summary.to_csv(
    OUTPUT_DIR / "segment_statistics.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "review_statistics_kpis.csv",
    index=False
)

corr.to_csv(
    OUTPUT_DIR / "correlation_matrix.csv"
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
    player_summary["Player_Type"],
    player_summary["Transaction_Value_Crore"],
    "Transaction Value by Player Type",
    "Player Type",
    "Transaction Value (Crore)",
    "transaction_value_by_player_type.png",
    "#4472C4",
    20,
)


save_bar(
    industry_summary["Industry"],
    industry_summary["Average_Digital_Adoption"],
    "Average Digital Adoption by Industry",
    "Industry",
    "Average Digital Adoption (%)",
    "digital_adoption_by_industry.png",
    "#ED7D31",
    20,
)


save_bar(
    region_summary["Region"],
    region_summary["Active_Customers_Lakh"],
    "Active Customers by Region",
    "Region",
    "Active Customers (Lakh)",
    "active_customers_by_region.png",
    "#70AD47",
)


save_bar(
    player_frequency["Player_Type"],
    player_frequency["Frequency"],
    "Player-Type Record Frequency",
    "Player Type",
    "Records",
    "player_type_frequency.png",
    "#8064A2",
    20,
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


print("Day 077 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")