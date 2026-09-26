"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Day: 015
Topic: W4_L2 — Representing Data Visually

Purpose:
Create basic business-data visualizations using Python.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# DATASET
# ============================================================

data = {
    "Region": ["North", "South", "East", "West"],
    "Sales": [179000, 175000, 149000, 171000],
    "Orders": [64, 66, 54, 61],
}

df = pd.DataFrame(data)

print("Business Data:")
print(df)


# ============================================================
# 1. BAR CHART — SALES BY REGION
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(df["Region"], df["Sales"])

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()


# ============================================================
# 2. LINE CHART — ORDERS BY REGION
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    df["Region"],
    df["Orders"],
    marker="o"
)

plt.title("Orders by Region")
plt.xlabel("Region")
plt.ylabel("Orders")

plt.tight_layout()
plt.show()


# ============================================================
# 3. PIE CHART — SALES SHARE BY REGION
# ============================================================

plt.figure(figsize=(7, 7))

plt.pie(
    df["Sales"],
    labels=df["Region"],
    autopct="%1.1f%%"
)

plt.title("Sales Share by Region")

plt.tight_layout()
plt.show()


# ============================================================
# 4. SEABORN BAR CHART
# ============================================================

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Region",
    y="Sales"
)

plt.title("Sales by Region — Seaborn")

plt.tight_layout()
plt.show()


# ============================================================
# 5. BASIC INSIGHTS
# ============================================================

highest_sales_region = df.loc[df["Sales"].idxmax(), "Region"]
highest_orders_region = df.loc[df["Orders"].idxmax(), "Region"]

print("\nBusiness Insights:")
print(f"Highest sales region: {highest_sales_region}")
print(f"Highest orders region: {highest_orders_region}")