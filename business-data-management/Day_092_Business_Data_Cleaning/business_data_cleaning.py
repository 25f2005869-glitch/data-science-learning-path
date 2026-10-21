# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 092
# Topic: Business Data Cleaning


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =========================================================
# 1. FILE AND FOLDER SETUP
# =========================================================

input_file = "Day_092_Business_Data_Cleaning.xlsx"
input_sheet = "Raw_Business_Data"

output_folder = "day_092_outputs"

os.makedirs(output_folder, exist_ok=True)


# =========================================================
# 2. READ RAW BUSINESS DATA
# =========================================================

print("\n" + "=" * 60)
print("DAY 092 - BUSINESS DATA CLEANING")
print("=" * 60)

print("\nReading Excel file...")

try:
    df = pd.read_excel(
        input_file,
        sheet_name=input_sheet,
        header=3
    )

except FileNotFoundError:
    print("\nERROR: Excel file not found.")
    print("Make sure the Excel file is in the same folder as this Python file.")
    raise

except Exception as error:
    print("\nERROR while reading Excel file:")
    print(error)
    raise


# =========================================================
# 3. BASIC DATA INSPECTION
# =========================================================

print("\n" + "=" * 60)
print("RAW DATA INSPECTION")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nNumber of Rows:", len(df))
print("Number of Columns:", len(df.columns))

print("\nColumn Names:")

for column in df.columns:
    print("-", column)


# =========================================================
# 4. DATA TYPES
# =========================================================

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)


# =========================================================
# 5. MISSING VALUE CHECK
# =========================================================

print("\n" + "=" * 60)
print("MISSING VALUES BEFORE CLEANING")
print("=" * 60)

missing_before = df.isna().sum()

print(missing_before)


# =========================================================
# 6. DUPLICATE CHECK
# =========================================================

print("\n" + "=" * 60)
print("DUPLICATE CHECK")
print("=" * 60)

duplicate_rows_before = df.duplicated().sum()

print("Duplicate complete rows:", duplicate_rows_before)

if "Record_ID" in df.columns:

    duplicate_record_ids = df["Record_ID"].duplicated(
        keep=False
    ).sum()

    print(
        "Rows having duplicate Record_ID:",
        duplicate_record_ids
    )


# =========================================================
# 7. DATA QUALITY REPORT BEFORE CLEANING
# =========================================================

quality_report_before = pd.DataFrame({
    "Column": df.columns,
    "Data_Type": df.dtypes.astype(str).values,
    "Missing_Values": df.isna().sum().values,
    "Unique_Values": df.nunique(dropna=True).values
})

quality_report_before.to_csv(
    os.path.join(
        output_folder,
        "data_quality_report_before_cleaning.csv"
    ),
    index=False
)


# =========================================================
# 8. CREATE COPY FOR CLEANING
# =========================================================

cleaned = df.copy()


# =========================================================
# 9. CLEAN TEXT COLUMNS
# =========================================================

print("\n" + "=" * 60)
print("TEXT CLEANING")
print("=" * 60)

text_columns = [
    "Customer_Name",
    "Business_Function",
    "Region",
    "Product_Category",
    "Email",
    "Status"
]

for column in text_columns:

    if column in cleaned.columns:

        cleaned[column] = (
            cleaned[column]
            .astype("string")
            .str.strip()
        )

        print(f"Cleaned: {column}")


# =========================================================
# 10. STANDARDISE BUSINESS FUNCTION
# =========================================================

if "Business_Function" in cleaned.columns:

    cleaned["Business_Function"] = (
        cleaned["Business_Function"]
        .str.strip()
        .str.title()
    )

    print("\nBusiness Function values:")
    print(
        cleaned["Business_Function"]
        .dropna()
        .unique()
    )


# =========================================================
# 11. STANDARDISE REGION
# =========================================================

if "Region" in cleaned.columns:

    cleaned["Region"] = (
        cleaned["Region"]
        .str.strip()
        .str.title()
    )

    print("\nRegion values:")
    print(
        cleaned["Region"]
        .dropna()
        .unique()
    )


