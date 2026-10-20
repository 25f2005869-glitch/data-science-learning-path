from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# Day 089 — W12 L2 — How Businesses are Managed
# --------------------------------------------------

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 089
# Topic: How Businesses are Managed


CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

EXCEL_FILE = (
    BASE_DIR
    / "Day_089_W12_L2_How_Businesses_are_Managed.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 1. Read Excel Dataset
# --------------------------------------------------

df = pd.read_excel(
    EXCEL_FILE,
    sheet_name="Management_Data",
    header=2
)


# --------------------------------------------------
# 2. Calculate Management KPIs
# --------------------------------------------------

df["Target_Achievement_%"] = (
    df["Actual_Rupee"]
    / df["Target_Rupee"]
    * 100
)

df["Budget_Utilisation_%"] = (
    df["Actual_Cost_Rupee"]
    / df["Budget_Rupee"]
    * 100
)

df["Task_Completion_%"] = (
    df["Tasks_Completed"]
    / df["Tasks_Planned"]
    * 100
)

df["Cost_Variance_Rupee"] = (
    df["Actual_Cost_Rupee"]
    - df["Budget_Rupee"]
)


# --------------------------------------------------
# 3. Business Function Summary
# --------------------------------------------------

function_summary = (
    df.groupby("Business_Function")
    .agg(
        Team_Size_Avg=("Team_Size", "mean"),
        Target_Rupee=("Target_Rupee", "sum"),
        Actual_Rupee=("Actual_Rupee", "sum"),
        Budget_Rupee=("Budget_Rupee", "sum"),
        Actual_Cost_Rupee=("Actual_Cost_Rupee", "sum"),
        Tasks_Planned=("Tasks_Planned", "sum"),
        Tasks_Completed=("Tasks_Completed", "sum"),
        Issues_Resolved=("Issues_Resolved", "sum"),
        Customer_Satisfaction_pct=(
            "Customer_Satisfaction_%",
            "mean"
        ),
    )
    .reset_index()
)

function_summary["Target_Achievement_%"] = (
    function_summary["Actual_Rupee"]
    / function_summary["Target_Rupee"]
    * 100
)

function_summary["Budget_Utilisation_%"] = (
    function_summary["Actual_Cost_Rupee"]
    / function_summary["Budget_Rupee"]
    * 100
)

function_summary["Task_Completion_%"] = (
    function_summary["Tasks_Completed"]
    / function_summary["Tasks_Planned"]
    * 100
)


# --------------------------------------------------
# 4. Monthly Summary
# --------------------------------------------------

monthly_summary = (
    df.groupby("Month")
    .agg(
        Target_Rupee=("Target_Rupee", "sum"),
        Actual_Rupee=("Actual_Rupee", "sum"),
        Budget_Rupee=("Budget_Rupee", "sum"),
        Actual_Cost_Rupee=("Actual_Cost_Rupee", "sum"),
        Tasks_Planned=("Tasks_Planned", "sum"),
        Tasks_Completed=("Tasks_Completed", "sum"),
        Customer_Satisfaction_pct=(
            "Customer_Satisfaction_%",
            "mean"
        ),
    )
    .reset_index()
)

monthly_summary["Target_Achievement_%"] = (
    monthly_summary["Actual_Rupee"]
    / monthly_summary["Target_Rupee"]
    * 100
)

monthly_summary["Budget_Utilisation_%"] = (
    monthly_summary["Actual_Cost_Rupee"]
    / monthly_summary["Budget_Rupee"]
    * 100
)

monthly_summary["Task_Completion_%"] = (
    monthly_summary["Tasks_Completed"]
    / monthly_summary["Tasks_Planned"]
    * 100
)


# --------------------------------------------------
# 5. Overall KPIs
# --------------------------------------------------

total_target = df["Target_Rupee"].sum()
total_actual = df["Actual_Rupee"].sum()

total_budget = df["Budget_Rupee"].sum()
total_actual_cost = df["Actual_Cost_Rupee"].sum()

total_tasks_planned = df["Tasks_Planned"].sum()
total_tasks_completed = df["Tasks_Completed"].sum()

average_satisfaction = (
    df["Customer_Satisfaction_%"].mean()
)

target_achievement = (
    total_actual
    / total_target
    * 100
)

budget_utilisation = (
    total_actual_cost
    / total_budget
    * 100
)

task_completion = (
    total_tasks_completed
    / total_tasks_planned
    * 100
)

cost_variance = (
    total_actual_cost
    - total_budget
)


kpis = pd.DataFrame(
    {
        "KPI": [
            "Total Target (Rupee)",
            "Total Actual (Rupee)",
            "Total Budget (Rupee)",
            "Total Actual Cost (Rupee)",
            "Target Achievement (%)",
            "Budget Utilisation (%)",
            "Task Completion (%)",
            "Average Customer Satisfaction (%)",
            "Cost Variance (Rupee)",
        ],
        "Value": [
            total_target,
            total_actual,
            total_budget,
            total_actual_cost,
            target_achievement,
            budget_utilisation,
            task_completion,
            average_satisfaction,
            cost_variance,
        ],
    }
)


# --------------------------------------------------
# 6. Export CSV Files
# --------------------------------------------------

function_summary.to_csv(
    OUTPUT_DIR / "function_summary.csv",
    index=False
)

monthly_summary.to_csv(
    OUTPUT_DIR / "monthly_management_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "management_kpi_summary.csv",
    index=False
)


# --------------------------------------------------
# 7. Actual Performance by Function
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    function_summary["Business_Function"],
    function_summary["Actual_Rupee"]
)

