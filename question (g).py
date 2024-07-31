import numpy as np

# Define the function to integrate
def f(x):
    return x**2

# Define the trapezoidal rule function
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    area = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return area

# Integration parameters
a = 0  # lower limit
b = 1  # upper limit
n = 1000  # number of trapezoids

# Calculate the area
area = trapezoidal_rule(f, a, b, n)
print(f"Approximate area under f(x) from {a} to {b}: {area}")
