from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 048
# Topic: Production Scheduling Data — Plans vs Actual
# ============================================================


# ------------------------------------------------------------
# 1. Paths
# ------------------------------------------------------------

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_048_W8_L1_Production_Scheduling_Data_Plans_vs_Actual.xlsx"
)

OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


# ------------------------------------------------------------
# 2. Read Excel data
# ------------------------------------------------------------

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Production_Scheduling_Data"
)


# ------------------------------------------------------------
# 3. Product-level analysis
# ------------------------------------------------------------

product_summary = (
    df.groupby("Product", as_index=False)
    .agg(
        Planned_Production=("Planned_Production", "sum"),
        Actual_Production=("Actual_Production", "sum")
    )
)

product_summary["Variance_Units"] = (
    product_summary["Actual_Production"]
    - product_summary["Planned_Production"]
)

product_summary["Variance_%"] = (
    product_summary["Variance_Units"]
    / product_summary["Planned_Production"]
)

product_summary["Plan_Achievement_%"] = (
    product_summary["Actual_Production"]
    / product_summary["Planned_Production"]
)


# ------------------------------------------------------------
# 4. Monthly analysis
# ------------------------------------------------------------

monthly = (
    df.groupby("Month", as_index=False)
    .agg(
        Planned_Production=("Planned_Production", "sum"),
        Actual_Production=("Actual_Production", "sum")
    )
)

monthly["Variance_Units"] = (
    monthly["Actual_Production"]
    - monthly["Planned_Production"]
)

monthly["Plan_Achievement_%"] = (
    monthly["Actual_Production"]
    / monthly["Planned_Production"]
)


# ------------------------------------------------------------
# 5. Product-region variance analysis
# ------------------------------------------------------------

variance = (
    df.groupby(
        ["Product", "Region"],
        as_index=False
    )
    .agg(
        Planned_Production=("Planned_Production", "sum"),
        Actual_Production=("Actual_Production", "sum")
    )
)

variance["Variance_Units"] = (
    variance["Actual_Production"]
    - variance["Planned_Production"]
)

variance["Variance_%"] = (
    variance["Variance_Units"]
    / variance["Planned_Production"]
)

variance["Plan_Achievement_%"] = (
    variance["Actual_Production"]
    / variance["Planned_Production"]
)


# ------------------------------------------------------------
# 6. Export analysis tables
# ------------------------------------------------------------

product_summary.to_csv(
    OUTPUT_DIR / "product_summary.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "monthly_production.csv",
    index=False
)

variance.to_csv(
    OUTPUT_DIR / "variance_analysis.csv",
    index=False
)


# ------------------------------------------------------------
# 7. Chart — Planned vs Actual Production
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

x = range(len(product_summary))
width = 0.35

plt.bar(
    [value - width / 2 for value in x],
    product_summary["Planned_Production"],
    width=width,
    label="Planned",
    color="#4472C4"
)

plt.bar(
    [value + width / 2 for value in x],
    product_summary["Actual_Production"],
    width=width,
    label="Actual",
    color="#ED7D31"
)

plt.xticks(
    list(x),
    product_summary["Product"]
)

plt.title("Planned vs Actual Production")
plt.xlabel("Product")
plt.ylabel("Production Units")
plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "planned_vs_actual_production.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 8. Chart — Monthly Planned vs Actual
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    monthly["Month"],
    monthly["Planned_Production"],
    marker="o",
    label="Planned",
    color="#4472C4"
)

plt.plot(
    monthly["Month"],
    monthly["Actual_Production"],
    marker="o",
    label="Actual",
    color="#ED7D31"
)

plt.title("Monthly Planned vs Actual Production")
plt.xlabel("Month")
plt.ylabel("Production Units")
plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_planned_vs_actual.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 9. Chart — Production Variance
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    product_summary["Product"],
    product_summary["Variance_Units"],
    color="#70AD47"
)

plt.axhline(
    0,
    linewidth=1
)

plt.title("Production Variance by Product")
plt.xlabel("Product")
plt.ylabel("Variance Units")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "production_variance_by_product.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 10. Chart — Plan Achievement
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.bar(
    monthly["Month"],
    monthly["Plan_Achievement_%"],
    color="#8064A2"
)

plt.title("Plan Achievement by Month")
plt.xlabel("Month")
plt.ylabel("Plan Achievement %")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "plan_achievement_by_month.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 11. Overall metrics
# ------------------------------------------------------------

total_planned = df["Planned_Production"].sum()

total_actual = df["Actual_Production"].sum()

total_variance = total_actual - total_planned

overall_achievement = (
    total_actual / total_planned
)


# ------------------------------------------------------------
# 12. Console output
# ------------------------------------------------------------

print("=" * 60)
print("DAY 048 — PRODUCTION SCHEDULING ANALYSIS")
print("=" * 60)

print(f"Total Planned Production : {total_planned:,.0f}")
print(f"Total Actual Production  : {total_actual:,.0f}")
print(f"Total Variance            : {total_variance:,.0f}")
print(
    f"Overall Plan Achievement  : "
    f"{overall_achievement:.2%}"
)

print("\nPRODUCT SUMMARY")
print(product_summary)

print("\nMONTHLY PRODUCTION")
print(monthly)

print("\nVARIANCE ANALYSIS")
print(variance)

print("\nAnalysis completed successfully.")