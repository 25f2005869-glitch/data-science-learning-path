# ============================================================
# Day 026 - Volume Pareto
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Course: Business Data Management
# Day: 026
# Topic: Volume Pareto
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ------------------------------------------------------------
# PATH SETUP
# ------------------------------------------------------------

CODE_DIR = Path(__file__).resolve().parent

BASE_DIR = CODE_DIR.parent

OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(
    exist_ok=True
)


# ------------------------------------------------------------
# FIND EXCEL WORKBOOK
# ------------------------------------------------------------

excel_files = list(
    BASE_DIR.glob("*.xlsx")
)

if not excel_files:
    raise FileNotFoundError(
        "No Excel workbook found in the Day 026 folder."
    )

INPUT_FILE = excel_files[0]


# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Ecommerce_Data"
)


# ------------------------------------------------------------
# BASIC INFORMATION
# ------------------------------------------------------------

print("=" * 70)

print(
    "DAY 026 - VOLUME PARETO"
)

print("=" * 70)

print(
    "Workbook:",
    INPUT_FILE.name
)

print(
    "Rows:",
    df.shape[0]
)

print(
    "Columns:",
    df.shape[1]
)


print("\nFirst five rows:")

print(
    df.head()
)


# ------------------------------------------------------------
# TOTAL VOLUME
# ------------------------------------------------------------

total_units = df[
    "Units"
].sum()


total_orders = df[
    "Orders"
].sum()


total_revenue = df[
    "Revenue_Lakh"
].sum()


print("\nTOTAL BUSINESS MEASURES")

print(
    "Total Units:",
    total_units
)

print(
    "Total Orders:",
    total_orders
)

print(
    "Total Revenue (Lakh):",
    round(
        total_revenue,
        2
    )
)


# ------------------------------------------------------------
# PRODUCT VOLUME
# ------------------------------------------------------------

product = (

    df.groupby(
        "Product"
    )

    .agg(

        Orders=(
            "Orders",
            "sum"
        ),

        Units=(
            "Units",
            "sum"
        ),

        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        )

    )

    .reset_index()

    .sort_values(
        "Units",
        ascending=False
    )

)


# ------------------------------------------------------------
# UNIT SHARE
# ------------------------------------------------------------

product[
    "Unit_Share_Percent"
] = (

    product["Units"]

    / total_units

    * 100

).round(2)


# ------------------------------------------------------------
# CUMULATIVE UNITS
# ------------------------------------------------------------

product[
    "Cumulative_Units"
] = (

    product[
        "Units"
    ]

    .cumsum()

)


# ------------------------------------------------------------
# CUMULATIVE SHARE
# ------------------------------------------------------------

product[
    "Cumulative_Share_Percent"
] = (

    product[
        "Cumulative_Units"
    ]

    / total_units

    * 100

).round(2)


# ------------------------------------------------------------
# PARETO 80 GROUP
# ------------------------------------------------------------

product[
    "Pareto_80_Flag"
] = "Remaining Volume"


for index, row in product.iterrows():

    product.loc[
        index,
        "Pareto_80_Flag"
    ] = "Core Volume Group"

    if (
        row[
            "Cumulative_Share_Percent"
        ]
        >= 80
    ):

        break


# ------------------------------------------------------------
# DISPLAY PRODUCT ANALYSIS
# ------------------------------------------------------------

print(
    "\nPRODUCT VOLUME ANALYSIS"
)

print(
    product
)


# ------------------------------------------------------------
# SAVE PRODUCT ANALYSIS
# ------------------------------------------------------------

product.to_csv(

    OUTPUT_DIR
    / "product_volume_pareto.csv",

    index=False

)


# ------------------------------------------------------------
# MONTHLY VOLUME
# ------------------------------------------------------------

monthly = (

    df.groupby(
        "Month",
        sort=False
    )

    .agg(

        Orders=(
            "Orders",
            "sum"
        ),

        Units=(
            "Units",
            "sum"
        ),

        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        )

    )

    .reset_index()

)


print(
    "\nMONTHLY VOLUME"
)

print(
    monthly
)


monthly.to_csv(

    OUTPUT_DIR
    / "monthly_volume.csv",

    index=False

)


# ------------------------------------------------------------
# CHANNEL VOLUME
# ------------------------------------------------------------

channel = (

    df.groupby(
        "Channel"
    )

    .agg(

        Orders=(
            "Orders",
            "sum"
        ),

        Units=(
            "Units",
            "sum"
        ),

        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        )

    )

    .reset_index()

    .sort_values(
        "Units",
        ascending=False
    )

)


print(
    "\nCHANNEL VOLUME"
)

print(
    channel
)


channel.to_csv(

    OUTPUT_DIR
    / "channel_volume.csv",

    index=False

)


