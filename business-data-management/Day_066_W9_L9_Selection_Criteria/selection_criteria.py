from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 066
# Topic: Selection Criteria

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_066_W9_L9_Selection_Criteria.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Selection_Data"
)

numeric_cols = [
    "Experience_Years",
    "Technical_Score",
    "Communication_Score",
    "Interview_Score",
    "Overall_Score",
    "Selected_Flag"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["Technical_Eligible"] = (
    df["Technical_Score"] >= 70
).astype(int)

df["Communication_Eligible"] = (
    df["Communication_Score"] >= 75
).astype(int)

df["Interview_Eligible"] = (
    df["Interview_Score"] >= 80
).astype(int)

df["Overall_Eligible"] = (
    df["Overall_Score"] >= 75
).astype(int)

df["Experience_Eligible"] = (
    df["Experience_Years"] >= 1
).astype(int)

df["Criteria_Pass_Count"] = df[
    [
        "Technical_Eligible",
        "Communication_Eligible",
        "Interview_Eligible",
        "Overall_Eligible",
        "Experience_Eligible"
    ]
].sum(axis=1)

df["Weighted_Score"] = (
    df["Technical_Score"] * 0.30
    + df["Communication_Score"] * 0.20
    + df["Interview_Score"] * 0.30
    + df["Overall_Score"] * 0.20
)

df["Criteria_Met"] = (
    df["Criteria_Pass_Count"] >= 4
).astype(int)

department = df.groupby(
    "Department",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Criteria_Met=("Criteria_Met", "sum"),
    Selected=("Selected_Flag", "sum"),
    Average_Weighted_Score=("Weighted_Score", "mean"),
    Average_Overall_Score=("Overall_Score", "mean")
)

department["Criteria_Met_Rate_%"] = (
    department["Criteria_Met"]
    / department["Candidates"]
    * 100
)

role = df.groupby(
    "Target_Role",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Criteria_Met=("Criteria_Met", "sum"),
    Selected=("Selected_Flag", "sum"),
    Average_Score=("Overall_Score", "mean")
)

role["Criteria_Met_Rate_%"] = (
    role["Criteria_Met"]
    / role["Candidates"]
    * 100
)

level = df.groupby(
    "Experience_Level",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Criteria_Met=("Criteria_Met", "sum"),
    Selected=("Selected_Flag", "sum"),
    Average_Weighted_Score=("Weighted_Score", "mean")
)

level["Criteria_Met_Rate_%"] = (
    level["Criteria_Met"]
    / level["Candidates"]
    * 100
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Criteria_Met=("Criteria_Met", "sum"),
    Selected=("Selected_Flag", "sum"),
    Average_Score=("Overall_Score", "mean")
)

region["Criteria_Met_Rate_%"] = (
    region["Criteria_Met"]
    / region["Candidates"]
    * 100
)

df.to_csv(
    OUTPUT_DIR / "selection_data_with_criteria.csv",
    index=False
)

department.to_csv(
    OUTPUT_DIR / "department_selection_criteria.csv",
    index=False
)

role.to_csv(
    OUTPUT_DIR / "role_selection_criteria.csv",
    index=False
)

level.to_csv(
    OUTPUT_DIR / "experience_level_selection_criteria.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_selection_criteria.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    department["Department"],
    department["Candidates"],
    color="#4472C4"
)

plt.title("Candidates by Department")
plt.xlabel("Department")
plt.ylabel("Candidates")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "candidates_by_department.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    department["Department"],
    department["Criteria_Met_Rate_%"],
    color="#ED7D31"
)

plt.title("Criteria Met Rate by Department")
plt.xlabel("Department")
plt.ylabel("Criteria Met Rate %")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "criteria_met_rate_by_department.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    level["Experience_Level"],
    level["Criteria_Met_Rate_%"],
    color="#70AD47"
)

plt.title("Criteria Met Rate by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Criteria Met Rate %")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "criteria_met_rate_by_experience_level.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    region["Region"],
    region["Average_Score"],
    color="#8064A2"
)

plt.title("Average Score by Region")
plt.xlabel("Region")
plt.ylabel("Average Overall Score")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_score_by_region.png",
    dpi=160
)

plt.close()

print("Day 066 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")