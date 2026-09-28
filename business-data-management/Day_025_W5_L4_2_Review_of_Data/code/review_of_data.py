# ============================================================
# Day 025 - Review of Data
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Course: Business Data Management
# Day: 025
# Topic: Review of Data
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ------------------------------------------------------------
# 1. PATH SETUP
# ------------------------------------------------------------

# This Python file is inside the "code" folder.
CODE_DIR = Path(__file__).resolve().parent

# The Excel workbook is one level above the "code" folder.
BASE_DIR = CODE_DIR.parent

# Folder for generated outputs.
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(
    exist_ok=True
)


# ------------------------------------------------------------
# 2. FIND EXCEL WORKBOOK
# ------------------------------------------------------------

excel_files = list(
    BASE_DIR.glob("*.xlsx")
)

if not excel_files:

    raise FileNotFoundError(
        "No Excel workbook found in the Day 025 folder."
    )


INPUT_FILE = excel_files[0]


# ------------------------------------------------------------
# 3. START
# ------------------------------------------------------------

print("=" * 70)

print(
    "DAY 025 - REVIEW OF DATA"
)

print("=" * 70)

print(
    "Workbook:",
    INPUT_FILE.name
)


# ------------------------------------------------------------
# 4. LOAD DATA
# ------------------------------------------------------------

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Ecommerce_Data"
)


# ------------------------------------------------------------
# 5. DATASET STRUCTURE
# ------------------------------------------------------------

print("\nDATASET STRUCTURE")

print(
    "Rows:",
    df.shape[0]
)

print(
    "Columns:",
    df.shape[1]
)


print("\nColumns:")

for column in df.columns:

    print(
        "-",
        column
    )


print("\nData types:")

print(
    df.dtypes
)


print("\nFirst five rows:")

print(
    df.head()
)


# ------------------------------------------------------------
# 6. MISSING VALUE REVIEW
# ------------------------------------------------------------

print(
    "\nMISSING VALUE REVIEW"
)

missing = df.isna().sum()

print(
    missing
)

total_missing = int(
    missing.sum()
)

print(
    "Total missing values:",
    total_missing
)


missing_table = missing.reset_index()

missing_table.columns = [
    "Column",
    "Missing_Count"
]


missing_table.to_csv(
    OUTPUT_DIR / "missing_value_check.csv",
    index=False
)


# ------------------------------------------------------------
# 7. DUPLICATE REVIEW
# ------------------------------------------------------------

print(
    "\nDUPLICATE REVIEW"
)


duplicate_rows = int(
    df.duplicated().sum()
)


duplicate_ids = int(
    df["Order_ID"].duplicated().sum()
)


print(
    "Duplicate rows:",
    duplicate_rows
)


print(
    "Duplicate Order_IDs:",
    duplicate_ids
)


duplicate_table = pd.DataFrame({

    "Check": [
        "Duplicate rows",
        "Duplicate Order_IDs"
    ],

    "Count": [
        duplicate_rows,
        duplicate_ids
    ]

})


duplicate_table.to_csv(
    OUTPUT_DIR / "duplicate_check.csv",
    index=False
)


# ------------------------------------------------------------
# 8. CATEGORICAL REVIEW
# ------------------------------------------------------------

print(
    "\nCATEGORICAL REVIEW"
)


categorical_columns = [

    "Month",

    "Category",

    "Channel",

    "Region",

    "Customer_Type"

]


category_rows = []


for column in categorical_columns:

    values = (
        df[column]
        .dropna()
        .unique()
        .tolist()
    )


    print(
        f"\n{column}:"
    )


    print(
        values
    )


    category_rows.append({

        "Column": column,

        "Unique_Count": len(values),

        "Unique_Values": ", ".join(
            str(value)
            for value in values
        )

    })


category_table = pd.DataFrame(
    category_rows
)


category_table.to_csv(
    OUTPUT_DIR / "category_review.csv",
    index=False
)


# ------------------------------------------------------------
# 9. NUMERICAL REVIEW
# ------------------------------------------------------------

print(
    "\nNUMERICAL REVIEW"
)


numeric_columns = [

    "Orders",

    "Units",

    "Discount_Percent",

    "Revenue_Lakh"

]


numeric_summary = (

    df[numeric_columns]

    .describe()

    .round(2)

)


print(
    numeric_summary
)


numeric_summary.to_csv(
    OUTPUT_DIR / "numeric_summary.csv"
)


# ------------------------------------------------------------
# 10. BUSINESS MEASURES
# ------------------------------------------------------------

print(
    "\nBUSINESS MEASURES"
)


total_orders = df[
    "Orders"
].sum()


total_units = df[
    "Units"
].sum()


total_revenue = df[
    "Revenue_Lakh"
].sum()


average_discount = df[
    "Discount_Percent"
].mean()


print(
    "Total Orders:",
    total_orders
)


print(
    "Total Units:",
    total_units
)


print(
    "Total Revenue (Lakh):",
    round(
        total_revenue,
        2
    )
)


print(
    "Average Discount (%):",
    round(
        average_discount,
        2
    )
)


# ------------------------------------------------------------
# 11. MONTHLY REVIEW
# ------------------------------------------------------------

print(
    "\nMONTHLY REVIEW"
)


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
        ),

        Average_Discount=(
            "Discount_Percent",
            "mean"
        )

    )

    .reset_index()

)


print(
    monthly
)


monthly.to_csv(
    OUTPUT_DIR / "monthly_review.csv",
    index=False
)


# ------------------------------------------------------------
# 12. CATEGORY REVIEW
# ------------------------------------------------------------

