from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm

from matplotlib.ticker import LinearLocator, FormatStrFormatter

from scipy.interpolate import griddata
import matplotlib.pyplot as plt

import numpy as np


f = open('wavefunctionXYZ.txt') 

length = 305
f2 = open('mmomentXYZ.txt')
x = [0. for i in range(length)] 
y = [0. for i in range(length)]
z = [0. for i in range(length)]
xm = [0. for i in range(length)] 
ym = [0. for i in range(length)] 
zm = [0. for i in range(length)] 
i = 0

for line in f: 

  l = line.split() 
  x[i] = float(l[0]) 
  y[i] = float(l[1])
  z[i] = float(l[2])
  i += 1
i = 0
for line in f2:
  l = line.split()
  xm[i] = float(l[0])
  ym[i] = float(l[1])
  zm[i] = float(l[2])
  i += 1

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0, antialiased=False)
#plt.show()
res = 40 
xnew, ynew = np.mgrid[0.325:0.342:40j, 0.57:0.585:40j]
xi = np.linspace(0.325,0.342,res)
yi = np.linspace(0.57,0.585,res)
#rbf = Rbf(x,y,z, epsilon = 2)
#znew = rbf(xnew,ynew)
znew = griddata((x,y),z,(xi[None,:], yi[:,None]), method = 'cubic')  
xmi = np.linspace(0.325,0.342,res)
ymi = np.linspace(0.57,0.585,res)
zmnew = griddata((xm,ym),zm,(xmi[None,:], ymi[:,None]), method = 'cubic')
print(znew.min())
print(znew.max())
print(zmnew.min())
print(zmnew.max())
znewcopy = znew
#for i in range(res):
#  for j in range(res):
#    if znew[i,j] < 0.005:
#      znewcopy[i,j] = np.nan 
fig = plt.figure()

ax = fig.gca(projection='3d')
#surf = ax.plot_surface(xnew, ynew,znewcopy,vmin= 0.0015, vmax = 0.015,rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False, shade = False)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
cset = ax.contourf(xnew,ynew,znew,res, cmap= cm.coolwarm, zdir = 'z', offset = 0.01)
fig.colorbar(cset, shrink = 0.5, ticks = np.arange(0.001,0.015,0.002))
cset2 = ax.contourf(xnew,ynew,zmnew, res, zdir = 'z', offset = -0.01)
fig.colorbar(cset2, shrink = 0.5,ticks = np.arange(0,-10,-2) )
ax.set_zlim(-0.012, 0.015)
#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
