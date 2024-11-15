import numpy as np
import matplotlib.pyplot as plt
import os

# Load the points from the text file
points = np.loadtxt("points.txt", delimiter=',', max_rows=50)

# Extract the x and y coordinates
x = points[:, 0]
y = points[:, 1]
A = np.array([4, 4]).reshape(-1,1)
M = np.array([1, 5]).reshape(-1,1)
B = np.array([-2, 6]).reshape(-1,1)
plt.figure()
plt.plot(x, y, label='AB', linestyle='-', color='blue')

tri_coords = np.block([A,M,B])
plt.plot(tri_coords[0, :], tri_coords[1, :], linestyle='-', color='red', label='line')
plt.scatter(tri_coords[0,:], tri_coords[1, :])
vert_labels = ['A','M','B'];
for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    plt.text(tri_coords[0, i], tri_coords[1, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f})',
             fontsize=12, color = 'black', ha='center', va='bottom')
plt.xlabel("x")
plt.ylabel("y")
plt.title("plot of points A,M,B")
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
