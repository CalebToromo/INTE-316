import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Given data points
x_coords = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_coords = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Create a linear interpolation function
linear_interpolator = interp1d(x_coords, y_coords)

# Find the y-coordinate at x = 4.0
x_value = 4.0
y_value = linear_interpolator(x_value)

print(f"The interpolated value of y at x = {x_value} is {y_value}")

# Plotting the points and the interpolation line
plt.scatter(x_coords, y_coords, color='red', label='Data points')
plt.plot(x_coords, y_coords, label='Linear Interpolation', color='blue')
plt.scatter(x_value, y_value, color='green', label=f'Interpolated point (x={x_value})')
plt.xlabel('X (in)')
plt.ylabel('Y (in)')
plt.title('Linear Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()
