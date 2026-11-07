from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 062
# Topic: Internal Sourcing — Ranking of Internal Candidates

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_062_W9_L5_Internal_Sourcing_Ranking_of_Internal_Candidates.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Candidate_Data",
    header=2
)

for col in [
    "Experience_Years",
    "Performance_Score",
    "Skill_Match_Score",
    "Leadership_Score",
    "Assessment_Score",
    "Selected_Flag",
]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Composite_Score"] = (
    df["Performance_Score"] * 0.30
    + df["Skill_Match_Score"] * 0.30
    + df["Leadership_Score"] * 0.20
    + (df["Experience_Years"] / 8) * 5 * 0.10
    + (df["Assessment_Score"] / 30) * 5 * 0.10
)

df["Rank"] = (
    df["Composite_Score"]
    .rank(method="min", ascending=False)
    .astype(int)
)

df["Selection_Status"] = df["Selected_Flag"].map(
    {
        1: "Selected",
        0: "Not Selected"
    }
)

ranking = (
    df
    .sort_values(
        ["Rank", "Candidate_ID"]
    )
    .reset_index(drop=True)
)

department = (
    df
    .groupby("Department", as_index=False)
    .agg(
        Candidates=("Candidate_ID", "count"),
        Avg_Composite_Score=("Composite_Score", "mean"),
        Avg_Performance=("Performance_Score", "mean"),
        Avg_Skill_Match=("Skill_Match_Score", "mean"),
        Avg_Leadership=("Leadership_Score", "mean"),
        Selected=("Selected_Flag", "sum"),
    )
)

source = (
    df
    .groupby("Sourcing_Type", as_index=False)
    .agg(
        Candidates=("Candidate_ID", "count"),
        Avg_Composite_Score=("Composite_Score", "mean"),
        Avg_Assessment=("Assessment_Score", "mean"),
        Selected=("Selected_Flag", "sum"),
    )
)

region = (
    df
    .groupby("Region", as_index=False)
    .agg(
        Candidates=("Candidate_ID", "count"),
        Avg_Composite_Score=("Composite_Score", "mean"),
        Selected=("Selected_Flag", "sum"),
    )
)

ranking.to_csv(
    OUTPUT_DIR / "candidate_ranking.csv",
    index=False
)

department.to_csv(
    OUTPUT_DIR / "department_candidate_ranking.csv",
    index=False
)

source.to_csv(
    OUTPUT_DIR / "sourcing_type_ranking.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_candidate_ranking.csv",
    index=False
)

# Chart 1 — Top 10 candidates

top10 = ranking.head(10)

plt.figure(figsize=(10, 5))

plt.bar(
    top10["Candidate_Name"],
    top10["Composite_Score"],
    color="#4472C4"
)

plt.title(
    "Top 10 Candidates by Composite Score"
)

plt.xlabel("Candidate")
plt.ylabel("Composite Score")

plt.xticks(
    rotation=35,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_10_candidate_scores.png",
    dpi=160
)

plt.close()

# Chart 2 — Department

plt.figure(figsize=(9, 5))

plt.bar(
    department["Department"],
    department["Avg_Composite_Score"],
    color="#ED7D31"
)

plt.title(
    "Average Composite Score by Department"
)

plt.xlabel("Department")
plt.ylabel("Average Composite Score")

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_score_by_department.png",
    dpi=160
)

plt.close()

# Chart 3 — Sourcing Type

plt.figure(figsize=(8, 5))

plt.bar(
    source["Sourcing_Type"],
    source["Avg_Composite_Score"],
    color="#70AD47"
)

plt.title(
    "Average Composite Score by Sourcing Type"
)

plt.xlabel("Sourcing Type")
plt.ylabel("Average Composite Score")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_score_by_sourcing_type.png",
    dpi=160
)

plt.close()

# Chart 4 — Selection Status

status = (
    df
    .groupby("Selection_Status", as_index=False)
    .agg(
        Candidates=("Candidate_ID", "count")
    )
)

plt.figure(figsize=(8, 5))

plt.bar(
    status["Selection_Status"],
    status["Candidates"],
    color="#8064A2"
)

plt.title(
    "Candidates by Selection Status"
)

plt.xlabel("Selection Status")
plt.ylabel("Candidates")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "selection_status.png",
    dpi=160
)

plt.close()

print("Day 062 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")