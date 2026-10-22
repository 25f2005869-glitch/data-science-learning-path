# Day_094_Inventory_Analytics
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 094
# Topic: Inventory Analytics

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. FILE PATH
# ============================================================

possible_paths = [
    "data/Day_094_Inventory_Analytics.xlsx",
    "Day_094_Inventory_Analytics.xlsx",
    "../data/Day_094_Inventory_Analytics.xlsx",
    "/mnt/data/Day_094_Inventory_Analytics.xlsx"
]

input_file = next((path for path in possible_paths if os.path.exists(path)), None)

if input_file is None:
    raise FileNotFoundError(
        "Day_094_Inventory_Analytics.xlsx was not found."
    )

output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)


# ============================================================
# 2. LOAD RAW INVENTORY DATA
# ============================================================

df = pd.read_excel(
    input_file,
    sheet_name="Raw_Inventory_Data",
    header=3
)

df.columns = df.columns.astype(str).str.strip()


# ============================================================
# 3. DATA INSPECTION
# ============================================================

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isna().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())


# ============================================================
# 4. STANDARDISE COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
)


# ============================================================
# 5. CLEAN TEXT COLUMNS
# ============================================================

text_columns = [
    "Product_ID",
    "Product",
    "Category",
    "Warehouse",
    "Supplier",
    "Stock_Status"
]

for column in text_columns:
    if column in df.columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.title()
        )


# ============================================================
# 6. CLEAN DATE COLUMN
# ============================================================

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )


# ============================================================
# 7. CONVERT NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    "Opening_Stock",
    "Stock_In",
    "Stock_Out",
    "Closing_Stock",
    "Unit_Cost",
    "Inventory_Value",
    "Reorder_Level"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# 8. PRODUCT REFERENCE FOR MISSING UNIT COST
# ============================================================

product_unit_cost = {
    "Laptop": 52000,
    "Keyboard": 1800,
    "Mouse": 900,
    "Monitor": 12500,
    "Office Chair": 8500,
    "Desk": 12000,
    "Notebook": 120,
    "Printer Paper": 450,
    "Pen Pack": 180,
    "Headphones": 2200,
    "Backpack": 1500,
    "Usb Drive": 750
}

if "Unit_Cost" in df.columns:
    df["Unit_Cost"] = df["Unit_Cost"].fillna(
        df["Product"].map(product_unit_cost)
    )


# ============================================================
# 9. HANDLE MISSING STOCK IN
# ============================================================

if "Stock_In" in df.columns:
    df["Stock_In"] = df["Stock_In"].fillna(0)


# ============================================================
# 10. HANDLE NEGATIVE STOCK OUT
# ============================================================

if "Stock_Out" in df.columns:
    df["Stock_Out"] = df["Stock_Out"].fillna(0)

    df.loc[df["Stock_Out"] < 0, "Stock_Out"] = 0


# ============================================================
# 11. CALCULATE CLOSING STOCK
# ============================================================

df["Calculated_Closing_Stock"] = (
    df["Opening_Stock"]
    + df["Stock_In"]
    - df["Stock_Out"]
)

df["Closing_Stock"] = df["Closing_Stock"].fillna(
    df["Calculated_Closing_Stock"]
)

df["Closing_Stock"] = df["Calculated_Closing_Stock"]


# ============================================================
# 12. CALCULATE INVENTORY VALUE
# ============================================================

df["Inventory_Value"] = (
    df["Closing_Stock"]
    * df["Unit_Cost"]
)


# ============================================================
# 13. REMOVE EXACT DUPLICATES
# ============================================================

df = df.drop_duplicates().reset_index(drop=True)


# ============================================================
# 14. ADD NET MOVEMENT
# ============================================================

df["Net_Movement"] = (
    df["Stock_In"]
    - df["Stock_Out"]
)


# ============================================================
# 15. REORDER CONDITION
# ============================================================

df["Reorder_Required"] = np.where(
    df["Closing_Stock"] <= df["Reorder_Level"],
    "Yes",
    "No"
)


