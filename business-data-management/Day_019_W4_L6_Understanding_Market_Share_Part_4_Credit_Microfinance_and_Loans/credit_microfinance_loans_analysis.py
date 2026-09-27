"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Course: Business Data Management
Day: 019
Lecture: W4_L6
Topic: Understanding Market Share — Part 4 | Credit, Microfinance & Loans

Purpose:
Analyse credit, microfinance and loan lending data,
compare market share, study monthly trends,
and create pivot-style business summaries.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 4,
    "Institution": (
        ["Alpha Finance"] * 6
        + ["Beta Finance"] * 6
        + ["Gamma Finance"] * 6
        + ["Delta Finance"] * 6
    ),
    "Segment": (
        ["Credit"] * 6
        + ["Microfinance"] * 6
        + ["Loans"] * 6
        + ["Microfinance"] * 6
    ),
    "Loans_Cr": [
        520, 540, 565, 590, 620, 650,
        360, 375, 392, 410, 430, 455,
        280, 292, 305, 320, 338, 355,
        205, 214, 224, 235, 248, 262
    ],
    "Borrowers_Lakh": [
        4.2, 4.3, 4.5, 4.7, 4.9, 5.1,
        6.8, 6.9, 7.1, 7.3, 7.5, 7.8,
        3.9, 4.0, 4.2, 4.4, 4.6, 4.8,
        5.2, 5.3, 5.5, 5.7, 5.9, 6.1
    ],
    "NPA_Percent": [
        2.2, 2.1, 2.0, 1.9, 1.9, 1.8,
        2.8, 2.7, 2.6, 2.5, 2.4, 2.3,
        3.4, 3.3, 3.2, 3.1, 3.0, 2.9,
        4.0, 3.9, 3.8, 3.7, 3.6, 3.5
    ]
}

df = pd.DataFrame(data)

total_lending = df["Loans_Cr"].sum()

institution_summary = (
    df.groupby("Institution", as_index=False)
      .agg(
          Total_Lending_Cr=("Loans_Cr", "sum"),
          Total_Borrowers_Lakh=("Borrowers_Lakh", "sum"),
          Average_NPA=("NPA_Percent", "mean")
      )
)

institution_summary["Market_Share_Percent"] = (
    institution_summary["Total_Lending_Cr"]
    / total_lending
    * 100
).round(2)

institution_summary = institution_summary.sort_values(
    "Market_Share_Percent",
    ascending=False
)

monthly_summary = (
    df.groupby("Month", as_index=False)
      .agg(
          Total_Lending_Cr=("Loans_Cr", "sum")
      )
)

monthly_summary["Market_Share_Percent"] = (
    monthly_summary["Total_Lending_Cr"]
    / total_lending
    * 100
).round(2)

segment_summary = (
    df.groupby("Segment", as_index=False)
      .agg(
          Total_Lending_Cr=("Loans_Cr", "sum"),
          Total_Borrowers_Lakh=("Borrowers_Lakh", "sum")
      )
)

segment_summary["Share_Percent"] = (
    segment_summary["Total_Lending_Cr"]
    / total_lending
    * 100
).round(2)

institution_month = pd.pivot_table(
    df,
    values="Loans_Cr",
    index="Institution",
    columns="Month",
    aggfunc="sum"
)

print("\nDAY 019 — CREDIT, MICROFINANCE & LOANS")
print("=" * 70)
print(df)

print("\nInstitution Summary")
print(institution_summary)

print("\nMonthly Summary")
print(monthly_summary)

print("\nSegment Summary")
print(segment_summary)

print("\nInstitution × Month Pivot Table")
print(institution_month)

institution_summary.to_csv(
    "day_019_institution_summary.csv",
    index=False
)

monthly_summary.to_csv(
    "day_019_monthly_summary.csv",
    index=False
)

segment_summary.to_csv(
    "day_019_segment_summary.csv",
    index=False
)

institution_month.to_csv(
    "day_019_institution_month_pivot.csv"
)

plt.figure(figsize=(9, 5))
plt.plot(
    monthly_summary["Month"],
    monthly_summary["Total_Lending_Cr"],
    marker="o"
)
plt.title("Monthly Credit, Microfinance & Loan Lending Trend")
plt.xlabel("Month")
plt.ylabel("Lending (Cr)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
plt.bar(
    institution_summary["Institution"],
    institution_summary["Total_Lending_Cr"]
)
plt.title("Total Lending by Institution")
plt.xlabel("Institution")
plt.ylabel("Lending (Cr)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(
    segment_summary["Segment"],
    segment_summary["Total_Lending_Cr"]
)
plt.title("Lending by Segment")
plt.xlabel("Segment")
plt.ylabel("Lending (Cr)")
plt.tight_layout()
plt.show()

growth = (
    df.groupby("Institution")
      .agg(
          Starting_Lending=("Loans_Cr", "first"),
          Ending_Lending=("Loans_Cr", "last")
      )
)

growth["Growth_Percent"] = (
    (
        growth["Ending_Lending"]
        - growth["Starting_Lending"]
    )
    / growth["Starting_Lending"]
    * 100
).round(2)

growth_leader = growth["Growth_Percent"].idxmax()

share_leader = institution_summary.iloc[0]

print("\nBUSINESS INSIGHTS")
print("=" * 70)

print(
    f"1. {share_leader['Institution']} has the largest "
    f"measured lending share at "
    f"{share_leader['Market_Share_Percent']}%."
)

print(
    f"2. {growth_leader} has the highest Jan-to-Jun "
    f"lending growth in this dataset."
)

print(
    "3. The segment summary compares credit, "
    "microfinance and loan lending volumes."
)

print(
    "4. The institution-month pivot shows how lending "
    "changes across institutions and time."
)

print("\nDay 019 analysis completed successfully.")