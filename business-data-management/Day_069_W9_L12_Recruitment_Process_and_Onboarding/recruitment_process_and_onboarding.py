from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 069
# Topic: Recruitment Process and Onboarding

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_069_W9_L12_Recruitment_Process_and_Onboarding.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Recruitment_Data",
    header=2
)

numeric_cols = [
    "Applications",
    "Days_to_Fill",
    "Recruitment_Cost",
    "Assessment_Score",
    "Selected_Flag",
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["Cost_per_Day"] = (
    df["Recruitment_Cost"]
    / df["Days_to_Fill"]
)

channel = df.groupby(
    "Recruitment_Channel",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Applications=("Applications", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Recruitment_Cost=("Recruitment_Cost", "mean"),
    Total_Recruitment_Cost=("Recruitment_Cost", "sum"),
    Avg_Assessment_Score=("Assessment_Score", "mean"),
)

channel["Selection_Rate_%"] = (
    channel["Selected"]
    / channel["Candidates"]
    * 100
)

channel["Cost_per_Selected"] = (
    channel["Total_Recruitment_Cost"]
    / channel["Selected"]
)

department = df.groupby(
    "Department",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Recruitment_Cost=("Recruitment_Cost", "mean"),
    Avg_Assessment_Score=("Assessment_Score", "mean"),
)

department["Selection_Rate_%"] = (
    department["Selected"]
    / department["Candidates"]
    * 100
)

monthly = df.groupby(
    "Month",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Total_Recruitment_Cost=("Recruitment_Cost", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Assessment_Score=("Assessment_Score", "mean"),
)

monthly["Selection_Rate_%"] = (
    monthly["Selected"]
    / monthly["Candidates"]
    * 100
)

stage = df.groupby(
    "Stage",
    as_index=False
).agg(
    Records=("Record_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Avg_Days=("Days_to_Fill", "mean"),
)

onboarding = pd.read_excel(
    INPUT_FILE,
    sheet_name="Onboarding_Data",
    header=2
)

onboarding["Task_Days"] = pd.to_numeric(
    onboarding["Task_Days"],
    errors="coerce"
)

onboarding_summary = onboarding.groupby(
    "Onboarding_Task",
    as_index=False
).agg(
    Tasks=("Candidate_ID", "count"),
    Completed=(
        "Task_Status",
        lambda s: (s == "Completed").sum()
    ),
    Avg_Task_Days=("Task_Days", "mean"),
)

onboarding_summary["Completion_Rate_%"] = (
    onboarding_summary["Completed"]
    / onboarding_summary["Tasks"]
    * 100
)

df.to_csv(
    OUTPUT_DIR / "recruitment_process_data.csv",
    index=False
)

channel.to_csv(
    OUTPUT_DIR / "recruitment_channel_summary.csv",
    index=False
)

department.to_csv(
    OUTPUT_DIR / "department_recruitment_summary.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_recruitment_summary.csv",
    index=False
)

stage.to_csv(
    OUTPUT_DIR / "recruitment_stage_summary.csv",
    index=False
)

onboarding.to_csv(
    OUTPUT_DIR / "onboarding_task_data.csv",
    index=False
)

onboarding_summary.to_csv(
    OUTPUT_DIR / "onboarding_task_summary.csv",
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


save_bar(
    channel["Recruitment_Channel"],
    channel["Candidates"],
    "Candidates by Recruitment Channel",
    "Recruitment Channel",
    "Candidates",
    "candidates_by_recruitment_channel.png",
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
    onboarding_summary["Onboarding_Task"],
    onboarding_summary["Completion_Rate_%"],
    "Onboarding Completion Rate by Task",
    "Onboarding Task",
    "Completion Rate %",
    "onboarding_completion_rate_by_task.png",
    "#70AD47",
    30,
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

print("Day 069 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")