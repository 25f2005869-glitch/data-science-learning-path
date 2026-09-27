"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Course: Business Data Management
Day: 017
Lecture: W4_L4
Topic: Understanding Market Share — Part 2 | Loan Data and Pivot Tables

Purpose:
Analyse loan data by company, region and loan type,
calculate market share, create pivot-style summaries,
and visualize business findings.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Company": ["Alpha Finance"]*4 + ["Beta Finance"]*4 + ["Gamma Finance"]*4 + ["Delta Finance"]*4,
    "Region": ["North", "South", "East", "West"] * 4,
    "Loan_Type": ["Personal", "Personal", "Home", "Home"] * 4,
    "Loans": [
        4200, 3600, 2800, 2300,
        3500, 3100, 2200, 1900,
        2500, 2100, 1500, 1200,
        1800, 1500, 1000, 900
    ],
    "Customers": [
        15500, 13200, 8200, 7100,
        14200, 12100, 6900, 6100,
        9800, 8700, 4800, 4100,
        7200, 6300, 3300, 3000
    ]
}

df = pd.DataFrame(data)

print("\nDAY 017 — LOAN DATA")
print("=" * 60)
print(df)

total_loans = df["Loans"].sum()
df["Market_Share"] = df["Loans"] / total_loans

company_summary = (
    df.groupby("Company", as_index=False)
      .agg(
          Total_Loans=("Loans", "sum"),
          Total_Customers=("Customers", "sum")
      )
)

company_summary["Market_Share_Percent"] = (
    company_summary["Total_Loans"] / total_loans * 100
).round(2)

company_summary = company_summary.sort_values(
    "Market_Share_Percent",
    ascending=False
)

region_summary = (
    df.groupby("Region", as_index=False)
      .agg(
          Total_Loans=("Loans", "sum"),
          Total_Customers=("Customers", "sum")
      )
)

region_summary["Market_Share_Percent"] = (
    region_summary["Total_Loans"] / total_loans * 100
).round(2)

loan_type_summary = (
    df.groupby("Loan_Type", as_index=False)
      .agg(
          Total_Loans=("Loans", "sum"),
          Total_Customers=("Customers", "sum")
      )
)

loan_type_summary["Share_Percent"] = (
    loan_type_summary["Total_Loans"] / total_loans * 100
).round(2)

print("\nCompany Summary:")
print(company_summary)

print("\nRegion Summary:")
print(region_summary)

print("\nLoan Type Summary:")
print(loan_type_summary)

pivot_company_region = pd.pivot_table(
    df,
    values="Loans",
    index="Company",
    columns="Region",
    aggfunc="sum",
    fill_value=0
)

print("\nCompany × Region Pivot Table:")
print(pivot_company_region)

company_summary.to_csv(
    "day_017_company_summary.csv",
    index=False
)

region_summary.to_csv(
    "day_017_region_summary.csv",
    index=False
)

loan_type_summary.to_csv(
    "day_017_loan_type_summary.csv",
    index=False
)

pivot_company_region.to_csv(
    "day_017_company_region_pivot.csv"
)

plt.figure(figsize=(9, 5))
plt.bar(
    company_summary["Company"],
    company_summary["Total_Loans"]
)
plt.title("Total Loans by Company")
plt.xlabel("Company")
plt.ylabel("Total Loans")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(
    region_summary["Region"],
    region_summary["Total_Loans"]
)
plt.title("Total Loans by Region")
plt.xlabel("Region")
plt.ylabel("Total Loans")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 7))
plt.pie(
    company_summary["Total_Loans"],
    labels=company_summary["Company"],
    autopct="%1.1f%%"
)
plt.title("Market Share by Company")
plt.tight_layout()
plt.show()

leader = company_summary.iloc[0]
smallest = company_summary.iloc[-1]

largest_region = region_summary.sort_values(
    "Total_Loans",
    ascending=False
).iloc[0]

print("\nBUSINESS INSIGHTS")
print("=" * 60)

print(
    f"1. {leader['Company']} has the highest measured "
    f"market share at {leader['Market_Share_Percent']}%."
)

print(
    f"2. {smallest['Company']} has the lowest measured "
    f"market share at {smallest['Market_Share_Percent']}%."
)

print(
    f"3. {largest_region['Region']} has the highest regional "
    f"loan volume at {largest_region['Total_Loans']}."
)

print(
    "4. The company-region pivot shows where each company's "
    "loan volume is concentrated."
)

print("\nDay 017 analysis completed successfully.")