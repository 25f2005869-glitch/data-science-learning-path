from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 050
# Topic: OEE Discussion
# ============================================================


# ------------------------------------------------------------
# 1. Paths
# ------------------------------------------------------------

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_050_W8_L3_OEE_Discussion.xlsx"

OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


# ------------------------------------------------------------
# 2. Read Excel data
# ------------------------------------------------------------

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="OEE_Data"
)


# ------------------------------------------------------------
# 3. Calculate ideal output
# ------------------------------------------------------------

df["Ideal_Output"] = (
    df["Run_Time_Min"]
    * 60
    / df["Ideal_Cycle_Time_Sec"]
)


# ------------------------------------------------------------
# 4. Product-level OEE
# ------------------------------------------------------------

product = (
    df.groupby("Product", as_index=False)
    .agg(
        Planned_Time_Min=("Planned_Time_Min", "sum"),
        Run_Time_Min=("Run_Time_Min", "sum"),
        Total_Count=("Total_Count", "sum"),
        Good_Count=("Good_Count", "sum"),
        Ideal_Output=("Ideal_Output", "sum")
    )
)

product["Availability"] = (
    product["Run_Time_Min"]
    / product["Planned_Time_Min"]
)

product["Performance"] = (
    product["Total_Count"]
    / product["Ideal_Output"]
)

product["Quality"] = (
    product["Good_Count"]
    / product["Total_Count"]
)

product["OEE"] = (
    product["Availability"]
    * product["Performance"]
    * product["Quality"]
)


# ------------------------------------------------------------
# 5. Monthly OEE
# ------------------------------------------------------------

monthly = (
    df.groupby("Month", as_index=False)
    .agg(
        Planned_Time_Min=("Planned_Time_Min", "sum"),
        Run_Time_Min=("Run_Time_Min", "sum"),
        Total_Count=("Total_Count", "sum"),
        Good_Count=("Good_Count", "sum"),
        Ideal_Output=("Ideal_Output", "sum")
    )
)

monthly["Availability"] = (
    monthly["Run_Time_Min"]
    / monthly["Planned_Time_Min"]
)

monthly["Performance"] = (
    monthly["Total_Count"]
    / monthly["Ideal_Output"]
)

monthly["Quality"] = (
    monthly["Good_Count"]
    / monthly["Total_Count"]
)

monthly["OEE"] = (
    monthly["Availability"]
    * monthly["Performance"]
    * monthly["Quality"]
)


# ------------------------------------------------------------
# 6. Regional OEE
# ------------------------------------------------------------

region = (
    df.groupby("Region", as_index=False)
    .agg(
        Planned_Time_Min=("Planned_Time_Min", "sum"),
        Run_Time_Min=("Run_Time_Min", "sum"),
        Total_Count=("Total_Count", "sum"),
        Good_Count=("Good_Count", "sum"),
        Ideal_Output=("Ideal_Output", "sum")
    )
)

region["Availability"] = (
    region["Run_Time_Min"]
    / region["Planned_Time_Min"]
)

region["Performance"] = (
    region["Total_Count"]
    / region["Ideal_Output"]
)

region["Quality"] = (
    region["Good_Count"]
    / region["Total_Count"]
)

region["OEE"] = (
    region["Availability"]
    * region["Performance"]
    * region["Quality"]
)


# ------------------------------------------------------------
# 7. Product-region OEE
# ------------------------------------------------------------

product_region = (
    df.groupby(
        ["Product", "Region"],
        as_index=False
    )
    .agg(
        Planned_Time_Min=("Planned_Time_Min", "sum"),
        Run_Time_Min=("Run_Time_Min", "sum"),
        Total_Count=("Total_Count", "sum"),
        Good_Count=("Good_Count", "sum"),
        Ideal_Output=("Ideal_Output", "sum")
    )
)

product_region["Availability"] = (
    product_region["Run_Time_Min"]
    / product_region["Planned_Time_Min"]
)

product_region["Performance"] = (
    product_region["Total_Count"]
    / product_region["Ideal_Output"]
)

product_region["Quality"] = (
    product_region["Good_Count"]
    / product_region["Total_Count"]
)

product_region["OEE"] = (
    product_region["Availability"]
    * product_region["Performance"]
    * product_region["Quality"]
)


# ------------------------------------------------------------
# 8. Export CSV files
# ------------------------------------------------------------

product.to_csv(
    OUTPUT_DIR / "oee_product_summary.csv",
    index=False
)

monthly.to_csv(
    OUTPUT_DIR / "oee_monthly.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "oee_region.csv",
    index=False
)

product_region.to_csv(
    OUTPUT_DIR / "oee_product_region.csv",
    index=False
)


# ------------------------------------------------------------
# 9. Chart — OEE by Product
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    product["Product"],
    product["OEE"],
    color="#4472C4"
)

plt.title("OEE by Product")
plt.xlabel("Product")
plt.ylabel("OEE")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "oee_by_product.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 10. Chart — Monthly OEE
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    monthly["Month"],
    monthly["OEE"],
    marker="o",
    color="#ED7D31"
)

plt.title("Monthly OEE Trend")
plt.xlabel("Month")
plt.ylabel("OEE")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_oee_trend.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 11. Chart — OEE Components
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

x = range(len(product))
width = 0.25

plt.bar(
    [value - width for value in x],
    product["Availability"],
    width=width,
    label="Availability",
    color="#70AD47"
)

plt.bar(
    x,
    product["Performance"],
    width=width,
    label="Performance",
    color="#8064A2"
)

plt.bar(
    [value + width for value in x],
    product["Quality"],
    width=width,
    label="Quality",
    color="#5B9BD5"
)

plt.xticks(
    list(x),
    product["Product"]
)

plt.title("OEE Components by Product")
plt.xlabel("Product")
plt.ylabel("Rate")
plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "oee_components_by_product.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 12. Chart — OEE by Region
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    region["Region"],
    region["OEE"],
    color="#A5A5A5"
)

plt.title("OEE by Region")
plt.xlabel("Region")
plt.ylabel("OEE")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "oee_by_region.png",
    dpi=160
)

plt.close()


# ------------------------------------------------------------
# 13. Overall OEE
# ------------------------------------------------------------

overall_availability = (
    df["Run_Time_Min"].sum()
    / df["Planned_Time_Min"].sum()
)

overall_quality = (
    df["Good_Count"].sum()
    / df["Total_Count"].sum()
)

overall_performance = (
    df["Total_Count"].sum()
    / df["Ideal_Output"].sum()
)

overall_oee = (
    overall_availability
    * overall_performance
    * overall_quality
)


# ------------------------------------------------------------
# 14. Console output
# ------------------------------------------------------------

print("=" * 60)
print("DAY 050 — OEE DISCUSSION")
print("=" * 60)

print(f"Availability : {overall_availability:.2%}")
print(f"Performance  : {overall_performance:.2%}")
print(f"Quality      : {overall_quality:.2%}")
print(f"OEE          : {overall_oee:.2%}")

print("\nPRODUCT OEE")
print(product)

print("\nMONTHLY OEE")
print(monthly)

print("\nREGION OEE")
print(region)

print("\nAnalysis completed successfully.")