import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as xl

# Read the Excel file and print the DataFrame
df = pd.read_excel("Book1.xlsx")
print(df)

# Extract the two sets of values from the DataFrame
y1 = df["Reads top"]  # First dataset (bars extending outward)
y2 = df["Reads bottom"]     # Second dataset (bars extending inward)

# Number of data points
N = len(y1)

# Base radius from which the bars will extend
R_base = 0

# Compute the angles for each bar
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
theta = np.pi/2 - theta  # Adjust to start from the top

# Width of each bar
width = (2 * np.pi) / N * 1 # Adjusted width for better spacing

# Create a polar subplot
fig = plt.figure(figsize=(8, 8))  # Adjust the figure size as needed
ax = plt.subplot(111, polar=True)

# Plot the first dataset (bars extending outward from R_base)
bars1 = ax.bar(theta, y1, width=width*10, bottom=R_base, color='red', alpha=1)

# Plot the second dataset (bars extending inward towards the center)
# Negative radii are used to extend bars inward
bars2 = ax.bar(theta, -y2, width=width*10, bottom=R_base, color='black', alpha=1)

# Set the maximum radius based on your data
max_radius = max(y1.max(), y2.max())
ax.set_ylim(-2*max_radius,2*max_radius)

# Customize the plot appearance
ax.grid(False)                        # Remove grid lines
ax.set_xticks([])                     # Remove x-axis ticks
ax.set_yticks([])                     # Remove y-axis ticks
plt.axis("off")                       # Turn off the axis

# Save and display the plot
plt.savefig("S1Meghanew", dpi=1200, bbox_inches='tight', pad_inches=0)
plt.show()
