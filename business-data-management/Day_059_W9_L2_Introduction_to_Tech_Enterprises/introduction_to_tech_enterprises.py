from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Author: Saloni Tiwari
# Programme: IIT Madras BS Degree — Diploma Level
# Day: 059
# Topic: Introduction to Tech Enterprises

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_059_W9_L2_Introduction_to_Tech_Enterprises.xlsx"
OUTPUT_DIR = BASE_DIR / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Tech_Enterprise_Data",
    header=2
)

sector = (
    df.groupby(
        "Technology_Sector",
        as_index=False
    )
    .agg(
        Enterprises=("Enterprise_ID", "count"),
        Employees=("Employees", "sum"),
        Avg_Revenue_Lakh=("Annual_Revenue_Lakh", "mean"),
        Total_Revenue_Lakh=("Annual_Revenue_Lakh", "sum"),
        Avg_Active_Clients=("Active_Clients", "mean"),
        Total_New_Clients=("New_Clients", "sum"),
        Avg_Satisfaction=("Client_Satisfaction", "mean"),
    )
)

region = (
    df.groupby(
        "Region",
        as_index=False
    )
    .agg(
        Enterprises=("Enterprise_ID", "count"),
        Employees=("Employees", "sum"),
        Total_Revenue_Lakh=("Annual_Revenue_Lakh", "sum"),
        Avg_Revenue_Lakh=("Annual_Revenue_Lakh", "mean"),
        Total_Active_Clients=("Active_Clients", "sum"),
        Total_New_Clients=("New_Clients", "sum"),
        Avg_Satisfaction=("Client_Satisfaction", "mean"),
    )
)

model = (
    df.groupby(
        "Business_Model",
        as_index=False
    )
    .agg(
        Enterprises=("Enterprise_ID", "count"),
        Employees=("Employees", "sum"),
        Total_Revenue_Lakh=("Annual_Revenue_Lakh", "sum"),
        Avg_Revenue_Lakh=("Annual_Revenue_Lakh", "mean"),
        Total_Active_Clients=("Active_Clients", "sum"),
        Avg_Satisfaction=("Client_Satisfaction", "mean"),
    )
)

kpis = pd.DataFrame({
    "Metric": [
        "Total Technology Enterprises",
        "Total Employees",
        "Total Annual Revenue (Lakh)",
        "Average Enterprise Revenue (Lakh)",
        "Total Active Clients",
        "Total New Clients",
        "Average Client Satisfaction",
    ],
    "Value": [
        len(df),
        df["Employees"].sum(),
        df["Annual_Revenue_Lakh"].sum(),
        df["Annual_Revenue_Lakh"].mean(),
        df["Active_Clients"].sum(),
        df["New_Clients"].sum(),
        df["Client_Satisfaction"].mean(),
    ],
})

sector.to_csv(
    OUTPUT_DIR / "technology_sector_summary.csv",
    index=False
)

region.to_csv(
    OUTPUT_DIR / "technology_region_summary.csv",
    index=False
)

model.to_csv(
    OUTPUT_DIR / "business_model_summary.csv",
    index=False
)

kpis.to_csv(
    OUTPUT_DIR / "technology_enterprise_kpis.csv",
    index=False
)

plt.figure(figsize=(9, 5))

plt.bar(
    sector["Technology_Sector"],
    sector["Employees"],
    color="#4472C4"
)

plt.title(
    "Employees by Technology Sector"
)

plt.xlabel(
    "Technology Sector"
)

plt.ylabel(
    "Employees"
)

plt.xticks(
    rotation=35
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "employees_by_technology_sector.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    sector["Technology_Sector"],
    sector["Total_Revenue_Lakh"],
    color="#ED7D31"
)

plt.title(
    "Revenue by Technology Sector"
)

plt.xlabel(
    "Technology Sector"
)

plt.ylabel(
    "Revenue (Lakh)"
)

plt.xticks(
    rotation=35
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_technology_sector.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    region["Region"],
    region["Total_Active_Clients"],
    color="#70AD47"
)

plt.title(
    "Active Clients by Region"
)

plt.xlabel(
    "Region"
)

plt.ylabel(
    "Active Clients"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "active_clients_by_region.png",
    dpi=160
)

plt.close()

plt.figure(figsize=(9, 5))

plt.bar(
    sector["Technology_Sector"],
    sector["Avg_Satisfaction"],
    color="#8064A2"
)

plt.title(
    "Average Client Satisfaction by Technology Sector"
)

plt.xlabel(
    "Technology Sector"
)

plt.ylabel(
    "Satisfaction Score"
)

plt.ylim(
    0,
    5
)

plt.xticks(
    rotation=35
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "client_satisfaction_by_sector.png",
    dpi=160
)

plt.close()

print(
    "Day 059 analysis complete."
)

print(
    f"Input: {INPUT_FILE}"
)

print(
    f"Output folder: {OUTPUT_DIR}"
)