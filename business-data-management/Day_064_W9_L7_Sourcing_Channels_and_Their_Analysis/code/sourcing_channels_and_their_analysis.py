from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 064
# Topic: Sourcing Channels and Their Analysis

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_064_W9_L7_Sourcing_Channels_and_Their_Analysis.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="Sourcing_Data", header=2)

numeric_cols = [
    "Application_Count",
    "Days_to_Fill",
    "Sourcing_Cost",
    "Satisfaction_Score",
    "Selected_Flag"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Cost_per_Day"] = df["Sourcing_Cost"] / df["Days_to_Fill"]

channel = df.groupby("Sourcing_Channel", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Selection_Rate=("Selected_Flag", "mean"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean"),
    Total_Sourcing_Cost=("Sourcing_Cost", "sum"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
)

channel["Selection_Rate_Pct"] = channel["Selection_Rate"] * 100

channel["Cost_per_Selected"] = (
    channel["Total_Sourcing_Cost"] / channel["Selected"]
)

department = df.groupby("Department", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
)

region = df.groupby("Region", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean")
)

monthly = df.groupby("Month", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Total_Sourcing_Cost=("Sourcing_Cost", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
)

role = df.groupby("Target_Role", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean")
)

channel.to_csv(
    OUTPUT_DIR / "sourcing_channel_summary.csv",
    index=False
)

department.to_csv(
    OUTPUT_DIR / "department_sourcing_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_sourcing_summary.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_sourcing_summary.csv",
    index=False
)

role.to_csv(
    OUTPUT_DIR / "role_sourcing_summary.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    channel["Sourcing_Channel"],
    channel["Candidates"],
    color="#4472C4"
)

plt.title("Candidates by Sourcing Channel")
plt.xlabel("Sourcing Channel")
plt.ylabel("Candidates")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "candidates_by_sourcing_channel.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    channel["Sourcing_Channel"],
    channel["Selection_Rate_Pct"],
    color="#ED7D31"
)

plt.title("Selection Rate by Sourcing Channel")
plt.xlabel("Sourcing Channel")
plt.ylabel("Selection Rate %")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "selection_rate_by_channel.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    channel["Sourcing_Channel"],
    channel["Avg_Sourcing_Cost"],
    color="#70AD47"
)

plt.title("Average Sourcing Cost by Channel")
plt.xlabel("Sourcing Channel")
plt.ylabel("Average Sourcing Cost")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_sourcing_cost_by_channel.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    channel["Sourcing_Channel"],
    channel["Avg_Days_to_Fill"],
    color="#8064A2"
)

plt.title("Average Days to Fill by Channel")
plt.xlabel("Sourcing Channel")
plt.ylabel("Average Days")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_days_to_fill_by_channel.png",
    dpi=160
)

plt.close()

print("Day 064 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")