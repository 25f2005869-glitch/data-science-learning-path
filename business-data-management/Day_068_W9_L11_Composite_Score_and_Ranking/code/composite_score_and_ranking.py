from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 068
# Topic: Composite Score and Ranking


# Find the project folder.
SCRIPT_FOLDER = Path(__file__).resolve().parent

if SCRIPT_FOLDER.name.lower() == "code":
    PROJECT_FOLDER = SCRIPT_FOLDER.parent
else:
    PROJECT_FOLDER = SCRIPT_FOLDER


# Find the Excel workbook.
possible_files = [
    PROJECT_FOLDER / "Day_068_W9_L11_Composite_Score_and_Ranking_Corrected.xlsx",
    PROJECT_FOLDER / "Day_068_W9_L11_Composite_Score_and_Ranking(1).xlsx",
    PROJECT_FOLDER / "Day_068_W9_L11_Composite_Score_and_Ranking.xlsx",
]

INPUT_FILE = None

for file in possible_files:
    if file.exists():
        INPUT_FILE = file
        break

if INPUT_FILE is None:
    raise FileNotFoundError(
        "Day 068 Excel workbook was not found in the project folder."
    )


# Create the folder for the output files.
OUTPUT_FOLDER = PROJECT_FOLDER / "python_outputs"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# Read candidate details.
df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Candidate_Data"
)


# Convert score columns to numbers.
numeric_cols = [
    "Experience_Years",
    "Technical_Score",
    "Communication_Score",
    "Interview_Score",
    "Overall_Score",
    "Selected_Flag",
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# Calculate the composite score using the given weights.
df["Composite_Score"] = (
    df["Technical_Score"] * 0.30
    + df["Communication_Score"] * 0.20
    + df["Interview_Score"] * 0.30
    + df["Overall_Score"] * 0.20
)


# Give the highest composite score rank 1.
df["Composite_Rank"] = (
    df["Composite_Score"]
    .rank(method="min", ascending=False)
    .astype(int)
)


# Calculate percentile so the highest score receives 100%.
df["Composite_Percentile"] = (
    df["Composite_Score"].rank(ascending=True, pct=True) * 100
)


# Summarise results by department.
department = df.groupby(
    "Department",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Average_Composite_Score=("Composite_Score", "mean"),
    Highest_Composite_Score=("Composite_Score", "max"),
    Selected=("Selected_Flag", "sum"),
)

department["Selection_Rate_%"] = (
    department["Selected"] / department["Candidates"] * 100
)


# Summarise results by experience level.
level = df.groupby(
    "Experience_Level",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Average_Composite_Score=("Composite_Score", "mean"),
    Highest_Composite_Score=("Composite_Score", "max"),
    Selected=("Selected_Flag", "sum"),
)

level["Selection_Rate_%"] = (
    level["Selected"] / level["Candidates"] * 100
)


# Summarise results by region.
region = df.groupby(
    "Region",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Average_Composite_Score=("Composite_Score", "mean"),
    Highest_Composite_Score=("Composite_Score", "max"),
    Selected=("Selected_Flag", "sum"),
)

region["Selection_Rate_%"] = (
    region["Selected"] / region["Candidates"] * 100
)


# Summarise results by target role.
role = df.groupby(
    "Target_Role",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Average_Composite_Score=("Composite_Score", "mean"),
    Highest_Composite_Score=("Composite_Score", "max"),
    Selected=("Selected_Flag", "sum"),
)

role["Selection_Rate_%"] = (
    role["Selected"] / role["Candidates"] * 100
)


# Keep the ten highest-scoring candidates.
top10 = (
    df.sort_values(
        ["Composite_Score", "Candidate_ID"],
        ascending=[False, True]
    )
    .head(10)
)


# Save the tables as CSV files.
tables = {
    "candidate_composite_scores.csv": df,
    "department_composite_summary.csv": department,
    "experience_level_composite_summary.csv": level,
    "region_composite_summary.csv": region,
    "role_composite_summary.csv": role,
    "top_10_composite_ranking.csv": top10,
}

for file_name, table in tables.items():
    table.to_csv(OUTPUT_FOLDER / file_name, index=False)


# Create a chart and save it in the output folder.
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

    plt.bar(x, y, color=color)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=rotation, ha="right")

    plt.tight_layout()
    plt.savefig(OUTPUT_FOLDER / filename, dpi=160)
    plt.close()


# Department chart.
save_bar(
    department["Department"],
    department["Average_Composite_Score"],
    "Average Composite Score by Department",
    "Department",
    "Composite Score",
    "average_composite_score_by_department.png",
    "#4472C4",
    rotation=25,
)


# Experience-level chart.
save_bar(
    level["Experience_Level"],
    level["Average_Composite_Score"],
    "Average Composite Score by Experience Level",
    "Experience Level",
    "Composite Score",
    "average_composite_score_by_experience_level.png",
    "#ED7D31",
    rotation=25,
)


# Region chart.
save_bar(
    region["Region"],
    region["Average_Composite_Score"],
    "Average Composite Score by Region",
    "Region",
    "Composite Score",
    "average_composite_score_by_region.png",
    "#70AD47",
    rotation=25,
)


# Top ten candidates chart.
save_bar(
    top10["Candidate_ID"],
    top10["Composite_Score"],
    "Top 10 Composite Score Ranking",
    "Candidate",
    "Composite Score",
    "top_10_composite_ranking.png",
    "#8064A2",
    rotation=30,
)


# Show a short summary.
print("Day 068 analysis complete.")
print("Total candidates:", df["Candidate_ID"].nunique())
print("Highest composite score:", df["Composite_Score"].max())
print("Lowest composite score:", df["Composite_Score"].min())
print("Highest percentile:", df["Composite_Percentile"].max())
print("Output folder:", OUTPUT_FOLDER)