# =========================================================
# 12. STANDARDISE PRODUCT CATEGORY
# =========================================================

if "Product_Category" in cleaned.columns:

    cleaned["Product_Category"] = (
        cleaned["Product_Category"]
        .str.strip()
        .str.title()
    )

    print("\nProduct Category values:")
    print(
        cleaned["Product_Category"]
        .dropna()
        .unique()
    )


# =========================================================
# 13. CLEAN CUSTOMER NAMES
# =========================================================

if "Customer_Name" in cleaned.columns:

    cleaned["Customer_Name"] = (
        cleaned["Customer_Name"]
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
        .str.title()
    )


# =========================================================
# 14. CLEAN EMAIL
# =========================================================

if "Email" in cleaned.columns:

    cleaned["Email"] = (
        cleaned["Email"]
        .str.replace(" ", "", regex=False)
        .str.strip()
        .str.lower()
    )


# =========================================================
# 15. STANDARDISE STATUS
# =========================================================

if "Status" in cleaned.columns:

    cleaned["Status"] = (
        cleaned["Status"]
        .str.strip()
        .str.title()
    )

    print("\nStatus values:")
    print(
        cleaned["Status"]
        .dropna()
        .unique()
    )


# =========================================================
# 16. CLEAN DATE COLUMN
# =========================================================

print("\n" + "=" * 60)
print("DATE CLEANING")
print("=" * 60)

if "Date" in cleaned.columns:

    cleaned["Date"] = pd.to_datetime(
        cleaned["Date"],
        errors="coerce",
        dayfirst=True
    )

    invalid_dates = cleaned["Date"].isna().sum()

    print(
        "Invalid or missing dates after conversion:",
        invalid_dates
    )


# =========================================================
# 17. CLEAN NUMERIC COLUMNS
# =========================================================

print("\n" + "=" * 60)
print("NUMERIC DATA CLEANING")
print("=" * 60)

numeric_columns = [
    "Orders",
    "Revenue_Rupee",
    "Cost_Rupee",
    "Returned_Orders",
    "Customer_Satisfaction_%"
]

for column in numeric_columns:

    if column in cleaned.columns:

        cleaned[column] = (
            cleaned[column]
            .astype("string")
            .str.replace(",", "", regex=False)
            .str.replace("₹", "", regex=False)
            .str.strip()
        )

        cleaned[column] = pd.to_numeric(
            cleaned[column],
            errors="coerce"
        )

        print(f"Converted to numeric: {column}")


# =========================================================
# 18. HANDLE NEGATIVE ORDERS
# =========================================================

if "Orders" in cleaned.columns:

    mask = (
        cleaned["Orders"] < 0
    ).fillna(False)

    negative_orders = mask.sum()

    print(
        "\nNegative Orders found:",
        negative_orders
    )

    cleaned.loc[
        mask,
        "Orders"
    ] = np.nan


# =========================================================
# 19. HANDLE NEGATIVE COST
# =========================================================

if "Cost_Rupee" in cleaned.columns:

    mask = (
        cleaned["Cost_Rupee"] < 0
    ).fillna(False)

    negative_cost = mask.sum()

    print(
        "Negative Cost values found:",
        negative_cost
    )

    cleaned.loc[
        mask,
        "Cost_Rupee"
    ] = np.nan


# =========================================================
# 20. HANDLE NEGATIVE RETURNED ORDERS
# =========================================================

if "Returned_Orders" in cleaned.columns:

    mask = (
        cleaned["Returned_Orders"] < 0
    ).fillna(False)

    negative_returns = mask.sum()

    print(
        "Negative Returned Orders found:",
        negative_returns
    )

    cleaned.loc[
        mask,
        "Returned_Orders"
    ] = np.nan


# =========================================================
# 21. VALIDATE CUSTOMER SATISFACTION
# =========================================================

if "Customer_Satisfaction_%" in cleaned.columns:

    below_zero = (
        cleaned["Customer_Satisfaction_%"] < 0
    ).fillna(False)

    above_hundred = (
        cleaned["Customer_Satisfaction_%"] > 100
    ).fillna(False)

    invalid_satisfaction = (
        below_zero | above_hundred
    ).fillna(False)

    print(
        "\nInvalid Customer Satisfaction values:",
        invalid_satisfaction.sum()
    )

    cleaned.loc[
        invalid_satisfaction,
        "Customer_Satisfaction_%"
    ] = np.nan


