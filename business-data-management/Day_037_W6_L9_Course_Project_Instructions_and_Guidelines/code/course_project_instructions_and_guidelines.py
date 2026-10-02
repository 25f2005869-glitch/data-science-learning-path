from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

files = list(BASE_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError("No Day 037 Excel workbook found.")

xlsx_path = files[0]

checklist = pd.read_excel(
    xlsx_path,
    sheet_name="Project_Checklist"
)

quality = pd.read_excel(
    xlsx_path,
    sheet_name="Data_Quality"
)

kpis = pd.read_excel(
    xlsx_path,
    sheet_name="KPI_Framework"
)

analysis_plan = pd.read_excel(
    xlsx_path,
    sheet_name="Analysis_Plan"
)

# Project readiness summary
status_summary = (
    checklist
    .groupby("Status", as_index=False)
    .size()
    .rename(columns={"size": "Count"})
)

status_summary.to_csv(
    BASE_DIR / "project_status_summary.csv",
    index=False
)

# Export planning tables
quality.to_csv(
    BASE_DIR / "data_quality_checklist.csv",
    index=False
)

kpis.to_csv(
    BASE_DIR / "kpi_framework.csv",
    index=False
)

analysis_plan.to_csv(
    BASE_DIR / "analysis_plan.csv",
    index=False
)

# Project workload visualization
phase_counts = pd.DataFrame({
    "Phase": [
        "Planning",
        "Data",
        "Analysis",
        "Visualization",
        "Communication",
        "Review"
    ],
    "Tasks": [2, 3, 3, 1, 2, 1]
})

plt.figure(figsize=(9, 5))

plt.bar(
    phase_counts["Phase"],
    phase_counts["Tasks"],
    color="#4472C4"
)

plt.title("BDM Project Workload by Phase")
plt.xlabel("Phase")
plt.ylabel("Task Count")
plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    BASE_DIR / "project_workload_by_phase.png",
    dpi=160
)

plt.close()

print("Day 037 project planning analysis completed.")
print(status_summary)