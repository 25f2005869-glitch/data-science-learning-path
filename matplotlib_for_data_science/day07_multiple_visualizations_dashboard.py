# Author: Saloni Tiwari
# Topic: Subplots (Dashboard Visualization)
# Day: 07
# Description: Combine multiple plots in one figure (dashboard style)

import matplotlib.pyplot as plt
import numpy as np

# Data
x = [1, 2, 3, 4]

line_data = [10, 20, 30, 40]
bar_data = [5, 7, 8, 6]
scatter_x = [1, 2, 3, 4]
scatter_y = [2, 4, 6, 8]
hist_data = np.random.randint(0, 50, 20)

# Create figure
plt.figure(figsize=(12, 8))

# 1️⃣ Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, line_data, marker='o')
plt.title("Line Plot")
plt.grid(True)

# 2️⃣ Bar Chart
plt.subplot(2, 2, 2)
plt.bar(x, bar_data)
plt.title("Bar Chart")

# 3️⃣ Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(scatter_x, scatter_y)
plt.title("Scatter Plot")

# 4️⃣ Histogram
plt.subplot(2, 2, 4)
plt.hist(hist_data, bins=5, edgecolor='black')
plt.title("Histogram")

# Layout adjustment
plt.tight_layout()

# Save graph
plt.savefig("day07_multiple_visualizations_dashboard.png")

# Show graph
plt.show()