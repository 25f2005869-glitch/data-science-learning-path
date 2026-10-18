from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 081
# Topic: A/B Testing of PayLater Nudges

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_081_W11_L2_A_B_Testing_of_PayLater_Nudges.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="PayLater_AB_Data",
    header=3
)

for col in [
    "Eligibility_Flag",
    "Nudge_Shown",
    "Clicked",
    "PayLater_Used_Flag",
    "Purchase_Value_Rupee",
    "PayLater_Due_Rupee",
    "Repayment_Flag"
]:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

variant_summary = df.groupby(
    "Variant",
    as_index=False
).agg(
    Eligible_Customers=("Eligibility_Flag", "sum"),
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    PayLater_Users=("PayLater_Used_Flag", "sum"),
    Purchase_Value=("Purchase_Value_Rupee", "sum"),
    Repayments=("Repayment_Flag", "sum")
)

variant_summary["Click_Rate_%"] = (
    variant_summary["Clicks"]
    / variant_summary["Exposures"].replace(0, 1)
    * 100
)

variant_summary["PayLater_Conversion_%"] = (
    variant_summary["PayLater_Users"]
    / variant_summary["Exposures"].replace(0, 1)
    * 100
)

variant_summary["Repayment_Rate_%"] = (
    variant_summary["Repayments"]
    / variant_summary["PayLater_Users"].replace(0, 1)
    * 100
)

variant_summary["Average_Purchase_Value_Rupee"] = (
    variant_summary["Purchase_Value"]
    / variant_summary["PayLater_Users"].replace(0, 1)
)

control_rate = float(
    variant_summary.loc[
        variant_summary["Variant"] == "Control",
        "PayLater_Conversion_%"
    ].iloc[0]
)

treatment_rate = float(
    variant_summary.loc[
        variant_summary["Variant"] == "Treatment",
        "PayLater_Conversion_%"
    ].iloc[0]
)

ab_metrics = pd.DataFrame({
    "Metric": [
        "Control PayLater Conversion %",
        "Treatment PayLater Conversion %",
        "Absolute Lift (percentage points)",
        "Relative Lift %",
        "Control Click Rate %",
        "Treatment Click Rate %",
        "Control Repayment Rate %",
        "Treatment Repayment Rate %",
        "Total PayLater Purchase Value (Rupee)"
    ],
    "Value": [
        control_rate,
        treatment_rate,
        treatment_rate - control_rate,
        (
            (treatment_rate - control_rate)
            / control_rate
            * 100
        ) if control_rate else 0,
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
        float(
            variant_summary.loc[
                variant_summary["Variant"] == "Control",
                "Repayment_Rate_%"
            ].iloc[0]
        ),
        float(
            variant_summary.loc[
                variant_summary["Variant"] == "Treatment",
                "Repayment_Rate_%"
            ].iloc[0]
        ),
        int(
            df["Purchase_Value_Rupee"].sum()
        )
    ]
})

segment_summary = df.groupby(
    ["Customer_Segment", "Variant"],
    as_index=False
).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    PayLater_Users=("PayLater_Used_Flag", "sum"),
    Purchase_Value=("Purchase_Value_Rupee", "sum"),
    Repayments=("Repayment_Flag", "sum")
)

segment_summary["Conversion_Rate_%"] = (
    segment_summary["PayLater_Users"]
    / segment_summary["Exposures"].replace(0, 1)
    * 100
)

region_summary = df.groupby(
    ["Region", "Variant"],
    as_index=False
).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    PayLater_Users=("PayLater_Used_Flag", "sum"),
    Purchase_Value=("Purchase_Value_Rupee", "sum")
)

region_summary["Conversion_Rate_%"] = (
    region_summary["PayLater_Users"]
    / region_summary["Exposures"].replace(0, 1)
    * 100
)

device_summary = df.groupby(
    ["Device", "Variant"],
    as_index=False
).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    PayLater_Users=("PayLater_Used_Flag", "sum"),
    Purchase_Value=("Purchase_Value_Rupee", "sum")
)

