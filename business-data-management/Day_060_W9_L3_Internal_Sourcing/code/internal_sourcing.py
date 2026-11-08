from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 060
# Topic: Internal Sourcing

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_060_W9_L3_Internal_Sourcing.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="Internal_Sourcing_Data", header=2)

df["Time_Variance_Days"] = df["Actual_Days"] - df["Planned_Days"]
df["On_Time_Flag"] = (df["Actual_Days"] <= df["Planned_Days"]).astype(int)
df["Cost_per_Day"] = df["Internal_Cost"] / df["Actual_Days"]

department = (
    df.groupby("Department", as_index=False)
    .agg(
        Requests=("Request_ID", "count"),
        Total_Cost=("Internal_Cost", "sum"),
        Avg_Cost=("Internal_Cost", "mean"),
        Avg_Planned_Days=("Planned_Days", "mean"),
        Avg_Actual_Days=("Actual_Days", "mean"),
        Avg_Satisfaction=("Internal_Satisfaction", "mean"),
        Completed=("Completed_Flag", "sum"),
        On_Time=("On_Time_Flag", "sum"),
    )
)
department["Completion_Rate_%"] = department["Completed"] / department["Requests"] * 100
department["On_Time_Rate_%"] = department["On_Time"] / department["Requests"] * 100
department["Avg_Time_Variance_Days"] = (
    department["Avg_Actual_Days"] - department["Avg_Planned_Days"]
)

source = (
    df.groupby("Internal_Source", as_index=False)
    .agg(
        Requests=("Request_ID", "count"),
        Total_Cost=("Internal_Cost", "sum"),
        Avg_Cost=("Internal_Cost", "mean"),
        Avg_Actual_Days=("Actual_Days", "mean"),
        Avg_Satisfaction=("Internal_Satisfaction", "mean"),
        Completed=("Completed_Flag", "sum"),
    )
)
source["Completion_Rate_%"] = source["Completed"] / source["Requests"] * 100

region = (
    df.groupby("Region", as_index=False)
    .agg(
        Requests=("Request_ID", "count"),
        Total_Cost=("Internal_Cost", "sum"),
        Avg_Cost=("Internal_Cost", "mean"),
        Avg_Satisfaction=("Internal_Satisfaction", "mean"),
        Completed=("Completed_Flag", "sum"),
    )
)
region["Completion_Rate_%"] = region["Completed"] / region["Requests"] * 100

monthly = (
    df.groupby("Month", sort=False, as_index=False)
    .agg(
        Requests=("Request_ID", "count"),
        Total_Cost=("Internal_Cost", "sum"),
        Avg_Actual_Days=("Actual_Days", "mean"),
        Avg_Satisfaction=("Internal_Satisfaction", "mean"),
        Completed=("Completed_Flag", "sum"),
    )
)
monthly["Completion_Rate_%"] = monthly["Completed"] / monthly["Requests"] * 100

kpis = pd.DataFrame({
    "Metric": [
        "Total Internal Requests",
        "Total Internal Cost",
        "Average Request Cost",
        "Average Actual Days",
        "Average Satisfaction",
        "Completed Requests",
        "Completion Rate %",
        "On-Time Rate %",
    ],
    "Value": [
        len(df),
        df["Internal_Cost"].sum(),
        df["Internal_Cost"].mean(),
        df["Actual_Days"].mean(),
        df["Internal_Satisfaction"].mean(),
        df["Completed_Flag"].sum(),
        df["Completed_Flag"].mean() * 100,
        df["On_Time_Flag"].mean() * 100,
    ],
})

department.to_csv(OUTPUT_DIR / "department_internal_sourcing.csv", index=False)
source.to_csv(OUTPUT_DIR / "internal_source_summary.csv", index=False)
region.to_csv(OUTPUT_DIR / "region_internal_sourcing.csv", index=False)
monthly.to_csv(OUTPUT_DIR / "monthly_internal_sourcing.csv", index=False)
kpis.to_csv(OUTPUT_DIR / "internal_sourcing_kpis.csv", index=False)

plt.figure(figsize=(9, 5))
plt.bar(department["Department"], department["Requests"], color="#4472C4")
plt.title("Internal Requests by Department")
plt.xlabel("Department")
plt.ylabel("Requests")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "internal_requests_by_department.png", dpi=160)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(department["Department"], department["Total_Cost"], color="#ED7D31")
plt.title("Internal Cost by Department")
plt.xlabel("Department")
plt.ylabel("Internal Cost")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "internal_cost_by_department.png", dpi=160)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(source["Internal_Source"], source["Avg_Actual_Days"], color="#70AD47")
plt.title("Average Actual Days by Internal Source")
plt.xlabel("Internal Source")
plt.ylabel("Average Actual Days")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "average_actual_days_by_internal_source.png", dpi=160)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(department["Department"], department["Avg_Satisfaction"], color="#8064A2")
plt.title("Average Satisfaction by Department")
plt.xlabel("Department")
plt.ylabel("Satisfaction Score")
plt.ylim(0, 5)
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "average_satisfaction_by_department.png", dpi=160)
plt.close()

print("Day 060 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output folder: {OUTPUT_DIR}")