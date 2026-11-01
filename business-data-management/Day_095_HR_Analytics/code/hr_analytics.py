# Day_095_HR_Analytics
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 095
# Topic: HR Analytics

from pathlib import Path

import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.utils import get_column_letter


# Keep this file inside the code folder.
project = Path(__file__).resolve().parent
if project.name.lower() == "code":
    project = project.parent

source = project / "Day_095_HR_Analytics.xlsx"
if not source.exists():
    source = project / "Day_095_HR_Analytics_Updated.xlsx"

if not source.exists():
    raise FileNotFoundError(
        "Keep Day_095_HR_Analytics.xlsx in the main Day_095_HR_Analytics folder."
    )

output = project / "Day_095_HR_Analytics_Updated.xlsx"
output_dir = project / "outputs"
output_dir.mkdir(exist_ok=True)


# Read the raw sheet. The first three rows are the workbook heading.
raw = pd.read_excel(source, sheet_name="Raw_HR_Data", header=3)
raw.columns = (
    raw.columns.astype(str)
    .str.strip()
    .str.replace(" ", "_", regex=False)
)

# Keep a copy of the source values for the quality report.
df = raw.copy()
df = df.drop_duplicates().reset_index(drop=True)

text_columns = [
    "Employee_ID", "Employee_Name", "Department", "Job_Role",
    "Education", "Location", "Employment_Type",
    "Employee_Status", "Attrition"
]

