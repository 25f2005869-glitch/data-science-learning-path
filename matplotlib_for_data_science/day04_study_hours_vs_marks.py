# Author: Saloni Tiwari
# Topic: Scatter Plot (Study vs Performance)
# Day: 04
# Description: Analyze relationship between study hours and marks

import matplotlib.pyplot as plt

# Data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [50, 55, 65, 70, 75, 85, 90, 95]

# Create figure
plt.figure(figsize=(10, 6))

# Scatter plot
plt.scatter(hours_studied, marks)

# Add labels to each point (annotation)
for i in range(len(hours_studied)):
    plt.text(hours_studied[i], marks[i], f"({hours_studied[i]}, {marks[i]})")

# Titles and labels
plt.title("Study Hours vs Marks Analysis")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")

# Grid
plt.grid(True)

# Save graph
plt.savefig("day04_study_hours_vs_marks.png")

# Show graph
plt.show()