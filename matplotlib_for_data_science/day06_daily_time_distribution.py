# Author: Saloni Tiwari
# Topic: Pie Chart (Daily Time Distribution)
# Day: 06
# Description: Analyze how time is spent on daily activities

import matplotlib.pyplot as plt

# Data
activities = ['Study', 'Sleep', 'Exercise', 'Entertainment', 'Others']
time_spent = [6, 8, 2, 4, 4]  # hours

# Create figure
plt.figure(figsize=(7, 7))

# Pie chart
plt.pie(
    time_spent,
    labels=activities,
    autopct='%1.1f%%',
    startangle=90,
    explode=(0.1, 0, 0, 0, 0)  # highlight Study
)

# Title
plt.title("Daily Time Distribution")

# Equal aspect ratio
plt.axis('equal')

# Save graph
plt.savefig("day06_daily_time_distribution.png")

# Show graph
plt.show()