from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 047
# Topic: Region-wise Revenue and Sales Agent Planning

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_047_W7_L10_Region_Wise_Revenue_and_Sales_Agent_Planning.xlsx"
)

OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Revenue_Agent_Data"
)

# ---------------------------------------
# Region Revenue
# ---------------------------------------

region = (
    df.groupby("Region", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Orders=("Orders", "sum"),
        Sales_Units=("Sales_Units", "sum"),
        Gross_Margin=("Gross_Margin", "sum")
    )
)

region["Revenue_Share_%"] = (
    region["Revenue"] / region["Revenue"].sum()
)

region["Margin_%"] = (
    region["Gross_Margin"] / region["Revenue"]
)

region = (
    region
    .sort_values("Revenue", ascending=False)
    .reset_index(drop=True)
)

# ---------------------------------------
# Sales Agent Performance
# ---------------------------------------

agent = (
    df.groupby("Sales_Agent", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Orders=("Orders", "sum"),
        Sales_Units=("Sales_Units", "sum"),
        Gross_Margin=("Gross_Margin", "sum"),
        Regions_Covered=("Region", "nunique")
    )
)

agent["Revenue_Share_%"] = (
    agent["Revenue"] / agent["Revenue"].sum()
)

agent["Margin_%"] = (
    agent["Gross_Margin"] / agent["Revenue"]
)

agent["Revenue_Rank"] = (
    agent["Revenue"]
    .rank(method="dense", ascending=False)
    .astype(int)
)

agent = (
    agent
    .sort_values("Revenue", ascending=False)
    .reset_index(drop=True)
)

# ---------------------------------------
# Region-Agent Summary
# ---------------------------------------

region_agent = (
    df.groupby(
        ["Region", "Sales_Agent"],
        as_index=False
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Orders=("Orders", "sum"),
        Sales_Units=("Sales_Units", "sum"),
        Gross_Margin=("Gross_Margin", "sum")
    )
)

region_agent["Revenue_Share_%"] = (
    region_agent["Revenue"] /
    region_agent["Revenue"].sum()
)

region_agent = (
    region_agent
    .sort_values("Revenue", ascending=False)
    .reset_index(drop=True)
)

# ---------------------------------------
# Monthly Agent Revenue
# ---------------------------------------

monthly_agent = (
    df.pivot_table(
        index="Month",
        columns="Sales_Agent",
        values="Revenue",
        aggfunc="sum"
    )
    .reset_index()
)

# ---------------------------------------
# Region-Agent Matrix
# ---------------------------------------

region_agent_matrix = (
    df.pivot_table(
        index="Region",
        columns="Sales_Agent",
        values="Revenue",
        aggfunc="sum"
    )
    .reset_index()
)

# ---------------------------------------
# Export CSV files
# ---------------------------------------

region.to_csv(
    OUTPUT_DIR / "region_revenue.csv",
    index=False
)

agent.to_csv(
    OUTPUT_DIR / "sales_agent_performance.csv",
    index=False
)

region_agent.to_csv(
    OUTPUT_DIR / "region_agent_summary.csv",
    index=False
)

monthly_agent.to_csv(
    OUTPUT_DIR / "monthly_agent_revenue.csv",
    index=False
)

region_agent_matrix.to_csv(
    OUTPUT_DIR / "region_agent_matrix.csv",
    index=False
)

# ---------------------------------------
# Chart 1 — Revenue by Region
# ---------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    region["Region"],
    region["Revenue"],
    color="#4472C4"
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_region.png",
    dpi=160
)

plt.close()

# ---------------------------------------
# Chart 2 — Revenue by Sales Agent
# ---------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    agent["Sales_Agent"],
    agent["Revenue"],
    color="#ED7D31"
)

plt.title("Revenue by Sales Agent")
plt.xlabel("Sales Agent")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_sales_agent.png",
    dpi=160
)

plt.close()

# ---------------------------------------
# Chart 3 — Monthly Agent Revenue
# ---------------------------------------

plt.figure(figsize=(10, 5))

agent_colors = {
    "Amit": "#4472C4",
    "Neha": "#ED7D31",
    "Ravi": "#70AD47",
    "Priya": "#8064A2",
    "Karan": "#5B9BD5",
    "Meera": "#A5A5A5"
}

for agent_name, color in agent_colors.items():

    if agent_name in monthly_agent.columns:

        plt.plot(
            monthly_agent["Month"],
            monthly_agent[agent_name],
            marker="o",
            label=agent_name,
            color=color
        )

plt.title("Monthly Revenue by Sales Agent")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_revenue_by_sales_agent.png",
    dpi=160
)

plt.close()

# ---------------------------------------
# Chart 4 — Region-Agent Revenue
# ---------------------------------------

plt.figure(figsize=(11, 5))

x = range(len(region_agent_matrix))

agent_names = [
    "Amit",
    "Neha",
    "Ravi",
    "Priya",
    "Karan",
    "Meera"
]

width = 0.12

for i, agent_name in enumerate(agent_names):

    if agent_name in region_agent_matrix.columns:

        plt.bar(
            [
                value + (i - 2.5) * width
                for value in x
            ],
            region_agent_matrix[agent_name],
            width=width,
            label=agent_name,
            color=agent_colors[agent_name]
        )

plt.xticks(
    list(x),
    region_agent_matrix["Region"]
)

plt.title("Revenue by Region and Sales Agent")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "region_agent_revenue.png",
    dpi=160
)

plt.close()

# ---------------------------------------
# Final Output
# ---------------------------------------

print(
    "Day 047 region-wise revenue and "
    "sales-agent planning analysis completed."
)

print()

print(
    agent[
        [
            "Sales_Agent",
            "Revenue",
            "Revenue_Share_%",
            "Regions_Covered",
            "Revenue_Rank"
        ]
    ]
)