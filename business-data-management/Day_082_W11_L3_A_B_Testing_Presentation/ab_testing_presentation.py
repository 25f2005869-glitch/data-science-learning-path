from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 082
# Topic: A/B Testing Presentation

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent
INPUT_FILE = BASE_DIR / "Day_082_W11_L3_A_B_Testing_Presentation.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="PayLater_AB_Data", header=4)

for col in [
    "Eligibility_Flag",
    "Nudge_Shown",
    "Clicked",
    "PayLater_Used_Flag",
    "Purchase_Value_Rupee",
    "Repayment_Flag"
]:
    df[col] = pd.to_numeric(df[col], errors="coerce")


def summarize(group_cols):
    s = df.groupby(group_cols, as_index=False).agg(
        Exposures=("Nudge_Shown", "sum"),
        Clicks=("Clicked", "sum"),
        PayLater_Users=("PayLater_Used_Flag", "sum"),
        Purchase_Value_Rupee=("Purchase_Value_Rupee", "sum"),
        Repayments=("Repayment_Flag", "sum")
    )

    s["Click_Rate_%"] = (
        s["Clicks"] /
        s["Exposures"].replace(0, 1) *
        100
    )

    s["Conversion_Rate_%"] = (
        s["PayLater_Users"] /
        s["Exposures"].replace(0, 1) *
        100
    )

    s["Repayment_Rate_%"] = (
        s["Repayments"] /
        s["PayLater_Users"].replace(0, 1) *
        100
    )

    return s


variant = summarize(["Variant"])
nudge = summarize(["Nudge_Type"])
segment = summarize(["Customer_Segment", "Variant"])
region = summarize(["Region", "Variant"])
device = summarize(["Device", "Variant"])


control_rate = float(
    variant.loc[
        variant["Variant"] == "Control",
        "Conversion_Rate_%"
    ].iloc[0]
)

treatment_rate = float(
    variant.loc[
        variant["Variant"] == "Treatment",
        "Conversion_Rate_%"
    ].iloc[0]
)


metrics = pd.DataFrame({
    "Metric": [
        "Control Conversion %",
        "Treatment Conversion %",
        "Absolute Lift (pp)",
        "Relative Lift %",
        "Control Click Rate %",
        "Treatment Click Rate %",
        "Total Purchase Value (Rupee)",
        "Total PayLater Users"
    ],
    "Value": [
        control_rate,
        treatment_rate,
        treatment_rate - control_rate,
        (
            (treatment_rate - control_rate)
            / control_rate *
            100
        ) if control_rate else 0,
        float(
            variant.loc[
                variant["Variant"] == "Control",
                "Click_Rate_%"
            ].iloc[0]
        ),
        float(
            variant.loc[
                variant["Variant"] == "Treatment",
                "Click_Rate_%"
            ].iloc[0]
        ),
        int(df["Purchase_Value_Rupee"].sum()),
        int(df["PayLater_Used_Flag"].sum())
    ]
})


kpis = pd.DataFrame({
    "KPI": [
        "Total Records",
        "Eligible Records",
        "Total Exposures",
        "Total Clicks",
        "Total PayLater Users",
        "Overall Conversion %",
        "Total Purchase Value",
        "Control Conversion %",
        "Treatment Conversion %",
        "Absolute Lift pp",
        "Relative Lift %"
    ],
    "Value": [
        len(df),
        int(df["Eligibility_Flag"].sum()),
        int(df["Nudge_Shown"].sum()),
        int(df["Clicked"].sum()),
        int(df["PayLater_Used_Flag"].sum()),
        (
            df["PayLater_Used_Flag"].sum()
            / max(df["Nudge_Shown"].sum(), 1)
            * 100
        ),
        int(df["Purchase_Value_Rupee"].sum()),
        control_rate,
        treatment_rate,
        treatment_rate - control_rate,
        (
            (treatment_rate - control_rate)
            / control_rate *
            100
        ) if control_rate else 0
    ]
})


df.to_csv(
    OUTPUT_DIR / "paylater_ab_testing_presentation_data.csv",
    index=False
)

variant.to_csv(
    OUTPUT_DIR / "variant_presentation_summary.csv",
    index=False
)

nudge.to_csv(
    OUTPUT_DIR / "nudge_presentation_summary.csv",
    index=False
)

segment.to_csv(
    OUTPUT_DIR / "segment_presentation_analysis.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_presentation_analysis.csv",
    index=False
)

device.to_csv(
    OUTPUT_DIR / "device_presentation_analysis.csv",
    index=False
)

metrics.to_csv(
    OUTPUT_DIR / "ab_testing_presentation_metrics.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "ab_testing_presentation_kpis.csv",
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
    plt.bar(x, y, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=160
    )
    plt.close()


save_bar(
    variant["Variant"],
    variant["Conversion_Rate_%"],
    "Control vs Treatment PayLater Conversion",
    "Variant",
    "Conversion Rate (%)",
    "control_vs_treatment_conversion.png",
    "#4472C4"
)


save_bar(
    nudge["Nudge_Type"],
    nudge["Conversion_Rate_%"],
    "PayLater Conversion by Nudge Type",
    "Nudge Type",
    "Conversion Rate (%)",
    "nudge_conversion_presentation.png",
    "#ED7D31",
    25
)


seg_plot = segment.pivot(
    index="Customer_Segment",
    columns="Variant",
    values="Conversion_Rate_%"
)

seg_plot.plot(
    kind="bar",
    figsize=(9, 5),
    color=["#70AD47", "#8064A2"]
)

plt.title(
    "PayLater Conversion by Customer Segment"
)

plt.xlabel("Customer Segment")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR /
    "segment_conversion_presentation.png",
    dpi=160
)

plt.close()


reg_plot = region.pivot(
    index="Region",
    columns="Variant",
    values="Conversion_Rate_%"
)

reg_plot.plot(
    kind="line",
    marker="o",
    figsize=(9, 5),
    color=["#5B9BD5", "#A5A5A5"]
)

plt.title(
    "PayLater Conversion by Region"
)

plt.xlabel("Region")
plt.ylabel("Conversion Rate (%)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR /
    "regional_conversion_presentation.png",
    dpi=160
)

plt.close()


print("Day 082 analysis complete.")
print(f"Input: {INPUT_FILE}")
print(f"Output: {OUTPUT_DIR}")