# ============================================================
# 16. STOCK VALUE
# ============================================================

df["Stock_Value"] = (
    df["Closing_Stock"]
    * df["Unit_Cost"]
)


# ============================================================
# 17. STOCK TURNOVER RATIO
# ============================================================

df["Stock_Turnover_Ratio"] = np.where(
    df["Opening_Stock"] > 0,
    df["Stock_Out"] / df["Opening_Stock"],
    0
)


# ============================================================
# 18. STOCK COVERAGE STATUS
# ============================================================

df["Stock_Coverage_Status"] = np.where(
    df["Closing_Stock"] <= df["Reorder_Level"],
    "Below Reorder Level",
    "Healthy Stock"
)


# ============================================================
# 19. INVENTORY SUMMARY
# ============================================================

inventory_summary = pd.DataFrame({
    "Metric": [
        "Total Inventory Value",
        "Total Stock In",
        "Total Stock Out",
        "Total Closing Stock",
        "Average Inventory Value",
        "Reorder-Level Records"
    ],
    "Value": [
        df["Inventory_Value"].sum(),
        df["Stock_In"].sum(),
        df["Stock_Out"].sum(),
        df["Closing_Stock"].sum(),
        df["Inventory_Value"].mean(),
        (df["Reorder_Required"] == "Yes").sum()
    ]
})

inventory_summary.to_csv(
    f"{output_dir}/inventory_summary.csv",
    index=False
)


# ============================================================
# 20. PRODUCT INVENTORY ANALYSIS
# ============================================================

product_analysis = (
    df.groupby(
        ["Product_ID", "Product", "Category"],
        as_index=False
    )
    .agg(
        Closing_Stock=("Closing_Stock", "sum"),
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Inventory_Value=("Inventory_Value", "sum"),
        Reorder_Records=("Reorder_Required", lambda x: (x == "Yes").sum())
    )
    .sort_values(
        "Inventory_Value",
        ascending=False
    )
)

product_analysis.to_csv(
    f"{output_dir}/product_inventory_analysis.csv",
    index=False
)


# ============================================================
# 21. CATEGORY ANALYSIS
# ============================================================

category_analysis = (
    df.groupby(
        "Category",
        as_index=False
    )
    .agg(
        Closing_Stock=("Closing_Stock", "sum"),
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Inventory_Value=("Inventory_Value", "sum"),
        Reorder_Records=("Reorder_Required", lambda x: (x == "Yes").sum()),
        Records=("Inventory_ID", "count")
    )
    .sort_values(
        "Inventory_Value",
        ascending=False
    )
)

category_analysis.to_csv(
    f"{output_dir}/category_inventory_analysis.csv",
    index=False
)


# ============================================================
# 22. WAREHOUSE ANALYSIS
# ============================================================

warehouse_analysis = (
    df.groupby(
        "Warehouse",
        as_index=False
    )
    .agg(
        Closing_Stock=("Closing_Stock", "sum"),
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Inventory_Value=("Inventory_Value", "sum"),
        Reorder_Records=("Reorder_Required", lambda x: (x == "Yes").sum()),
        Records=("Inventory_ID", "count")
    )
    .sort_values(
        "Inventory_Value",
        ascending=False
    )
)

warehouse_analysis.to_csv(
    f"{output_dir}/warehouse_analysis.csv",
    index=False
)


# ============================================================
# 23. MONTHLY INVENTORY ANALYSIS
# ============================================================

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_inventory = (
    df.groupby(
        "Month",
        as_index=False
    )
    .agg(
        Opening_Stock=("Opening_Stock", "sum"),
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Closing_Stock=("Closing_Stock", "sum"),
        Inventory_Value=("Inventory_Value", "sum")
    )
)

monthly_inventory.to_csv(
    f"{output_dir}/monthly_inventory_analysis.csv",
    index=False
)


# ============================================================
# 24. STOCK MOVEMENT ANALYSIS
# ============================================================

