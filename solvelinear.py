import numpy as np
m = [1,1,1,1]
a = np.array([[3*m[0],1*m[1]],[1*m[2],2*m[3]]]) 
b = np.array([9,8]) 

x = np.linalg.solve(a, b) 
print x
