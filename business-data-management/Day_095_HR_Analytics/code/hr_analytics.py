# Day_095_HR_Analytics
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 095
# Topic: HR Analytics

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. FILE PATH
# ============================================================

possible_paths = [
    "data/Day_095_HR_Analytics.xlsx",
    "Day_095_HR_Analytics.xlsx",
    "../data/Day_095_HR_Analytics.xlsx",
    "/mnt/data/Day_095_HR_Analytics.xlsx"
]

input_file = next(
    (path for path in possible_paths if os.path.exists(path)),
    None
)

if input_file is None:
    raise FileNotFoundError(
        "Day_095_HR_Analytics.xlsx was not found."
    )

output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)


# ============================================================
# 2. LOAD RAW HR DATA
# ============================================================

df = pd.read_excel(
    input_file,
    sheet_name="Raw_HR_Data",
    header=3
)

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.replace(" ", "_", regex=False)
)


# ============================================================
# 3. DATA INSPECTION
# ============================================================

print("\n===== HR DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isna().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())


# ============================================================
# 4. CLEAN TEXT COLUMNS
# ============================================================

text_columns = [
    "Employee_ID",
    "Employee_Name",
    "Department",
    "Job_Role",
    "Education",
    "Location",
    "Employment_Type",
    "Employee_Status",
    "Attrition"
]

for column in text_columns:
    if column in df.columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.title()
        )


# ============================================================
# 5. CLEAN DATE COLUMN
# ============================================================

df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    errors="coerce"
)


# ============================================================
# 6. CONVERT NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    "Age",
    "Experience_Years",
    "Monthly_Salary"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ============================================================
# 7. HANDLE MISSING VALUES
# ============================================================

# Educational practice rules matching the workbook
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

df["Experience_Years"] = df["Experience_Years"].fillna(
    df["Experience_Years"].median()
)

df["Monthly_Salary"] = df["Monthly_Salary"].fillna(
    df["Monthly_Salary"].median()
)

df["Department"] = df["Department"].fillna(
    "Finance"
)


# ============================================================
# 8. VALIDATE EXPERIENCE
# ============================================================

df.loc[
    df["Experience_Years"] < 0,
    "Experience_Years"
] = df["Experience_Years"].median()


# ============================================================
# 9. REMOVE DUPLICATE RECORDS
# ============================================================

df = (
    df
    .drop_duplicates()
    .reset_index(drop=True)
)


# ============================================================
# 10. EMPLOYEE SUMMARY
# ============================================================

employee_summary = pd.DataFrame({
    "Metric": [
        "Total Employees",
        "Average Age",
        "Average Experience (Years)",
        "Average Monthly Salary",
        "Total Monthly Salary Cost",
        "Active Employees",
        "Attrition Count"
    ],
    "Value": [
        len(df),
        df["Age"].mean(),
        df["Experience_Years"].mean(),
        df["Monthly_Salary"].mean(),
        df["Monthly_Salary"].sum(),
        (df["Employee_Status"] == "Active").sum(),
        (df["Attrition"] == "Yes").sum()
    ]
})

employee_summary.to_csv(
    f"{output_dir}/hr_summary.csv",
    index=False
)


# ============================================================
# 11. DEPARTMENT ANALYSIS
# ============================================================

department_analysis = (
    df.groupby(
        "Department",
        as_index=False
    )
    .agg(
        Employee_Count=("Employee_ID", "count"),
        Average_Salary=("Monthly_Salary", "mean"),
        Total_Salary=("Monthly_Salary", "sum"),
        Average_Experience=("Experience_Years", "mean"),
        Attrition_Count=(
            "Attrition",
            lambda x: (x == "Yes").sum()
        )
    )
)

department_analysis["Attrition_Rate_%"] = np.where(
    department_analysis["Employee_Count"] > 0,
    department_analysis["Attrition_Count"]
    / department_analysis["Employee_Count"]
    * 100,
    0
)

department_analysis = department_analysis.sort_values(
    "Employee_Count",
    ascending=False
)

department_analysis.to_csv(
    f"{output_dir}/department_analysis.csv",
    index=False
)


# ============================================================
# 12. JOB ROLE ANALYSIS
# ============================================================

job_role_analysis = (
    df.groupby(
        "Job_Role",
        as_index=False
    )
    .agg(
        Employee_Count=("Employee_ID", "count"),
        Average_Salary=("Monthly_Salary", "mean"),
        Total_Salary=("Monthly_Salary", "sum"),
        Average_Experience=("Experience_Years", "mean")
    )
    .sort_values(
        "Employee_Count",
        ascending=False
    )
)

job_role_analysis.to_csv(
    f"{output_dir}/job_role_analysis.csv",
    index=False
)


# ============================================================
# 13. SALARY ANALYSIS
# ============================================================

