import matplotlib.pyplot as plt
import numpy as np

# Generate random 3D points
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
performance_scores = np.random.rand(100)  # Example performance scores

# Create a color map based on performance scores
cmap = plt.cm.get_cmap('coolwarm')

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Define thresholds for dividing the plot into quarters
x_threshold = 0.5
y_threshold = 0.5

# Plot x vs. y
scatter = axes[0, 0].scatter(x, y, c=performance_scores, cmap=cmap, marker='o')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 0].set_title('X vs. Y')

# Add dotted lines to separate the quarters
axes[0, 0].axvline(x_threshold, linestyle='dotted', color='gray')
axes[0, 0].axhline(y_threshold, linestyle='dotted', color='gray')

# Label the quarters
axes[0, 0].text(0.25, 0.75, 'Good', fontsize=12, color='black')
axes[0, 0].text(0.25, 0.25, 'Bad', fontsize=12, color='black')
axes[0, 0].text(0.75, 0.75, 'Good', fontsize=12, color='black')
axes[0, 0].text(0.75, 0.25, 'Bad', fontsize=12, color='black')

# Plot x vs. z
axes[0, 1].scatter(x, z, c=performance_scores, cmap=cmap, marker='o')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Z')
axes[0, 1].set_title('X vs. Z')

# Add dotted lines to separate the quarters
axes[0, 1].axvline(x_threshold, linestyle='dotted', color='gray')
axes[0, 1].axhline(y_threshold, linestyle='dotted', color='gray')

# Label the quarters
axes[0, 1].text(0.25, 0.75, 'Good', fontsize=12, color='black')
axes[0, 1].text(0.25, 0.25, 'Bad', fontsize=12, color='black')
axes[0, 1].text(0.75, 0.75, 'Good', fontsize=12, color='black')
axes[0, 1].text(0.75, 0.25, 'Bad', fontsize=12, color='black')

# Plot y vs. z
axes[1, 0].scatter(y, z, c=performance_scores, cmap=cmap, marker='o')
axes[1, 0].set_xlabel('Y')
axes[1, 0].set_ylabel('Z')
axes[1, 0].set_title('Y vs. Z')

# Add dotted lines to separate the quarters
axes[1, 0].axvline(x_threshold, linestyle='dotted', color='gray')
axes[1, 0].axhline(y_threshold, linestyle='dotted', color='gray')

# Label the quarters
axes[1, 0].text(0.25, 0.75, 'Good', fontsize=12, color='black')
axes[1, 0].text(0.25, 0.25, 'Bad', fontsize=12, color='black')
axes[1, 0].text(0.75, 0.75, 'Good', fontsize=12, color='black')
axes[1, 0].text(0.75, 0.25, 'Bad', fontsize=12, color='black')

# Remove the unused subplot
fig.delaxes(axes[1, 1])

# Adjust the spacing between subplots
plt.tight_layout()

# Add a color bar for the scatter plots
cbar = fig.colorbar(scatter, ax=axes.ravel().tolist())
cbar.set_label('Performance')

# Show the plot
plt.show()
