from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 079
# Topic: Factors for Nudge Presentation

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_079_W10_L8_Factors_for_Nudge_Presentation.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="Nudge_Factor_Data", header=3)

numeric_cols = [
    "Nudge_Shown",
    "Clicked",
    "Purchased_Flag",
    "Order_Value_Rupee",
    "Repeat_Visit_Flag",
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Click_Rate_Flag"] = df["Clicked"]
df["Conversion_Rate_Flag"] = df["Purchased_Flag"]
df["Order_Value_per_Exposure"] = (
    df["Order_Value_Rupee"] / df["Nudge_Shown"].replace(0, 1)
)
df["Engagement_Flag"] = (
    (df["Clicked"] == 1) | (df["Repeat_Visit_Flag"] == 1)
).astype(int)

factor_summary = df.groupby("Nudge_Type", as_index=False).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Total_Order_Value=("Order_Value_Rupee", "sum"),
    Repeat_Visits=("Repeat_Visit_Flag", "sum"),
    Avg_Order_Value=("Order_Value_Rupee", "mean"),
)

factor_summary["Click_Rate_%"] = (
    factor_summary["Clicks"]
    / factor_summary["Exposures"].replace(0, 1)
    * 100
)

factor_summary["Conversion_Rate_%"] = (
    factor_summary["Purchases"]
    / factor_summary["Exposures"].replace(0, 1)
    * 100
)

factor_summary["Repeat_Visit_Rate_%"] = (
    factor_summary["Repeat_Visits"]
    / factor_summary["Exposures"].replace(0, 1)
    * 100
)

baseline = df[df["Nudge_Type"] == "Default Recommendation"]
baseline_rate = (
    baseline["Purchased_Flag"].sum()
    / max(baseline["Nudge_Shown"].sum(), 1)
    * 100
)

factor_summary["Lift_vs_Default_pp"] = (
    factor_summary["Conversion_Rate_%"] - baseline_rate
)

segment_summary = df.groupby("Customer_Segment", as_index=False).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Order_Value=("Order_Value_Rupee", "sum"),
    Repeat_Visits=("Repeat_Visit_Flag", "sum"),
)

segment_summary["Click_Rate_%"] = (
    segment_summary["Clicks"]
    / segment_summary["Exposures"].replace(0, 1)
    * 100
)

segment_summary["Conversion_Rate_%"] = (
    segment_summary["Purchases"]
    / segment_summary["Exposures"].replace(0, 1)
    * 100
)

region_summary = df.groupby("Region", as_index=False).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Order_Value=("Order_Value_Rupee", "sum"),
)

region_summary["Conversion_Rate_%"] = (
    region_summary["Purchases"]
    / region_summary["Exposures"].replace(0, 1)
    * 100
)

device_summary = df.groupby("Device", as_index=False).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Order_Value=("Order_Value_Rupee", "sum"),
)

device_summary["Click_Rate_%"] = (
    device_summary["Clicks"]
    / device_summary["Exposures"].replace(0, 1)
    * 100
)

device_summary["Conversion_Rate_%"] = (
    device_summary["Purchases"]
    / device_summary["Exposures"].replace(0, 1)
    * 100
)

category_summary = df.groupby("Category", as_index=False).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Order_Value=("Order_Value_Rupee", "sum"),
)

category_summary["Conversion_Rate_%"] = (
    category_summary["Purchases"]
    / category_summary["Exposures"].replace(0, 1)
    * 100
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Observations",
        "Total Nudge Exposures",
        "Total Clicks",
        "Total Purchases",
        "Overall Click Rate %",
        "Overall Conversion Rate %",
        "Total Order Value (Rupee)",
        "Average Order Value (Rupee)",
    ],
    "Value": [
        len(df),
        df["Nudge_Shown"].sum(),
        df["Clicked"].sum(),
        df["Purchased_Flag"].sum(),
        df["Clicked"].sum() / max(df["Nudge_Shown"].sum(), 1) * 100,
        df["Purchased_Flag"].sum() / max(df["Nudge_Shown"].sum(), 1) * 100,
        df["Order_Value_Rupee"].sum(),
        df.loc[df["Order_Value_Rupee"] > 0, "Order_Value_Rupee"].mean(),
    ],
})

df.to_csv(OUTPUT_DIR / "nudge_factor_data.csv", index=False)
factor_summary.to_csv(OUTPUT_DIR / "nudge_factor_summary.csv", index=False)
segment_summary.to_csv(OUTPUT_DIR / "customer_segment_summary.csv", index=False)
region_summary.to_csv(OUTPUT_DIR / "region_factor_summary.csv", index=False)
device_summary.to_csv(OUTPUT_DIR / "device_factor_summary.csv", index=False)
category_summary.to_csv(OUTPUT_DIR / "category_factor_summary.csv", index=False)
kpis.to_csv(OUTPUT_DIR / "nudge_factor_kpis.csv", index=False)

def save_bar(x, y, title, xlabel, ylabel, filename, color, rotation=0):
    plt.figure(figsize=(9, 5))
    plt.bar(x, y, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=160)
    plt.close()

save_bar(
    factor_summary["Nudge_Type"],
    factor_summary["Conversion_Rate_%"],
    "Conversion Rate by Nudge Type",
    "Nudge Type",
    "Conversion Rate (%)",
    "conversion_rate_by_nudge_type.png",
    "#4472C4",
    25,
)

save_bar(
    factor_summary["Nudge_Type"],
    factor_summary["Lift_vs_Default_pp"],
    "Lift vs Default Reference",
    "Nudge Type",
    "Lift (percentage points)",
    "lift_vs_default.png",
    "#ED7D31",
    25,
)

save_bar(
    segment_summary["Customer_Segment"],
    segment_summary["Conversion_Rate_%"],
    "Conversion Rate by Customer Segment",
    "Customer Segment",
    "Conversion Rate (%)",
    "conversion_rate_by_segment.png",
    "#70AD47",
    15,
)

save_bar(
    device_summary["Device"],
    device_summary["Conversion_Rate_%"],
    "Conversion Rate by Device",
    "Device",
    "Conversion Rate (%)",
    "conversion_rate_by_device.png",
    "#8064A2",
)

plt.figure(figsize=(8, 5))
plt.scatter(
    df["Clicked"],
    df["Order_Value_Rupee"],
    color="#5B9BD5"
)
plt.title("Order Value vs Click Response")
plt.xlabel("Clicked (0/1)")
plt.ylabel("Order Value (Rupee)")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "order_value_vs_click.png",
    dpi=160
)
plt.close()

print("Day 079 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")