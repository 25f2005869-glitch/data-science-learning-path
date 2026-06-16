# Author: Saloni Tiwari
# Topic: Bar Chart (Student Performance Comparison)
# Day: 03
# Description: Compare marks of students using grouped bar chart

import matplotlib.pyplot as plt
import numpy as np

# Data
subjects = ['Math', 'Physics', 'Chemistry', 'Biology']

student_A = [85, 78, 92, 88]
student_B = [75, 82, 85, 80]
student_C = [90, 88, 95, 92]

# X positions
x = np.arange(len(subjects))
width = 0.25

# Create figure
plt.figure(figsize=(10, 6))

# Plot bars
plt.bar(x - width, student_A, width, label='Student A')
plt.bar(x, student_B, width, label='Student B')
plt.bar(x + width, student_C, width, label='Student C')

# Labels and title
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Performance Comparison")

# X ticks
plt.xticks(x, subjects)

# Grid and legend
plt.grid(axis='y')
plt.legend()

# Save graph
plt.savefig("day03_student_performance_bar.png")

# Show graph
plt.show()