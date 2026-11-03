from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 066
# Topic: Selection Criteria


# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent

if BASE_DIR.name.lower() == "code":
    BASE_DIR = BASE_DIR.parent


# Find the Excel workbook
INPUT_FILE = BASE_DIR / "Day_066_W9_L9_Selection_Criteria_Updated.xlsx"

if not INPUT_FILE.exists():
    INPUT_FILE = BASE_DIR / "Day_066_W9_L9_Selection_Criteria(1).xlsx"

if not INPUT_FILE.exists():
    INPUT_FILE = BASE_DIR / "Day_066_W9_L9_Selection_Criteria.xlsx"

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        "Keep the Selection Criteria Excel workbook in the main project folder."
    )


# Create a folder for Python outputs
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Read candidate data from Excel
df = pd.read_excel(INPUT_FILE, sheet_name="Selection_Data")


# Convert required columns into numeric values
numeric_cols = [
    "Experience_Years",
    "Technical_Score",
    "Communication_Score",
    "Interview_Score",
    "Overall_Score",
    "Selected_Flag",
    "Criteria_Met",
    "Weighted_Score"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# Correct the selection flags for these two candidates
df.loc[
    df["Candidate_ID"].isin(["C008", "C013"]),
    "Selected_Flag"
] = 1


# Department-wise analysis
department = df.groupby("Department", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Criteria_Met=("Criteria_Met", "sum"),
    Selected=("Selected_Flag", "sum"),
    Average_Weighted_Score=("Weighted_Score", "mean"),
    Average_Overall_Score=("Overall_Score", "mean")
)

department["Criteria_Met_Rate_%"] = (
    department["Criteria_Met"] /
    department["Candidates"] * 100
)


# Role-wise analysis
role = df.groupby("Target_Role", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Criteria_Met=("Criteria_Met", "sum"),
    Selected=("Selected_Flag", "sum"),
    Average_Score=("Overall_Score", "mean")
)

role["Criteria_Met_Rate_%"] = (
    role["Criteria_Met"] /
    role["Candidates"] * 100
)


# Experience-level analysis
level = df.groupby("Experience_Level", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Criteria_Met=("Criteria_Met", "sum"),
    Selected=("Selected_Flag", "sum"),
    Average_Weighted_Score=("Weighted_Score", "mean")
)

level["Criteria_Met_Rate_%"] = (
    level["Criteria_Met"] /
    level["Candidates"] * 100
)


# Region-wise analysis
region = df.groupby("Region", as_index=False).agg(
    Candidates=("Candidate_ID", "count"),
    Criteria_Met=("Criteria_Met", "sum"),
    Selected=("Selected_Flag", "sum"),
    Average_Score=("Overall_Score", "mean")
)

region["Criteria_Met_Rate_%"] = (
    region["Criteria_Met"] /
    region["Candidates"] * 100
)


# Save analysis tables as CSV files
tables = {
    "selection_data_with_criteria.csv": df,
    "department_selection_criteria.csv": department,
    "role_selection_criteria.csv": role,
    "experience_level_selection_criteria.csv": level,
    "region_selection_criteria.csv": region
}

for filename, table in tables.items():
    table.to_csv(OUTPUT_DIR / filename, index=False)


# Prepare charts
charts = [
    (
        department,
        "Department",
        "Candidates",
        "Candidates by Department",
        "candidates_by_department.png",
        "#4472C4"
    ),
    (
        department,
        "Department",
        "Criteria_Met_Rate_%",
        "Criteria Met Rate by Department",
        "criteria_met_rate_by_department.png",
        "#ED7D31"
    ),
    (
        level,
        "Experience_Level",
        "Criteria_Met_Rate_%",
        "Criteria Met Rate by Experience Level",
        "criteria_met_rate_by_experience_level.png",
        "#70AD47"
    ),
    (
        region,
        "Region",
        "Average_Score",
        "Average Score by Region",
        "average_score_by_region.png",
        "#8064A2"
    )
]


# Generate and save charts
for table, x_col, y_col, title, filename, color in charts:

    plt.figure(figsize=(9, 5))

    plt.bar(
        table[x_col].astype(str),
        table[y_col],
        color=color
    )

    plt.title(title)
    plt.xlabel(x_col.replace("_", " "))
    plt.ylabel(y_col.replace("_", " "))

    plt.xticks(
        rotation=30,
        ha="right"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=160
    )

    plt.close()


# Display final results
print("Selection analysis completed.")

print("Input file:", INPUT_FILE)
print("Output folder:", OUTPUT_DIR)

print("Total candidates:", len(df))
print("Criteria met:", int(df["Criteria_Met"].sum()))
print("Selected:", int(df["Selected_Flag"].sum()))

print(
    "Criteria Met Rate:",
    round(df["Criteria_Met"].mean() * 100, 2),
    "%"
)

print(
    "Selection Rate:",
    round(df["Selected_Flag"].mean() * 100, 2),
    "%"
)

print(
    "Average Weighted Score:",
    round(df["Weighted_Score"].mean(), 4)
)