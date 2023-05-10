import numpy as np
import scipy.integrate

def fun(x): return np.exp(-4*x**2)

I1,err1,info = scipy.integrate.quad(fun, -1.0, +1.0, full_output=1)

I2,err2 = scipy.integrate.fixed_quad(fun, -1.0, +1.0, n=20)

I = 0.8820813907624216799674810359140540372245

print( "%s%20.15f,%12.2e" % ("quad    :",I1,(I1-I)/I ))
print( "%s%20.15f,%12.2e" % ("Gauss   :",I2,(I2-I)/I ))
print( "%s%20.15f"        % ("exact   :",I           ))