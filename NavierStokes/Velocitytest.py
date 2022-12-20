import numpy as np
import matplotlib.pyplot as plt

# Generate some data for the velocity field
nx, ny = 41, 41 # number of points in the x and y directions
x = np.linspace(0, 1, nx) # coordinates in the x direction
y = np.linspace(0, 1, ny) # coordinates in the y direction
X, Y = np.meshgrid(x, y) # generates a grid of points
u = -np.cos(2*np.pi*X) * np.sin(2*np.pi*Y) # velocity in the x direction
v = np.sin(2*np.pi*X) * np.cos(2*np.pi*Y) # velocity in the y direction

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the streamlines
ax.streamplot(x, y, u, v, density=1)

# Add a colorbar to show the velocity magnitude
magnitude = np.sqrt(u**2 + v**2)
cbar = plt.colorbar(ax.streamplot(x, y, u, v, color=magnitude, cmap='jet', density=1))
cbar.set_label('Velocity magnitude (m/s)')

# Add labels and show the plot
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
plt.show()


