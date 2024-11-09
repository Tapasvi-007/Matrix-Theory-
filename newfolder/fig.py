import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

A=np.array([4,4]).reshape(-1,1)
B=np.array([-2,6]).reshape(-1,1)
M=np.array([1,5]).reshape(-1,1)
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(M[0,:],M[1,:],label='$Midpoint$')

colors = np.arange(1,4)
#Labeling the coordinates
tri_coords = np.block([A,B,M])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['A','B','M']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
    #plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,-5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.text(A[0], A[1], '(4, 4)', fontsize=10, verticalalignment='bottom')
plt.text(B[0], B[1], '(-2, 6)', fontsize=10, verticalalignment='bottom')
plt.text(M[0], M[1], '(1, 5)', fontsize=10, verticalalignment='bottom')

plt.xlim(-3, 5)
plt.ylim(0, 7)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.title('Points A, B, and Midpoint M')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.axis('equal')
plt.show()
