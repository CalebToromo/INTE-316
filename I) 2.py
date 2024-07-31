import numpy as np

def newton_divided_difference(x, y):
    """
    Compute the coefficients of Newton's divided difference polynomial.

    Parameters:
    x (array): Array of x data points.
    y (array): Array of y data points.

    Returns:
    function: A function representing Newton's divided difference polynomial.
    """
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])

    def P(x_val):
        result = coef[0, 0]
        for i in range(1, n):
            term = coef[0, i]
            for j in range(i):
                term *= (x_val - x[j])
            result += term
        return result

    return P

# Example data points
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

# Compute the Newton's divided difference polynomial
P = newton_divided_difference(x, y)

# Test the polynomial at a new point
x_val = 2.5
print(f"P({x_val}) = {P(x_val)}")
