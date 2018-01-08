import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize 
pi = 3.14159
def func(x,*p):
  a, b1,c1,d1,b2,c2,d2,b3,c3,d3,A0,Eg,dE = p  
  return a + 2./pi*b1*(c1/(4.*(x-d1)**2 + c1**2))+ \
      2./pi*b2*(c2/(4.*(x-d2)**2 + c2**2))+ \
      2./pi*b3*(c3/(4.*(x-d3)**2 + c3**2))+ \
      A0/(1.+np.exp((x-Eg)/dE)) 
  #return a * np.exp(-b * x) + c
def func1(x,b1,c1,d1):
  return 2./pi*b1*(c1/(4.*(x-d1)**2 + c1**2)) 
def func2(x,A0, Eg, dE):
  return A0/(1.+np.exp((x-Eg)/dE)) 
fx= open('X1.txt') 
fy = open('Y1.txt') 
n1 = int(fx.readline()) 
n2 = int(fy.readline()) 
if n1 != n2: 
  print 'error' 
else:
#  n1 = 1038 
  x = [ 0. for i in range(n1)] 
  y = [ 0. for i in range(n1)]
  for i in range(n1):
    x[i] = float(fx.readline()) 
    y[i] = float(fy.readline())
err = lambda p: np.mean((func(x,*p)-y)**2)
p_init = [0.0, 8., 3.36, 636.8,\
    130.10, 10.75, 711.4, \
    155.,67.7,754,\
    1.17, 772.,20.] 
p_opt = minimize( err,\
    p_init,\
  #  bounds = [(None,None),(None,None),(None,None),(None,None),\
  #  (None,None),(None,None),(None,None),\
  #  (None,None),(None,None),(None,None),\
  #  (None,None),(None,None),(None,None)],\
    method = "BFGS").x 


#ppot, pcov = curve_fit(func,x, y,bounds =(0,[0.2, 10.,5.,700.])) 
#ppot[0] = 0.087 
#ppot[1] = 8.69 
#ppot[2] = 3.36 
#ppot[3] = 636.8 
print p_opt
yfit = func(x, *p_opt)
yfit1 = func1(x,p_opt[1],p_opt[2],p_opt[3]) 
yfit2 = func1(x,p_opt[4],p_opt[5],p_opt[6]) 
yfit3 = func1(x,p_opt[7],p_opt[8],p_opt[9]) 
yfit4 = p_opt[0]+func2(x,p_opt[10],p_opt[11],p_opt[12])
#print ppot 
plt.plot(x,y,'black')
plt.plot(x,yfit)
plt.plot(x,yfit1)
plt.plot(x,yfit2)
plt.plot(x,yfit3)
plt.plot(x,yfit4)
plt.show()
#plt.savefig('bg76')