salary_analysis = (
    df.groupby(
        "Department",
        as_index=False
    )
    .agg(
        Average_Salary=("Monthly_Salary", "mean"),
        Minimum_Salary=("Monthly_Salary", "min"),
        Maximum_Salary=("Monthly_Salary", "max"),
        Total_Salary=("Monthly_Salary", "sum")
    )
)

salary_analysis.to_csv(
    f"{output_dir}/salary_analysis.csv",
    index=False
)


# ============================================================
# 14. ATTRITION ANALYSIS
# ============================================================

attrition_analysis = (
    df.groupby(
        "Department",
        as_index=False
    )
    .agg(
        Employees=("Employee_ID", "count"),
        Attrition_Count=(
            "Attrition",
            lambda x: (x == "Yes").sum()
        )
    )
)

attrition_analysis["Attrition_Rate_%"] = np.where(
    attrition_analysis["Employees"] > 0,
    attrition_analysis["Attrition_Count"]
    / attrition_analysis["Employees"]
    * 100,
    0
)

attrition_analysis.to_csv(
    f"{output_dir}/attrition_analysis.csv",
    index=False
)


# ============================================================
# 15. MONTHLY HR ANALYSIS
# ============================================================

df["Month"] = (
    df["Joining_Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_hr_analysis = (
    df.groupby(
        "Month",
        as_index=False
    )
    .agg(
        Employee_Records=("Employee_ID", "count"),
        New_Joiners=("Employee_ID", "count"),
        Attrition_Count=(
            "Attrition",
            lambda x: (x == "Yes").sum()
        ),
        Total_Monthly_Salary=(
            "Monthly_Salary",
            "sum"
        )
    )
)

monthly_hr_analysis.to_csv(
    f"{output_dir}/monthly_hr_analysis.csv",
    index=False
)


# ============================================================
# 16. HR KPIs
# ============================================================

total_employees = len(df)

attrition_count = (
    df["Attrition"] == "Yes"
).sum()

if total_employees > 0:
    attrition_rate = (
        attrition_count
        / total_employees
        * 100
    )
else:
    attrition_rate = 0

hr_kpi = pd.DataFrame({
    "KPI": [
        "Total Employees",
        "Average Age",
        "Average Experience (Years)",
        "Average Monthly Salary",
        "Total Monthly Salary Cost",
        "Attrition Count",
        "Attrition Rate (%)"
    ],
    "Value": [
        total_employees,
        df["Age"].mean(),
        df["Experience_Years"].mean(),
        df["Monthly_Salary"].mean(),
        df["Monthly_Salary"].sum(),
        attrition_count,
        attrition_rate
    ]
})

hr_kpi.to_csv(
    f"{output_dir}/hr_kpi_summary.csv",
    index=False
)


# ============================================================
# 17. SAVE CLEANED HR DATA
# ============================================================

df.to_csv(
    f"{output_dir}/cleaned_hr_data.csv",
    index=False
)


# ============================================================
# 18. CHART — EMPLOYEE COUNT BY DEPARTMENT
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    department_analysis["Department"],
    department_analysis["Employee_Count"]
)

plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    f"{output_dir}/employee_count_by_department.png",
    dpi=300
)

plt.close()


# ============================================================
# 19. CHART — AVERAGE SALARY BY DEPARTMENT
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    department_analysis["Department"],
    department_analysis["Average_Salary"]
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Salary")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    f"{output_dir}/salary_by_department.png",
    dpi=300
)

plt.close()


# ============================================================
# 20. CHART — ATTRITION BY DEPARTMENT
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    attrition_analysis["Department"],
    attrition_analysis["Attrition_Count"]
)

plt.title("Attrition Count by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Count")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    f"{output_dir}/attrition_by_department.png",
    dpi=300
)

plt.close()


# ============================================================
# 21. CHART — MONTHLY HR TREND
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_hr_analysis["Month"],
    monthly_hr_analysis["Employee_Records"],
    marker="o"
)

plt.title("Monthly HR Trend")
plt.xlabel("Month")
plt.ylabel("Employee Records")

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    f"{output_dir}/monthly_hr_trend.png",
    dpi=300
)

plt.close()


# ============================================================
# 22. PRINT FINAL RESULTS
# ============================================================

print("\n===== HR ANALYTICS COMPLETED =====")

print(
    "Total Employees:",
    total_employees
)

print(
    "Average Age:",
    round(df["Age"].mean(), 2)
)

print(
    "Average Experience:",
    round(df["Experience_Years"].mean(), 2)
)

print(
    "Average Monthly Salary:",
    round(df["Monthly_Salary"].mean(), 2)
)

print(
    "Total Monthly Salary Cost:",
    round(df["Monthly_Salary"].sum(), 2)
)

print(
    "Attrition Count:",
    int(attrition_count)
)

print(
    "Attrition Rate:",
    round(attrition_rate, 2),
    "%"
)

print(
    "\nOutput files saved in:",
    output_dir
)