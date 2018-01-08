import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize 
pi = 3.14169
def func(x,*p):
  a, b,c,d = p  
  return a + 2./pi*b*(c/(4.*(x-d)**2 + c**2))      
  #return a * np.exp(-b * x) + c
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
p0 = [0.00, 8., 3.36, 636.8] 
err = lambda p: np.mean((func(x,*p)-y)**2)
p_init = [0.087, 8.69, 3.36, 636.8] 
p_opt = minimize( err, p_init, bounds = [(None,None),(None,None),(None,None),(None,None)], method = "L-BFGS-B").x 


#ppot, pcov = curve_fit(func,x, y,bounds =(0,[0.2, 10.,5.,700.])) 
#ppot[0] = 0.087 
#ppot[1] = 8.69 
#ppot[2] = 3.36 
#ppot[3] = 636.8 
print p_opt
yfit = func(x, *p_opt) 
#print ppot 
plt.plot(x,y,'black')
plt.plot(x,yfit)
plt.show()