for column in text_columns:
    df[column] = (
        df[column].astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

# Standardise department names without changing HR and IT to Hr and It.
department_names = {
    "sales": "Sales",
    "finance": "Finance",
    "hr": "HR",
    "it": "IT",
    "marketing": "Marketing",
    "operations": "Operations"
}
df["Department"] = (
    df["Department"].str.casefold().map(department_names)
    .fillna(df["Department"])
)

# Standardise role names while keeping the HR acronym.
role_names = {
    "sales executive": "Sales Executive",
    "financial analyst": "Financial Analyst",
    "hr executive": "HR Executive",
    "software analyst": "Software Analyst",
    "operations executive": "Operations Executive",
    "marketing executive": "Marketing Executive"
}
df["Job_Role"] = (
    df["Job_Role"].str.casefold().map(role_names)
    .fillna(df["Job_Role"])
)

for column in ["Employee_Status", "Attrition", "Employment_Type", "Education", "Location"]:
    df[column] = df[column].str.title()

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"], errors="coerce")

for column in ["Age", "Experience_Years", "Monthly_Salary"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# Check role and department combinations against the known role mapping.
role_department = {
    "Sales Executive": "Sales",
    "Financial Analyst": "Finance",
    "HR Executive": "HR",
    "Software Analyst": "IT",
    "Operations Executive": "Operations",
    "Marketing Executive": "Marketing"
}

df["Expected_Department"] = df["Job_Role"].map(role_department)

df["Role_Department_Check"] = np.select(
    [
        df["Department"].isna(),
        df["Expected_Department"].isna(),
        df["Department"].fillna("").ne(df["Expected_Department"].fillna(""))
    ],
    [
        "Department Missing",
        "Role Mapping Not Defined",
        "Mismatch"
    ],
    default="OK"
)

# Flag impossible age and experience combinations. Do not silently change them.
df["Age_Experience_Conflict"] = (
    df["Age"].notna()
    & df["Experience_Years"].notna()
    & (df["Experience_Years"] > df["Age"] - 18)
)

# Fill missing or invalid values using the employee's department median.
# If the department is unknown, use the overall median and record that fallback.
imputation_log = []

for column in ["Age", "Experience_Years", "Monthly_Salary"]:
    bad = df[column].isna()
    if column == "Experience_Years":
        bad = bad | df[column].lt(0)

    for index in df.index[bad]:
        department = df.at[index, "Department"]
        group_values = df.loc[
            df["Department"].eq(department) & df[column].ge(0)
            if column == "Experience_Years"
            else df["Department"].eq(department),
            column
        ].dropna()

        if pd.notna(department) and not group_values.empty:
            replacement = group_values.median()
            method = "Department median"
        else:
            valid_values = df.loc[
                df[column].ge(0) if column == "Experience_Years"
                else df[column].notna(),
                column
            ].dropna()
            replacement = valid_values.median()
            method = "Overall median fallback"

        old_value = df.at[index, column]
        df.at[index, column] = replacement

        imputation_log.append([
            df.at[index, "Employee_ID"],
            column,
            old_value,
            replacement,
            department if pd.notna(department) else "Unknown",
            method
        ])

# Do not guess the missing department. Keep it clearly labelled.
df["Department"] = df["Department"].fillna("Unknown")

# Recalculate the age/experience flag after imputation, but retain the
# original conflict flag as a data-quality indicator.
df["Age_Experience_Conflict"] = (
    df["Age"].notna()
    & df["Experience_Years"].notna()
    & (df["Experience_Years"] > df["Age"] - 18)
)

df["Month"] = df["Joining_Date"].dt.to_period("M").astype("string")


# Main workforce measures.
total_employees = df["Employee_ID"].nunique()
active_employees = df["Employee_Status"].eq("Active").sum()
attrition_count = df["Attrition"].str.casefold().eq("yes").sum()
attrition_rate = (
    attrition_count / total_employees * 100 if total_employees else 0
)

employee_summary = pd.DataFrame([
    ["Total Employees", total_employees],
    ["Active Employees", active_employees],
    ["Attrition Count", attrition_count],
    ["Attrition Rate (%)", attrition_rate],
    ["Average Age", df["Age"].mean()],
    ["Average Experience (Years)", df["Experience_Years"].mean()],
    ["Average Monthly Salary", df["Monthly_Salary"].mean()],
    ["Total Monthly Salary Cost", df["Monthly_Salary"].sum()]
], columns=["Metric", "Value"])


def department_summary(data, group_column):
    result = (
        data.groupby(group_column, dropna=False)
        .agg(
            Employee_Count=("Employee_ID", "nunique"),
            Average_Salary=("Monthly_Salary", "mean"),
            Total_Salary=("Monthly_Salary", "sum"),
            Average_Experience=("Experience_Years", "mean"),
            Attrition_Count=("Attrition", lambda values: values.str.casefold().eq("yes").sum())
        )
        .reset_index()
    )
    result["Attrition_Rate_%"] = np.where(
        result["Employee_Count"].gt(0),
        result["Attrition_Count"] / result["Employee_Count"] * 100,
        0
    )
    return result.sort_values("Employee_Count", ascending=False)


department_analysis = department_summary(df, "Department")

job_role_analysis = (
    df.groupby("Job_Role", dropna=False)
    .agg(
        Employee_Count=("Employee_ID", "nunique"),
        Average_Salary=("Monthly_Salary", "mean"),
        Total_Salary=("Monthly_Salary", "sum"),
        Average_Experience=("Experience_Years", "mean")
    )
    .reset_index()
    .sort_values("Employee_Count", ascending=False)
)

salary_analysis = (
    df.groupby("Department", dropna=False)
    .agg(
        Average_Salary=("Monthly_Salary", "mean"),
        Minimum_Salary=("Monthly_Salary", "min"),
        Maximum_Salary=("Monthly_Salary", "max"),
        Total_Salary=("Monthly_Salary", "sum")
    )
    .reset_index()
)

attrition_analysis = (
    df.groupby("Department", dropna=False)
    .agg(
        Employees=("Employee_ID", "nunique"),
        Attrition_Count=("Attrition", lambda values: values.str.casefold().eq("yes").sum())
    )
    .reset_index()
)
attrition_analysis["Attrition_Rate_%"] = np.where(
    attrition_analysis["Employees"].gt(0),
    attrition_analysis["Attrition_Count"] / attrition_analysis["Employees"] * 100,
    0
)

monthly_hr = (
    df.dropna(subset=["Month"])
    .groupby("Month")
    .agg(
        New_Joiners=("Employee_ID", "nunique"),
        Attrition_Records=("Attrition", lambda values: values.str.casefold().eq("yes").sum()),
        Monthly_Salary_Cost=("Monthly_Salary", "sum")
    )
    .reset_index()
    .sort_values("Month")
)

hr_kpi = pd.DataFrame([
    ["Total Employees", total_employees, "Unique employee IDs after exact duplicate removal"],
    ["Active Employees", active_employees, "Employees marked Active"],
    ["Average Age", df["Age"].mean(), "Mean age after documented imputation"],
    ["Average Experience (Years)", df["Experience_Years"].mean(), "Mean experience after department median imputation"],
    ["Average Monthly Salary", df["Monthly_Salary"].mean(), "Mean salary after department median imputation"],
    ["Total Monthly Salary Cost", df["Monthly_Salary"].sum(), "Sum of monthly salaries after imputation"],
    ["Attrition Count", attrition_count, "Records marked Yes"],
    ["Attrition Rate (%)", attrition_rate, "Attrition count divided by total unique employees"]
], columns=["KPI", "Value", "Description"])


# Quality checks and the exact records changed by imputation.
quality_rows = [
    ["Raw records", len(raw), "Source rows including duplicates"],
    ["Duplicate rows removed", int(raw.duplicated().sum()), "Exact duplicate rows"],
    ["Missing Age in source", int(pd.to_numeric(raw["Age"], errors="coerce").isna().sum()), "Filled with department median where available"],
    ["Missing Department in source", int(raw["Department"].isna().sum() + raw["Department"].astype("string").str.strip().eq("").sum()), "Kept as Unknown; not guessed"],
    ["Missing Experience in source", int(pd.to_numeric(raw["Experience_Years"], errors="coerce").isna().sum()), "Filled with department median where available"],
    ["Negative Experience in source", int(pd.to_numeric(raw["Experience_Years"], errors="coerce").lt(0).sum()), "Replaced with department median"],
    ["Missing Salary in source", int(pd.to_numeric(raw["Monthly_Salary"], errors="coerce").isna().sum()), "Filled with department median where available"],
    ["Age and experience conflicts", int(df["Age_Experience_Conflict"].sum()), "Flagged for review; not silently corrected"],
    ["Role and department issues", int(df["Role_Department_Check"].ne("OK").sum()), "Flagged using the role-to-department mapping"]
]
quality_check = pd.DataFrame(
    quality_rows,
    columns=["Check", "Result", "Action"]
)

imputation_log = pd.DataFrame(
    imputation_log,
    columns=["Employee_ID", "Column", "Original_Value", "Updated_Value", "Department", "Method"]
)

role_issues = df.loc[
    df["Role_Department_Check"].ne("OK"),
    ["Employee_ID", "Department", "Job_Role", "Expected_Department", "Role_Department_Check"]
].copy()

age_issues = df.loc[
    df["Age_Experience_Conflict"],
    ["Employee_ID", "Age", "Experience_Years", "Age_Experience_Conflict"]
].copy()


# Create business observations from the calculated results.
top_department = department_analysis.iloc[0] if not department_analysis.empty else None
highest_salary_department = (
    salary_analysis.loc[salary_analysis["Average_Salary"].idxmax()]
    if not salary_analysis.empty else None
)
highest_attrition_department = (
    attrition_analysis.loc[attrition_analysis["Attrition_Rate_%"].idxmax()]
    if not attrition_analysis.empty else None
)

insights = [
    ["Workforce", f"The dataset contains {total_employees} unique employees.", "Use this as the workforce count after duplicate removal."],
    ["Active Employees", f"{active_employees} employees are marked Active.", "Compare active headcount with the full employee list."],
    ["Department", f"{top_department['Department']} has the largest employee count." if top_department is not None else "No department data.", "Review staffing distribution across departments."],
    ["Salary", f"{highest_salary_department['Department']} has the highest average monthly salary." if highest_salary_department is not None else "No salary data.", "Check role mix and salary bands before drawing conclusions."],
    ["Attrition", f"{attrition_count} employees are marked for attrition ({attrition_rate:.2f}% of the workforce).", "Review exit reasons and time period before making retention decisions."],
    ["Department Attrition", f"{highest_attrition_department['Department']} has the highest department attrition rate." if highest_attrition_department is not None else "No attrition data.", "Small department counts can make rates move sharply."],
    ["Data Quality", f"{len(imputation_log)} values were imputed and {len(role_issues) + len(age_issues)} records were flagged for review.", "Keep the quality and imputation sheets with the analysis."]
]

final_analysis = [
    ["Workforce", f"{total_employees} unique employees after duplicate removal."],
    ["Active Employees", str(active_employees)],
    ["Average Age", round(df["Age"].mean(), 2)],
    ["Average Experience", round(df["Experience_Years"].mean(), 2)],
    ["Average Monthly Salary", round(df["Monthly_Salary"].mean(), 2)],
    ["Total Monthly Salary Cost", round(df["Monthly_Salary"].sum(), 2)],
    ["Attrition Count", int(attrition_count)],
    ["Attrition Rate", f"{attrition_rate:.2f}%"],
    ["Data Quality", f"{len(imputation_log)} imputed values; {len(role_issues)} role/department issues; {len(age_issues)} age/experience conflicts."],
    ["Limitation", "Age/experience and role/department flags need HR confirmation. The script does not invent corrected employee details."]
]


# Save supporting CSV files.
tables = {
    "cleaned_hr_data": df,
    "hr_summary": employee_summary,
    "department_analysis": department_analysis,
    "job_role_analysis": job_role_analysis,
    "salary_analysis": salary_analysis,
    "attrition_analysis": attrition_analysis,
    "monthly_hr_analysis": monthly_hr,
    "hr_kpi_summary": hr_kpi,
    "data_quality_check": quality_check,
    "imputation_log": imputation_log,
    "role_department_issues": role_issues,
    "age_experience_issues": age_issues,
    "hr_insights": pd.DataFrame(insights, columns=["Insight_Area", "Observation", "Business_Interpretation"])
}

for name, table in tables.items():
    table.to_csv(output_dir / f"{name}.csv", index=False)


# Create charts as PNG files too.
def save_bar(data, category, value, title, filename):
    plt.figure(figsize=(9, 5))
    plt.bar(data[category].astype(str), data[value])
    plt.title(title)
    plt.xlabel(category.replace("_", " "))
    plt.ylabel(value.replace("_", " "))
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output_dir / filename, dpi=200)
    plt.close()


save_bar(department_analysis, "Department", "Employee_Count",
         "Employee Count by Department", "employee_count_by_department.png")
save_bar(department_analysis, "Department", "Average_Salary",
         "Average Salary by Department", "salary_by_department.png")
save_bar(attrition_analysis, "Department", "Attrition_Count",
         "Attrition by Department", "attrition_by_department.png")

plt.figure(figsize=(10, 5))
plt.plot(monthly_hr["Month"], monthly_hr["New_Joiners"], marker="o")
plt.title("Monthly New Joiners")
plt.xlabel("Month")
plt.ylabel("New Joiners")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(output_dir / "monthly_hr_trend.png", dpi=200)
plt.close()


# Update the workbook while keeping the original raw data and instructions.
wb = openpyxl.load_workbook(source)

navy = "17365D"
pale = "EAF2F8"


def write_sheet(name, title, subtitle, headers, rows):
    if name in wb.sheetnames:
        ws = wb[name]
        for merged in list(ws.merged_cells.ranges):
            ws.unmerge_cells(str(merged))
        ws.delete_rows(1, ws.max_row)
        ws._charts = []
    else:
        ws = wb.create_sheet(name)

    ws.append([title])
    ws.append([subtitle])
    ws.append([])
    ws.append(list(headers))

    for row in rows:
        ws.append([
            None if pd.isna(value) else value
            for value in row
        ])

    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A5"
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(headers))
    ws["A1"].font = Font(bold=True, size=16, color="FFFFFF")
    ws["A1"].fill = PatternFill("solid", fgColor=navy)
    ws["A2"].font = Font(italic=True, color="666666")

    for cell in ws[4]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor=navy)
        cell.alignment = Alignment(wrap_text=True)

    for row in ws.iter_rows(min_row=5):
        for cell in row:
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            if cell.row % 2 == 0:
                cell.fill = PatternFill("solid", fgColor=pale)

    for col in range(1, len(headers) + 1):
        letter = get_column_letter(col)
        values = [
            len(str(ws.cell(r, col).value or ""))
            for r in range(4, ws.max_row + 1)
        ]
        ws.column_dimensions[letter].width = min(max(max(values, default=14) + 3, 14), 48)

    return ws


