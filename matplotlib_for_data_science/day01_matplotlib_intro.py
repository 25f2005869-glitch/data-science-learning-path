# Author: Saloni Tiwari
# Topic: Matplotlib Introduction (Advanced)
# Day: 01
# Description: Multiple plots, styles, and customization

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [40, 30, 20, 10, 5]

# Create figure
plt.figure(figsize=(8, 5))

# Plot multiple lines
plt.plot(x, y1, label="Sales", color='blue', linestyle='-', marker='o')
plt.plot(x, y2, label="Expenses", color='red', linestyle='--', marker='s')

# Title and labels
plt.title("Company Performance Analysis")
plt.xlabel("Months")
plt.ylabel("Amount")

# Grid and legend
plt.grid(True)
plt.legend()

# Show plot
plt.show()