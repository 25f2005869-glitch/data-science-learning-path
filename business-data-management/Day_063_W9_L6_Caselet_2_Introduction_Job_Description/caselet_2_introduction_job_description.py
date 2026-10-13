from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 063
# Topic: Caselet 2 — Introduction: Job Description

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_063_W9_L6_Caselet_2_Introduction_Job_Description.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Job_Descriptions",
    header=2
)

df["Required_Skill_Count"] = (
    df["Required_Skills"]
    .str.split(", ")
    .str.len()
)

df["Experience_Years_Min"] = (
    df["Experience_Required"]
    .str.extract(r"(\d+)")[0]
    .astype(int)
)

df["Description_Completeness_Score"] = (
    df[
        [
            "Job_Title",
            "Department",
            "Qualification",
            "Required_Skills",
            "Experience_Required",
            "Role_Summary",
            "Key_KPIs",
            "Reports_To"
        ]
    ]
    .notna()
    .sum(axis=1)
    / 8
    * 100
)

department = (
    df
    .groupby("Department", as_index=False)
    .agg(
        Job_Count=("Job_ID", "count"),
        Avg_Required_Skills=("Required_Skill_Count", "mean"),
        Avg_Experience_Years=("Experience_Years_Min", "mean"),
        Avg_Completeness=(
            "Description_Completeness_Score",
            "mean"
        )
    )
)

level = (
    df
    .groupby("Level", as_index=False)
    .agg(
        Job_Count=("Job_ID", "count"),
        Avg_Required_Skills=("Required_Skill_Count", "mean"),
        Avg_Experience_Years=("Experience_Years_Min", "mean")
    )
)

context = (
    df
    .groupby("Business_Context", as_index=False)
    .agg(
        Job_Count=("Job_ID", "count"),
        Avg_Experience_Years=("Experience_Years_Min", "mean"),
        Avg_Required_Skills=("Required_Skill_Count", "mean")
    )
)

function = (
    df
    .groupby("Function", as_index=False)
    .agg(
        Job_Count=("Job_ID", "count"),
        Avg_Experience_Years=("Experience_Years_Min", "mean")
    )
)

skill_rows = []

for skill in [
    "Excel",
    "SQL",
    "Python",
    "Power BI",
    "Communication",
    "Statistics",
    "Presentation"
]:

    mask = df["Required_Skills"].str.contains(
        skill,
        case=False,
        regex=False
    )

    skill_rows.append(
        {
            "Skill": skill,
            "Job_Count": int(mask.sum()),
            "Job_Share_%": float(mask.mean() * 100)
        }
    )

skill_summary = pd.DataFrame(skill_rows)

department.to_csv(
    OUTPUT_DIR / "department_job_description_summary.csv",
    index=False
)

level.to_csv(
    OUTPUT_DIR / "job_level_summary.csv",
    index=False
)

context.to_csv(
    OUTPUT_DIR / "business_context_summary.csv",
    index=False
)

function.to_csv(
    OUTPUT_DIR / "function_summary.csv",
    index=False
)

skill_summary.to_csv(
    OUTPUT_DIR / "required_skill_summary.csv",
    index=False
)

# Chart 1 — Department

plt.figure(figsize=(9, 5))

plt.bar(
    department["Department"],
    department["Job_Count"],
    color="#4472C4"
)

plt.title(
    "Job Descriptions by Department"
)

plt.xlabel("Department")
plt.ylabel("Job Count")

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "job_descriptions_by_department.png",
    dpi=160
)

plt.close()

# Chart 2 — Required Skills

plt.figure(figsize=(9, 5))

plt.bar(
    skill_summary["Skill"],
    skill_summary["Job_Count"],
    color="#ED7D31"
)

plt.title(
    "Required Skills Frequency"
)

plt.xlabel("Skill")
plt.ylabel("Job Count")

plt.xticks(
    rotation=35,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "required_skills_frequency.png",
    dpi=160
)

plt.close()

# Chart 3 — Job Level

plt.figure(figsize=(8, 5))

plt.bar(
    level["Level"],
    level["Job_Count"],
    color="#70AD47"
)

plt.title(
    "Job Descriptions by Level"
)

plt.xlabel("Level")
plt.ylabel("Job Count")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "job_descriptions_by_level.png",
    dpi=160
)

plt.close()

# Chart 4 — Business Context

plt.figure(figsize=(8, 5))

plt.bar(
    context["Business_Context"],
    context["Job_Count"],
    color="#8064A2"
)

plt.title(
    "Job Descriptions by Business Context"
)

plt.xlabel("Business Context")
plt.ylabel("Job Count")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "job_descriptions_by_business_context.png",
    dpi=160
)

plt.close()

print("Day 063 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")