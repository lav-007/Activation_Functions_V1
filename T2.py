import numpy as np

A=np.array([[1,2],[3,4]])
B=np.array([1,2])

x=np.linalg.inv(A).dot(B.T)

print(x)
#  QUESTION:
A=np.array([[1,1],[1.5,4]])
b=np.array([2200,5050])
X=np.linalg.solve(A,b)
print('number of children and adults are=',X)
