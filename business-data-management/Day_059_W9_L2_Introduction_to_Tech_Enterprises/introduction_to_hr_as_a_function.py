from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 058
# Topic: Introduction to HR as a Function

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_058_W9_L1_Introduction_to_HR_as_a_Function.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="HR_Data",
    header=2
)

department = (
    df.groupby("Department", as_index=False)
    .agg(
        Employees=("Employee_ID", "count"),
        Avg_Salary=("Monthly_Salary", "mean"),
        Avg_Performance=("Performance_Score", "mean"),
        Attrition_Count=("Attrition_Flag", "sum"),
        Avg_Training_Hours=("Training_Hours", "mean"),
        Avg_Attendance=("Attendance_%", "mean"),
    )
)

department["Attrition_Rate_%"] = (
    department["Attrition_Count"]
    / department["Employees"]
    * 100
)

region = (
    df.groupby("Region", as_index=False)
    .agg(
        Employees=("Employee_ID", "count"),
        Avg_Salary=("Monthly_Salary", "mean"),
        Avg_Performance=("Performance_Score", "mean"),
        Attrition_Count=("Attrition_Flag", "sum"),
        Avg_Attendance=("Attendance_%", "mean"),
    )
)

region["Attrition_Rate_%"] = (
    region["Attrition_Count"]
    / region["Employees"]
    * 100
)

employment = (
    df.groupby("Employment_Type", as_index=False)
    .agg(
        Employees=("Employee_ID", "count"),
        Avg_Salary=("Monthly_Salary", "mean"),
        Avg_Performance=("Performance_Score", "mean"),
        Attrition_Count=("Attrition_Flag", "sum"),
        Avg_Training_Hours=("Training_Hours", "mean"),
    )
)

employment["Attrition_Rate_%"] = (
    employment["Attrition_Count"]
    / employment["Employees"]
    * 100
)

kpis = pd.DataFrame({
    "Metric": [
        "Total Employees",
        "Average Monthly Salary",
        "Average Performance Score",
        "Total Attrition Cases",
        "Overall Attrition Rate %",
        "Average Training Hours",
        "Average Attendance %",
    ],
    "Value": [
        len(df),
        df["Monthly_Salary"].mean(),
        df["Performance_Score"].mean(),
        df["Attrition_Flag"].sum(),
        df["Attrition_Flag"].mean() * 100,
        df["Training_Hours"].mean(),
        df["Attendance_%"].mean(),
    ],
})

department.to_csv(
    OUTPUT_DIR / "department_hr_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_hr_summary.csv",
    index=False
)

employment.to_csv(
    OUTPUT_DIR / "employment_type_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "hr_kpis.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    department["Department"],
    department["Employees"],
    color="#4472C4"
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "employees_by_department.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    department["Department"],
    department["Avg_Salary"],
    color="#ED7D31"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Salary")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_salary_by_department.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    department["Department"],
    department["Attrition_Count"],
    color="#70AD47"
)

plt.title("Attrition Cases by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Cases")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "attrition_cases_by_department.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.plot(
    department["Department"],
    department["Avg_Performance"],
    marker="o",
    color="#8064A2"
)

plt.title("Average Performance Score by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")
plt.ylim(0, 5)
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "performance_by_department.png",
    dpi=160
)

plt.close()

print("Day 058 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output folder: {OUTPUT_DIR}")