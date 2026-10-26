"""
Day 099 - Power BI Extension
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Day: 099
Topic: Power BI Extension

Prepares reference CSV files from the Day 099 workbook.
The interactive report itself is created in Power BI Desktop.
"""

from pathlib import Path
import pandas as pd


def find_workbook():
    candidates = [
        Path("/mnt/data/Day_099_Power_BI_Extension.xlsx"),
        Path(__file__).resolve().parent.parent / "data" / "Day_099_Power_BI_Extension.xlsx",
        Path(__file__).resolve().parent.parent / "Day_099_Power_BI_Extension.xlsx",
    ]

    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError("Day_099_Power_BI_Extension.xlsx was not found.")


def main():
    workbook = find_workbook()
    output_dir = workbook.parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    sales = pd.read_excel(workbook, sheet_name="SalesData")
    customers = pd.read_excel(
        workbook, sheet_name="Customer Dimension (Dim_Customer)"
    )
    products = pd.read_excel(
        workbook, sheet_name="Product Dimension (Dim_Product)"
    )
    dates = pd.read_excel(
        workbook, sheet_name="Date Dimension (Dim_Date)"
    )

    sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")

    for column in ["Quantity", "Unit_Price", "Discount_%", "Revenue", "Cost"]:
        if column in sales.columns:
            sales[column] = pd.to_numeric(sales[column], errors="coerce")

    sales["Revenue"] = sales["Revenue"].fillna(
        sales["Quantity"].fillna(0) * sales["Unit_Price"].fillna(0)
    )
    sales["Cost"] = sales["Cost"].fillna(0)
    sales["Profit"] = sales["Revenue"] - sales["Cost"]

    sales.to_csv(output_dir / "sales_data_for_power_bi.csv", index=False)
    customers.to_csv(output_dir / "dim_customer.csv", index=False)
    products.to_csv(output_dir / "dim_product.csv", index=False)
    dates.to_csv(output_dir / "dim_date.csv", index=False)

    summary = pd.DataFrame({
        "Metric": [
            "Total Revenue",
            "Total Cost",
            "Total Profit",
            "Total Orders",
            "Total Quantity",
            "Customers",
        ],
        "Value": [
            sales["Revenue"].sum(),
            sales["Cost"].sum(),
            sales["Profit"].sum(),
            sales["Order_ID"].nunique(),
            sales["Quantity"].sum(),
            sales["Customer_ID"].nunique(),
        ],
    })

    summary.to_csv(output_dir / "power_bi_summary.csv", index=False)

    print("Day 099 Power BI preparation completed.")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