cleaned_rows = df.astype(object).where(pd.notna(df), None).itertuples(index=False, name=None)
write_sheet(
    "Cleaned_HR_Data", "Cleaned HR Data",
    "Department medians are used for missing or invalid numeric values. Flags remain visible for review.",
    list(df.columns), cleaned_rows
)

write_sheet(
    "Data_Quality_Check", "HR Data Quality Check",
    "Checks are based on the raw source and the cleaned employee records.",
    list(quality_check.columns), quality_check.itertuples(index=False, name=None)
)

write_sheet(
    "HR_Cleaning", "HR Data Cleaning",
    "Actions taken by the script. Unverified business conflicts are flagged, not guessed.",
    ["Issue", "Action"],
    [
        ["Text formatting", "Trim extra spaces and standardise department and job-role names."],
        ["Acronyms", "Keep HR and IT uppercase."],
        ["Missing Age", "Use department median; overall median only when a department median is unavailable."],
        ["Missing Salary", "Use department median; overall median only when a department median is unavailable."],
        ["Missing Experience", "Use department median; overall median only when a department median is unavailable."],
        ["Negative Experience", "Treat as invalid and replace using department median."],
        ["Age and Experience", "Flag experience above age minus 18 for HR review."],
        ["Role and Department", "Compare job role with the expected department and flag missing or mismatched values."],
        ["Missing Department", "Keep as Unknown instead of assigning an unsupported department."],
        ["Duplicates", "Remove exact duplicate rows."]
    ]
)

