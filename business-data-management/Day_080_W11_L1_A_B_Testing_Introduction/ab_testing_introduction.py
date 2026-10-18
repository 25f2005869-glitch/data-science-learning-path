from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 080
# Topic: A/B Testing Introduction

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_080_W11_L1_A_B_Testing_Introduction.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="AB_Test_Data",
    header=3
)

for col in [
    "Exposed_Flag",
    "Clicked",
    "Purchased_Flag",
    "Order_Value_Rupee",
]:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

variant_summary = df.groupby(
    "Variant",
    as_index=False
).agg(
    Observations=("Experiment_ID", "count"),
    Exposures=("Exposed_Flag", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Total_Order_Value=("Order_Value_Rupee", "sum"),
)

variant_summary["Click_Rate_%"] = (
    variant_summary["Clicks"]
    / variant_summary["Exposures"].replace(0, 1)
    * 100
)

variant_summary["Conversion_Rate_%"] = (
    variant_summary["Purchases"]
    / variant_summary["Exposures"].replace(0, 1)
    * 100
)

variant_summary["Average_Order_Value_Rupee"] = (
    variant_summary["Total_Order_Value"]
    / variant_summary["Purchases"].replace(0, 1)
)

control_rate = float(
    variant_summary.loc[
        variant_summary["Variant"] == "Control",
        "Conversion_Rate_%"
    ].iloc[0]
)

treatment_rate = float(
    variant_summary.loc[
        variant_summary["Variant"] == "Treatment",
        "Conversion_Rate_%"
    ].iloc[0]
)

ab_metrics = pd.DataFrame({
    "Metric": [
        "Control Conversion Rate %",
        "Treatment Conversion Rate %",
        "Absolute Lift (percentage points)",
        "Relative Lift %",
        "Control Click Rate %",
        "Treatment Click Rate %",
        "Control Purchases",
        "Treatment Purchases",
    ],
    "Value": [
        control_rate,
        treatment_rate,
        treatment_rate - control_rate,
        ((treatment_rate - control_rate) / control_rate * 100)
        if control_rate else 0,
        float(
            variant_summary.loc[
                variant_summary["Variant"] == "Control",
                "Click_Rate_%"
            ].iloc[0]
        ),
        float(
            variant_summary.loc[
                variant_summary["Variant"] == "Treatment",
                "Click_Rate_%"
            ].iloc[0]
        ),
        int(
            variant_summary.loc[
                variant_summary["Variant"] == "Control",
                "Purchases"
            ].iloc[0]
        ),
        int(
            variant_summary.loc[
                variant_summary["Variant"] == "Treatment",
                "Purchases"
            ].iloc[0]
        ),
    ]
})

segment_summary = df.groupby(
    [
        "Customer_Segment",
        "Variant"
    ],
    as_index=False
).agg(
    Exposures=("Exposed_Flag", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Order_Value=("Order_Value_Rupee", "sum"),
)

segment_summary["Conversion_Rate_%"] = (
    segment_summary["Purchases"]
    / segment_summary["Exposures"].replace(0, 1)
    * 100
)

region_summary = df.groupby(
    [
        "Region",
        "Variant"
    ],
    as_index=False
).agg(
    Exposures=("Exposed_Flag", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Order_Value=("Order_Value_Rupee", "sum"),
)

region_summary["Conversion_Rate_%"] = (
    region_summary["Purchases"]
    / region_summary["Exposures"].replace(0, 1)
    * 100
)

device_summary = df.groupby(
    [
        "Device",
        "Variant"
    ],
    as_index=False
).agg(
    Exposures=("Exposed_Flag", "sum"),
    Clicks=("Clicked", "sum"),
    Purchases=("Purchased_Flag", "sum"),
    Order_Value=("Order_Value_Rupee", "sum"),
)

device_summary["Conversion_Rate_%"] = (
    device_summary["Purchases"]
    / device_summary["Exposures"].replace(0, 1)
    * 100
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Observations",
        "Control Exposures",
        "Treatment Exposures",
        "Control Conversion Rate %",
        "Treatment Conversion Rate %",
        "Absolute Lift (pp)",
        "Relative Lift %",
        "Total Order Value (Rupee)",
    ],
    "Value": [
        len(df),
        int(
            df.loc[
                df["Variant"] == "Control",
                "Exposed_Flag"
            ].sum()
        ),
        int(
            df.loc[
                df["Variant"] == "Treatment",
                "Exposed_Flag"
            ].sum()
        ),
        control_rate,
        treatment_rate,
        treatment_rate - control_rate,
        (
            (treatment_rate - control_rate)
            / control_rate
            * 100
        ) if control_rate else 0,
        int(
            df["Order_Value_Rupee"].sum()
        ),
    ]
})

df.to_csv(
    OUTPUT_DIR / "ab_test_data.csv",
    index=False
)

variant_summary.to_csv(
    OUTPUT_DIR / "variant_summary.csv",
    index=False
)

ab_metrics.to_csv(
    OUTPUT_DIR / "ab_test_metrics.csv",
    index=False
)

segment_summary.to_csv(
    OUTPUT_DIR / "segment_ab_analysis.csv",
    index=False
)

region_summary.to_csv(
    OUTPUT_DIR / "region_ab_analysis.csv",
    index=False
)

device_summary.to_csv(
    OUTPUT_DIR / "device_ab_analysis.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "ab_testing_kpis.csv",
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
    variant_summary["Variant"],
    variant_summary["Conversion_Rate_%"],
    "Conversion Rate: Control vs Treatment",
    "Variant",
    "Conversion Rate (%)",
    "conversion_rate_control_vs_treatment.png",
    "#4472C4",
)

save_bar(
    variant_summary["Variant"],
    variant_summary["Click_Rate_%"],
    "Click Rate by Variant",
    "Variant",
    "Click Rate (%)",
    "click_rate_by_variant.png",
    "#ED7D31",
)

pivot = segment_summary.pivot(
    index="Customer_Segment",
    columns="Variant",
    values="Conversion_Rate_%"
)

pivot.plot(
    kind="bar",
    figsize=(9, 5),
    color=[
        "#70AD47",
        "#8064A2"
    ]
)

plt.title(
    "Conversion Rate by Customer Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Conversion Rate (%)"
)

plt.xticks(
    rotation=15
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "conversion_rate_by_segment.png",
    dpi=160
)

plt.close()


plt.figure(figsize=(8, 5))

plt.scatter(
    df["Clicked"],
    df["Order_Value_Rupee"],
    color="#5B9BD5"
)

plt.title(
    "Order Value vs Click Response"
)

plt.xlabel(
    "Clicked (0/1)"
)

plt.ylabel(
    "Order Value (Rupee)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "order_value_vs_click.png",
    dpi=160
)

plt.close()


print("Day 080 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")