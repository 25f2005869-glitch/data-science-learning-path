# Day 090 — Processing Business Process Data Using Spreadsheets
# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 090
# Topic: Processing Business Process Data Using Spreadsheets

import os
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# 1. File Configuration
# ---------------------------------------------------------

INPUT_FILE = "Day_090_W12_L3_Processing_Business_Process_Data_Using_Spreadsheets.xlsx"
OUTPUT_DIR = "day_090_outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------------------------------------------------
# 2. Load Business Process Data
# ---------------------------------------------------------

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Business_Process_Data",
    header=2
)

df.columns = df.columns.str.strip()


# ---------------------------------------------------------
# 3. Display Basic Information
# ---------------------------------------------------------

print("\n===== DATASET INFORMATION =====")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())


# ---------------------------------------------------------
# 4. Data Cleaning
# ---------------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

numeric_columns = [
    "Orders",
    "Revenue_Rupee",
    "Cost_Rupee",
    "Delivery_Days",
    "On_Time_Deliveries",
    "Deliveries",
    "Returned_Orders",
    "Customer_Satisfaction_%"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# ---------------------------------------------------------
# 5. Calculated Business Metrics
# ---------------------------------------------------------

df["Profit_Rupee"] = (
    df["Revenue_Rupee"] - df["Cost_Rupee"]
)

df["AOV_Rupee"] = (
    df["Revenue_Rupee"] / df["Orders"].replace(0, pd.NA)
)

df["Cost_Per_Order_Rupee"] = (
    df["Cost_Rupee"] / df["Orders"].replace(0, pd.NA)
)

df["On_Time_Delivery_Rate_%"] = (
    df["On_Time_Deliveries"]
    / df["Deliveries"].replace(0, pd.NA)
    * 100
)

df["Return_Rate_%"] = (
    df["Returned_Orders"]
    / df["Orders"].replace(0, pd.NA)
    * 100
)

df["Profit_Margin_%"] = (
    df["Profit_Rupee"]
    / df["Revenue_Rupee"].replace(0, pd.NA)
    * 100
)


# ---------------------------------------------------------
# 6. Overall KPI Summary
# ---------------------------------------------------------

total_orders = df["Orders"].sum()
total_revenue = df["Revenue_Rupee"].sum()
total_cost = df["Cost_Rupee"].sum()
total_profit = df["Profit_Rupee"].sum()
total_deliveries = df["Deliveries"].sum()
total_on_time = df["On_Time_Deliveries"].sum()
total_returns = df["Returned_Orders"].sum()

overall_aov = (
    total_revenue / total_orders
    if total_orders != 0
    else 0
)

overall_cost_per_order = (
    total_cost / total_orders
    if total_orders != 0
    else 0
)

overall_on_time_rate = (
    total_on_time / total_deliveries * 100
    if total_deliveries != 0
    else 0
)

overall_return_rate = (
    total_returns / total_orders * 100
    if total_orders != 0
    else 0
)

overall_profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue != 0
    else 0
)

overall_customer_satisfaction = (
    df["Customer_Satisfaction_%"].mean()
)


kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Orders",
        "Total Revenue",
        "Total Cost",
        "Total Profit",
        "Average Order Value",
        "Cost per Order",
        "On-Time Delivery Rate",
        "Return Rate",
        "Profit Margin",
        "Average Customer Satisfaction"
    ],
    "Value": [
        total_orders,
        total_revenue,
        total_cost,
        total_profit,
        overall_aov,
        overall_cost_per_order,
        overall_on_time_rate,
        overall_return_rate,
        overall_profit_margin,
        overall_customer_satisfaction
    ]
})


print("\n===== KPI SUMMARY =====")
print(kpi_summary)


# ---------------------------------------------------------
# 7. Function Summary
# ---------------------------------------------------------

function_summary = (
    df.groupby("Business_Function")
    .agg(
        Total_Orders=("Orders", "sum"),
        Total_Revenue_Rupee=("Revenue_Rupee", "sum"),
        Total_Cost_Rupee=("Cost_Rupee", "sum"),
        Total_Profit_Rupee=("Profit_Rupee", "sum"),
        Average_Delivery_Days=("Delivery_Days", "mean"),
        Average_Customer_Satisfaction=(
            "Customer_Satisfaction_%",
            "mean"
        )
    )
    .reset_index()
)


print("\n===== FUNCTION SUMMARY =====")
print(function_summary)


# ---------------------------------------------------------
# 8. Process Summary
# ---------------------------------------------------------

process_summary = (
    df.groupby("Process")
    .agg(
        Total_Orders=("Orders", "sum"),
        Total_Revenue_Rupee=("Revenue_Rupee", "sum"),
        Total_Cost_Rupee=("Cost_Rupee", "sum"),
        Total_Profit_Rupee=("Profit_Rupee", "sum"),
        Average_Delivery_Days=("Delivery_Days", "mean"),
        Total_Returned_Orders=("Returned_Orders", "sum"),
        Average_Customer_Satisfaction=(
            "Customer_Satisfaction_%",
            "mean"
        )
    )
    .reset_index()
)


