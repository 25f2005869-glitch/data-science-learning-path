# Author: Saloni Tiwari
# Topic: Advanced Customization & Annotation
# Day: 08
# Description: Styling, annotations, limits, and professional visualization

import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [50, 65, 80, 70, 90]

# Create figure
plt.figure(figsize=(10, 6))

# Plot line
plt.plot(months, sales, marker='o', linestyle='-', color='blue', linewidth=2)

# Title and labels
plt.title("Monthly Sales Trend", fontsize=16, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales", fontsize=12)

# Grid customization
plt.grid(True, linestyle='--', alpha=0.6)

# Highlight highest point
max_value = max(sales)
max_index = sales.index(max_value)

plt.annotate(
    f"Highest: {max_value}",
    xy=(months[max_index], max_value),
    xytext=(months[max_index], max_value + 5),
    arrowprops=dict(facecolor='black', shrink=0.05)
)

# Axis limits
plt.ylim(0, 100)

# Style improvement
plt.xticks(rotation=30)

# Save graph
plt.savefig("day08_advanced_plot_customization.png")

# Show plot
plt.show()