print(
    "\nCATEGORY REVIEW"
)


category = (

    df.groupby(
        "Category"
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
        ),

        Average_Discount=(
            "Discount_Percent",
            "mean"
        )

    )

    .reset_index()

    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )

)


print(
    category
)


category.to_csv(
    OUTPUT_DIR / "category_review.csv",
    index=False
)


# ------------------------------------------------------------
# 13. CHANNEL REVIEW
# ------------------------------------------------------------

print(
    "\nCHANNEL REVIEW"
)


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
        "Revenue_Lakh",
        ascending=False
    )

)


print(
    channel
)


channel.to_csv(
    OUTPUT_DIR / "channel_review.csv",
    index=False
)


# ------------------------------------------------------------
# 14. REGION REVIEW
# ------------------------------------------------------------

print(
    "\nREGION REVIEW"
)


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
        "Revenue_Lakh",
        ascending=False
    )

)


print(
    region
)


region.to_csv(
    OUTPUT_DIR / "region_review.csv",
    index=False
)


# ------------------------------------------------------------
# 15. CUSTOMER REVIEW
# ------------------------------------------------------------

print(
    "\nCUSTOMER REVIEW"
)


customer = (

    df.groupby(
        "Customer_Type"
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
        "Revenue_Lakh",
        ascending=False
    )

)


print(
    customer
)


customer.to_csv(
    OUTPUT_DIR / "customer_review.csv",
    index=False
)


# ------------------------------------------------------------
# 16. DATA REVIEW SUMMARY
# ------------------------------------------------------------

print(
    "\nDATA REVIEW SUMMARY"
)


review_summary = pd.DataFrame({

    "Review_Area": [

        "Dataset rows",

        "Dataset columns",

        "Missing values",

        "Duplicate rows",

        "Duplicate Order_IDs",

        "Month range",

        "Category count",

        "Channel count",

        "Region count",

        "Customer type count"

    ],

    "Result": [

        df.shape[0],

        df.shape[1],

        total_missing,

        duplicate_rows,

        duplicate_ids,

        (
            f"{df['Month'].iloc[0]} "
            f"to "
            f"{df['Month'].iloc[-1]}"
        ),

        df["Category"].nunique(),

        df["Channel"].nunique(),

        df["Region"].nunique(),

        df["Customer_Type"].nunique()

    ]

})


print(
    review_summary
)


review_summary.to_csv(

    OUTPUT_DIR /
    "data_review_summary.csv",

    index=False

)


# ------------------------------------------------------------
# 17. MONTHLY REVENUE CHART
# ------------------------------------------------------------

print(
    "\nMONTHLY REVENUE CHART"
)


plt.figure(
    figsize=(10, 5)
)


plt.bar(

    monthly["Month"],

    monthly["Revenue_Lakh"]

)


plt.title(
    "Monthly Revenue — Data Review"
)


plt.xlabel(
    "Month"
)


plt.ylabel(
    "Revenue (Lakh)"
)


plt.xticks(
    rotation=45
)


plt.tight_layout()


plt.savefig(

    OUTPUT_DIR /
    "monthly_revenue_review.png",

    dpi=150

)


plt.close()


# ------------------------------------------------------------
# 18. CATEGORY REVENUE CHART
# ------------------------------------------------------------

print(
    "\nCATEGORY REVENUE CHART"
)


plt.figure(
    figsize=(9, 5)
)


plt.bar(

    category["Category"],

    category["Revenue_Lakh"]

)


plt.title(
    "Revenue by Category — Data Review"
)


plt.xlabel(
    "Category"
)


plt.ylabel(
    "Revenue (Lakh)"
)


plt.tight_layout()


plt.savefig(

    OUTPUT_DIR /
    "category_revenue_review.png",

    dpi=150

)


plt.close()


# ------------------------------------------------------------
# 19. DATA QUALITY CHART
# ------------------------------------------------------------

print(
    "\nDATA QUALITY CHART"
)


quality = pd.DataFrame({

    "Check": [

        "Missing Values",

        "Duplicate Rows",

        "Duplicate Order IDs"

    ],

    "Count": [

        total_missing,

        duplicate_rows,

        duplicate_ids

    ]

})


plt.figure(
    figsize=(9, 5)
)


plt.bar(

    quality["Check"],

    quality["Count"]

)


plt.title(
    "Data Quality Review"
)


plt.xlabel(
    "Check"
)


plt.ylabel(
    "Count"
)


plt.xticks(
    rotation=20
)


plt.tight_layout()


plt.savefig(

    OUTPUT_DIR /
    "data_quality_review.png",

    dpi=150

)


plt.close()


# ------------------------------------------------------------
# 20. FINAL MESSAGE
# ------------------------------------------------------------

print(
    "\n" + "=" * 70
)


print(
    "DAY 025 — REVIEW OF DATA COMPLETED SUCCESSFULLY"
)


print(
    "=" * 70
)


print(
    "\nOutput folder:"
)


print(
    OUTPUT_DIR
)


print(
    "\nGenerated CSV files:"
)


print(
    "- missing_value_check.csv"
)


print(
    "- duplicate_check.csv"
)


print(
    "- category_review.csv"
)


print(
    "- numeric_summary.csv"
)


print(
    "- monthly_review.csv"
)


print(
    "- channel_review.csv"
)


print(
    "- region_review.csv"
)


print(
    "- customer_review.csv"
)


print(
    "- data_review_summary.csv"
)


print(
    "\nGenerated charts:"
)


print(
    "- monthly_revenue_review.png"
)


print(
    "- category_revenue_review.png"
)


print(
    "- data_quality_review.png"
)