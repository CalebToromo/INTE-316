import numpy as np

def lagrange_polynomial(x, y):
    """
    Compute the Lagrange polynomial that interpolates the given data points.

    Parameters:
    x (array-like): Array of x data points.
    y (array-like): Array of y data points.

    Returns:
    function: A function representing the Lagrange polynomial.
    """
    def L(k, x_val):
        # Compute the k-th Lagrange basis polynomial L_k(x)
        term = [(x_val - x[j]) / (x[k] - x[j]) for j in range(len(x)) if j != k]
        return np.prod(term)

    def P(x_val):
        # Compute the Lagrange polynomial P(x)
        return sum(y[k] * L(k, x_val) for k in range(len(x)))

    return P

# Example data points
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

# Compute the Lagrange polynomial
P = lagrange_polynomial(x, y)

# Test the polynomial at a new point
x_val = 2.5
print(f"P({x_val}) = {P(x_val)}")
