import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

x0=np.array([-3.2,-2.5,-1.7,-0.8,0.1,1.1,1.8,3.2])
y0=np.array([1.7,0.0,-2.9,-0.3,2.5,-0.7,1.2,-1.3])
z0=np.exp(-0.3*(x0**2+y0**2))

pt=np.zeros((8,2))
pt[:,0]=x0
pt[:,1]=y0

ext=[-4,+4,-4,+4]

x=np.linspace(-3.2,+3.2,100)
y=np.linspace(-3.2,+3.2,100)

x,y=np.meshgrid(x,y)

int_near=scipy.interpolate.NearestNDInterpolator(pt,z0)
z1=int_near(x,y)

int_lin=scipy.interpolate.LinearNDInterpolator(pt,z0)
z2=int_lin(x,y)

z3=scipy.interpolate.griddata(pt,z0,(x,y),method='cubic')

int_rbf=scipy.interpolate.RBFInterpolator(pt,z0,kernel='multiquadric',epsilon=1)
z4=int_rbf(np.array([x,y]).reshape(2,-1).T).reshape(100,100)

plt.subplot(2,2,1)
plt.imshow(z1,extent=ext,cmap='jet',aspect='auto',origin='lower',interpolation='none')
plt.plot(x0,y0,'wo')
plt.subplot(2,2,2)
plt.imshow(z2,extent=ext,cmap='jet',aspect='auto',origin='lower',interpolation='none')
plt.plot(x0,y0,'wo')
plt.subplot(2,2,3)
plt.imshow(z3,extent=ext,cmap='jet',aspect='auto',origin='lower',interpolation='none')
plt.plot(x0,y0,'wo')
plt.subplot(2,2,4)
plt.imshow(z4,extent=ext,cmap='jet',aspect='auto',origin='lower',interpolation='none')
plt.plot(x0,y0,'wo')
plt.show()