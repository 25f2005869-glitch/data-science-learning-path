"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Course: Business Data Management
Day: 016
Lecture: W4_L3
Topic: Understanding Market Share — Part 1

Purpose:
Practical market-share analysis using Python,
Pandas, Matplotlib and Seaborn.
"""

# ============================================================
# 01. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 02. CREATE BUSINESS DATA
# ============================================================

data = {
    "Company": [
        "Alpha Finance",
        "Beta Finance",
        "Gamma Finance",
        "Delta Finance"
    ],
    "Loans": [
        14900,
        12500,
        8500,
        6100
    ],
    "Customers": [
        64100,
        55300,
        38900,
        28400
    ],
    "Revenue_Lakh": [
        2980,
        2510,
        1700,
        1220
    ]
}


# ============================================================
# 03. CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(data)

print("\n" + "=" * 60)
print("BUSINESS DATA")
print("=" * 60)

print(df)


# ============================================================
# 04. CHECK DATASET INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(df.info())


# ============================================================
# 05. CHECK BASIC STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("BASIC STATISTICS")
print("=" * 60)

print(df.describe())


# ============================================================
# 06. CALCULATE TOTAL MARKET LOANS
# ============================================================

total_market_loans = df["Loans"].sum()

print("\n" + "=" * 60)
print("TOTAL MARKET LOANS")
print("=" * 60)

print("Total Market Loans:", total_market_loans)


# ============================================================
# 07. CALCULATE MARKET SHARE
# ============================================================

df["Market_Share"] = (
    df["Loans"] / total_market_loans
)

print("\n" + "=" * 60)
print("MARKET SHARE")
print("=" * 60)

print(
    df[
        [
            "Company",
            "Loans",
            "Market_Share"
        ]
    ]
)


# ============================================================
# 08. CONVERT MARKET SHARE INTO PERCENTAGE
# ============================================================

df["Market_Share_Percent"] = (
    df["Market_Share"] * 100
)

print("\n" + "=" * 60)
print("MARKET SHARE PERCENTAGE")
print("=" * 60)

print(
    df[
        [
            "Company",
            "Loans",
            "Market_Share_Percent"
        ]
    ]
)


# ============================================================
# 09. ROUND MARKET SHARE
# ============================================================

df["Market_Share_Percent"] = (
    df["Market_Share_Percent"].round(2)
)

print("\nRounded Market Share:")
print(
    df[
        [
            "Company",
            "Market_Share_Percent"
        ]
    ]
)


# ============================================================
# 10. VERIFY MARKET SHARE TOTAL
# ============================================================

share_total = df["Market_Share_Percent"].sum()

print("\n" + "=" * 60)
print("MARKET SHARE VALIDATION")
print("=" * 60)

print("Total Market Share:", share_total, "%")


# ============================================================
# 11. SORT COMPANIES BY MARKET SHARE
# ============================================================

ranked_df = df.sort_values(
    by="Market_Share_Percent",
    ascending=False
)

print("\n" + "=" * 60)
print("MARKET SHARE RANKING")
print("=" * 60)

print(
    ranked_df[
        [
            "Company",
            "Loans",
            "Market_Share_Percent"
        ]
    ]
)


# ============================================================
# 12. ADD RANK COLUMN
# ============================================================

ranked_df = ranked_df.reset_index(drop=True)

ranked_df["Rank"] = (
    ranked_df.index + 1
)

print("\nRanking with Rank Number:")
print(
    ranked_df[
        [
            "Rank",
            "Company",
            "Market_Share_Percent"
        ]
    ]
)


# ============================================================
# 13. BAR CHART — TOTAL LOANS
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    df["Company"],
    df["Loans"]
)

plt.title("Total Loans by Company")
plt.xlabel("Company")
plt.ylabel("Total Loans")

plt.xticks(rotation=15)

plt.tight_layout()

plt.show()


# ============================================================
# 14. BAR CHART — MARKET SHARE
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    df["Company"],
    df["Market_Share_Percent"]
)

plt.title("Market Share by Company")
plt.xlabel("Company")
plt.ylabel("Market Share (%)")

plt.xticks(rotation=15)

plt.tight_layout()

plt.show()


# ============================================================
# 15. PIE CHART — MARKET SHARE
# ============================================================

plt.figure(figsize=(7, 7))

plt.pie(
    df["Loans"],
    labels=df["Company"],
    autopct="%1.1f%%"
)

plt.title("Market Share Distribution")

plt.tight_layout()

plt.show()


# ============================================================
# 16. REVENUE COMPARISON
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    df["Company"],
    df["Revenue_Lakh"]
)

plt.title("Revenue by Company")
plt.xlabel("Company")
plt.ylabel("Revenue (Lakh)")

plt.xticks(rotation=15)

plt.tight_layout()

plt.show()


# ============================================================
# 17. CUSTOMER COMPARISON
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    df["Company"],
    df["Customers"]
)

plt.title("Customers by Company")
plt.xlabel("Company")
plt.ylabel("Customers")

plt.xticks(rotation=15)

plt.tight_layout()

plt.show()


# ============================================================
# 18. SEABORN MARKET-SHARE CHART
# ============================================================

plt.figure(figsize=(9, 5))

sns.barplot(
    data=df,
    x="Company",
    y="Market_Share_Percent"
)

plt.title("Market Share by Company — Seaborn")
plt.xlabel("Company")
plt.ylabel("Market Share (%)")

plt.xticks(rotation=15)

plt.tight_layout()

plt.show()


# ============================================================
# 19. IDENTIFY MARKET LEADER
# ============================================================

leader_row = df.loc[
    df["Market_Share_Percent"].idxmax()
]

leader = leader_row["Company"]

leader_share = leader_row[
    "Market_Share_Percent"
]

print("\n" + "=" * 60)
print("MARKET LEADER")
print("=" * 60)

print("Company:", leader)
print("Market Share:", leader_share, "%")


# ============================================================
# 20. IDENTIFY LOWEST MARKET SHARE
# ============================================================

lowest_row = df.loc[
    df["Market_Share_Percent"].idxmin()
]

lowest_company = lowest_row["Company"]

lowest_share = lowest_row[
    "Market_Share_Percent"
]

print("\n" + "=" * 60)
print("LOWEST MARKET SHARE")
print("=" * 60)

print("Company:", lowest_company)
print("Market Share:", lowest_share, "%")


# ============================================================
# 21. SECOND-LARGEST COMPANY
# ============================================================

second_company = ranked_df.iloc[1]["Company"]

second_share = ranked_df.iloc[1][
    "Market_Share_Percent"
]

print("\n" + "=" * 60)
print("SECOND-LARGEST COMPANY")
print("=" * 60)

print("Company:", second_company)
print("Market Share:", second_share, "%")


# ============================================================
# 22. CREATE FINAL ANALYSIS TABLE
# ============================================================

final_table = ranked_df[
    [
        "Rank",
        "Company",
        "Loans",
        "Customers",
        "Revenue_Lakh",
        "Market_Share_Percent"
    ]
]

print("\n" + "=" * 60)
print("FINAL MARKET SHARE ANALYSIS")
print("=" * 60)

print(final_table)


# ============================================================
# 23. SAVE ANALYSIS TABLE
# ============================================================

final_table.to_csv(
    "market_share_analysis.csv",
    index=False
)

print("\nAnalysis table saved as:")
print("market_share_analysis.csv")


# ============================================================
# 24. BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print(
    f"1. {leader} has the highest measured market share "
    f"at {leader_share}%."
)

print(
    f"2. {lowest_company} has the lowest measured market share "
    f"at {lowest_share}%."
)

print(
    f"3. {second_company} is the second-largest company "
    f"with a market share of {second_share}%."
)


# ============================================================
# 25. FINAL LEARNING MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("DAY 016 COMPLETE")
print("=" * 60)

print("Learning Flow:")
print(
    "Business Data → Total Market → Market Share "
    "→ Ranking → Visualization → Insight"
)

print("\nMarket-share analysis completed successfully.")