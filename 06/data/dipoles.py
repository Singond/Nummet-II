import numpy as np
import scipy.optimize

def f(x):
    return -np.sin(x[0])*np.sin(x[1])
    
res1=scipy.optimize.minimize(f,[0,1],method='Nelder-Mead')

print(res1.x)

def fgrad(x):
    return np.array([ -np.cos(x[0])*np.sin(x[1]), -np.sin(x[0])*np.cos(x[1]) ])
    
res2=scipy.optimize.minimize(f,[0,1],method='BFGS',jac=fgrad)

print(res2.x)