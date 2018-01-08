from scipy import stats
import numpy as np 
import matplotlib.pyplot as plt 

y = np.random.random(10)
x = np.random.random(10)

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) 

yfit = slope * x + intercept
print (r_value)
print (p_value)
plt.plot(x,y,'o') 
plt.plot(x,yfit)
plt.show()