stock_movement = (
    df.groupby(
        "Product",
        as_index=False
    )
    .agg(
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Net_Movement=("Net_Movement", "sum")
    )
    .sort_values(
        "Net_Movement",
        ascending=False
    )
)

stock_movement.to_csv(
    f"{output_dir}/stock_movement_analysis.csv",
    index=False
)


# ============================================================
# 25. INVENTORY KPIs
# ============================================================

total_opening_stock = df["Opening_Stock"].sum()
total_stock_out = df["Stock_Out"].sum()

if total_opening_stock > 0:
    inventory_utilisation = (
        total_stock_out
        / total_opening_stock
        * 100
    )
else:
    inventory_utilisation = 0

inventory_kpi = pd.DataFrame({
    "KPI": [
        "Total Inventory Value",
        "Total Stock In",
        "Total Stock Out",
        "Total Closing Stock",
        "Average Inventory Value",
        "Reorder-Level Records",
        "Inventory Utilisation (%)"
    ],
    "Value": [
        df["Inventory_Value"].sum(),
        df["Stock_In"].sum(),
        df["Stock_Out"].sum(),
        df["Closing_Stock"].sum(),
        df["Inventory_Value"].mean(),
        (df["Reorder_Required"] == "Yes").sum(),
        inventory_utilisation
    ]
})

inventory_kpi.to_csv(
    f"{output_dir}/inventory_kpi_summary.csv",
    index=False
)


# ============================================================
# 26. SAVE CLEANED DATA
# ============================================================

df.to_csv(
    f"{output_dir}/cleaned_inventory_data.csv",
    index=False
)


# ============================================================
# 27. CHART — INVENTORY VALUE BY PRODUCT
# ============================================================

product_chart = product_analysis.head(12)

plt.figure(figsize=(12, 6))

plt.bar(
    product_chart["Product"],
    product_chart["Inventory_Value"]
)

plt.title("Inventory Value by Product")
plt.xlabel("Product")
plt.ylabel("Inventory Value")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    f"{output_dir}/inventory_by_product.png",
    dpi=300
)

plt.close()


# ============================================================
# 28. CHART — INVENTORY VALUE BY CATEGORY
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    category_analysis["Category"],
    category_analysis["Inventory_Value"]
)

plt.title("Inventory Value by Category")
plt.xlabel("Category")
plt.ylabel("Inventory Value")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    f"{output_dir}/inventory_by_category.png",
    dpi=300
)

plt.close()


# ============================================================
# 29. CHART — INVENTORY VALUE BY WAREHOUSE
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    warehouse_analysis["Warehouse"],
    warehouse_analysis["Inventory_Value"]
)

plt.title("Inventory Value by Warehouse")
plt.xlabel("Warehouse")
plt.ylabel("Inventory Value")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    f"{output_dir}/inventory_by_warehouse.png",
    dpi=300
)

plt.close()


# ============================================================
# 30. CHART — MONTHLY INVENTORY VALUE TREND
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_inventory["Month"],
    monthly_inventory["Inventory_Value"],
    marker="o"
)

plt.title("Monthly Inventory Value Trend")
plt.xlabel("Month")
plt.ylabel("Inventory Value")

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    f"{output_dir}/monthly_inventory_trend.png",
    dpi=300
)

plt.close()


# ============================================================
# 31. FINAL OUTPUT
# ============================================================

print("\n===== INVENTORY ANALYTICS COMPLETED =====")

print("\nCleaned Records:", len(df))

print(
    "Total Inventory Value:",
    round(df["Inventory_Value"].sum(), 2)
)

print(
    "Total Stock In:",
    round(df["Stock_In"].sum(), 2)
)

print(
    "Total Stock Out:",
    round(df["Stock_Out"].sum(), 2)
)

print(
    "Total Closing Stock:",
    round(df["Closing_Stock"].sum(), 2)
)

print(
    "Reorder-Level Records:",
    int((df["Reorder_Required"] == "Yes").sum())
)

print(
    "Inventory Utilisation:",
    round(inventory_utilisation, 2),
    "%"
)

print("\nOutput files saved in:", output_dir)