# =========================================================
# 22. REMOVE EXACT DUPLICATE ROWS
# =========================================================

print("\n" + "=" * 60)
print("DUPLICATE REMOVAL")
print("=" * 60)

rows_before_duplicates = len(cleaned)

cleaned = cleaned.drop_duplicates()

rows_after_duplicates = len(cleaned)

duplicates_removed = (
    rows_before_duplicates -
    rows_after_duplicates
)

print(
    "Duplicate rows removed:",
    duplicates_removed
)


# =========================================================
# 23. CALCULATE PROFIT
# =========================================================

print("\n" + "=" * 60)
print("BUSINESS METRICS")
print("=" * 60)

if {
    "Revenue_Rupee",
    "Cost_Rupee"
}.issubset(cleaned.columns):

    cleaned["Profit_Rupee"] = (
        cleaned["Revenue_Rupee"]
        -
        cleaned["Cost_Rupee"]
    )


# =========================================================
# 24. CALCULATE PROFIT MARGIN
# =========================================================

if {
    "Revenue_Rupee",
    "Profit_Rupee"
}.issubset(cleaned.columns):

    revenue_valid = (
        cleaned["Revenue_Rupee"]
        .notna()
        &
        cleaned["Revenue_Rupee"]
        .ne(0)
    )

    cleaned["Profit_Margin_%"] = np.nan

    cleaned.loc[
        revenue_valid,
        "Profit_Margin_%"
    ] = (
        cleaned.loc[
            revenue_valid,
            "Profit_Rupee"
        ]
        /
        cleaned.loc[
            revenue_valid,
            "Revenue_Rupee"
        ]
    ) * 100


# =========================================================
# 25. CALCULATE RETURN RATE
# =========================================================

if {
    "Orders",
    "Returned_Orders"
}.issubset(cleaned.columns):

    orders_valid = (
        cleaned["Orders"]
        .notna()
        &
        cleaned["Orders"]
        .ne(0)
    )

    cleaned["Return_Rate_%"] = np.nan

    cleaned.loc[
        orders_valid,
        "Return_Rate_%"
    ] = (
        cleaned.loc[
            orders_valid,
            "Returned_Orders"
        ]
        /
        cleaned.loc[
            orders_valid,
            "Orders"
        ]
    ) * 100


# =========================================================
# 26. VALIDATION REPORT
# =========================================================

print("\n" + "=" * 60)
print("VALIDATION")
print("=" * 60)

validation_rows = []


# Blank Record ID

if "Record_ID" in cleaned.columns:

    blank_record_id = cleaned["Record_ID"].isna().sum()

else:

    blank_record_id = 0


validation_rows.append({
    "Check": "Blank Record_ID",
    "Invalid_Count": blank_record_id
})


# Negative Orders

if "Orders" in cleaned.columns:

    negative_orders_after = (
        cleaned["Orders"] < 0
    ).fillna(False).sum()

else:

    negative_orders_after = 0


validation_rows.append({
    "Check": "Negative Orders",
    "Invalid_Count": negative_orders_after
})


# Negative Cost

if "Cost_Rupee" in cleaned.columns:

    negative_cost_after = (
        cleaned["Cost_Rupee"] < 0
    ).fillna(False).sum()

else:

    negative_cost_after = 0


validation_rows.append({
    "Check": "Negative Cost",
    "Invalid_Count": negative_cost_after
})


# Negative Returned Orders

if "Returned_Orders" in cleaned.columns:

    negative_returns_after = (
        cleaned["Returned_Orders"] < 0
    ).fillna(False).sum()

else:

    negative_returns_after = 0


validation_rows.append({
    "Check": "Negative Returned Orders",
    "Invalid_Count": negative_returns_after
})


# Satisfaction below 0

