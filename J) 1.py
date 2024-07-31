import numpy as np

def power_iteration(A, num_simulations: int):
   
    b_k = np.random.rand(A.shape[1])
    
    for _ in range(num_simulations):
        
        b_k1 = np.dot(A, b_k)
        
        # Calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        
        # Re normalize the vector
        b_k = b_k1 / b_k1_norm
    
    
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k))
    
    return eigenvalue, b_k

A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

eigenvalue, eigenvector = power_iteration(A, 1000)
print(f"Eigenvalue: {eigenvalue}")
print(f"Eigenvector: {eigenvector}")
