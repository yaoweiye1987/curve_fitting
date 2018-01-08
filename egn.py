import numpy as np
import matplotlib.pyplot as plt
delta = 0. 
gama1 = 0.4 
k = 0.008 * np.arange(-50.,50.) 
#print k
v4 = 0.0
w = np.array([[0.,0.,0.,0.] for i in k]) 
#print w
v1 = np.array([[[0.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,0.,0.]] for i in k])
#v2 = np.array([[0.,0.,0.,0.] for i in k])
#v3 = np.array([[0.,0.,0.,0.] for i in k])
#v4m = np.array([[0.,0.,0.,0.] for i in k])
for i in range(100): 
  a = np.array([[-delta/2., 0., - v4*k[i], k[i]], \
      [0., delta/2., k[i], -v4*k[i]], \
      [-v4*k[i], k[i], delta/2., gama1],\
      [k[i], -v4*k[i], gama1, -delta/2.]])
  eValues,eVectors = np.linalg.eig(a)
  print eValues
  print eVectors
  idx = eValues.argsort()[::-1]   
  print idx
  w[i] = eValues[idx]
  v1[i] = eVectors[idx,:]
  print v1[i]
  v1[i,0] = v1[i,0] * (v1[i,0,0]/abs(v1[i,0,0]))
  v1[i,1] = v1[i,1] * (v1[i,1,0]/abs(v1[i,1,0])) 
  v1[i,2] = v1[i,2] * (v1[i,2,0]/abs(v1[i,2,0]))
  v1[i,3] = v1[i,3] * (v1[i,3,0]/abs(v1[i,3,0]))  
  print 'after ***'  
  print v1[i]
 # print v2[i]
 # print v3[i]
 # print v4m[i]
file = open("newfile.txt", "w")
file.write(str(w)) 
file.close() 
plt.plot(k,v1[:,0,0],'red')
plt.plot(k,v1[:,0,1],'green')
plt.plot(k,v1[:,0,2],'blue')
plt.plot(k,v1[:,0,3],'black')

plt.show()
