from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 075
# Topic: Nudge Economics — Consumer Behavior in E-Commerce

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_075_W10_L4_Nudge_Economics_Consumer_Behavior_in_E_Commerce.xlsx"
)

OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Nudge_Experiment_Data",
    header=2
)

numeric_cols = [
    "Nudge_Shown",
    "Clicked",
    "Order_Value_Rupee",
    "Purchased_Flag",
    "Repeat_Visit_Flag"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["Conversion_Flag"] = df["Purchased_Flag"]

df["Conversion_Rate_%"] = (
    df["Purchased_Flag"] * 100
)

df["Revenue_per_Visit"] = (
    df["Order_Value_Rupee"]
    * df["Purchased_Flag"]
)

nudge = df.groupby(
    "Nudge_Type",
    as_index=False
).agg(
    Exposures=("Experiment_ID", "count"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Total_Order_Value=("Order_Value_Rupee", "sum"),
    Average_Order_Value=("Order_Value_Rupee", "mean")
)

nudge["Conversion_Rate_%"] = (
    nudge["Purchases"]
    / nudge["Exposures"]
    * 100
)

nudge["Click_Rate_%"] = (
    nudge["Clicks"]
    / nudge["Exposures"]
    * 100
)

baseline_rate = (
    df.loc[
        df["Nudge_Type"] == "No Nudge",
        "Purchased_Flag"
    ].mean()
    * 100
)

nudge["Lift_vs_Baseline_pp"] = (
    nudge["Conversion_Rate_%"]
    - baseline_rate
)

region = df.groupby(
    "Region",
    as_index=False
).agg(
    Visits=("Experiment_ID", "count"),
    Purchases=("Purchased_Flag", "sum"),
    Total_Order_Value=("Order_Value_Rupee", "sum")
)

region["Conversion_Rate_%"] = (
    region["Purchases"]
    / region["Visits"]
    * 100
)

category = df.groupby(
    "Category",
    as_index=False
).agg(
    Visits=("Experiment_ID", "count"),
    Purchases=("Purchased_Flag", "sum"),
    Total_Order_Value=("Order_Value_Rupee", "sum")
)

category["Conversion_Rate_%"] = (
    category["Purchases"]
    / category["Visits"]
    * 100
)

device = df.groupby(
    "Device",
    as_index=False
).agg(
    Visits=("Experiment_ID", "count"),
    Purchases=("Purchased_Flag", "sum"),
    Clicks=("Clicked", "sum"),
    Total_Order_Value=("Order_Value_Rupee", "sum")
)

device["Conversion_Rate_%"] = (
    device["Purchases"]
    / device["Visits"]
    * 100
)

device["Click_Rate_%"] = (
    device["Clicks"]
    / device["Visits"]
    * 100
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Experiments",
        "Nudge Exposures",
        "Total Purchases",
        "Overall Conversion Rate %",
        "Baseline Conversion Rate %",
        "Total Order Value (Rupee)",
        "Average Order Value (Rupee)"
    ],
    "Value": [
        len(df),
        df["Nudge_Shown"].sum(),
        df["Purchased_Flag"].sum(),
        df["Purchased_Flag"].mean() * 100,
        baseline_rate,
        df["Order_Value_Rupee"].sum(),
        df["Order_Value_Rupee"].mean()
    ]
})

df.to_csv(
    OUTPUT_DIR / "nudge_experiment_data.csv",
    index=False
)

nudge.to_csv(
    OUTPUT_DIR / "nudge_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_nudge_summary.csv",
    index=False
)

category.to_csv(
    OUTPUT_DIR / "category_nudge_summary.csv",
    index=False
)

device.to_csv(
    OUTPUT_DIR / "device_nudge_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "nudge_economics_kpis.csv",
    index=False
)


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
    plt.figure(figsize=(9, 5))

    plt.bar(
        x,
        y,
        color=color
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(
        rotation=rotation
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=160
    )

    plt.close()


save_bar(
    nudge["Nudge_Type"],
    nudge["Conversion_Rate_%"],
    "Conversion Rate by Nudge Type",
    "Nudge Type",
    "Conversion Rate %",
    "conversion_rate_by_nudge.png",
    "#4472C4",
    25
)

save_bar(
    nudge["Nudge_Type"],
    nudge["Lift_vs_Baseline_pp"],
    "Percentage-Point Lift vs Baseline",
    "Nudge Type",
    "Lift (percentage points)",
    "lift_vs_baseline.png",
    "#ED7D31",
    25
)

save_bar(
    region["Region"],
    region["Conversion_Rate_%"],
    "Conversion Rate by Region",
    "Region",
    "Conversion Rate %",
    "conversion_rate_by_region.png",
    "#70AD47"
)

save_bar(
    device["Device"],
    device["Click_Rate_%"],
    "Click Rate by Device",
    "Device",
    "Click Rate %",
    "click_rate_by_device.png",
    "#8064A2"
)

print("Day 075 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")