import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

def f(x,a,b):
    return a+b*x
    
data=np.loadtxt('xdata1A') 

res=scipy.optimize.curve_fit(f,data[:,0],data[:,1])

a,b=res[0]

print(a,b)

x=np.linspace(-0.1,+1.1,1000)
y=f(x,a,b)

plt.plot(x,y,'b-')
plt.errorbar(data[:,0],data[:,1],data[:,2],fmt='r.')
plt.show()