write_sheet(
    "Employee_Summary", "Employee Summary",
    "Workforce measures after cleaning and exact duplicate removal.",
    ["Metric", "Value"], employee_summary.itertuples(index=False, name=None)
)

for sheet, title, frame in [
    ("Department_Analysis", "Department Analysis", department_analysis),
    ("Job_Role_Analysis", "Job Role Analysis", job_role_analysis),
    ("Salary_Analysis", "Salary Analysis", salary_analysis),
    ("Attrition_Analysis", "Attrition Analysis", attrition_analysis),
    ("Monthly_HR", "Monthly HR Analysis", monthly_hr)
]:
    write_sheet(
        sheet, title, "Calculated from the cleaned employee records.",
        list(frame.columns), frame.itertuples(index=False, name=None)
    )

write_sheet(
    "HR_KPI", "HR KPI Summary",
    "Core workforce and attrition measures.",
    list(hr_kpi.columns), hr_kpi.itertuples(index=False, name=None)
)

write_sheet(
    "Pivot_Department", "Department Summary",
    "Department-level workforce summary.",
    list(department_analysis.columns),
    department_analysis.itertuples(index=False, name=None)
)

write_sheet(
    "Pivot_Role", "Job Role Summary",
    "Job-role workforce summary.",
    list(job_role_analysis.columns),
    job_role_analysis.itertuples(index=False, name=None)
)

