def qr_algorithm(A, num_iterations: int):
    n = A.shape[0]
    Q_total = np.eye(n)
    for _ in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = R @ Q
        Q_total = Q_total @ Q
    eigenvalues = np.diag(A)
    return eigenvalues, Q_total

eigenvalues, eigenvectors = qr_algorithm(A, 1000)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors: {eigenvectors}")
