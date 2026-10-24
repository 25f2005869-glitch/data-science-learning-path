# Day 097 — A/B Testing Practice
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 097
# Topic: A/B Testing Practice

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. FILE PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_FILE = BASE_DIR / "data" / "Day_097_A_B_Testing_Practice.xlsx"

if not EXCEL_FILE.exists():
    alternative_paths = [
        Path("/mnt/data/Day_097_A_B_Testing_Practice.xlsx"),
        Path("Day_097_A_B_Testing_Practice.xlsx"),
        Path("data/Day_097_A_B_Testing_Practice.xlsx"),
    ]

    for path in alternative_paths:
        if path.exists():
            EXCEL_FILE = path
            break

if not EXCEL_FILE.exists():
    raise FileNotFoundError(
        "Day_097_A_B_Testing_Practice.xlsx was not found."
    )


OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD RAW DATA
# ============================================================

df = pd.read_excel(
    EXCEL_FILE,
    sheet_name="Raw_AB_Test_Data",
    header=3
)

print("\n" + "=" * 60)
print("DAY 097 — A/B TESTING PRACTICE")
print("=" * 60)

print("\nRaw Data Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Information:")
print(df.info())

print("\nMissing Values:")
print(df.isna().sum())


# ============================================================
# 3. STANDARDISE COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
)


# ============================================================
# 4. DATA CLEANING
# ============================================================

# Make a copy
cleaned_df = df.copy()


# ------------------------------------------------------------
# Text columns
# ------------------------------------------------------------

text_columns = [
    "Group",
    "Customer_Segment",
    "Device",
    "Channel",
    "Conversion_Status"
]

for column in text_columns:
    if column in cleaned_df.columns:
        cleaned_df[column] = (
            cleaned_df[column]
            .astype("string")
            .str.strip()
        )


# Standardise Group
cleaned_df["Group"] = (
    cleaned_df["Group"]
    .str.upper()
    .replace({
        "CONTROL": "A",
        "TREATMENT": "B"
    })
)


# Standardise Customer Segment
cleaned_df["Customer_Segment"] = (
    cleaned_df["Customer_Segment"]
    .str.title()
)


# Standardise Device
cleaned_df["Device"] = (
    cleaned_df["Device"]
    .str.title()
)


# Standardise Channel
cleaned_df["Channel"] = (
    cleaned_df["Channel"]
    .str.title()
)


# ------------------------------------------------------------
# Date
# ------------------------------------------------------------

cleaned_df["Date"] = pd.to_datetime(
    cleaned_df["Date"],
    errors="coerce"
)

