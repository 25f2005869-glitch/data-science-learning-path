"""
Day 094 - Inventory Analytics
Author: Saloni Tiwari
Programme: IIT Madras BS Degree - Diploma Level

A learning exercise using a synthetic practice dataset.
The data does not represent a real company or market.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INPUT_FILE = Path("../Day_094_Inventory_Analytics_Improved.xlsx")
OUTPUT_DIR = Path("inventory_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

PRODUCT_UNIT_COST = {
    "Laptop": 52000, "Keyboard": 1800, "Mouse": 900, "Monitor": 12500,
    "Office Chair": 8500, "Desk": 12000, "Notebook": 120,
    "Printer Paper": 450, "Pen Pack": 180, "Headphones": 2200,
    "Backpack": 1500, "USB Drive": 750
}


def load_data():
    """Load the raw inventory sheet from the workbook."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"{INPUT_FILE} was not found. Keep it beside this script."
        )

    data = pd.read_excel(
        INPUT_FILE,
        sheet_name="Raw_Inventory_Data",
        header=0
    )
    data.columns = data.columns.astype(str).str.strip()
    return data


def clean_data(data):
    """Clean the supplied rows and calculate consistent inventory fields."""
    df = data.copy()

    text_columns = [
        "Inventory_ID", "Product_ID", "Product", "Category",
        "Warehouse", "Supplier", "Stock_Status"
    ]
    for column in text_columns:
        if column in df.columns:
            df[column] = (
                df[column].astype("string")
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
            )

    for column in ["Category", "Warehouse", "Stock_Status", "Supplier"]:
        if column in df.columns:
            df[column] = df[column].str.title()

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    number_columns = [
        "Opening_Stock", "Stock_In", "Stock_Out", "Closing_Stock",
        "Unit_Cost", "Inventory_Value", "Reorder_Level"
    ]
    for column in number_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Remove fully repeated rows, keeping the first occurrence.
    df = df.drop_duplicates().reset_index(drop=True)

    # These are explicit assumptions for this practice dataset.
    df["Stock_In"] = df["Stock_In"].fillna(0)
    df["Stock_Out"] = df["Stock_Out"].fillna(0).clip(lower=0)
    df["Unit_Cost"] = df["Unit_Cost"].fillna(
        df["Product"].map(PRODUCT_UNIT_COST)
    )

    # Rebuild the calculated values rather than using stale source totals.
    df["Closing_Stock"] = (
        df["Opening_Stock"] + df["Stock_In"] - df["Stock_Out"]
    )
    df["Inventory_Value"] = df["Closing_Stock"] * df["Unit_Cost"]
    df["Net_Movement"] = df["Stock_In"] - df["Stock_Out"]

    df["Reorder_Required"] = np.where(
        df["Reorder_Level"].notna()
        & (df["Closing_Stock"] <= df["Reorder_Level"]),
        "Yes", "No"
    )
    df["Stock_Coverage_Status"] = np.where(
        df["Reorder_Required"] == "Yes",
        "Below Reorder Level", "Healthy Stock"
    )
    df["Stock_Turnover_Ratio"] = np.where(
        df["Opening_Stock"] > 0,
        df["Stock_Out"] / df["Opening_Stock"],
        np.nan
    )
    df["Month"] = df["Date"].dt.to_period("M").astype("string")
    return df