write_sheet(
    "HR_Insights", "HR Business Insights",
    "Observations are calculated from this practice dataset.",
    ["Insight Area", "Observation", "Business Interpretation"], insights
)

write_sheet(
    "Final_HR_Analysis", "Final HR Analysis",
    "Summary of the HR analysis and its data limitations.",
    ["Section", "Finding"], final_analysis
)

write_sheet(
    "Imputation_Log", "Imputation Log",
    "Every filled or corrected numeric value is recorded here.",
    list(imputation_log.columns),
    imputation_log.itertuples(index=False, name=None)
)

write_sheet(
    "Role_Department_Issues", "Role and Department Checks",
    "Records that need review based on the role-to-department mapping.",
    list(role_issues.columns),
    role_issues.itertuples(index=False, name=None)
)

write_sheet(
    "Age_Experience_Issues", "Age and Experience Checks",
    "Records with experience above age minus 18 are flagged for review.",
    list(age_issues.columns),
    age_issues.itertuples(index=False, name=None)
)


# Chart data and charts inside Excel.
chart_data = wb["Chart_Data"]
for merged in list(chart_data.merged_cells.ranges):
    chart_data.unmerge_cells(str(merged))
chart_data.delete_rows(1, chart_data.max_row)

chart_sections = [
    ("Employee Count", department_analysis, "Department", "Employee_Count"),
    ("Average Salary", department_analysis, "Department", "Average_Salary"),
    ("Attrition Count", attrition_analysis, "Department", "Attrition_Count"),
    ("Monthly New Joiners", monthly_hr, "Month", "New_Joiners")
]