# ------------------------------------------------------------
# REGION VOLUME
# ------------------------------------------------------------

region = (

    df.groupby(
        "Region"
    )

    .agg(

        Orders=(
            "Orders",
            "sum"
        ),

        Units=(
            "Units",
            "sum"
        ),

        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        )

    )

    .reset_index()

    .sort_values(
        "Units",
        ascending=False
    )

)


print(
    "\nREGION VOLUME"
)

print(
    region
)


region.to_csv(

    OUTPUT_DIR
    / "region_volume.csv",

    index=False

)


# ------------------------------------------------------------
# PARETO RESULT
# ------------------------------------------------------------

core_group = product[
    product[
        "Pareto_80_Flag"
    ]
    == "Core Volume Group"
]


top_product = product.iloc[
    0
]["Product"]


top_share = product.iloc[
    0
]["Unit_Share_Percent"]


core_share = core_group.iloc[
    -1
]["Cumulative_Share_Percent"]


print(
    "\nPARETO RESULT"
)


print(
    "Top Volume Product:",
    top_product
)


print(
    "Top Product Unit Share:",
    f"{top_share:.2f}%"
)


print(
    "Core Volume Group:",
    ", ".join(
        core_group["Product"].tolist()
    )
)


print(
    "Core Group Cumulative Share:",
    f"{core_share:.2f}%"
)


# ------------------------------------------------------------
# MONTHLY CHART
# ------------------------------------------------------------

plt.figure(
    figsize=(10, 5)
)


plt.bar(

    monthly["Month"],

    monthly["Units"]

)


plt.title(
    "Monthly Unit Volume"
)


plt.xlabel(
    "Month"
)


plt.ylabel(
    "Units"
)


plt.xticks(
    rotation=45
)


plt.tight_layout()


plt.savefig(

    OUTPUT_DIR
    / "monthly_volume.png",

    dpi=150

)


plt.close()


# ------------------------------------------------------------
# PRODUCT VOLUME CHART
# ------------------------------------------------------------

plt.figure(
    figsize=(10, 5)
)


plt.bar(

    product["Product"],

    product["Units"]

)


plt.title(
    "Product Units — Volume Pareto"
)


plt.xlabel(
    "Product"
)


plt.ylabel(
    "Units"
)


plt.xticks(
    rotation=30
)


plt.tight_layout()


plt.savefig(

    OUTPUT_DIR
    / "volume_pareto_units.png",

    dpi=150

)


plt.close()


# ------------------------------------------------------------
# PARETO COMBINATION CHART
# ------------------------------------------------------------

fig, ax1 = plt.subplots(
    figsize=(10, 6)
)


ax1.bar(

    product["Product"],

    product["Units"]

)


ax1.set_xlabel(
    "Product"
)


ax1.set_ylabel(
    "Units"
)


ax1.tick_params(
    axis="x",
    rotation=30
)


ax2 = ax1.twinx()


ax2.plot(

    product["Product"],

    product[
        "Cumulative_Share_Percent"
    ],

    marker="o"

)


ax2.set_ylabel(
    "Cumulative Share (%)"
)


ax2.axhline(

    80,

    linestyle="--"

)


plt.title(
    "Volume Pareto — Product Units"
)


fig.tight_layout()


plt.savefig(

    OUTPUT_DIR
    / "volume_pareto_chart.png",

    dpi=150

)


plt.close()


# ------------------------------------------------------------
# PRODUCT SHARE CHART
# ------------------------------------------------------------

plt.figure(
    figsize=(9, 5)
)


plt.bar(

    product["Product"],

    product[
        "Unit_Share_Percent"
    ]

)


plt.title(
    "Product Share of Total Volume"
)


plt.xlabel(
    "Product"
)


plt.ylabel(
    "Unit Share (%)"
)


plt.xticks(
    rotation=30
)


plt.tight_layout()


plt.savefig(

    OUTPUT_DIR
    / "product_unit_share.png",

    dpi=150

)


plt.close()


# ------------------------------------------------------------
# FINAL MESSAGE
# ------------------------------------------------------------

print(
    "\n" + "=" * 70
)


print(
    "DAY 026 — VOLUME PARETO COMPLETED SUCCESSFULLY"
)


print(
    "=" * 70
)


print(
    "Output folder:",
    OUTPUT_DIR
)


print(
    "\nGenerated files:"
)


print(
    "- product_volume_pareto.csv"
)


print(
    "- monthly_volume.csv"
)


print(
    "- channel_volume.csv"
)


print(
    "- region_volume.csv"
)


print(
    "- monthly_volume.png"
)


print(
    "- volume_pareto_units.png"
)


print(
    "- volume_pareto_chart.png"
)


print(
    "- product_unit_share.png"
)