def build_reports(df):
    """Create the main inventory summaries and KPI table."""
    product = df.groupby(
        ["Product_ID", "Product", "Category"], as_index=False
    ).agg(
        Closing_Stock=("Closing_Stock", "sum"),
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Inventory_Value=("Inventory_Value", "sum"),
        Reorder_Records=("Reorder_Required", lambda s: (s == "Yes").sum()),
        Records=("Inventory_ID", "count")
    ).sort_values("Inventory_Value", ascending=False)

    category = df.groupby("Category", as_index=False).agg(
        Closing_Stock=("Closing_Stock", "sum"),
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Inventory_Value=("Inventory_Value", "sum"),
        Reorder_Records=("Reorder_Required", lambda s: (s == "Yes").sum()),
        Records=("Inventory_ID", "count")
    ).sort_values("Inventory_Value", ascending=False)

    warehouse = df.groupby("Warehouse", as_index=False).agg(
        Closing_Stock=("Closing_Stock", "sum"),
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Inventory_Value=("Inventory_Value", "sum"),
        Reorder_Records=("Reorder_Required", lambda s: (s == "Yes").sum()),
        Records=("Inventory_ID", "count")
    ).sort_values("Inventory_Value", ascending=False)

    movement = df.groupby("Product", as_index=False).agg(
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Net_Movement=("Net_Movement", "sum")
    ).sort_values("Net_Movement", ascending=False)

    monthly = df.groupby("Month", as_index=False).agg(
        Opening_Stock=("Opening_Stock", "sum"),
        Stock_In=("Stock_In", "sum"),
        Stock_Out=("Stock_Out", "sum"),
        Closing_Stock=("Closing_Stock", "sum"),
        Inventory_Value=("Inventory_Value", "sum")
    )

    opening_total = df["Opening_Stock"].sum()
    utilisation = (
        df["Stock_Out"].sum() / opening_total * 100
        if opening_total > 0 else 0
    )
    kpis = pd.DataFrame([
        ["Total Inventory Value", df["Inventory_Value"].sum()],
        ["Total Stock In", df["Stock_In"].sum()],
        ["Total Stock Out", df["Stock_Out"].sum()],
        ["Total Closing Stock", df["Closing_Stock"].sum()],
        ["Average Inventory Value per Record", df["Inventory_Value"].mean()],
        ["Reorder-Level Records", (df["Reorder_Required"] == "Yes").sum()],
        ["Inventory Utilisation (%)", utilisation]
    ], columns=["KPI", "Value"])

    return product, category, warehouse, movement, monthly, kpis


def save_charts(product, category, warehouse, monthly):
    """Save four charts for the practice analysis."""
    chart_list = [
        (product, "Product", "Inventory_Value", "Inventory value by product",
         "inventory_by_product.png"),
        (category, "Category", "Inventory_Value", "Inventory value by category",
         "inventory_by_category.png"),
        (warehouse, "Warehouse", "Inventory_Value", "Inventory value by warehouse",
         "inventory_by_warehouse.png")
    ]

    for table, label, value, title, filename in chart_list:
        plt.figure(figsize=(11, 5))
        plt.bar(table[label].astype(str), table[value])
        plt.title(title)
        plt.xlabel(label)
        plt.ylabel("Inventory value")
        plt.xticks(rotation=35, ha="right")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / filename, dpi=200)
        plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["Month"], monthly["Inventory_Value"], marker="o")
    plt.title("Monthly inventory value trend")
    plt.xlabel("Month")
    plt.ylabel("Inventory value")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_inventory_trend.png", dpi=200)
    plt.close()


def main():
    raw_data = load_data()
    cleaned = clean_data(raw_data)
    product, category, warehouse, movement, monthly, kpis = build_reports(cleaned)

    cleaned.to_csv(OUTPUT_DIR / "cleaned_inventory_data.csv", index=False)
    product.to_csv(OUTPUT_DIR / "product_inventory_analysis.csv", index=False)
    category.to_csv(OUTPUT_DIR / "category_inventory_analysis.csv", index=False)
    warehouse.to_csv(OUTPUT_DIR / "warehouse_analysis.csv", index=False)
    movement.to_csv(OUTPUT_DIR / "stock_movement_analysis.csv", index=False)
    monthly.to_csv(OUTPUT_DIR / "monthly_inventory_analysis.csv", index=False)
    kpis.to_csv(OUTPUT_DIR / "inventory_kpi_summary.csv", index=False)

    save_charts(product, category, warehouse, monthly)

    print("Inventory analytics completed.")
    print("Dataset type: synthetic practice data")
    print(kpis.to_string(index=False))
    print(f"Output folder: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
