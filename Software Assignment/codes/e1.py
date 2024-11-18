import numpy as np

def qr_decomposition(A):
    """Compute the QR decomposition of matrix A using Gram-Schmidt process"""
    n = A.shape[0]
    Q = np.zeros((n, n))
    R = np.zeros((n, n))
    
    for k in range(n):
        # v is the k-th column of A
        v = A[:, k]
        
        for i in range(k):
            # Project onto previous q's
            R[i, k] = np.dot(Q[:, i], v)
            v = v - R[i, k] * Q[:, i]
        
        # Normalize the vector to get q
        R[k, k] = np.linalg.norm(v)
        Q[:, k] = v / R[k, k]
    
    return Q, R

def qr_algorithm(A, iterations=100):
    """Perform the QR algorithm to compute eigenvalues of A"""
    A_copy = A.copy()
    n = A_copy.shape[0]
    
    for _ in range(iterations):
        # Step 1: QR decomposition of A
        Q, R = qr_decomposition(A_copy)
        
        # Step 2: A = R * Q (new A)
        A_copy = np.dot(R, Q)
    
    # Return the diagonal elements as eigenvalues
    return np.diag(A_copy)

# Matrix A = [[6, 2], [2, 5]]
A = np.array([[6, 2],
              [2, 5]])

# Run QR algorithm
eigenvalues = qr_algorithm(A, iterations=100)

print("Eigenvalues of the matrix A:")
print(eigenvalues)

