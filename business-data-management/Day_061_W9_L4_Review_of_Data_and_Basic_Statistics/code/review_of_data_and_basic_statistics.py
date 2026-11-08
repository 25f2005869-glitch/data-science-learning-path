from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 061
# Topic: Review of Data and Basic Statistics

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_061_W9_L4_Review_of_Data_and_Basic_Statistics.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="Data_Review", header=2)

df["Time_Variance_Days"] = df["Actual_Days"] - df["Planned_Days"]
df["Cost_per_Day"] = df["Internal_Cost"] / df["Actual_Days"]
df["On_Time_Flag"] = (df["Actual_Days"] <= df["Planned_Days"]).astype(int)

numeric_cols = [
    "Internal_Cost",
    "Planned_Days",
    "Actual_Days",
    "Internal_Satisfaction",
    "Time_Variance_Days",
    "Cost_per_Day",
]

rows = []
for col in numeric_cols:
    s = df[col]
    rows.append({
        "Metric": col,
        "Count": s.count(),
        "Mean": s.mean(),
        "Median": s.median(),
        "Std_Dev": s.std(),
        "Minimum": s.min(),
        "Maximum": s.max(),
        "Range": s.max() - s.min(),
        "Q1": s.quantile(0.25),
        "Q3": s.quantile(0.75),
        "IQR": s.quantile(0.75) - s.quantile(0.25),
        "Sum": s.sum(),
    })

stats = pd.DataFrame(rows)

department = df.groupby("Department", as_index=False).agg(
    Requests=("Request_ID", "count"),
    Total_Cost=("Internal_Cost", "sum"),
    Avg_Cost=("Internal_Cost", "mean"),
    Avg_Actual_Days=("Actual_Days", "mean"),
    Avg_Satisfaction=("Internal_Satisfaction", "mean"),
    Completed=("Completed_Flag", "sum"),
)

region = df.groupby("Region", as_index=False).agg(
    Requests=("Request_ID", "count"),
    Total_Cost=("Internal_Cost", "sum"),
    Avg_Cost=("Internal_Cost", "mean"),
    Avg_Actual_Days=("Actual_Days", "mean"),
    Avg_Satisfaction=("Internal_Satisfaction", "mean"),
)

source = df.groupby("Internal_Source", as_index=False).agg(
    Requests=("Request_ID", "count"),
    Total_Cost=("Internal_Cost", "sum"),
    Avg_Cost=("Internal_Cost", "mean"),
    Avg_Actual_Days=("Actual_Days", "mean"),
    Avg_Satisfaction=("Internal_Satisfaction", "mean"),
)

monthly = df.groupby("Month", as_index=False).agg(
    Requests=("Request_ID", "count"),
    Total_Cost=("Internal_Cost", "sum"),
    Avg_Actual_Days=("Actual_Days", "mean"),
    Avg_Satisfaction=("Internal_Satisfaction", "mean"),
)

stats.to_csv(OUTPUT_DIR / "basic_statistics.csv", index=False)
department.to_csv(OUTPUT_DIR / "department_basic_statistics.csv", index=False)
region.to_csv(OUTPUT_DIR / "region_basic_statistics.csv", index=False)
source.to_csv(OUTPUT_DIR / "source_basic_statistics.csv", index=False)
monthly.to_csv(OUTPUT_DIR / "monthly_basic_statistics.csv", index=False)

# Chart 1
plt.figure(figsize=(9, 5))
plt.bar(department["Department"], department["Requests"], color="#4472C4")
plt.title("Requests by Department")
plt.xlabel("Department")
plt.ylabel("Requests")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "requests_by_department.png", dpi=160)
plt.close()

# Chart 2
plt.figure(figsize=(8, 5))
plt.bar(
    ["Mean", "Median"],
    [df["Internal_Cost"].mean(), df["Internal_Cost"].median()],
    color="#ED7D31"
)
plt.title("Mean vs Median Internal Cost")
plt.ylabel("Internal Cost")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "mean_vs_median_cost.png", dpi=160)
plt.close()

# Chart 3
plt.figure(figsize=(10, 5))
plt.bar(
    source["Internal_Source"],
    source["Avg_Actual_Days"],
    color="#70AD47"
)
plt.title("Average Actual Days by Internal Source")
plt.xlabel("Internal Source")
plt.ylabel("Average Actual Days")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "average_actual_days_by_source.png", dpi=160)
plt.close()

# Chart 4
plt.figure(figsize=(9, 5))
plt.plot(
    monthly["Month"],
    monthly["Total_Cost"],
    marker="o",
    color="#8064A2",
    linewidth=2
)
plt.title("Monthly Internal Cost")
plt.xlabel("Month")
plt.ylabel("Internal Cost")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_internal_cost.png", dpi=160)
plt.close()

print("Day 061 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")