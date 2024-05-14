import data_processing
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Get data from data_processing.py
selected_data = data_processing.selected_data.copy()

# Filter the data for ages between 18 and 40
filtered_data = selected_data[(selected_data['age'] >= 18) & (selected_data['age'] <= 40)]

# Group by age and sum the match counts
grouped_data = filtered_data.groupby('age')['dec'].sum().reset_index()

# Extracting data for plotting
ages = grouped_data['age']
match_counts = grouped_data['dec']

# Set the width of the bars
width = 1
height = 1

# Specify the size of the window
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for the bars
xpos, ypos = np.meshgrid(ages, [0])
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Construct the bars
dx = width * np.ones_like(zpos)
dy = height * np.ones_like(zpos)  # Set the height to a fixed value
dz = match_counts

# Plot the bars as cuboids
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='lightgreen', edgecolor='black', linewidth=0.5, zsort='max', alpha=0.8)

# Remove grid lines
ax.grid(False)

# Remove unnecessary bottom y axis number
ax.set_yticks([])

# Labels
ax.set_xlabel('Age')
ax.set_zlabel('Matches')
ax.set_title('Columbia University 2001-2004 \n speed-dating experiment')
ax.set_box_aspect([1, 0.5, 1])  # Adjust the numbers according to your preference

plt.show()