chart_ranges = {}
for title, frame, category, value in chart_sections:
    chart_data.append([title])
    chart_data.append([category, value])
    start = chart_data.max_row
    for row in frame[[category, value]].itertuples(index=False, name=None):
        chart_data.append(list(row))
    chart_ranges[title] = (start, chart_data.max_row)
    chart_data.append([])

charts = wb["Charts"]
for merged in list(charts.merged_cells.ranges):
    charts.unmerge_cells(str(merged))
charts.delete_rows(1, charts.max_row)
charts._charts = []
charts["A1"] = "HR Analytics Dashboard"
charts["A1"].font = Font(bold=True, size=18, color="FFFFFF")
charts["A1"].fill = PatternFill("solid", fgColor=navy)
charts["A2"] = "Workforce, salary, attrition and joining trends"


def add_excel_chart(title, section, position, line=False):
    start, end = chart_ranges[section]
    chart = LineChart() if line else BarChart()
    if not line:
        chart.type = "col"
        chart.style = 10
    chart.title = title
    chart.height = 8
    chart.width = 15
    chart.add_data(
        Reference(chart_data, min_col=2, min_row=start, max_row=end),
        titles_from_data=True
    )
    chart.set_categories(
        Reference(chart_data, min_col=1, min_row=start + 1, max_row=end)
    )
    charts.add_chart(chart, position)


add_excel_chart("Employee Count by Department", "Employee Count", "A4")
add_excel_chart("Average Salary by Department", "Average Salary", "J4")
add_excel_chart("Attrition Count by Department", "Attrition Count", "A20")
add_excel_chart("Monthly New Joiners", "Monthly New Joiners", "J20", line=True)

# Save the completed workbook.
wb.save(output)

print("HR analysis completed.")
print("Workbook:", output)
print("Output folder:", output_dir)
print("Employees:", total_employees)
print("Total monthly salary cost:", round(df["Monthly_Salary"].sum(), 2))
print("Attrition rate:", round(attrition_rate, 2), "%")
print("Values imputed:", len(imputation_log))
print("Role/department issues:", len(role_issues))
print("Age/experience conflicts:", len(age_issues))