if cleaned_df["Date"].isna().any():
    valid_dates = cleaned_df["Date"].dropna()

    if not valid_dates.empty:
        median_date = valid_dates.sort_values().iloc[len(valid_dates) // 2]
        cleaned_df["Date"] = cleaned_df["Date"].fillna(median_date)


# ------------------------------------------------------------
# Numeric columns
# ------------------------------------------------------------

numeric_columns = [
    "Age",
    "Visitors",
    "Converted",
    "Order_Value",
    "Revenue"
]

for column in numeric_columns:
    cleaned_df[column] = pd.to_numeric(
        cleaned_df[column],
        errors="coerce"
    )


# ------------------------------------------------------------
# Age
# ------------------------------------------------------------

valid_age = cleaned_df.loc[
    cleaned_df["Age"].between(18, 80, inclusive="both"),
    "Age"
]

if not valid_age.empty:
    age_median = valid_age.median()
else:
    age_median = 30

cleaned_df.loc[
    ~cleaned_df["Age"].between(18, 80, inclusive="both"),
    "Age"
] = np.nan

cleaned_df["Age"] = cleaned_df["Age"].fillna(age_median)


# ------------------------------------------------------------
# Visitors
# ------------------------------------------------------------

cleaned_df.loc[
    cleaned_df["Visitors"] < 1,
    "Visitors"
] = np.nan

cleaned_df["Visitors"] = cleaned_df["Visitors"].fillna(1)


# ------------------------------------------------------------
# Converted
# ------------------------------------------------------------

cleaned_df["Converted"] = np.where(
    cleaned_df["Converted"] == 1,
    1,
    0
)


# ------------------------------------------------------------
# Order Value
# ------------------------------------------------------------

cleaned_df.loc[
    cleaned_df["Order_Value"] < 0,
    "Order_Value"
] = np.nan

cleaned_df["Order_Value"] = cleaned_df["Order_Value"].fillna(0)


# ------------------------------------------------------------
# Revenue
# ------------------------------------------------------------

# Revenue is recalculated instead of relying on the raw value.
cleaned_df["Revenue"] = (
    cleaned_df["Converted"]
    * cleaned_df["Order_Value"]
)


# ------------------------------------------------------------
# Conversion Status
# ------------------------------------------------------------

cleaned_df["Conversion_Status"] = np.where(
    cleaned_df["Converted"] == 1,
    "Converted",
    "Not Converted"
)


# ============================================================
# 5. REMOVE DUPLICATES
# ============================================================

before_duplicates = len(cleaned_df)

cleaned_df = cleaned_df.drop_duplicates().reset_index(drop=True)

after_duplicates = len(cleaned_df)

print("\nDuplicate Rows Removed:")
print(before_duplicates - after_duplicates)


# ============================================================
# 6. VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)

print("\nMissing Values After Cleaning:")
print(cleaned_df.isna().sum())

print("\nGroup Values:")
print(cleaned_df["Group"].value_counts(dropna=False))

print("\nConverted Values:")
print(cleaned_df["Converted"].value_counts(dropna=False))

print("\nNegative Visitors:")
print((cleaned_df["Visitors"] < 0).sum())

print("\nNegative Order Values:")
print((cleaned_df["Order_Value"] < 0).sum())

print("\nInvalid Ages:")
print(
    (
        ~cleaned_df["Age"].between(
            18,
            80,
            inclusive="both"
        )
    ).sum()
)


# ============================================================
# 7. GROUP-LEVEL A/B TEST ANALYSIS
# ============================================================

group_analysis = (
    cleaned_df
    .groupby("Group", as_index=False)
    .agg(
        Visitors=("Visitors", "sum"),
        Conversions=("Converted", "sum"),
        Revenue=("Revenue", "sum")
    )
)

group_analysis["Conversion Rate %"] = np.where(
    group_analysis["Visitors"] > 0,
    group_analysis["Conversions"]
    / group_analysis["Visitors"] * 100,
    0
)

group_analysis["Average Order Value"] = np.where(
    group_analysis["Conversions"] > 0,
    group_analysis["Revenue"]
    / group_analysis["Conversions"],
    0
)

print("\n" + "=" * 60)
print("A/B TEST GROUP ANALYSIS")
print("=" * 60)

print(group_analysis)


# ============================================================
# 8. CONVERSION ANALYSIS
# ============================================================

conversion_analysis = group_analysis[
    [
        "Group",
        "Visitors",
        "Conversions",
        "Conversion Rate %"
    ]
].copy()

if {"A", "B"}.issubset(
    set(conversion_analysis["Group"])
):
    rate_a = conversion_analysis.loc[
        conversion_analysis["Group"] == "A",
        "Conversion Rate %"
    ].iloc[0]

    rate_b = conversion_analysis.loc[
        conversion_analysis["Group"] == "B",
        "Conversion Rate %"
    ].iloc[0]

    conversion_difference = rate_b - rate_a

    print("\nControl Conversion Rate:")
    print(f"{rate_a:.2f}%")

    print("\nTreatment Conversion Rate:")
    print(f"{rate_b:.2f}%")

    print("\nConversion Rate Difference (B - A):")
    print(f"{conversion_difference:.2f} percentage points")


# ============================================================
# 9. REVENUE ANALYSIS
# ============================================================

revenue_analysis = group_analysis[
    [
        "Group",
        "Revenue",
        "Conversions",
        "Average Order Value"
    ]
].copy()

print("\n" + "=" * 60)
print("REVENUE ANALYSIS")
print("=" * 60)

print(revenue_analysis)


# ============================================================
# 10. CUSTOMER SEGMENT ANALYSIS
# ============================================================

segment_analysis = (
    cleaned_df
    .groupby(
        ["Customer_Segment", "Group"],
        as_index=False
    )
    .agg(
        Visitors=("Visitors", "sum"),
        Conversions=("Converted", "sum"),
        Revenue=("Revenue", "sum")
    )
)

segment_analysis["Conversion Rate %"] = np.where(
    segment_analysis["Visitors"] > 0,
    segment_analysis["Conversions"]
    / segment_analysis["Visitors"] * 100,
    0
)

segment_analysis["Average Order Value"] = np.where(
    segment_analysis["Conversions"] > 0,
    segment_analysis["Revenue"]
    / segment_analysis["Conversions"],
    0
)

print("\n" + "=" * 60)
print("CUSTOMER SEGMENT ANALYSIS")
print("=" * 60)

print(segment_analysis)


# ============================================================
# 11. PRODUCT / CHANNEL / DEVICE ANALYSIS
# ============================================================

channel_analysis = (
    cleaned_df
    .groupby(
        ["Channel", "Group"],
        as_index=False
    )
    .agg(
        Visitors=("Visitors", "sum"),
        Conversions=("Converted", "sum"),
        Revenue=("Revenue", "sum")
    )
)

channel_analysis["Conversion Rate %"] = np.where(
    channel_analysis["Visitors"] > 0,
    channel_analysis["Conversions"]
    / channel_analysis["Visitors"] * 100,
    0
)


device_analysis = (
    cleaned_df
    .groupby(
        ["Device", "Group"],
        as_index=False
    )
    .agg(
        Visitors=("Visitors", "sum"),
        Conversions=("Converted", "sum"),
        Revenue=("Revenue", "sum")
    )
)

device_analysis["Conversion Rate %"] = np.where(
    device_analysis["Visitors"] > 0,
    device_analysis["Conversions"]
    / device_analysis["Visitors"] * 100,
    0
)


# ============================================================
# 12. DAILY A/B TEST ANALYSIS
# ============================================================

daily_analysis = (
    cleaned_df
    .groupby(
        ["Date", "Group"],
        as_index=False
    )
    .agg(
        Visitors=("Visitors", "sum"),
        Conversions=("Converted", "sum"),
        Revenue=("Revenue", "sum")
    )
)

daily_analysis["Conversion Rate %"] = np.where(
    daily_analysis["Visitors"] > 0,
    daily_analysis["Conversions"]
    / daily_analysis["Visitors"] * 100,
    0
)

daily_analysis = daily_analysis.sort_values(
    ["Date", "Group"]
).reset_index(drop=True)

print("\n" + "=" * 60)
print("DAILY A/B TEST ANALYSIS")
print("=" * 60)

print(daily_analysis.head(10))


# ============================================================
# 13. KPI SUMMARY
# ============================================================

kpi_summary = (
    group_analysis
    .set_index("Group")
    .T
    .reset_index()
)

kpi_summary.columns.name = None

print("\n" + "=" * 60)
print("KPI SUMMARY")
print("=" * 60)

print(kpi_summary)


# ============================================================
# 14. EXPORT CLEANED DATA
# ============================================================

cleaned_df.to_csv(
    OUTPUT_DIR / "cleaned_ab_test_data.csv",
    index=False
)

group_analysis.to_csv(
    OUTPUT_DIR / "ab_test_summary.csv",
    index=False
)

conversion_analysis.to_csv(
    OUTPUT_DIR / "conversion_analysis.csv",
    index=False
)

revenue_analysis.to_csv(
    OUTPUT_DIR / "revenue_analysis.csv",
    index=False
)

segment_analysis.to_csv(
    OUTPUT_DIR / "segment_analysis.csv",
    index=False
)

daily_analysis.to_csv(
    OUTPUT_DIR / "daily_ab_test_analysis.csv",
    index=False
)

channel_analysis.to_csv(
    OUTPUT_DIR / "channel_analysis.csv",
    index=False
)

device_analysis.to_csv(
    OUTPUT_DIR / "device_analysis.csv",
    index=False
)

kpi_summary.to_csv(
    OUTPUT_DIR / "ab_test_kpi_summary.csv",
    index=False
)


# ============================================================
# 15. CHART 1 — CONVERSION RATE BY GROUP
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    group_analysis["Group"],
    group_analysis["Conversion Rate %"]
)

