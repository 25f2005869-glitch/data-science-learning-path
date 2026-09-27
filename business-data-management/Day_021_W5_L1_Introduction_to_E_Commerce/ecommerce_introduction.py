"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Day: 021
Topic: Introduction to E-Commerce
"""

import pandas as pd
import matplotlib.pyplot as plt

data = [
    ["Jan", "Electronics", "Website", "North", 120, 150, 18.5],
    ["Jan", "Fashion", "Marketplace", "South", 180, 240, 12.8],
    ["Jan", "Grocery", "App", "West", 210, 310, 9.6],
    ["Feb", "Electronics", "Website", "East", 135, 168, 20.4],
    ["Feb", "Fashion", "App", "North", 195, 255, 14.2],
    ["Feb", "Grocery", "Marketplace", "South", 225, 330, 10.1],
    ["Mar", "Electronics", "App", "West", 150, 188, 22.1],
    ["Mar", "Fashion", "Website", "East", 205, 270, 15.3],
    ["Mar", "Grocery", "App", "North", 235, 345, 10.8],
    ["Apr", "Electronics", "Marketplace", "South", 165, 205, 24.0],
    ["Apr", "Fashion", "Website", "West", 220, 290, 16.1],
    ["Apr", "Grocery", "App", "East", 250, 365, 11.7],
    ["May", "Electronics", "Website", "North", 175, 218, 26.2],
    ["May", "Fashion", "Marketplace", "South", 235, 305, 17.4],
    ["May", "Grocery", "App", "West", 270, 395, 12.9],
    ["Jun", "Electronics", "App", "East", 190, 238, 28.0],
    ["Jun", "Fashion", "Website", "North", 250, 325, 18.6],
    ["Jun", "Grocery", "Marketplace", "South", 285, 420, 14.0],
]

df = pd.DataFrame(
    data,
    columns=[
        "Month",
        "Category",
        "Channel",
        "Region",
        "Orders",
        "Units",
        "Revenue_Lakh",
    ],
)

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

monthly = (
    df.groupby("Month")[["Orders", "Units", "Revenue_Lakh"]]
    .sum()
    .reindex(month_order)
)

category = df.groupby("Category")[["Orders", "Units", "Revenue_Lakh"]].sum()

channel = df.groupby("Channel")[["Orders", "Units", "Revenue_Lakh"]].sum()

region = df.groupby("Region")[["Orders", "Units", "Revenue_Lakh"]].sum()

total_orders = df["Orders"].sum()
total_units = df["Units"].sum()
total_revenue = df["Revenue_Lakh"].sum()

average_revenue_per_order = total_revenue / total_orders

print("=" * 50)
print("DAY 021 — INTRODUCTION TO E-COMMERCE")
print("=" * 50)

print("\nTOTAL ORDERS")
print(total_orders)

print("\nTOTAL UNITS")
print(total_units)

print("\nTOTAL REVENUE (LAKH)")
print(round(total_revenue, 2))

print("\nAVERAGE REVENUE PER ORDER")
print(round(average_revenue_per_order, 4))

print("\nMONTHLY SUMMARY")
print(monthly)

print("\nCATEGORY SUMMARY")
print(category.sort_values("Revenue_Lakh", ascending=False))

print("\nCHANNEL SUMMARY")
print(channel.sort_values("Revenue_Lakh", ascending=False))

print("\nREGION SUMMARY")
print(region.sort_values("Revenue_Lakh", ascending=False))

monthly.to_csv("monthly_ecommerce_summary.csv")
category.to_csv("category_ecommerce_summary.csv")
channel.to_csv("channel_ecommerce_summary.csv")
region.to_csv("region_ecommerce_summary.csv")

plt.figure(figsize=(8, 5))
plt.bar(monthly.index, monthly["Revenue_Lakh"])
plt.title("Monthly E-Commerce Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Lakh)")
plt.tight_layout()
plt.savefig("monthly_revenue.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(monthly.index, monthly["Orders"], marker="o")
plt.title("Monthly Orders Trend")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("monthly_orders_trend.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(category.index, category["Revenue_Lakh"])
plt.title("Revenue by E-Commerce Category")
plt.xlabel("Category")
plt.ylabel("Revenue (Lakh)")
plt.tight_layout()
plt.savefig("category_revenue.png", dpi=150)
plt.show()

top_category = category["Revenue_Lakh"].idxmax()
top_channel = channel["Revenue_Lakh"].idxmax()
top_region = region["Revenue_Lakh"].idxmax()

print("\nBUSINESS INSIGHTS")
print("Top sample category by revenue:", top_category)
print("Top sample channel by revenue:", top_channel)
print("Top sample region by revenue:", top_region)

print("\nAnalysis completed successfully.")