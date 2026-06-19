# ======================================
# Day 058: Time Series Basics
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Time Series Data
# using Pandas
# ======================================

print("=" * 50)
print("DAY 058 - TIME SERIES BASICS")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import pandas as pd
import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Time Series Data?

Time Series Data is data collected
over time intervals.

Examples:

1. Stock Prices
2. Temperature Data
3. Sales Data
4. Population Growth
5. Website Traffic

Pandas provides powerful tools
for working with dates and time.

Important Functions:

1. pd.to_datetime()
2. date_range()
3. resample()
4. shift()
5. rolling()
"""

# ======================================
# 1. CREATE DATE
# ======================================

print("\n1. CREATE DATE")

date = pd.to_datetime(
    "2026-06-18"
)

print(date)

# ======================================
# 2. DATE RANGE
# ======================================

print("\n2. DATE RANGE")

dates = pd.date_range(
    start="2026-01-01",
    periods=5,
    freq="D"
)

print(dates)

# ======================================
# 3. CREATE TIME SERIES
# ======================================

print("\n3. TIME SERIES")

sales = pd.Series(
    [100, 120, 150, 130, 180],
    index=dates
)

print(sales)

# ======================================
# 4. ACCESS DATA BY DATE
# ======================================

print("\n4. ACCESS BY DATE")

print(
    sales["2026-01-03"]
)

# ======================================
# 5. YEAR, MONTH, DAY
# ======================================

print("\n5. DATE COMPONENTS")

sample_date = pd.Timestamp(
    "2026-06-18"
)

print("Year :", sample_date.year)
print("Month:", sample_date.month)
print("Day  :", sample_date.day)

# ======================================
# 6. CREATE DATAFRAME
# ======================================

print("\n6. TIME SERIES DATAFRAME")

df = pd.DataFrame(
    {
        "Date": pd.date_range(
            "2026-01-01",
            periods=7
        ),
        "Sales": [
            100,
            120,
            150,
            130,
            180,
            200,
            210
        ]
    }
)

print(df)

# ======================================
# 7. SET DATE AS INDEX
# ======================================

print("\n7. SET DATE INDEX")

df.set_index(
    "Date",
    inplace=True
)

print(df)

# ======================================
# 8. FILTER DATE RANGE
# ======================================

print("\n8. FILTER DATE RANGE")

print(
    df[
        "2026-01-02":
        "2026-01-05"
    ]
)

# ======================================
# 9. RESAMPLING
# ======================================

print("\n9. RESAMPLING")

monthly_sales = df.resample(
    "M"
).sum()

print(monthly_sales)

# ======================================
# 10. SHIFT DATA
# ======================================

print("\n10. SHIFT")

df["Previous_Sales"] = (
    df["Sales"].shift(1)
)

print(df)

# ======================================
# 11. DIFFERENCE
# ======================================

print("\n11. DIFFERENCE")

df["Difference"] = (
    df["Sales"].diff()
)

print(df)

# ======================================
# 12. ROLLING MEAN
# ======================================

print("\n12. ROLLING MEAN")

df["Rolling_Avg"] = (
    df["Sales"]
    .rolling(window=3)
    .mean()
)

print(df)

# ======================================
# 13. EXPANDING MEAN
# ======================================

print("\n13. EXPANDING MEAN")

df["Expanding_Avg"] = (
    df["Sales"]
    .expanding()
    .mean()
)

print(df)

# ======================================
# 14. GENERATE RANDOM DATA
# ======================================

print("\n14. RANDOM TIME SERIES")

random_series = pd.Series(
    np.random.randint(
        50,
        100,
        size=10
    ),
    index=pd.date_range(
        "2026-01-01",
        periods=10
    )
)

print(random_series)

# ======================================
# 15. DATE FEATURES
# ======================================

print("\n15. DATE FEATURES")

date_df = pd.DataFrame(
    {
        "Date": pd.date_range(
            "2026-01-01",
            periods=5
        )
    }
)

date_df["Year"] = (
    date_df["Date"].dt.year
)

date_df["Month"] = (
    date_df["Date"].dt.month
)

date_df["Day"] = (
    date_df["Date"].dt.day
)

print(date_df)

# ======================================
# 16. USER INPUT EXAMPLE
# ======================================

print("\n16. USER INPUT EXAMPLE")

user_date = input(
    "Enter Date (YYYY-MM-DD): "
)

converted_date = pd.to_datetime(
    user_date
)

print(converted_date)

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT")

sales_data = pd.DataFrame(
    {
        "Date": pd.date_range(
            "2026-01-01",
            periods=10
        ),
        "Sales": [
            100,
            120,
            150,
            130,
            180,
            200,
            210,
            220,
            240,
            250
        ]
    }
)

sales_data.set_index(
    "Date",
    inplace=True
)

print("\nSALES DATA")
print(sales_data)

print("\nAVERAGE SALES")
print(
    sales_data["Sales"].mean()
)

print("\nMAXIMUM SALES")
print(
    sales_data["Sales"].max()
)

print("\nROLLING AVERAGE")
print(
    sales_data["Sales"]
    .rolling(3)
    .mean()
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a date range
for 10 days.

Exercise 2:
Create a time series
using sales data.

Exercise 3:
Calculate:

- Rolling Mean
- Difference

Exercise 4:
Extract:

- Year
- Month
- Day
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Monthly Sales Analyzer.

Store sales data for
30 days.

Calculate:

1. Total Sales
2. Average Sales
3. Rolling Average
4. Daily Difference
5. Highest Sales
6. Lowest Sales

Display a complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 058 Completed Successfully!")