if "Customer_Satisfaction_%" in cleaned.columns:

    satisfaction_below_zero = (
        cleaned["Customer_Satisfaction_%"] < 0
    ).fillna(False).sum()

else:

    satisfaction_below_zero = 0


validation_rows.append({
    "Check": "Customer Satisfaction Below 0",
    "Invalid_Count": satisfaction_below_zero
})


# Satisfaction above 100

if "Customer_Satisfaction_%" in cleaned.columns:

    satisfaction_above_100 = (
        cleaned["Customer_Satisfaction_%"] > 100
    ).fillna(False).sum()

else:

    satisfaction_above_100 = 0


validation_rows.append({
    "Check": "Customer Satisfaction Above 100",
    "Invalid_Count": satisfaction_above_100
})


validation = pd.DataFrame(
    validation_rows
)

print(validation)


# =========================================================
# 27. SAVE VALIDATION REPORT
# =========================================================

validation.to_csv(
    os.path.join(
        output_folder,
        "validation_report.csv"
    ),
    index=False
)


# =========================================================
# 28. CLEANING SUMMARY
# =========================================================

cleaning_summary = pd.DataFrame({
    "Metric": [
        "Raw Records",
        "Cleaned Records",
        "Rows Removed",
        "Raw Columns",
        "Final Columns",
        "Duplicate Rows Removed"
    ],
    "Value": [
        len(df),
        len(cleaned),
        len(df) - len(cleaned),
        len(df.columns),
        len(cleaned.columns),
        duplicates_removed
    ]
})

