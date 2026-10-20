from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# Day 088 — W12 L1 — How Businesses Operate
# --------------------------------------------------

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 088
# Topic: How Businesses Operate


CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

EXCEL_FILE = BASE_DIR / "Day_088_W12_L1_How_Businesses_Operate.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 1. Read Excel Dataset
# --------------------------------------------------

df = pd.read_excel(
    EXCEL_FILE,
    sheet_name="Business_Process_Data",
    header=2
)


# --------------------------------------------------
# 2. Calculate Business KPIs
# --------------------------------------------------

df["Profit_Rupee"] = (
    df["Revenue_Rupee"] - df["Cost_Rupee"]
)

df["Average_Order_Value"] = (
    df["Revenue_Rupee"] / df["Orders"]
)

df["Cost_Per_Order"] = (
    df["Cost_Rupee"] / df["Orders"]
)

df["On_Time_Rate_%"] = (
    df["On_Time_Deliveries"]
    / df["Deliveries"]
    * 100
)

df["Return_Rate_%"] = (
    df["Returned_Orders"]
    / df["Orders"]
    * 100
)


# --------------------------------------------------
# 3. Process-Level Summary
# --------------------------------------------------

process_summary = (
    df.groupby("Process")
    .agg(
        Orders=("Orders", "sum"),
        Revenue_Rupee=("Revenue_Rupee", "sum"),
        Cost_Rupee=("Cost_Rupee", "sum"),
        Profit_Rupee=("Profit_Rupee", "sum"),
        Deliveries=("Deliveries", "sum"),
        On_Time_Deliveries=("On_Time_Deliveries", "sum"),
        Returned_Orders=("Returned_Orders", "sum"),
        Avg_Delivery_Days=("Delivery_Days", "mean"),
    )
    .reset_index()
)

process_summary["On_Time_Rate_%"] = (
    process_summary["On_Time_Deliveries"]
    / process_summary["Deliveries"]
    * 100
)

process_summary["Return_Rate_%"] = (
    process_summary["Returned_Orders"]
    / process_summary["Orders"]
    * 100
)


# --------------------------------------------------
# 4. Business Function Summary
# --------------------------------------------------

function_summary = (
    df.groupby("Business_Function")
    .agg(
        Orders=("Orders", "sum"),
        Revenue_Rupee=("Revenue_Rupee", "sum"),
        Cost_Rupee=("Cost_Rupee", "sum"),
        Profit_Rupee=("Profit_Rupee", "sum"),
    )
    .reset_index()
)


# --------------------------------------------------
# 5. Overall KPI Summary
# --------------------------------------------------

total_orders = df["Orders"].sum()
total_revenue = df["Revenue_Rupee"].sum()
total_cost = df["Cost_Rupee"].sum()
total_profit = total_revenue - total_cost

total_deliveries = df["Deliveries"].sum()
total_on_time = df["On_Time_Deliveries"].sum()
total_returns = df["Returned_Orders"].sum()

average_order_value = (
    total_revenue / total_orders
)

cost_per_order = (
    total_cost / total_orders
)

on_time_rate = (
    total_on_time / total_deliveries * 100
)

return_rate = (
    total_returns / total_orders * 100
)

profit_margin = (
    total_profit / total_revenue * 100
)


kpis = pd.DataFrame(
    {
        "KPI": [
            "Total Orders",
            "Total Revenue (Rupee)",
            "Total Cost (Rupee)",
            "Total Profit (Rupee)",
            "Average Order Value (Rupee)",
            "Cost Per Order (Rupee)",
            "On-Time Delivery Rate (%)",
            "Return Rate (%)",
            "Profit Margin (%)",
        ],
        "Value": [
            total_orders,
            total_revenue,
            total_cost,
            total_profit,
            average_order_value,
            cost_per_order,
            on_time_rate,
            return_rate,
            profit_margin,
        ],
    }
)


# --------------------------------------------------
# 6. Export Summary CSV Files
# --------------------------------------------------

process_summary.to_csv(
    OUTPUT_DIR / "process_summary.csv",
    index=False
)

function_summary.to_csv(
    OUTPUT_DIR / "function_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "kpi_summary.csv",
    index=False
)


# --------------------------------------------------
# 7. Revenue by Process Chart
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    process_summary["Process"],
    process_summary["Revenue_Rupee"]
)

plt.title("Revenue by Business Process")
plt.xlabel("Process")
plt.ylabel("Revenue (Rupee)")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_process.png",
    dpi=150
)

plt.close()


# --------------------------------------------------
# 8. Profit by Process Chart
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    process_summary["Process"],
    process_summary["Profit_Rupee"]
)

plt.title("Profit by Business Process")
plt.xlabel("Process")
plt.ylabel("Profit (Rupee)")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "profit_by_process.png",
    dpi=150
)

plt.close()


# --------------------------------------------------
# 9. Print Results
# --------------------------------------------------

print("Day 088 analysis completed.")

print(f"Total Orders: {total_orders}")
print(f"Total Revenue: ₹{total_revenue:,.0f}")
print(f"Total Cost: ₹{total_cost:,.0f}")
print(f"Total Profit: ₹{total_profit:,.0f}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Cost Per Order: ₹{cost_per_order:,.2f}")
print(f"On-Time Delivery Rate: {on_time_rate:.2f}%")
print(f"Return Rate: {return_rate:.2f}%")
print(f"Profit Margin: {profit_margin:.2f}%")

print("Outputs saved in:")
print(OUTPUT_DIR)