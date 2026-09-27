"""
Author: Saloni Tiwari
Programme: IIT Madras BS Degree — Diploma Level
Course: Business Data Management
Day: 020
Lecture: W4_L7
Topic: Analysis of Aspirational Data

Purpose:
Analyse aspirational-district style indicator data,
compare regional and district performance,
rank districts, and identify patterns across indicators.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "District": [
        "Purnia", "Gaya", "Nandurbar", "Dahod",
        "Kiphire", "Ranchi", "Mewat", "Koraput",
        "Dantewada", "Baran", "Washim", "Aspirational X"
    ],
    "Region": [
        "East", "East", "West", "West",
        "North-East", "East", "North", "East",
        "Central", "North", "West", "Central"
    ],
    "Aspirational_Score": [
        68, 71, 74, 76, 62, 79,
        73, 69, 65, 72, 78, 67
    ],
    "Health_Score": [
        64, 69, 72, 75, 60, 77,
        71, 67, 63, 70, 76, 65
    ],
    "Education_Score": [
        70, 73, 76, 78, 65, 81,
        74, 72, 68, 75, 80, 69
    ],
    "Agriculture_Score": [
        72, 68, 70, 73, 58, 76,
        69, 70, 66, 67, 74, 71
    ],
    "Financial_Inclusion_Score": [
        66, 74, 78, 79, 64, 82,
        77, 65, 62, 76, 81, 63
    ]
}

df = pd.DataFrame(data)

print("\nDAY 020 — ANALYSIS OF ASPIRATIONAL DATA")
print("=" * 70)
print(df)

overall_average = df["Aspirational_Score"].mean()

region_summary = (
    df.groupby("Region", as_index=False)
      .agg(
          Average_Aspirational_Score=("Aspirational_Score", "mean"),
          Average_Health=("Health_Score", "mean"),
          Average_Education=("Education_Score", "mean"),
          Average_Agriculture=("Agriculture_Score", "mean"),
          Average_Financial_Inclusion=(
              "Financial_Inclusion_Score",
              "mean"
          )
      )
)

region_summary = region_summary.round(2)

district_ranking = df[
    ["District", "Region", "Aspirational_Score"]
].copy()

district_ranking["Rank"] = (
    district_ranking["Aspirational_Score"]
    .rank(method="min", ascending=False)
    .astype(int)
)

district_ranking = district_ranking.sort_values("Rank")

indicator_columns = [
    "Health_Score",
    "Education_Score",
    "Agriculture_Score",
    "Financial_Inclusion_Score"
]

indicator_summary = (
    df[indicator_columns]
    .mean()
    .round(2)
)

print("\nOverall Average Score:")
print(round(overall_average, 2))

print("\nRegional Summary:")
print(region_summary)

print("\nDistrict Ranking:")
print(district_ranking)

print("\nIndicator Averages:")
print(indicator_summary)

region_summary.to_csv(
    "day_020_region_summary.csv",
    index=False
)

district_ranking.to_csv(
    "day_020_district_ranking.csv",
    index=False
)

indicator_summary.to_csv(
    "day_020_indicator_averages.csv"
)

plt.figure(figsize=(9, 5))
plt.bar(
    region_summary["Region"],
    region_summary["Average_Aspirational_Score"]
)
plt.title("Average Aspirational Score by Region")
plt.xlabel("Region")
plt.ylabel("Average Score")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

plt.figure(figsize=(11, 5))
plt.bar(
    district_ranking["District"],
    district_ranking["Aspirational_Score"]
)
plt.title("District Aspirational Scores")
plt.xlabel("District")
plt.ylabel("Aspirational Score")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
plt.bar(
    indicator_summary.index,
    indicator_summary.values
)
plt.title("Average Indicator Scores")
plt.xlabel("Indicator")
plt.ylabel("Average Score")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

leader = district_ranking.iloc[0]
lowest = district_ranking.iloc[-1]

best_region = region_summary.sort_values(
    "Average_Aspirational_Score",
    ascending=False
).iloc[0]

print("\nBUSINESS INSIGHTS")
print("=" * 70)

print(
    f"1. {leader['District']} has the highest measured "
    f"aspirational score at {leader['Aspirational_Score']}."
)

print(
    f"2. {lowest['District']} has the lowest measured "
    f"aspirational score at {lowest['Aspirational_Score']}."
)

print(
    f"3. {best_region['Region']} has the highest regional "
    f"average score at "
    f"{best_region['Average_Aspirational_Score']}."
)

print(
    "4. Indicator averages help identify which dimensions "
    "are relatively stronger or weaker in the learning dataset."
)

print("\nDay 020 analysis completed successfully.")