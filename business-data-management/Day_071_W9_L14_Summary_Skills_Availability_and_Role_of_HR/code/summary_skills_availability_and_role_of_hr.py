from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 071
# Topic: Summary — Skills Availability and Role of HR


# Find the project folder
SCRIPT_FOLDER = Path(__file__).resolve().parent

if SCRIPT_FOLDER.name.lower() == "code":
    PROJECT_FOLDER = SCRIPT_FOLDER.parent
else:
    PROJECT_FOLDER = SCRIPT_FOLDER


# Locate the Excel workbook
possible_files = [
    PROJECT_FOLDER / "Day_071_W9_L14_Summary_Skills_Availability_and_Role_of_HR_Corrected.xlsx",
    PROJECT_FOLDER / "Day_071_W9_L14_Summary_Skills_Availability_and_Role_of_HR.xlsx"
]

INPUT_FILE = None

for file in possible_files:
    if file.exists():
        INPUT_FILE = file
        break

if INPUT_FILE is None:
    raise FileNotFoundError(
        "Day 071 Excel workbook was not found in the project folder."
    )


# Create the output folder
OUTPUT_FOLDER = PROJECT_FOLDER / "python_outputs"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# Read the Excel sheet and find the actual header row
SHEET_NAME = "Skills_Availability_Data"

required_columns = [
    "Employee_ID",
    "Department",
    "Region",
    "Job_Role",
    "Experience_Level",
    "Primary_Skill",
    "Skill_Score",
    "Skill_Available_Flag",
    "Training_Hours",
    "Skill_Gap_Flag",
    "Training_Need_Flag"
]

try:
    preview = pd.read_excel(
        INPUT_FILE,
        sheet_name=SHEET_NAME,
        header=None,
        nrows=15
    )

except ValueError as error:
    raise ValueError(
        f"Sheet '{SHEET_NAME}' was not found in the workbook."
    ) from error


# Find the row containing all required column names
header_row = None

for row_number in range(len(preview)):

    row_values = (
        preview.iloc[row_number]
        .astype(str)
        .str.strip()
        .tolist()
    )

    if all(column in row_values for column in required_columns):
        header_row = row_number
        break

if header_row is None:
    raise ValueError(
        "Required column headings were not found in the first 15 rows."
    )


# Load employee records
df = pd.read_excel(
    INPUT_FILE,
    sheet_name=SHEET_NAME,
    header=header_row
)


# Check whether all required columns are available
missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        "Missing columns: " + ", ".join(missing_columns)
    )


# Remove rows without an employee ID
df = df.dropna(subset=["Employee_ID"]).copy()

if df.empty:
    raise ValueError("No employee records were found in the Excel sheet.")


# Convert numerical columns into numeric values
numeric_columns = [
    "Skill_Score",
    "Skill_Available_Flag",
    "Training_Hours",
    "Performance_Score",
    "Skill_Gap_Flag",
    "Training_Need_Flag"
]

for column in numeric_columns:

    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# Check the three flag columns
flag_columns = [
    "Skill_Available_Flag",
    "Skill_Gap_Flag",
    "Training_Need_Flag"
]

for column in flag_columns:

    invalid_values = df.loc[
        df[column].notna() & ~df[column].isin([0, 1]),
        column
    ].unique()

    if len(invalid_values) > 0:
        raise ValueError(
            f"{column} must contain only 0 or 1. "
            f"Found values: {invalid_values.tolist()}"
        )

    if df[column].isna().any():
        raise ValueError(
            f"{column} contains blank or invalid values."
        )


# Skill-wise analysis
skill = df.groupby(
    "Primary_Skill",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
    Average_Training_Hours=("Training_Hours", "mean")
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


# Department-wise analysis
department = df.groupby(
    "Department",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
    Training_Needs=("Training_Need_Flag", "sum")
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


# Region-wise analysis
region = df.groupby(
    "Region",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
    Average_Training_Hours=("Training_Hours", "mean")
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


# Job role-wise analysis
role = df.groupby(
    "Job_Role",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum")
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


# Experience-level analysis
experience = df.groupby(
    "Experience_Level",
    as_index=False
).agg(
    Employees=("Employee_ID", "count"),
    Available=("Skill_Available_Flag", "sum"),
    Average_Skill_Score=("Skill_Score", "mean"),
    Skill_Gap=("Skill_Gap_Flag", "sum"),
    Average_Training_Hours=("Training_Hours", "mean")
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


# Calculate overall KPIs
total_employees = len(df)

available_count = int(
    df["Skill_Available_Flag"].sum()
)

skill_gap_count = int(
    df["Skill_Gap_Flag"].sum()
)

training_count = int(
    df["Training_Need_Flag"].sum()
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
        "Employees Requiring Training"
    ],

    "Value": [
        total_employees,
        available_count,
        available_count / total_employees * 100,
        skill_gap_count,
        skill_gap_count / total_employees * 100,
        df["Skill_Score"].mean(),
        df["Training_Hours"].mean(),
        training_count
    ]
})


# Save all analysis tables
tables = {
    "skills_availability_data.csv": df,
    "skill_summary.csv": skill,
    "department_skill_summary.csv": department,
    "region_skill_summary.csv": region,
    "role_skill_summary.csv": role,
    "experience_skill_summary.csv": experience,
    "skills_kpis.csv": kpis
}

for file_name, table in tables.items():

    table.to_csv(
        OUTPUT_FOLDER / file_name,
        index=False
    )


# Create and save bar charts
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

    plt.figure(figsize=(10, 5))

    plt.bar(
        x,
        y,
        color=color
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(
        rotation=rotation,
        ha="right" if rotation != 0 else "center"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_FOLDER / filename,
        dpi=160
    )

    plt.close()


# Employees by primary skill
save_bar(
    skill["Primary_Skill"],
    skill["Employees"],
    "Employees by Primary Skill",
    "Primary Skill",
    "Employees",
    "employees_by_skill.png",
    "#4472C4",
    rotation=45
)


# Skill gap rate by department
save_bar(
    department["Department"],
    department["Skill_Gap_Rate_%"],
    "Skill Gap Rate by Department",
    "Department",
    "Skill Gap Rate %",
    "skill_gap_rate_by_department.png",
    "#70AD47",
    rotation=45
)


# Skill availability by region
save_bar(
    region["Region"],
    region["Availability_Rate_%"],
    "Skill Availability Rate by Region",
    "Region",
    "Availability Rate %",
    "skill_availability_by_region.png",
    "#ED7D31",
    rotation=45
)


# Average skill score by job role
save_bar(
    role["Job_Role"],
    role["Average_Skill_Score"],
    "Average Skill Score by Role",
    "Job Role",
    "Average Skill Score",
    "average_skill_score_by_role.png",
    "#8064A2",
    rotation=45
)


# Display the final results
print("Day 071 analysis complete.")

print("Total employees:", total_employees)

print("Employees with available skill:", available_count)

print(
    "Overall skill availability:",
    round(available_count / total_employees * 100, 2),
    "%"
)

print("Employees with skill gap:", skill_gap_count)

print(
    "Overall skill gap rate:",
    round(skill_gap_count / total_employees * 100, 2),
    "%"
)

print("Employees requiring training:", training_count)

print("Header row found:", header_row + 1)

print("Output folder:", OUTPUT_FOLDER)