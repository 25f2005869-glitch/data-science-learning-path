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

# The HR_Dataset sheet contains 24 employee records below its header.
# The remaining rows on the worksheet contain reference tables and notes.
df = pd.read_excel(
    INPUT_FILE,
    sheet_name="HR_Dataset",
    header=0,
    nrows=24
)

# Clean categorical text so spacing and letter case do not create
# duplicate categories in summaries or crosstabs.
categorical_columns = ["Gender", "Department", "Job_Title"]

for col in categorical_columns:
    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .str.title()
    )

# Convert numeric fields safely.
numeric_cols = [
    "Age",
    "Monthly_Salary",
    "Performance_Score",
    "Attrition_Flag",
    "Training_Hours",
    "Attendance_%"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Gender-wise summary.
gender = (
    df.groupby("Gender", as_index=False)
    .agg(
        Employees=("Employee_ID", "count"),
        Average_Age=("Age", "mean"),
        Average_Salary=("Monthly_Salary", "mean"),
        Average_Performance=("Performance_Score", "mean"),
        Attrition_Count=("Attrition_Flag", "sum"),
        Average_Training_Hours=("Training_Hours", "mean"),
        Average_Attendance=("Attendance_%", "mean")
    )
)

gender["Gender_Share_%"] = gender["Employees"] / len(df) * 100

gender["Attrition_Rate_%"] = (
    gender["Attrition_Count"] / gender["Employees"] * 100
)

# Cross-tabulations after text standardisation.
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

# Overall KPIs.
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
        int((df["Gender"] == "Female").sum()),
        int((df["Gender"] == "Male").sum()),
        float((df["Gender"] == "Female").mean() * 100),
        float((df["Gender"] == "Male").mean() * 100)
    ]
})

# Save analysis tables.
gender.to_csv(OUTPUT_DIR / "gender_summary.csv", index=False)
department_gender.to_csv(
    OUTPUT_DIR / "department_gender_summary.csv", index=False
)
region_gender.to_csv(
    OUTPUT_DIR / "region_gender_summary.csv", index=False
)
role_gender.to_csv(OUTPUT_DIR / "role_gender_summary.csv", index=False)
kpis.to_csv(OUTPUT_DIR / "gender_diversity_kpis.csv", index=False)

# Chart 1: gender share as a pie chart.
plt.figure(figsize=(7, 6))
plt.pie(
    gender["Employees"],
    labels=gender["Gender"],
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5}
)
plt.title("Employee Share by Gender")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "gender_share_pie.png", dpi=180)
plt.close()

# Chart 2: grouped bars compare gender counts across departments.
department_chart = pd.crosstab(
    df["Department"],
    df["Gender"]
)

department_chart.plot(
    kind="bar",
    figsize=(10, 6),
    width=0.78
)
plt.title("Employee Count by Department and Gender")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=25, ha="right")
plt.legend(title="Gender")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "department_gender_grouped_bar.png", dpi=180)
plt.close()

# Other gender-wise comparisons.
chart_specs = [
    ("Average_Salary", "Average Salary by Gender",
     "Monthly Salary", "average_salary_by_gender.png"),
    ("Average_Performance", "Average Performance by Gender",
     "Performance Score", "average_performance_by_gender.png"),
    ("Average_Training_Hours", "Average Training Hours by Gender",
     "Training Hours", "average_training_hours_by_gender.png")
]

for column, title, y_label, filename in chart_specs:
    plt.figure(figsize=(8, 5))
    plt.bar(gender["Gender"], gender[column])
    plt.title(title)
    plt.xlabel("Gender")
    plt.ylabel(y_label)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=180)
    plt.close()

print("Gender diversity analysis completed.")
print("Employee records analysed:", len(df))
print("\nGender summary:")
print(gender.to_string(index=False))
print("\nDepartment-wise gender count:")
print(department_gender.to_string(index=False))
print("\nKPI summary:")
print(kpis.to_string(index=False))
print(f"\nOutput folder: {OUTPUT_DIR.resolve()}")
