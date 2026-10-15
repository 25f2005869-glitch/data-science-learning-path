from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 071
# Topic: Summary — Skills Availability and Role of HR

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_071_W9_L14_Summary_Skills_Availability_and_Role_of_HR.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Skills_Availability_Data",
    header=2
)

numeric_cols = [
    "Skill_Score",
    "Skill_Available_Flag",
    "Training_Hours",
    "Performance_Score",
    "Skill_Gap_Flag",
    "Training_Need_Flag",
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

skill = df.groupby(
    "Primary_Skill",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
    Average_Training_Hours=("Training_Hours", "mean"),
)

skill["Availability_Rate_%"] = (
    skill["Available"]
    / skill["Employees"]
    * 100
)

skill["Skill_Gap_Rate_%"] = (
    skill["Skill_Gap"]
    / skill["Employees"]
    * 100
)

department = df.groupby(
    "Department",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
    Training_Needs=("Training_Need_Flag", "sum"),
)

department["Availability_Rate_%"] = (
    department["Available"]
    / department["Employees"]
    * 100
)

department["Skill_Gap_Rate_%"] = (
    department["Skill_Gap"]
    / department["Employees"]
    * 100
)

department["Training_Need_Rate_%"] = (
    department["Training_Needs"]
    / department["Employees"]
    * 100
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
    Average_Training_Hours=("Training_Hours", "mean"),
)

region["Availability_Rate_%"] = (
    region["Available"]
    / region["Employees"]
    * 100
)

region["Skill_Gap_Rate_%"] = (
    region["Skill_Gap"]
    / region["Employees"]
    * 100
)

role = df.groupby(
    "Job_Role",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
)

role["Availability_Rate_%"] = (
    role["Available"]
    / role["Employees"]
    * 100
)

role["Skill_Gap_Rate_%"] = (
    role["Skill_Gap"]
    / role["Employees"]
    * 100
)

experience = df.groupby(
    "Experience_Level",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
    Average_Training_Hours=("Training_Hours", "mean"),
)

experience["Availability_Rate_%"] = (
    experience["Available"]
    / experience["Employees"]
    * 100
)

experience["Skill_Gap_Rate_%"] = (
    experience["Skill_Gap"]
    / experience["Employees"]
    * 100
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Employees",
        "Employees with Available Skill",
        "Overall Skill Availability %",
        "Employees with Skill Gap",
        "Overall Skill Gap %",
        "Average Skill Score",
        "Average Training Hours",
        "Employees Requiring Training",
    ],
    "Value": [
        len(df),
        int(df["Skill_Available_Flag"].sum()),
        df["Skill_Available_Flag"].mean() * 100,
        int(df["Skill_Gap_Flag"].sum()),
        df["Skill_Gap_Flag"].mean() * 100,
        df["Skill_Score"].mean(),
        df["Training_Hours"].mean(),
        int(df["Training_Need_Flag"].sum()),
    ],
})

df.to_csv(
    OUTPUT_DIR / "skills_availability_data.csv",
    index=False
)

skill.to_csv(
    OUTPUT_DIR / "skill_summary.csv",
    index=False
)

department.to_csv(
    OUTPUT_DIR / "department_skill_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_skill_summary.csv",
    index=False
)

role.to_csv(
    OUTPUT_DIR / "role_skill_summary.csv",
    index=False
)

experience.to_csv(
    OUTPUT_DIR / "experience_skill_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "skills_kpis.csv",
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
    skill["Primary_Skill"],
    skill["Employees"],
    "Employees by Primary Skill",
    "Primary Skill",
    "Employees",
    "employees_by_skill.png",
    "#4472C4",
    25,
)

save_bar(
    department["Department"],
    department["Skill_Gap_Rate_%"],
    "Skill Gap Rate by Department",
    "Department",
    "Skill Gap Rate %",
    "skill_gap_rate_by_department.png",
    "#70AD47",
    25,
)

save_bar(
    region["Region"],
    region["Availability_Rate_%"],
    "Skill Availability Rate by Region",
    "Region",
    "Availability Rate %",
    "skill_availability_by_region.png",
    "#ED7D31",
)

save_bar(
    role["Job_Role"],
    role["Average_Skill_Score"],
    "Average Skill Score by Role",
    "Job Role",
    "Average Skill Score",
    "average_skill_score_by_role.png",
    "#8064A2",
    25,
)

print("Day 071 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")