device_summary["Conversion_Rate_%"] = (
    device_summary["PayLater_Users"]
    / device_summary["Exposures"].replace(0, 1)
    * 100
)

nudge_summary = df.groupby(
    "Nudge_Type",
    as_index=False
).agg(
    Exposures=("Nudge_Shown", "sum"),
    Clicks=("Clicked", "sum"),
    PayLater_Users=("PayLater_Used_Flag", "sum"),
    Purchase_Value=("Purchase_Value_Rupee", "sum"),
    Repayments=("Repayment_Flag", "sum")
)

nudge_summary["Click_Rate_%"] = (
    nudge_summary["Clicks"]
    / nudge_summary["Exposures"].replace(0, 1)
    * 100
)

nudge_summary["Conversion_Rate_%"] = (
    nudge_summary["PayLater_Users"]
    / nudge_summary["Exposures"].replace(0, 1)
    * 100
)

nudge_summary["Repayment_Rate_%"] = (
    nudge_summary["Repayments"]
    / nudge_summary["PayLater_Users"].replace(0, 1)
    * 100
)

no_nudge_rate = float(
    nudge_summary.loc[
        nudge_summary["Nudge_Type"] == "No Nudge",
        "Conversion_Rate_%"
    ].iloc[0]
)

nudge_summary["Lift_vs_No_Nudge_pp"] = (
    nudge_summary["Conversion_Rate_%"]
    - no_nudge_rate
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Experiment Records",
        "Eligible Customers",
        "Total Exposures",
        "Total Clicks",
        "Total PayLater Users",
        "Overall PayLater Conversion %",
        "Total Purchase Value (Rupee)",
        "Total Repayments"
    ],
    "Value": [
        len(df),
        int(df["Eligibility_Flag"].sum()),
        int(df["Nudge_Shown"].sum()),
        int(df["Clicked"].sum()),
        int(df["PayLater_Used_Flag"].sum()),
        df["PayLater_Used_Flag"].sum()
        / max(df["Nudge_Shown"].sum(), 1)
        * 100,
        int(df["Purchase_Value_Rupee"].sum()),
        int(df["Repayment_Flag"].sum())
    ]
})

df.to_csv(
    OUTPUT_DIR / "paylater_ab_test_data.csv",
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

nudge_summary.to_csv(
    OUTPUT_DIR / "nudge_summary.csv",
    index=False
)

segment_summary.to_csv(
    OUTPUT_DIR / "segment_analysis.csv",
    index=False
)

region_summary.to_csv(
    OUTPUT_DIR / "region_analysis.csv",
    index=False
)

device_summary.to_csv(
    OUTPUT_DIR / "device_analysis.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "paylater_ab_testing_kpis.csv",
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
    variant_summary["PayLater_Conversion_%"],
    "PayLater Conversion: Control vs Treatment",
    "Variant",
    "Conversion Rate (%)",
    "conversion_rate_control_vs_treatment.png",
    "#4472C4"
)

save_bar(
    nudge_summary["Nudge_Type"],
    nudge_summary["Conversion_Rate_%"],
    "PayLater Conversion by Nudge Type",
    "Nudge Type",
    "Conversion Rate (%)",
    "conversion_rate_by_nudge.png",
    "#ED7D31",
    25
)

segment_pivot = segment_summary.pivot(
    index="Customer_Segment",
    columns="Variant",
    values="Conversion_Rate_%"
)

segment_pivot.plot(
    kind="bar",
    figsize=(9, 5),
    color=[
        "#70AD47",
        "#8064A2"
    ]
)

plt.title(
    "PayLater Conversion by Customer Segment"
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

region_pivot = region_summary.pivot(
    index="Region",
    columns="Variant",
    values="Conversion_Rate_%"
)

region_pivot.plot(
    kind="line",
    marker="o",
    figsize=(9, 5),
    color=[
        "#5B9BD5",
        "#A5A5A5"
    ]
)

plt.title(
    "PayLater Conversion by Region"
)

plt.xlabel(
    "Region"
)

plt.ylabel(
    "Conversion Rate (%)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "conversion_rate_by_region.png",
    dpi=160
)

plt.close()

print("Day 081 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")