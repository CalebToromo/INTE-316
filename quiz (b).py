import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import curve_fit
from scipy.interpolate import splrep, splev
from scipy.stats import linregress

# Function to differentiate and integrate
def f(x):
    return x**2 - x - 2

# Range of x values
x = np.linspace(0, 5, 100)

# Differentiation
df = np.gradient(f(x), x)
print("Differentiation (df/dx):")
print(df)

# Numerical Integration
a, b = 0, 5
integral, error = quad(f, a, b)
print(f"\nNumerical Integration of f(x) from {a} to {b}: {integral}")

# Curve Fitting (Using a linear model as an example)
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = f(x_data)  # or use real data points

def linear_model(x, a, b):
    return a * x + b

popt, pcov = curve_fit(linear_model, x_data, y_data)
print(f"\nCurve Fitting parameters (a, b): {popt}")

# Linear Regression
slope, intercept, r_value, p_value, std_err = linregress(x_data, y_data)
print(f"\nLinear Regression slope: {slope}, intercept: {intercept}")

# Spline Interpolation
spline = splrep(x_data, y_data)
x_spline = np.linspace(0, 5, 100)
y_spline = splev(x_spline, spline)

# Plotting
plt.figure(figsize=(14, 8))

# Original function and its derivative
plt.subplot(2, 2, 1)
plt.plot(x, f(x), label='f(x) = x^2 - x - 2')
plt.plot(x, df, label="df/dx (Numerical Derivative)")
plt.legend()
plt.title("Differentiation")

# Numerical Integration
plt.subplot(2, 2, 2)
plt.fill_between(x, f(x), color='skyblue', alpha=0.4, label="Integral of f(x)")
plt.plot(x, f(x), label='f(x) = x^2 - x - 2')
plt.legend()
plt.title("Numerical Integration")

# Curve Fitting
plt.subplot(2, 2, 3)
plt.scatter(x_data, y_data, label='Data')
plt.plot(x, linear_model(x, *popt), label='Fitted Line', color='red')
plt.legend()
plt.title("Curve Fitting")

# Spline Interpolation
plt.subplot(2, 2, 4)
plt.plot(x_data, y_data, 'o', label='Data')
plt.plot(x_spline, y_spline, label='Spline Interpolation', color='green')
plt.legend()
plt.title("Spline Interpolation")

plt.tight_layout()
plt.show()
