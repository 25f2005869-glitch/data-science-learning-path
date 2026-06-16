# Author: Saloni Tiwari
# Topic: Sales Comparison (Multiple Line Plot)
# Day: 02
# Description: Compare sales of multiple products over months

import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

product_A = [50, 60, 70, 80, 90]
product_B = [30, 40, 50, 60, 70]
product_C = [20, 30, 40, 50, 60]

# Create figure
plt.figure(figsize=(10, 6))

# Plot lines
plt.plot(months, product_A, label="Product A", marker='o', linestyle='-')
plt.plot(months, product_B, label="Product B", marker='s', linestyle='--')
plt.plot(months, product_C, label="Product C", marker='^', linestyle=':')

# Titles and labels
plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")

# Grid and legend
plt.grid(True)
plt.legend()

# Save graph
plt.savefig("day02_sales_comparison.png")

# Show graph
plt.show()