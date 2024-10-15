import numpy as np

A = np.array([
    [2, 0], 
    [4, -3]
])

B = np.array([4, 2])

solution = np.linalg.solve(A, B)
a = solution[0]
b = solution[1]

print(f"Value of a: {a}")
print(f"Value of b: {b}")
