# Author: Saloni Tiwari
# Topic: Histogram (Marks Distribution Analysis)
# Day: 05
# Description: Analyze distribution of students' marks

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data (marks of 100 students)
np.random.seed(42)
marks = np.random.randint(0, 100, 100)

# Create figure
plt.figure(figsize=(10, 6))

# Histogram
plt.hist(marks, bins=10, edgecolor='black')

# Titles and labels
plt.title("Distribution of Students' Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

# Mean line
mean_marks = np.mean(marks)
plt.axvline(mean_marks, linestyle='dashed', linewidth=2, label=f"Mean: {mean_marks:.2f}")

# Legend and grid
plt.legend()
plt.grid(axis='y')

# Save graph
plt.savefig("day05_exam_marks_distribution.png")

# Show graph
plt.show()