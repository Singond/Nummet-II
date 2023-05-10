import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

x0=np.array([-3.2,-2.5,-1.7,-0.8,0.1,1.1,2.4,3.2])
y0=np.exp(-0.7*x0**2)

x=np.linspace(-3.2,+3.2,1000)

int_near=scipy.interpolate.interp1d(x0,y0,kind='nearest')
int_lin =scipy.interpolate.interp1d(x0,y0,kind='linear')
int_poly=scipy.interpolate.BarycentricInterpolator(x0,y0)
int_cspl=scipy.interpolate.CubicSpline(x0,y0)

y1=int_near(x)
y2=int_lin(x)
y3=int_poly(x)
y4=int_cspl(x)

plt.subplot(2,2,1)
plt.plot(x,y1,'r-',x0,y0,'bo')
plt.subplot(2,2,2)
plt.plot(x,y2,'g-',x0,y0,'bo')
plt.subplot(2,2,3)
plt.plot(x,y3,'r-',x0,y0,'bo')
plt.subplot(2,2,4)
plt.plot(x,y4,'g-',x0,y0,'bo')
plt.show()