from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 067
# Topic: Channel Effectiveness


# The script works whether it is saved in the project folder or in a code folder.
SCRIPT_FOLDER = Path(__file__).resolve().parent
PROJECT_FOLDER = SCRIPT_FOLDER.parent if SCRIPT_FOLDER.name.lower() == "code" else SCRIPT_FOLDER

# Use the corrected workbook if it is available.
possible_files = [
    PROJECT_FOLDER / "Day_067_W9_L10_Channel_Effectiveness_Corrected.xlsx",
    PROJECT_FOLDER / "Day_067_W9_L10_Channel_Effectiveness(1).xlsx",
    PROJECT_FOLDER / "Day_067_W9_L10_Channel_Effectiveness.xlsx",
]

INPUT_FILE = next((file for file in possible_files if file.exists()), None)

if INPUT_FILE is None:
    raise FileNotFoundError(
        "The Day 067 Excel workbook was not found in the project folder."
    )

OUTPUT_FOLDER = PROJECT_FOLDER / "python_outputs"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# Read the original candidate records.
df = pd.read_excel(INPUT_FILE, sheet_name="Sourcing_Data")

number_columns = [
    "Application_Count",
    "Days_to_Fill",
    "Sourcing_Cost",
    "Satisfaction_Score",
    "Selected_Flag",
]

for column in number_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Avoid division by zero when calculating cost per day.
df["Cost_per_Day"] = (
    df["Sourcing_Cost"] / df["Days_to_Fill"].replace(0, pd.NA)
).fillna(0)


# Prepare the channel-wise figures.
channel = df.groupby("Sourcing_Channel", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Applications=("Application_Count", "sum"),
    Selected=("Selected_Flag", "sum"),
    Selection_Rate=("Selected_Flag", "mean"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean"),
    Total_Sourcing_Cost=("Sourcing_Cost", "sum"),
    Avg_Satisfaction=("Satisfaction_Score", "mean"),
)

channel["Selection_Rate_%"] = channel["Selection_Rate"] * 100

# A channel with no selected candidates gets 0 instead of infinity.
channel["Cost_per_Selected"] = (
    channel["Total_Sourcing_Cost"]
    / channel["Selected"].replace(0, pd.NA)
).fillna(0)


# Prepare the department-wise figures.
department = df.groupby("Department", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Applications=("Application_Count", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean"),
)

department["Selection_Rate_%"] = (
    department["Selected"] / department["Candidates"] * 100
)


# Prepare the region-wise figures.
region = df.groupby("Region", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Applications=("Application_Count", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean"),
)

region["Selection_Rate_%"] = (
    region["Selected"] / region["Candidates"] * 100
)


# Prepare the month-wise figures.
monthly = df.groupby("Month", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Applications=("Application_Count", "sum"),
    Total_Sourcing_Cost=("Sourcing_Cost", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean"),
)

monthly["Selection_Rate_%"] = (
    monthly["Selected"] / monthly["Candidates"] * 100
)


# Prepare the role-wise figures.
role = df.groupby("Target_Role", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Selected=("Selected_Flag", "sum"),
    Avg_Days_to_Fill=("Days_to_Fill", "mean"),
    Avg_Sourcing_Cost=("Sourcing_Cost", "mean"),
)

role["Selection_Rate_%"] = (
    role["Selected"] / role["Candidates"] * 100
)


# Save the tables so they can be checked later.
tables = {
    "channel_effectiveness_data.csv": df,
    "channel_effectiveness_summary.csv": channel,
    "department_channel_summary.csv": department,
    "region_channel_summary.csv": region,
    "monthly_channel_summary.csv": monthly,
    "role_channel_summary.csv": role,
}

for file_name, table in tables.items():
    table.to_csv(OUTPUT_FOLDER / file_name, index=False)


# Make one bar chart and save it in the output folder.
def save_bar(x_values, y_values, title, x_label, y_label, file_name, bar_color):
    plt.figure(figsize=(10, 5))
    plt.bar(x_values, y_values, color=bar_color)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Right alignment keeps longer channel names easier to read.
    plt.xticks(rotation=30, ha="right")

    plt.tight_layout()
    plt.savefig(OUTPUT_FOLDER / file_name, dpi=160)
    plt.close()


save_bar(
    channel["Sourcing_Channel"],
    channel["Candidates"],
    "Candidates by Sourcing Channel",
    "Sourcing Channel",
    "Candidates",
    "candidates_by_channel.png",
    "#4472C4",
)

save_bar(
    channel["Sourcing_Channel"],
    channel["Selection_Rate_%"],
    "Selection Rate by Sourcing Channel",
    "Sourcing Channel",
    "Selection Rate %",
    "selection_rate_by_channel.png",
    "#ED7D31",
)

save_bar(
    channel["Sourcing_Channel"],
    channel["Avg_Sourcing_Cost"],
    "Average Sourcing Cost by Channel",
    "Sourcing Channel",
    "Average Sourcing Cost",
    "average_sourcing_cost_by_channel.png",
    "#70AD47",
)

save_bar(
    channel["Sourcing_Channel"],
    channel["Avg_Days_to_Fill"],
    "Average Days to Fill by Channel",
    "Sourcing Channel",
    "Average Days",
    "average_days_to_fill_by_channel.png",
    "#8064A2",
)


# Print a short summary after the analysis is complete.
print("Day 067 analysis complete.")
print("Total candidates:", df["Candidate_ID"].nunique())
print("Total applications:", int(df["Application_Count"].sum()))
print("Total selected:", int(df["Selected_Flag"].sum()))
print("Cost per selected candidate:")
print(channel[["Sourcing_Channel", "Cost_per_Selected"]].to_string(index=False))
print("Files saved in:", OUTPUT_FOLDER)