plt.title("Actual Performance by Business Function")
plt.xlabel("Business Function")
plt.ylabel("Actual Value (Rupee)")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "actual_performance_by_function.png",
    dpi=150
)

plt.close()


# --------------------------------------------------
# 8. Target vs Actual
# --------------------------------------------------

x = range(len(function_summary))
width = 0.35

plt.figure(figsize=(10, 5))

plt.bar(
    [i - width / 2 for i in x],
    function_summary["Target_Rupee"],
    width=width,
    label="Target"
)

plt.bar(
    [i + width / 2 for i in x],
    function_summary["Actual_Rupee"],
    width=width,
    label="Actual"
)

plt.title("Target vs Actual by Business Function")
plt.xlabel("Business Function")
plt.ylabel("Rupee")

plt.xticks(
    list(x),
    function_summary["Business_Function"],
    rotation=30,
    ha="right"
)

plt.legend()
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "target_vs_actual.png",
    dpi=150
)

plt.close()


# --------------------------------------------------
# 9. Task Completion by Function
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    function_summary["Business_Function"],
    function_summary["Task_Completion_%"]
)

plt.title("Task Completion by Business Function")
plt.xlabel("Business Function")
plt.ylabel("Task Completion (%)")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "task_completion_by_function.png",
    dpi=150
)

plt.close()


# --------------------------------------------------
# 10. Print Results
# --------------------------------------------------

print("Day 089 analysis completed.")

print(f"Total Target: ₹{total_target:,.0f}")
print(f"Total Actual: ₹{total_actual:,.0f}")
print(f"Total Budget: ₹{total_budget:,.0f}")
print(f"Total Actual Cost: ₹{total_actual_cost:,.0f}")

print(
    f"Target Achievement: "
    f"{target_achievement:.2f}%"
)

print(
    f"Budget Utilisation: "
    f"{budget_utilisation:.2f}%"
)

print(
    f"Task Completion: "
    f"{task_completion:.2f}%"
)

print(
    f"Average Customer Satisfaction: "
    f"{average_satisfaction:.2f}%"
)

print(
    f"Cost Variance: "
    f"₹{cost_variance:,.0f}"
)

print("Outputs saved in:")
print(OUTPUT_DIR)