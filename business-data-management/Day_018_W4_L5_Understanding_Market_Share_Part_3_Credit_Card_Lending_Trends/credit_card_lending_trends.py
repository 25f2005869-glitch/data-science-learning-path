"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Course: Business Data Management
Day: 018
Lecture: W4_L5
Topic: Understanding Market Share — Part 3 | Credit Card Lending Trends
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 4,
    "Bank": (
        ["Alpha Finance"] * 6
        + ["Beta Finance"] * 6
        + ["Gamma Finance"] * 6
        + ["Delta Finance"] * 6
    ),
    "Credit_Card_Loans_Cr": [
        420, 438, 455, 472, 491, 515,
        350, 362, 375, 388, 402, 420,
        245, 252, 261, 270, 282, 295,
        180, 186, 193, 201, 210, 221
    ],
    "Active_Cards_Lakh": [
        8.4, 8.7, 9.0, 9.3, 9.6, 10.0,
        7.2, 7.4, 7.7, 7.9, 8.2, 8.5,
        5.4, 5.5, 5.7, 5.9, 6.1, 6.4,
        4.1, 4.2, 4.4, 4.5, 4.7, 4.9
    ],
    "Delinquency_Percent": [
        2.1, 2.0, 2.0, 1.9, 1.9, 1.8,
        2.7, 2.6, 2.5, 2.4, 2.4, 2.3,
        3.1, 3.0, 2.9, 2.8, 2.7, 2.6,
        3.6, 3.5, 3.4, 3.3, 3.2, 3.1
    ]
}

df = pd.DataFrame(data)

total = df["Credit_Card_Loans_Cr"].sum()

bank_summary = (
    df.groupby("Bank", as_index=False)
    .agg(
        Total_Lending_Cr=("Credit_Card_Loans_Cr", "sum"),
        Active_Cards_Lakh=("Active_Cards_Lakh", "sum"),
        Avg_Delinquency=("Delinquency_Percent", "mean")
    )
)

bank_summary["Market_Share_Percent"] = (
    bank_summary["Total_Lending_Cr"] / total * 100
).round(2)

monthly = (
    df.groupby("Month", as_index=False)
    .agg(
        Total_Lending_Cr=("Credit_Card_Loans_Cr", "sum")
    )
)

monthly["Monthly_Share_Percent"] = (
    monthly["Total_Lending_Cr"] / total * 100
).round(2)

trend = pd.pivot_table(
    df,
    values="Credit_Card_Loans_Cr",
    index="Month",
    columns="Bank",
    aggfunc="sum"
)

print("\nDAY 018 — CREDIT CARD LENDING TRENDS")
print("=" * 65)
print(df)

print("\nBank Summary")
print(bank_summary)

print("\nMonthly Market Summary")
print(monthly)

print("\nBank Monthly Trend")
print(trend)

bank_summary.to_csv(
    "day_018_bank_summary.csv",
    index=False
)

monthly.to_csv(
    "day_018_monthly_summary.csv",
    index=False
)

trend.to_csv(
    "day_018_bank_monthly_trend.csv"
)

plt.figure(figsize=(9, 5))
plt.plot(
    monthly["Month"],
    monthly["Total_Lending_Cr"],
    marker="o"
)
plt.title("Total Credit Card Lending Trend")
plt.xlabel("Month")
plt.ylabel("Lending (Cr)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
plt.bar(
    bank_summary["Bank"],
    bank_summary["Total_Lending_Cr"]
)
plt.title("Total Credit Card Lending by Bank")
plt.xlabel("Bank")
plt.ylabel("Lending (Cr)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

for bank in df["Bank"].unique():
    subset = df[df["Bank"] == bank]

    plt.plot(
        subset["Month"],
        subset["Credit_Card_Loans_Cr"],
        marker="o",
        label=bank
    )

plt.title("Bank-wise Credit Card Lending Trends")
plt.xlabel("Month")
plt.ylabel("Lending (Cr)")
plt.legend()
plt.tight_layout()
plt.show()

leader = bank_summary.sort_values(
    "Market_Share_Percent",
    ascending=False
).iloc[0]

highest_growth = (
    df.groupby("Bank")
    .agg(
        First_Month=("Credit_Card_Loans_Cr", "first"),
        Last_Month=("Credit_Card_Loans_Cr", "last")
    )
)

highest_growth["Growth_Percent"] = (
    (
        highest_growth["Last_Month"]
        - highest_growth["First_Month"]
    )
    / highest_growth["First_Month"]
    * 100
).round(2)

growth_leader = highest_growth[
    "Growth_Percent"
].idxmax()

print("\nBUSINESS INSIGHTS")
print("=" * 65)

print(
    f"1. {leader['Bank']} has the largest measured "
    f"lending share at {leader['Market_Share_Percent']}%."
)

print(
    f"2. {growth_leader} shows the highest Jan-to-Jun "
    f"lending growth in this dataset."
)

print(
    "3. Monthly totals provide a time-based view "
    "of credit card lending activity."
)

print(
    "4. Bank-level trends help compare both scale "
    "and direction of lending."
)

print("\nDay 018 analysis completed successfully.")