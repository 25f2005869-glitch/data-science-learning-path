from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 073
# Topic: Introduction to Payments Industry and Money Flow

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_073_W10_L2_Introduction_to_Payments_Industry_and_Money_Flow.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Payments_Data",
    header=2
)

numeric_cols = [
    "Transaction_Volume_Lakh",
    "Transaction_Value_Crore",
    "Average_Ticket_Value_Rupee",
    "Success_Flag",
    "Failure_Flag"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

channel = df.groupby(
    "Payment_Channel",
    as_index=False
).agg(
    Records=("Transaction_ID", "count"),
    Successful=("Success_Flag", "sum"),
    Failed=("Failure_Flag", "sum"),
    Transaction_Volume_Lakh=(
        "Transaction_Volume_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
    Average_Ticket_Value_Rupee=(
        "Average_Ticket_Value_Rupee",
        "mean"
    )
)

channel["Success_Rate_%"] = (
    channel["Successful"]
    / channel["Records"]
    * 100
)

channel["Failure_Rate_%"] = (
    channel["Failed"]
    / channel["Records"]
    * 100
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Records=("Transaction_ID", "count"),
    Successful=("Success_Flag", "sum"),
    Transaction_Volume_Lakh=(
        "Transaction_Volume_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    )
)

region["Success_Rate_%"] = (
    region["Successful"]
    / region["Records"]
    * 100
)

service = df.groupby(
    "Payment_Service",
    as_index=False
).agg(
    Records=("Transaction_ID", "count"),
    Transaction_Volume_Lakh=(
        "Transaction_Volume_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    ),
    Average_Ticket_Value_Rupee=(
        "Average_Ticket_Value_Rupee",
        "mean"
    )
)

status = df.groupby(
    "Transaction_Status",
    as_index=False
).agg(
    Records=("Transaction_ID", "count"),
    Transaction_Volume_Lakh=(
        "Transaction_Volume_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    )
)

money_flow = df.groupby(
    ["Region", "Payment_Channel"],
    as_index=False
).agg(
    Transaction_Volume_Lakh=(
        "Transaction_Volume_Lakh",
        "sum"
    ),
    Transaction_Value_Crore=(
        "Transaction_Value_Crore",
        "sum"
    )
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Payment Records",
        "Successful Records",
        "Failed Records",
        "Overall Success Rate %",
        "Total Transaction Volume (Lakh)",
        "Total Transaction Value (Crore)",
        "Average Ticket Value (Rupee)"
    ],
    "Value": [
        len(df),
        int(df["Success_Flag"].sum()),
        int(df["Failure_Flag"].sum()),
        df["Success_Flag"].mean() * 100,
        df["Transaction_Volume_Lakh"].sum(),
        df["Transaction_Value_Crore"].sum(),
        df["Average_Ticket_Value_Rupee"].mean()
    ]
})

df.to_csv(
    OUTPUT_DIR / "payments_data.csv",
    index=False
)

channel.to_csv(
    OUTPUT_DIR / "payment_channel_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_payment_summary.csv",
    index=False
)

service.to_csv(
    OUTPUT_DIR / "payment_service_summary.csv",
    index=False
)

status.to_csv(
    OUTPUT_DIR / "transaction_status_summary.csv",
    index=False
)

money_flow.to_csv(
    OUTPUT_DIR / "money_flow_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "payment_kpis.csv",
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
    channel["Payment_Channel"],
    channel["Transaction_Value_Crore"],
    "Transaction Value by Payment Channel",
    "Payment Channel",
    "Transaction Value (Crore)",
    "transaction_value_by_channel.png",
    "#4472C4",
    25
)

save_bar(
    channel["Payment_Channel"],
    channel["Success_Rate_%"],
    "Payment Channel Success Rate",
    "Payment Channel",
    "Success Rate %",
    "payment_success_rate.png",
    "#ED7D31",
    25
)

save_bar(
    region["Region"],
    region["Transaction_Volume_Lakh"],
    "Transaction Volume by Region",
    "Region",
    "Transaction Volume (Lakh)",
    "transaction_volume_by_region.png",
    "#70AD47"
)

save_bar(
    service["Payment_Service"],
    service["Transaction_Value_Crore"],
    "Transaction Value by Payment Service",
    "Payment Service",
    "Transaction Value (Crore)",
    "transaction_value_by_service.png",
    "#8064A2",
    25
)

print("Day 073 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")