# ============================================================
# Day 023 - E-Commerce Data | Post-COVID Sales Analysis
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Course: Business Data Management
# Day: 023
# Topic: E-Commerce Data | Post-COVID Sales Analysis
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# 1. FILE CONFIGURATION
# ============================================================

# Python file and Excel workbook are in the SAME Day 023 folder.
BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# 2. FIND EXCEL WORKBOOK
# ============================================================

excel_files = list(BASE_DIR.glob("*.xlsx"))

if not excel_files:
    raise FileNotFoundError(
        "No Excel (.xlsx) file found in the Day 023 folder."
    )

INPUT_FILE = excel_files[0]


# ============================================================
# 3. START PROGRAM
# ============================================================

print("=" * 70)
print("DAY 023 - POST-COVID E-COMMERCE SALES ANALYSIS")
print("=" * 70)

print("\nPython file:")
print(Path(__file__).name)

print("\nDay 023 folder:")
print(BASE_DIR)

print("\nExcel file selected:")
print(INPUT_FILE.name)


# ============================================================
# 4. LOAD DATASET
# ============================================================

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Ecommerce_Data"
)

print("\n" + "=" * 70)
print("DATASET LOADED")
print("=" * 70)

print("\nFirst five rows:")

print(df.head())


# ============================================================
# 5. DATASET INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

print("\nDataset shape:")

print(df.shape)

print("\nNumber of rows:")

print(df.shape[0])

print("\nNumber of columns:")

print(df.shape[1])

print("\nColumns:")

for column in df.columns:
    print("-", column)

print("\nData types:")

print(df.dtypes)


# ============================================================
# 6. DATA QUALITY CHECK
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

print(df.duplicated().sum())

if "Order_ID" in df.columns:

    print("\nDuplicate Order IDs:")

    print(
        df["Order_ID"].duplicated().sum()
    )


# ============================================================
# 7. UNIQUE VALUES
# ============================================================

print("\n" + "=" * 70)
print("UNIQUE VALUES")
print("=" * 70)

check_columns = [
    "Month",
    "Category",
    "Channel",
    "Region",
    "Customer_Type"
]

for column in check_columns:

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
# 8. OVERALL KPIs
# ============================================================

print("\n" + "=" * 70)
print("OVERALL BUSINESS KPIs")
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
# 9. MONTHLY ANALYSIS
# ============================================================

monthly = (
    df.groupby(
        "Month",
        sort=False
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
    .reset_index()
)

print("\n" + "=" * 70)
print("MONTHLY SUMMARY")
print("=" * 70)

print(monthly)

monthly.to_csv(
    OUTPUT_DIR / "monthly_summary.csv",
    index=False
)


# ============================================================
# 10. CATEGORY ANALYSIS
# ============================================================

category = (
    df.groupby(
        "Category"
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
    .reset_index()
    .sort_values(
        "Revenue_Lakh",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("CATEGORY SUMMARY")
print("=" * 70)

print(category)

category.to_csv(
    OUTPUT_DIR / "category_summary.csv",
    index=False
)


# ============================================================
# 11. CHANNEL ANALYSIS
# ============================================================

channel = (
    df.groupby(
        "Channel"
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
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

print("\n" + "=" * 70)
print("CHANNEL SUMMARY")
print("=" * 70)

print(channel)

channel.to_csv(
    OUTPUT_DIR / "channel_summary.csv",
    index=False
)


# ============================================================
# 12. REGIONAL ANALYSIS
# ============================================================

region = (
    df.groupby(
        "Region"
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
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

print("\n" + "=" * 70)
print("REGION SUMMARY")
print("=" * 70)

print(region)

region.to_csv(
    OUTPUT_DIR / "region_summary.csv",
    index=False
)


# ============================================================
# 13. CUSTOMER TYPE ANALYSIS
# ============================================================

customer = (
    df.groupby(
        "Customer_Type"
    )
    .agg(
        Orders=("Orders", "sum"),
        Units=("Units", "sum"),
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

print("\n" + "=" * 70)
print("CUSTOMER TYPE SUMMARY")
print("=" * 70)

print(customer)

customer.to_csv(
    OUTPUT_DIR / "customer_summary.csv",
    index=False
)


# ============================================================
# 14. TOP PERFORMERS
# ============================================================

top_month = monthly.loc[
    monthly["Revenue_Lakh"].idxmax()
]

top_category = category.iloc[0]

top_channel = channel.iloc[0]

top_region = region.iloc[0]

top_customer = customer.iloc[0]

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
# 15. BUSINESS SUMMARY
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
# 16. MONTHLY REVENUE CHART
# ============================================================

plt.figure(
    figsize=(10, 5)
)

plt.bar(
    monthly["Month"],
    monthly["Revenue_Lakh"]
)

plt.title(
    "Monthly Revenue — Post-COVID E-Commerce"
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
# 17. CATEGORY REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    category["Category"],
    category["Revenue_Lakh"]
)

plt.title(
    "Revenue by Category"
)

plt.xlabel(
    "Category"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "category_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 18. CHANNEL REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    channel["Channel"],
    channel["Revenue_Lakh"]
)

plt.title(
    "Revenue by Channel"
)

plt.xlabel(
    "Channel"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "channel_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 19. REGIONAL REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    region["Region"],
    region["Revenue_Lakh"]
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

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "regional_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 20. CUSTOMER TYPE REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    customer["Customer_Type"],
    customer["Revenue_Lakh"]
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

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "customer_type_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 21. SAVE ANALYSIS WORKBOOK
# ============================================================

output_workbook = (
    OUTPUT_DIR
    / "Day_023_Post_Covid_Sales_Analysis_Output.xlsx"
)

with pd.ExcelWriter(
    output_workbook,
    engine="openpyxl"
) as writer:

    business_summary.to_excel(
        writer,
        sheet_name="Business_Summary",
        index=False
    )

    monthly.to_excel(
        writer,
        sheet_name="Monthly_Summary",
        index=False
    )

    category.to_excel(
        writer,
        sheet_name="Category_Summary",
        index=False
    )

    channel.to_excel(
        writer,
        sheet_name="Channel_Summary",
        index=False
    )

    region.to_excel(
        writer,
        sheet_name="Region_Summary",
        index=False
    )

    customer.to_excel(
        writer,
        sheet_name="Customer_Summary",
        index=False
    )


# ============================================================
# 22. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 70)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

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
    "- Day_023_Post_Covid_Sales_Analysis_Output.xlsx"
)

print(
    "\nDay 023 analysis completed successfully."
)