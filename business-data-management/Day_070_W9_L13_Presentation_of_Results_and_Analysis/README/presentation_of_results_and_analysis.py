from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 070
# Topic: Presentation of Results and Analysis

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_070_W9_L13_Presentation_of_Results_and_Analysis.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="Analysis_Data", header=2)

numeric_cols = [
    "Applications",
    "Days_to_Fill",
    "Recruitment_Cost",
    "Assessment_Score",
    "Selected_Flag",
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Cost_per_Day"] = df["Recruitment_Cost"] / df["Days_to_Fill"]

monthly = df.groupby("Month", as_index=False).agg(
    Candidates=("Record_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Total_Recruitment_Cost=("Recruitment_Cost", "sum"),
    Average_Days_to_Fill=("Days_to_Fill", "mean"),
    Average_Assessment_Score=("Assessment_Score", "mean"),
)

monthly["Selection_Rate_%"] = (
    monthly["Selected"] / monthly["Candidates"] * 100
)

channel = df.groupby("Recruitment_Channel", as_index=False).agg(
    Candidates=("Record_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Applications=("Applications", "sum"),
    Total_Recruitment_Cost=("Recruitment_Cost", "sum"),
    Average_Days_to_Fill=("Days_to_Fill", "mean"),
    Average_Assessment_Score=("Assessment_Score", "mean"),
)

channel["Selection_Rate_%"] = (
    channel["Selected"] / channel["Candidates"] * 100
)

channel["Cost_per_Selected"] = (
    channel["Total_Recruitment_Cost"] / channel["Selected"]
)

department = df.groupby("Department", as_index=False).agg(
    Candidates=("Record_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Total_Recruitment_Cost=("Recruitment_Cost", "sum"),
    Average_Days_to_Fill=("Days_to_Fill", "mean"),
    Average_Assessment_Score=("Assessment_Score", "mean"),
)

department["Selection_Rate_%"] = (
    department["Selected"] / department["Candidates"] * 100
)

region = df.groupby("Region", as_index=False).agg(
    Candidates=("Record_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Total_Recruitment_Cost=("Recruitment_Cost", "sum"),
    Average_Days_to_Fill=("Days_to_Fill", "mean"),
    Average_Assessment_Score=("Assessment_Score", "mean"),
)

region["Selection_Rate_%"] = (
    region["Selected"] / region["Candidates"] * 100
)

df.to_csv(
    OUTPUT_DIR / "presentation_analysis_data.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_results.csv",
    index=False
)

channel.to_csv(
    OUTPUT_DIR / "channel_results.csv",
    index=False
)

department.to_csv(
    OUTPUT_DIR / "department_results.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_results.csv",
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
    channel["Recruitment_Channel"],
    channel["Candidates"],
    "Candidates by Recruitment Channel",
    "Recruitment Channel",
    "Candidates",
    "candidates_by_channel.png",
    "#4472C4",
    25,
)

save_bar(
    department["Department"],
    department["Selection_Rate_%"],
    "Selection Rate by Department",
    "Department",
    "Selection Rate %",
    "selection_rate_by_department.png",
    "#ED7D31",
    25,
)

save_bar(
    region["Region"],
    region["Average_Days_to_Fill"],
    "Average Days to Fill by Region",
    "Region",
    "Average Days",
    "average_days_to_fill_by_region.png",
    "#70AD47",
)

save_bar(
    monthly["Month"],
    monthly["Total_Recruitment_Cost"],
    "Monthly Recruitment Cost",
    "Month",
    "Total Recruitment Cost",
    "monthly_recruitment_cost.png",
    "#8064A2",
)

print("Day 070 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")