print("\n" + "=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)

print(cleaning_summary)


cleaning_summary.to_csv(
    os.path.join(
        output_folder,
        "cleaning_summary.csv"
    ),
    index=False
)


# =========================================================
# 29. BEFORE AND AFTER COMPARISON
# =========================================================

before_after = pd.DataFrame({
    "Metric": [
        "Number of Records",
        "Number of Columns",
        "Missing Values",
        "Duplicate Rows"
    ],
    "Before_Cleaning": [
        len(df),
        len(df.columns),
        df.isna().sum().sum(),
        df.duplicated().sum()
    ],
    "After_Cleaning": [
        len(cleaned),
        len(cleaned.columns),
        cleaned.isna().sum().sum(),
        cleaned.duplicated().sum()
    ]
})

before_after.to_csv(
    os.path.join(
        output_folder,
        "before_after_comparison.csv"
    ),
    index=False
)


# =========================================================
# 30. CLEANED DATA QUALITY REPORT
# =========================================================

quality_report_after = pd.DataFrame({
    "Column": cleaned.columns,
    "Data_Type": cleaned.dtypes.astype(str).values,
    "Missing_Values": cleaned.isna().sum().values,
    "Unique_Values": cleaned.nunique(dropna=True).values
})

quality_report_after.to_csv(
    os.path.join(
        output_folder,
        "data_quality_report_after_cleaning.csv"
    ),
    index=False
)


# =========================================================
# 31. BUSINESS FUNCTION ANALYSIS
# =========================================================

print("\n" + "=" * 60)
print("BUSINESS FUNCTION ANALYSIS")
print("=" * 60)

if "Business_Function" in cleaned.columns:

    aggregation_dict = {}

    if "Orders" in cleaned.columns:
        aggregation_dict["Orders"] = ("Orders", "sum")

    if "Revenue_Rupee" in cleaned.columns:
        aggregation_dict["Revenue_Rupee"] = (
            "Revenue_Rupee",
            "sum"
        )

    if "Cost_Rupee" in cleaned.columns:
        aggregation_dict["Cost_Rupee"] = (
            "Cost_Rupee",
            "sum"
        )

    if "Profit_Rupee" in cleaned.columns:
        aggregation_dict["Profit_Rupee"] = (
            "Profit_Rupee",
            "sum"
        )

    if "Customer_Satisfaction_%" in cleaned.columns:
        aggregation_dict[
            "Average_Customer_Satisfaction"
        ] = (
            "Customer_Satisfaction_%",
            "mean"
        )

    function_summary = (
        cleaned
        .groupby(
            "Business_Function",
            dropna=False
        )
        .agg(**aggregation_dict)
        .reset_index()
    )

    print(function_summary)

    function_summary.to_csv(
        os.path.join(
            output_folder,
            "business_function_analysis.csv"
        ),
        index=False
    )

else:

    function_summary = pd.DataFrame()


# =========================================================
# 32. SAVE CLEANED DATA
# =========================================================

cleaned_csv = os.path.join(
    output_folder,
    "cleaned_business_data.csv"
)

cleaned.to_csv(
    cleaned_csv,
    index=False
)

print("\nCleaned dataset saved:")
print(cleaned_csv)


# =========================================================
# 33. EXPORT CLEANED DATA TO EXCEL
# =========================================================

cleaned_excel = os.path.join(
    output_folder,
    "cleaned_business_data.xlsx"
)

with pd.ExcelWriter(
    cleaned_excel,
    engine="openpyxl"
) as writer:

    cleaned.to_excel(
        writer,
        sheet_name="Cleaned_Data",
        index=False
    )

    validation.to_excel(
        writer,
        sheet_name="Validation",
        index=False
    )

    cleaning_summary.to_excel(
        writer,
        sheet_name="Cleaning_Summary",
        index=False
    )

    before_after.to_excel(
        writer,
        sheet_name="Before_After",
        index=False
    )

    quality_report_after.to_excel(
        writer,
        sheet_name="Quality_Report",
        index=False
    )

    if not function_summary.empty:

        function_summary.to_excel(
            writer,
            sheet_name="Function_Analysis",
            index=False
        )


# =========================================================
# 34. REVENUE CHART
# =========================================================

if not function_summary.empty and "Revenue_Rupee" in function_summary.columns:

    plt.figure(figsize=(10, 6))

    plt.bar(
        function_summary["Business_Function"].astype(str),
        function_summary["Revenue_Rupee"]
    )

    plt.title(
        "Revenue by Business Function"
    )

    plt.xlabel(
        "Business Function"
    )

    plt.ylabel(
        "Revenue (Rupee)"
    )

    plt.xticks(
        rotation=30
    )

    plt.tight_layout()

    revenue_chart = os.path.join(
        output_folder,
        "revenue_by_business_function.png"
    )

    plt.savefig(
        revenue_chart,
        dpi=150
    )

    plt.close()

    print("\nRevenue chart saved:")
    print(revenue_chart)


# =========================================================
# 35. PROFIT CHART
# =========================================================

if not function_summary.empty and "Profit_Rupee" in function_summary.columns:

    plt.figure(figsize=(10, 6))

    plt.bar(
        function_summary["Business_Function"].astype(str),
        function_summary["Profit_Rupee"]
    )

    plt.title(
        "Profit by Business Function"
    )

    plt.xlabel(
        "Business Function"
    )

    plt.ylabel(
        "Profit (Rupee)"
    )

    plt.xticks(
        rotation=30
    )

    plt.tight_layout()

    profit_chart = os.path.join(
        output_folder,
        "profit_by_business_function.png"
    )

    plt.savefig(
        profit_chart,
        dpi=150
    )

    plt.close()

    print("\nProfit chart saved:")
    print(profit_chart)


# =========================================================
# 36. FINAL MISSING VALUE REPORT
# =========================================================

print("\n" + "=" * 60)
print("MISSING VALUES AFTER CLEANING")
print("=" * 60)

print(
    cleaned.isna().sum()
)


# =========================================================
# 37. FINAL DATA PREVIEW
# =========================================================

print("\n" + "=" * 60)
print("CLEANED DATA PREVIEW")
print("=" * 60)

print(
    cleaned.head()
)


# =========================================================
# 38. FINAL OUTPUT SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nRaw records:", len(df))
print("Cleaned records:", len(cleaned))
print("Rows removed:", len(df) - len(cleaned))
print("Duplicate rows removed:", duplicates_removed)

print("\nOutput folder:")
print(
    os.path.abspath(output_folder)
)

print("\nGenerated files include:")

for filename in sorted(
    os.listdir(output_folder)
):

    print("-", filename)

print("\n" + "=" * 60)
print("DAY 092 COMPLETED")
print("=" * 60)