process_summary["Return_Rate_%"] = (
    process_summary["Total_Returned_Orders"]
    / process_summary["Total_Orders"].replace(0, pd.NA)
    * 100
)


print("\n===== PROCESS SUMMARY =====")
print(process_summary)


# ---------------------------------------------------------
# 9. Monthly Summary
# ---------------------------------------------------------

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_summary = (
    df.groupby("Month")
    .agg(
        Total_Orders=("Orders", "sum"),
        Total_Revenue_Rupee=("Revenue_Rupee", "sum"),
        Total_Cost_Rupee=("Cost_Rupee", "sum"),
        Total_Profit_Rupee=("Profit_Rupee", "sum")
    )
    .reset_index()
)


print("\n===== MONTHLY SUMMARY =====")
print(monthly_summary)


# ---------------------------------------------------------
# 10. Spreadsheet-Style Analysis
# ---------------------------------------------------------

sales_data = df[
    df["Business_Function"] == "Sales"
]

operations_data = df[
    df["Business_Function"] == "Operations"
]

delivery_data = df[
    df["Process"] == "Delivery"
]


print("\n===== FILTERED DATA COUNTS =====")

print("Sales records:", len(sales_data))
print("Operations records:", len(operations_data))
print("Delivery records:", len(delivery_data))


# ---------------------------------------------------------
# 11. Business Insights
# ---------------------------------------------------------

highest_revenue_process = process_summary.loc[
    process_summary["Total_Revenue_Rupee"].idxmax(),
    "Process"
]

highest_cost_function = function_summary.loc[
    function_summary["Total_Cost_Rupee"].idxmax(),
    "Business_Function"
]

highest_orders_process = process_summary.loc[
    process_summary["Total_Orders"].idxmax(),
    "Process"
]

highest_profit_process = process_summary.loc[
    process_summary["Total_Profit_Rupee"].idxmax(),
    "Process"
]

highest_return_process = process_summary.loc[
    process_summary["Return_Rate_%"].idxmax(),
    "Process"
]


business_insights = pd.DataFrame({
    "Question": [
        "Which process generates the highest revenue?",
        "Which function has the highest cost?",
        "Which process has the highest number of orders?",
        "Which process has the highest profit?",
        "Which process has the highest return rate?"
    ],
    "Answer": [
        highest_revenue_process,
        highest_cost_function,
        highest_orders_process,
        highest_profit_process,
        highest_return_process
    ]
})


print("\n===== BUSINESS INSIGHTS =====")
print(business_insights)


# ---------------------------------------------------------
# 12. Save Processed Data
# ---------------------------------------------------------

processed_file = os.path.join(
    OUTPUT_DIR,
    "processed_business_process_data.csv"
)

df.to_csv(
    processed_file,
    index=False
)


# ---------------------------------------------------------
# 13. Save Summary Files
# ---------------------------------------------------------

function_summary.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "function_summary.csv"
    ),
    index=False
)

process_summary.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "process_summary.csv"
    ),
    index=False
)

monthly_summary.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "monthly_summary.csv"
    ),
    index=False
)

kpi_summary.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "kpi_summary.csv"
    ),
    index=False
)

business_insights.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "business_insights.csv"
    ),
    index=False
)


# ---------------------------------------------------------
# 14. Chart 1 — Revenue by Process
# ---------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    process_summary["Process"],
    process_summary["Total_Revenue_Rupee"]
)

plt.title("Revenue by Business Process")
plt.xlabel("Business Process")
plt.ylabel("Revenue (Rupee)")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "revenue_by_process.png"
    )
)

plt.show()


# ---------------------------------------------------------
# 15. Chart 2 — Orders by Business Function
# ---------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    function_summary["Business_Function"],
    function_summary["Total_Orders"]
)

plt.title("Orders by Business Function")
plt.xlabel("Business Function")
plt.ylabel("Total Orders")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "orders_by_function.png"
    )
)

plt.show()


# ---------------------------------------------------------
# 16. Chart 3 — Cost by Business Function
# ---------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    function_summary["Business_Function"],
    function_summary["Total_Cost_Rupee"]
)

plt.title("Cost by Business Function")
plt.xlabel("Business Function")
plt.ylabel("Cost (Rupee)")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "cost_by_function.png"
    )
)

plt.show()


# ---------------------------------------------------------
# 17. Chart 4 — Monthly Revenue
# ---------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_summary["Month"],
    monthly_summary["Total_Revenue_Rupee"],
    marker="o"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rupee)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "monthly_revenue.png"
    )
)

plt.show()


# ---------------------------------------------------------
# 18. Final Output Message
# ---------------------------------------------------------

print("\n========================================")
print("Day 090 analysis completed successfully.")
print("Processed files saved in:", OUTPUT_DIR)
print("========================================")