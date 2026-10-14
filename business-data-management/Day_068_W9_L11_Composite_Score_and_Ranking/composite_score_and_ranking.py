from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 068
# Topic: Composite Score and Ranking

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_068_W9_L11_Composite_Score_and_Ranking.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Candidate_Data"
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

df["Composite_Score"] = (
    df["Technical_Score"] * 0.30
    + df["Communication_Score"] * 0.20
    + df["Interview_Score"] * 0.30
    + df["Overall_Score"] * 0.20
)

df["Composite_Rank"] = (
    df["Composite_Score"]
    .rank(
        method="min",
        ascending=False
    )
    .astype(int)
)

df["Composite_Percentile"] = (
    df["Composite_Score"]
    .rank(pct=True)
    * 100
)

department = df.groupby(
    "Department",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Average_Composite_Score=("Composite_Score", "mean"),
    Highest_Composite_Score=("Composite_Score", "max"),
    Selected=("Selected_Flag", "sum")
)

department["Selection_Rate_%"] = (
    department["Selected"]
    / department["Candidates"]
    * 100
)

level = df.groupby(
    "Experience_Level",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Average_Composite_Score=("Composite_Score", "mean"),
    Highest_Composite_Score=("Composite_Score", "max"),
    Selected=("Selected_Flag", "sum")
)

level["Selection_Rate_%"] = (
    level["Selected"]
    / level["Candidates"]
    * 100
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Average_Composite_Score=("Composite_Score", "mean"),
    Highest_Composite_Score=("Composite_Score", "max"),
    Selected=("Selected_Flag", "sum")
)

region["Selection_Rate_%"] = (
    region["Selected"]
    / region["Candidates"]
    * 100
)

role = df.groupby(
    "Target_Role",
    as_index=False
).agg(
    Candidates=("Candidate_ID", "count"),
    Average_Composite_Score=("Composite_Score", "mean"),
    Highest_Composite_Score=("Composite_Score", "max"),
    Selected=("Selected_Flag", "sum")
)

role["Selection_Rate_%"] = (
    role["Selected"]
    / role["Candidates"]
    * 100
)

top10 = (
    df.sort_values(
        [
            "Composite_Score",
            "Candidate_ID"
        ],
        ascending=[
            False,
            True
        ]
    )
    .head(10)
)

df.to_csv(
    OUTPUT_DIR / "candidate_composite_scores.csv",
    index=False
)

department.to_csv(
    OUTPUT_DIR / "department_composite_summary.csv",
    index=False
)

level.to_csv(
    OUTPUT_DIR / "experience_level_composite_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_composite_summary.csv",
    index=False
)

role.to_csv(
    OUTPUT_DIR / "role_composite_summary.csv",
    index=False
)

top10.to_csv(
    OUTPUT_DIR / "top_10_composite_ranking.csv",
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
    department["Department"],
    department["Average_Composite_Score"],
    "Average Composite Score by Department",
    "Department",
    "Composite Score",
    "average_composite_score_by_department.png",
    "#4472C4"
)

save_bar(
    level["Experience_Level"],
    level["Average_Composite_Score"],
    "Average Composite Score by Experience Level",
    "Experience Level",
    "Composite Score",
    "average_composite_score_by_experience_level.png",
    "#ED7D31"
)

save_bar(
    region["Region"],
    region["Average_Composite_Score"],
    "Average Composite Score by Region",
    "Region",
    "Composite Score",
    "average_composite_score_by_region.png",
    "#70AD47"
)

save_bar(
    top10["Candidate_ID"],
    top10["Composite_Score"],
    "Top 10 Composite Score Ranking",
    "Candidate",
    "Composite Score",
    "top_10_composite_ranking.png",
    "#8064A2",
    rotation=30
)

print("Day 068 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")