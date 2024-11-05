import matplotlib.pyplot as plt

# Points A, B, and P
A = (4, 4)  # A(4, 4)
B = (-2, 6) # B(-2, 6)
P = (1, 5)  # Midpoint P(1, 5)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(*A, 'ro', label='Point A (4, 4)')
plt.plot(*B, 'bo', label='Point B (-2, 6)')
plt.plot(*P, 'go', label='Midpoint P (1, 5)')

# Draw the line segment
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label='Line segment AB')

# Adding annotations
plt.text(A[0], A[1], ' A (4, 4)', fontsize=10, verticalalignment='bottom')
plt.text(B[0], B[1], ' B (-2, 6)', fontsize=10, verticalalignment='bottom')
plt.text(P[0], P[1], ' P (1, 5)', fontsize=10, verticalalignment='bottom')

# Set the limits and labels
plt.xlim(-3, 5)
plt.ylim(0, 7)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.title('Points A, B, and Midpoint M')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()

