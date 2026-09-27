# ============================================================
# Day 022 - Introduction to the Case Study
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Course: Business Data Management
# Day: 022
# Topic: Introduction to the Case Study
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# 1. FILE CONFIGURATION
# ============================================================

# This Python file and Excel file are in the SAME folder.
BASE_DIR = Path(__file__).resolve().parent

# Find Excel workbook in the current Day 022 folder.
excel_files = list(BASE_DIR.glob("*.xlsx"))

if not excel_files:
    raise FileNotFoundError(
        "No Excel (.xlsx) file found in the Day 022 folder."
    )

# Select the Excel workbook.
INPUT_FILE = excel_files[0]

# Output folder.
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 70)
print("DAY 022 - INTRODUCTION TO THE CASE STUDY")
print("=" * 70)

print("\nPython file:")
print(Path(__file__).name)

print("\nDay 022 folder:")
print(BASE_DIR)

print("\nExcel file:")
print(INPUT_FILE.name)


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Case_Study_Data"
)

print("\n" + "=" * 70)
print("DATASET LOADED")
print("=" * 70)

print("\nDataset loaded successfully.")

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 3. DATASET INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

print("\nNumber of rows:")
print(df.shape[0])

print("\nNumber of columns:")
print(df.shape[1])

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")

for column in df.columns:
    print("-", column)

print("\nData types:")
print(df.dtypes)

print("\nDataset information:")
df.info()


# ============================================================
# 4. DATA QUALITY CHECK
# ============================================================

print("\n" + "=" * 70)
print("DATA QUALITY CHECK")
print("=" * 70)

print("\nMissing values:")

missing_values = df.isna().sum()

print(missing_values)

print("\nTotal missing values:")

print(missing_values.sum())

print("\nDuplicate rows:")

duplicate_rows = df.duplicated().sum()

print(duplicate_rows)


# ============================================================
# 5. DUPLICATE ORDER CHECK
# ============================================================

if "Order_ID" in df.columns:

    duplicate_orders = (
        df["Order_ID"]
        .duplicated()
        .sum()
    )

    print("\nDuplicate Order IDs:")

    print(duplicate_orders)


# ============================================================
# 6. UNIQUE VALUES
# ============================================================

print("\n" + "=" * 70)
print("UNIQUE VALUES")
print("=" * 70)

columns_to_check = [
    "Month",
    "Category",
    "Channel",
    "Region",
    "Customer_Type"
]

for column in columns_to_check:

    if column in df.columns:

        print(
            f"\nUnique values in {column}:"
        )

        values = (
            df[column]
            .dropna()
            .unique()
        )

        for value in values:
            print("-", value)


# ============================================================
# 7. OVERALL BUSINESS SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("OVERALL BUSINESS SUMMARY")
print("=" * 70)

total_orders = df["Orders"].sum()

total_units = df["Units"].sum()

total_revenue = df["Revenue_Lakh"].sum()

average_discount = (
    df["Discount_Percent"].mean()
)

print(
    f"\nTotal Orders: {total_orders}"
)

print(
    f"Total Units: {total_units}"
)

print(
    f"Total Revenue (Lakh): "
    f"{total_revenue:.2f}"
)

print(
    f"Average Discount (%): "
    f"{average_discount:.2f}"
)


# ============================================================
# 8. MONTHLY ANALYSIS
# ============================================================

monthly_summary = (
    df.groupby(
        "Month",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        ),
        Average_Discount=(
            "Discount_Percent",
            "mean"
        )
    )
)

print("\n" + "=" * 70)
print("MONTHLY SUMMARY")
print("=" * 70)

print(monthly_summary)

monthly_summary.to_csv(
    OUTPUT_DIR / "monthly_summary.csv",
    index=False
)


# ============================================================
# 9. CATEGORY ANALYSIS
# ============================================================

category_summary = (
    df.groupby(
        "Category",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        ),
        Average_Discount=(
            "Discount_Percent",
            "mean"
        )
    )
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("CATEGORY SUMMARY")
print("=" * 70)

print(category_summary)

category_summary.to_csv(
    OUTPUT_DIR / "category_summary.csv",
    index=False
)


# ============================================================
# 10. CHANNEL ANALYSIS
# ============================================================

channel_summary = (
    df.groupby(
        "Channel",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        ),
        Average_Discount=(
            "Discount_Percent",
            "mean"
        )
    )
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("CHANNEL SUMMARY")
print("=" * 70)

print(channel_summary)

channel_summary.to_csv(
    OUTPUT_DIR / "channel_summary.csv",
    index=False
)


# ============================================================
# 11. REGIONAL ANALYSIS
# ============================================================

region_summary = (
    df.groupby(
        "Region",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        ),
        Average_Discount=(
            "Discount_Percent",
            "mean"
        )
    )
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("REGION SUMMARY")
print("=" * 70)

print(region_summary)

region_summary.to_csv(
    OUTPUT_DIR / "region_summary.csv",
    index=False
)


# ============================================================
# 12. CUSTOMER TYPE ANALYSIS
# ============================================================

customer_summary = (
    df.groupby(
        "Customer_Type",
        as_index=False
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        ),
        Average_Discount=(
            "Discount_Percent",
            "mean"
        )
    )
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("CUSTOMER TYPE SUMMARY")
print("=" * 70)

print(customer_summary)

customer_summary.to_csv(
    OUTPUT_DIR / "customer_summary.csv",
    index=False
)


# ============================================================
# 13. TOP PERFORMING SEGMENTS
# ============================================================

top_month = monthly_summary.loc[
    monthly_summary["Revenue_Lakh"].idxmax()
]