plt.title("Conversion Rate by Group")
plt.xlabel("Group")
plt.ylabel("Conversion Rate (%)")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "conversion_rate_by_group.png",
    dpi=300
)

plt.close()


# ============================================================
# 16. CHART 2 — REVENUE BY GROUP
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    group_analysis["Group"],
    group_analysis["Revenue"]
)

plt.title("Revenue by Group")
plt.xlabel("Group")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_group.png",
    dpi=300
)

plt.close()


# ============================================================
# 17. CHART 3 — DAILY CONVERSION RATE TREND
# ============================================================

daily_pivot = daily_analysis.pivot(
    index="Date",
    columns="Group",
    values="Conversion Rate %"
)

plt.figure(figsize=(12, 6))

if "A" in daily_pivot.columns:
    plt.plot(
        daily_pivot.index,
        daily_pivot["A"],
        marker="o",
        label="Control (A)"
    )

if "B" in daily_pivot.columns:
    plt.plot(
        daily_pivot.index,
        daily_pivot["B"],
        marker="o",
        label="Treatment (B)"
    )

plt.title("Daily Conversion Rate Trend")
plt.xlabel("Date")
plt.ylabel("Conversion Rate (%)")
plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "daily_conversion_trend.png",
    dpi=300
)

plt.close()


# ============================================================
# 18. CHART 4 — REVENUE BY SEGMENT
# ============================================================

segment_revenue = (
    segment_analysis
    .pivot(
        index="Customer_Segment",
        columns="Group",
        values="Revenue"
    )
)

segment_revenue.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Revenue by Customer Segment and Group")
plt.xlabel("Customer Segment")
plt.ylabel("Revenue")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_segment.png",
    dpi=300
)

plt.close()


# ============================================================
# 19. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL A/B TESTING SUMMARY")
print("=" * 60)

print("\nTotal Records After Cleaning:")
print(len(cleaned_df))

print("\nTotal Visitors:")
print(cleaned_df["Visitors"].sum())

print("\nTotal Conversions:")
print(cleaned_df["Converted"].sum())

print("\nTotal Revenue:")
print(f"₹{cleaned_df['Revenue'].sum():,.2f}")

print("\nGroup Performance:")
print(group_analysis)

print("\nOutput Files Created In:")
print(OUTPUT_DIR)

print("\nA/B testing analysis completed successfully.")