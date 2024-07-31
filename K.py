def f(x, y):
    return x**2 + y**2 - xy + x - y + 1

def grad_f(x, y):
    df_dx = 2*x - y + 1
    df_dy = 2*y - x - 1
    return np.array([df_dx, df_dy])

def gradient_descent(learning_rate, initial_guess, num_iterations):
    x, y = initial_guess
    for _ in range(num_iterations):
        grad = grad_f(x, y)
        x -= learning_rate * grad[0]
        y -= learning_rate * grad[1]
    return x, y

learning_rate = 0.1
initial_guess = (0, 0)
num_iterations = 1000

minimum = gradient_descent(learning_rate, initial_guess, num_iterations)
print(f"Minimum found at: {minimum}")