top_category = category_summary.iloc[0]

top_channel = channel_summary.iloc[0]

top_region = region_summary.iloc[0]

top_customer = customer_summary.iloc[0]

print("\n" + "=" * 70)
print("TOP PERFORMING SEGMENTS")
print("=" * 70)

print(
    f"\nHighest Revenue Month: "
    f"{top_month['Month']}"
)

print(
    f"Highest Revenue Category: "
    f"{top_category['Category']}"
)

print(
    f"Highest Revenue Channel: "
    f"{top_channel['Channel']}"
)

print(
    f"Highest Revenue Region: "
    f"{top_region['Region']}"
)

print(
    f"Highest Revenue Customer Type: "
    f"{top_customer['Customer_Type']}"
)


# ============================================================
# 14. BUSINESS SUMMARY TABLE
# ============================================================

business_summary = pd.DataFrame(
    {
        "Metric": [
            "Total Orders",
            "Total Units",
            "Total Revenue (Lakh)",
            "Average Discount (%)",
            "Highest Revenue Month",
            "Highest Revenue Category",
            "Highest Revenue Channel",
            "Highest Revenue Region",
            "Highest Revenue Customer Type"
        ],
        "Value": [
            total_orders,
            total_units,
            round(
                total_revenue,
                2
            ),
            round(
                average_discount,
                2
            ),
            top_month["Month"],
            top_category["Category"],
            top_channel["Channel"],
            top_region["Region"],
            top_customer["Customer_Type"]
        ]
    }
)

print("\n" + "=" * 70)
print("BUSINESS SUMMARY")
print("=" * 70)

print(business_summary)

business_summary.to_csv(
    OUTPUT_DIR / "business_summary.csv",
    index=False
)


# ============================================================
# 15. MONTHLY REVENUE CHART
# ============================================================

monthly_chart = (
    df.groupby(
        "Month",
        as_index=False
    )
    .agg(
        Revenue_Lakh=(
            "Revenue_Lakh",
            "sum"
        )
    )
)

plt.figure(
    figsize=(10, 5)
)

plt.bar(
    monthly_chart["Month"],
    monthly_chart["Revenue_Lakh"]
)

plt.title(
    "Monthly Revenue Analysis"
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
    OUTPUT_DIR / "monthly_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 16. CATEGORY REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    category_summary["Category"],
    category_summary["Revenue_Lakh"]
)

plt.title(
    "Revenue by Product Category"
)

plt.xlabel(
    "Category"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "category_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 17. CHANNEL REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    channel_summary["Channel"],
    channel_summary["Revenue_Lakh"]
)

plt.title(
    "Revenue by Sales Channel"
)

plt.xlabel(
    "Channel"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "channel_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 18. REGIONAL REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    region_summary["Region"],
    region_summary["Revenue_Lakh"]
)

plt.title(
    "Revenue by Region"
)

plt.xlabel(
    "Region"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "regional_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 19. CUSTOMER TYPE REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    customer_summary["Customer_Type"],
    customer_summary["Revenue_Lakh"]
)

plt.title(
    "Revenue by Customer Type"
)

plt.xlabel(
    "Customer Type"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "customer_type_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 20. BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 70)
print("BUSINESS INSIGHTS")
print("=" * 70)

print(
    f"\n1. Total revenue generated is "
    f"{total_revenue:.2f} lakh."
)

print(
    f"2. The highest-revenue month is "
    f"{top_month['Month']}."
)

print(
    f"3. The highest-revenue category is "
    f"{top_category['Category']}."
)

print(
    f"4. The highest-revenue channel is "
    f"{top_channel['Channel']}."
)

print(
    f"5. The highest-revenue region is "
    f"{top_region['Region']}."
)

print(
    f"6. The highest-revenue customer type is "
    f"{top_customer['Customer_Type']}."
)

print(
    "\nThese findings should be interpreted "
    "within the complete case-study context."
)


# ============================================================
# 21. SAVE ANALYSIS WORKBOOK
# ============================================================

summary_file = (
    OUTPUT_DIR
    / "Day_022_Case_Study_Analysis_Output.xlsx"
)

with pd.ExcelWriter(
    summary_file,
    engine="openpyxl"
) as writer:

    business_summary.to_excel(
        writer,
        sheet_name="Business_Summary",
        index=False
    )

    monthly_summary.to_excel(
        writer,
        sheet_name="Monthly_Summary",
        index=False
    )

    category_summary.to_excel(
        writer,
        sheet_name="Category_Summary",
        index=False
    )

    channel_summary.to_excel(
        writer,
        sheet_name="Channel_Summary",
        index=False
    )

    region_summary.to_excel(
        writer,
        sheet_name="Region_Summary",
        index=False
    )

    customer_summary.to_excel(
        writer,
        sheet_name="Customer_Summary",
        index=False
    )


# ============================================================
# 22. COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 70)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nOutput folder:")
print(OUTPUT_DIR)

print("\nGenerated CSV files:")

print("- monthly_summary.csv")
print("- category_summary.csv")
print("- channel_summary.csv")
print("- region_summary.csv")
print("- customer_summary.csv")
print("- business_summary.csv")

print("\nGenerated charts:")

print("- monthly_revenue.png")
print("- category_revenue.png")
print("- channel_revenue.png")
print("- regional_revenue.png")
print("- customer_type_revenue.png")

print("\nGenerated workbook:")

print(
    "- Day_022_Case_Study_Analysis_Output.xlsx"
)

print(
    "\nDay 022 case-study analysis is complete."
)