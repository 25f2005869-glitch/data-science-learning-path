from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 067
# Topic: Channel Effectiveness

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_067_W9_L10_Channel_Effectiveness.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="Sourcing_Data")

numeric_cols = [
    "Application_Count",
    "Days_to_Fill",
    "Sourcing_Cost",
    "Satisfaction_Score",
    "Selected_Flag"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Cost_per_Day"] = (
    df["Sourcing_Cost"] / df["Days_to_Fill"]
)

channel = df.groupby(
    "Sourcing_Channel",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Applications=("Application_Count", "sum"),
    Selected=("Selected_Flag", "sum"),
    Selection_Rate=("Selected_Flag", "mean"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean"),
    Total_Sourcing_Cost=("Sourcing_Cost", "sum"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
)

channel["Selection_Rate_%"] = (
    channel["Selection_Rate"] * 100
)

channel["Cost_per_Selected"] = (
    channel["Total_Sourcing_Cost"]
    / channel["Selected"]
)

department = df.groupby(
    "Department",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Applications=("Application_Count", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
)

department["Selection_Rate_%"] = (
    department["Selected"]
    / department["Candidates"]
    * 100
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Applications=("Application_Count", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean")
)

region["Selection_Rate_%"] = (
    region["Selected"]
    / region["Candidates"]
    * 100
)

monthly = df.groupby(
    "Month",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Applications=("Application_Count", "sum"),
    Total_Sourcing_Cost=("Sourcing_Cost", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
)

monthly["Selection_Rate_%"] = (
    monthly["Selected"]
    / monthly["Candidates"]
    * 100
)

role = df.groupby(
    "Target_Role",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean")
)

role["Selection_Rate_%"] = (
    role["Selected"]
    / role["Candidates"]
    * 100
)

df.to_csv(
    OUTPUT_DIR / "channel_effectiveness_data.csv",
    index=False
)

channel.to_csv(
    OUTPUT_DIR / "channel_effectiveness_summary.csv",
    index=False
)

department.to_csv(
    OUTPUT_DIR / "department_channel_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_channel_summary.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_channel_summary.csv",
    index=False
)

role.to_csv(
    OUTPUT_DIR / "role_channel_summary.csv",
    index=False
)


def save_bar(
    x,
    y,
    title,
    xlabel,
    ylabel,
    filename,
    color
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

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=160
    )

    plt.close()


save_bar(
    channel["Sourcing_Channel"],
    channel["Candidates"],
    "Candidates by Sourcing Channel",
    "Sourcing Channel",
    "Candidates",
    "candidates_by_channel.png",
    "#4472C4"
)

save_bar(
    channel["Sourcing_Channel"],
    channel["Selection_Rate_%"],
    "Selection Rate by Sourcing Channel",
    "Sourcing Channel",
    "Selection Rate %",
    "selection_rate_by_channel.png",
    "#ED7D31"
)

save_bar(
    channel["Sourcing_Channel"],
    channel["Avg_Sourcing_Cost"],
    "Average Sourcing Cost by Channel",
    "Sourcing Channel",
    "Average Sourcing Cost",
    "average_sourcing_cost_by_channel.png",
    "#70AD47"
)

save_bar(
    channel["Sourcing_Channel"],
    channel["Avg_Days_to_Fill"],
    "Average Days to Fill by Channel",
    "Sourcing Channel",
    "Average Days",
    "average_days_to_fill_by_channel.png",
    "#8064A2"
)

print("Day 067 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")