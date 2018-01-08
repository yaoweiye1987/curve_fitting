import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize 
pi = 3.14169
def func(x,a,b,c):
  #return a + 2./pi*b*(c/(4.*(x-d)**2 + c**2))      
  return a * np.exp(-b * x) + c
fx= open('X.txt') 
fy = open('Y.txt') 
n1 = int(fx.readline()) 
n2 = int(fy.readline()) 
if n1 != n2: 
  print 'error' 
else:
  x = [ 0. for i in range(n1)] 
  y = [ 0. for i in range(n1)]
  for i in range(n1):
    x[i] = float(fx.readline()) 
    y[i] = float(fy.readline())

ppot, pcov = curve_fit(func,x, y,bounds =(0,[0.2, 10.,5.,700.])) 
#ppot[0] = 0.087 
#ppot[1] = 8.69 
#ppot[2] = 3.36 
#ppot[3] = 636.8 

yfit = func(x, ppot[0],ppot[1],ppot[2]) 
print ppot 
plt.plot(x,y,'black')
plt.plot(x,yfit)
plt.show()
