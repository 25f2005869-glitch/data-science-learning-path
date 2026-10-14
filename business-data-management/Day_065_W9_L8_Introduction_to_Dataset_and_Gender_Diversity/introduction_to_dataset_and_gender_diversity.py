from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 065
# Topic: Introduction to Dataset and Gender Diversity

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_065_W9_L8_Introduction_to_Dataset_and_Gender_Diversity.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="HR_Dataset",
    header=0
)

numeric_cols = [
    "Age",
    "Monthly_Salary",
    "Performance_Score",
    "Attrition_Flag",
    "Training_Hours",
    "Attendance_%"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

gender = df.groupby(
    "Gender",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Average_Age=("Age", "mean"),
    Average_Salary=("Monthly_Salary", "mean"),
    Average_Performance=("Performance_Score", "mean"),
    Attrition_Count=("Attrition_Flag", "sum"),
    Average_Training_Hours=("Training_Hours", "mean"),
    Average_Attendance=("Attendance_%", "mean")
)

gender["Gender_Share_%"] = (
    gender["Employees"] / len(df) * 100
)

gender["Attrition_Rate_%"] = (
    gender["Attrition_Count"]
    / gender["Employees"]
    * 100
)

department_gender = pd.crosstab(
    df["Department"],
    df["Gender"]
).reset_index()

region_gender = pd.crosstab(
    df["Region"],
    df["Gender"]
).reset_index()

role_gender = pd.crosstab(
    df["Job_Title"],
    df["Gender"]
).reset_index()

kpis = pd.DataFrame({
    "KPI": [
        "Total Employees",
        "Female Employees",
        "Male Employees",
        "Female Share %",
        "Male Share %"
    ],
    "Value": [
        len(df),
        int(
            (df["Gender"] == "Female").sum()
        ),
        int(
            (df["Gender"] == "Male").sum()
        ),
        float(
            (df["Gender"] == "Female").mean() * 100
        ),
        float(
            (df["Gender"] == "Male").mean() * 100
        )
    ]
})

gender.to_csv(
    OUTPUT_DIR / "gender_summary.csv",
    index=False
)

department_gender.to_csv(
    OUTPUT_DIR / "department_gender_summary.csv",
    index=False
)

region_gender.to_csv(
    OUTPUT_DIR / "region_gender_summary.csv",
    index=False
)

role_gender.to_csv(
    OUTPUT_DIR / "role_gender_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "gender_diversity_kpis.csv",
    index=False
)

plt.figure(figsize=(8, 5))

plt.bar(
    gender["Gender"],
    gender["Employees"],
    color="#4472C4"
)

plt.title("Employees by Gender")
plt.xlabel("Gender")
plt.ylabel("Employees")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "employees_by_gender.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    gender["Gender"],
    gender["Average_Salary"],
    color="#ED7D31"
)

plt.title("Average Salary by Gender")
plt.xlabel("Gender")
plt.ylabel("Monthly Salary")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_salary_by_gender.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    gender["Gender"],
    gender["Average_Performance"],
    color="#70AD47"
)

plt.title("Average Performance by Gender")
plt.xlabel("Gender")
plt.ylabel("Performance Score")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_performance_by_gender.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(8, 5))

plt.bar(
    gender["Gender"],
    gender["Average_Training_Hours"],
    color="#8064A2"
)

plt.title("Average Training Hours by Gender")
plt.xlabel("Gender")
plt.ylabel("Training Hours")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_training_hours_by_gender.png",
    dpi=160
)

plt.close()

print("Day 065 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")