# ============================================================
# Day 024 - Review of Key Questions
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Course: Business Data Management
# Day: 024
# Topic: Review of Key Questions
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# 1. FILE CONFIGURATION
# ============================================================

# Python file और Excel workbook SAME Day 024 folder में हैं.
BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# 2. FIND EXCEL WORKBOOK
# ============================================================

# Day 024 folder में मौजूद Excel file automatically find होगी.
excel_files = list(BASE_DIR.glob("*.xlsx"))

if not excel_files:
    raise FileNotFoundError(
        "No Excel (.xlsx) file found in the Day 024 folder."
    )

INPUT_FILE = excel_files[0]


# ============================================================
# 3. START PROGRAM
# ============================================================

print("=" * 70)
print("DAY 024 - REVIEW OF KEY QUESTIONS")
print("=" * 70)

print("\nPython file:")
print(Path(__file__).name)

print("\nDay 024 folder:")
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
# 8. OVERALL BUSINESS KPIs
# ============================================================

print("\n" + "=" * 70)
print("OVERALL BUSINESS KPIs")
print("=" * 70)

total_revenue = (
    df["Revenue_Lakh"].sum()
)

total_orders = (
    df["Orders"].sum()
)

total_units = (
    df["Units"].sum()
)

average_discount = (
    df["Discount_Percent"].mean()
)

print(
    f"\nTotal Revenue (Lakh): "
    f"{total_revenue:.2f}"
)

print(
    f"Total Orders: "
    f"{total_orders}"
)

