import numpy as np

def qr_decomposition(A):
    """
    Perform the QR decomposition using Gram-Schmidt process.
    Given a matrix A, return orthogonal matrix Q and upper triangular matrix R such that A = Q * R.
    """
    n = A.shape[0]
    Q = np.zeros((n, n))
    R = np.zeros((n, n))
    
    for k in range(n):
        v = A[:, k]
        
        # Subtract projections onto previous q's
        for i in range(k):
            R[i, k] = np.dot(Q[:, i], v)
            v = v - R[i, k] * Q[:, i]
        
        # Normalize the vector to get q
        R[k, k] = np.linalg.norm(v)
        Q[:, k] = v / R[k, k]
    
    return Q, R

def qr_algorithm(A, iterations=100):
    """
    Perform the QR algorithm to compute the eigenvalues of A.
    Repeat the QR decomposition process and update A = R * Q for a given number of iterations.
    """
    A_copy = A.copy()
    for _ in range(iterations):
        Q, R = qr_decomposition(A_copy)
        A_copy = np.dot(R, Q)
    
    # Return the diagonal elements as the eigenvalues
    return np.diag(A_copy)

# Given matrix A
A = np.array([[4, -1, 1],
              [-1, 4, -2],
              [1, -2, 3]])

# Run QR algorithm
eigenvalues = qr_algorithm(A, iterations=100)

# Output the eigenvalues
print("Eigenvalues of the matrix A:")
print(eigenvalues)

