import numpy as np

M = np.array([[1,0],[0,1],[-2,3]])
b = np.array([[1],[0],[2]]) #given point

#Singular Value Decomposition
U, s, V=np.linalg.svd(M)

# Diagonalizing S
S = np.zeros(M.shape)
Sinv = S.T
S[:2,:2] = np.diag(s)
sinv = 1./s

#Moore Penrose Pseudo Inverse
Sinv[:2,:2] = np.diag(sinv)

#Foot of the perpendicular
x = V.T.dot(Sinv).dot(U.T).dot(b)
print("the foot of the perpendicular",x)