print(
    f"Total Units: "
    f"{total_units}"
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


# ============================================================
# 14. FIND ANSWERS TO KEY QUESTIONS
# ============================================================

highest_month = monthly.loc[
    monthly["Revenue_Lakh"].idxmax()
]

highest_order_month = monthly.loc[
    monthly["Orders"].idxmax()
]

highest_category = category.iloc[0]

highest_channel = channel.iloc[0]

highest_region = region.iloc[0]

highest_customer = customer.iloc[0]

highest_discount_category = category.loc[
    category["Average_Discount"].idxmax()
]


# ============================================================
# 15. KEY QUESTION REVIEW
# ============================================================

print("\n" + "=" * 70)
print("REVIEW OF KEY QUESTIONS")
print("=" * 70)

print(
    "\nQ1. What is the total revenue?"
)

print(
    f"Answer: {total_revenue:.2f} lakh"
)


print(
    "\nQ2. Which month has the highest revenue?"
)

print(
    f"Answer: {highest_month['Month']}"
)


print(
    "\nQ3. How does monthly revenue change?"
)

print(
    "Answer: Review the Monthly_Summary "
    "table and compare each month."
)


print(
    "\nQ4. Which category contributes the most revenue?"
)

print(
    f"Answer: {highest_category['Category']}"
)


print(
    "\nQ5. Which channel contributes the most revenue?"
)

print(
    f"Answer: {highest_channel['Channel']}"
)


print(
    "\nQ6. Which region contributes the most revenue?"
)

print(
    f"Answer: {highest_region['Region']}"
)


print(
    "\nQ7. How do New and Returning customers compare?"
)

print(
    f"Answer: {highest_customer['Customer_Type']} "
    "has the higher revenue in this dataset."
)


print(
    "\nQ8. Which month has the highest order volume?"
)

print(
    f"Answer: {highest_order_month['Month']}"
)


print(
    "\nQ9. Which category has the highest average discount?"
)

print(
    f"Answer: "
    f"{highest_discount_category['Category']}"
)


print(
    "\nQ10. What additional data could strengthen "
    "the analysis?"
)

print(
    "Answer: Profit, customer acquisition, "
    "website traffic, returns, detailed geography, "
    "and historical business context."
)


# ============================================================
# 16. EXPORT CSV FILES
# ============================================================

monthly.to_csv(
    OUTPUT_DIR / "monthly_summary.csv",
    index=False
)

category.to_csv(
    OUTPUT_DIR / "category_summary.csv",
    index=False
)

channel.to_csv(
    OUTPUT_DIR / "channel_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "region_summary.csv",
    index=False
)

customer.to_csv(
    OUTPUT_DIR / "customer_summary.csv",
    index=False
)


# ============================================================
# 17. REVIEW ANSWERS DATAFRAME
# ============================================================

answers = pd.DataFrame(
    {
        "Question": [
            "Total revenue",
            "Highest revenue month",
            "Monthly revenue trend",
            "Highest revenue category",
            "Highest revenue channel",
            "Highest revenue region",
            "Top customer type by revenue",
            "Highest order-volume month",
            "Highest average-discount category",
            "Additional data needed"
        ],
        "Answer": [
            round(
                total_revenue,
                2
            ),
            highest_month["Month"],
            "Review Monthly_Summary",
            highest_category["Category"],
            highest_channel["Channel"],
            highest_region["Region"],
            highest_customer["Customer_Type"],
            highest_order_month["Month"],
            highest_discount_category["Category"],
            "Profit, acquisition, traffic, returns, "
            "geography and historical context"
        ]
    }
)


# ============================================================
# 18. SAVE REVIEW ANSWERS
# ============================================================

answers.to_csv(
    OUTPUT_DIR / "review_answers.csv",
    index=False
)


# ============================================================
# 19. MONTHLY REVENUE CHART
# ============================================================

plt.figure(
    figsize=(10, 5)
)

plt.bar(
    monthly["Month"],
    monthly["Revenue_Lakh"]
)

plt.title(
    "Monthly Revenue — Review"
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
    OUTPUT_DIR / "review_monthly_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 20. CATEGORY REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    category["Category"],
    category["Revenue_Lakh"]
)

plt.title(
    "Revenue by Category — Review"
)

plt.xlabel(
    "Category"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "review_category_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 21. CHANNEL REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    channel["Channel"],
    channel["Revenue_Lakh"]
)

plt.title(
    "Revenue by Channel — Review"
)

plt.xlabel(
    "Channel"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "review_channel_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 22. REGIONAL REVENUE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    region["Region"],
    region["Revenue_Lakh"]
)

plt.title(
    "Revenue by Region — Review"
)

plt.xlabel(
    "Region"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "review_region_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 23. CUSTOMER TYPE CHART
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    customer["Customer_Type"],
    customer["Revenue_Lakh"]
)

plt.title(
    "Revenue by Customer Type — Review"
)

plt.xlabel(
    "Customer Type"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "review_customer_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 24. CREATE OUTPUT EXCEL
# ============================================================

output_workbook = (
    OUTPUT_DIR
    / "Day_024_Review_of_Key_Questions_Output.xlsx"
)

with pd.ExcelWriter(
    output_workbook,
    engine="openpyxl"
) as writer:

    answers.to_excel(
        writer,
        sheet_name="Review_Answers",
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
# 25. FINAL OUTPUT
# ============================================================

print("\n" + "=" * 70)
print("DAY 024 COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nOutput folder:")
print(OUTPUT_DIR)

print("\nGenerated CSV files:")

print(
    "- monthly_summary.csv"
)

print(
    "- category_summary.csv"
)

print(
    "- channel_summary.csv"
)

print(
    "- region_summary.csv"
)

print(
    "- customer_summary.csv"
)

print(
    "- review_answers.csv"
)

print("\nGenerated charts:")

print(
    "- review_monthly_revenue.png"
)

print(
    "- review_category_revenue.png"
)

print(
    "- review_channel_revenue.png"
)

print(
    "- review_region_revenue.png"
)

print(
    "- review_customer_revenue.png"
)

print("\nGenerated workbook:")

print(
    "- Day_024_Review_of_Key_Questions_Output.xlsx"
)

print(
    "\nDay 024 review and analysis completed successfully."
)