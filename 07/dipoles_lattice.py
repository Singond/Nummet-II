import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
import pars

Nx=4
Ny=4

R=np.zeros((Nx*Ny,2))
for i in range(Nx):
    for j in range(Ny):
        R[Ny*i+j,:]=np.array([i,j])

def energy(p):
    m=np.empty((Nx*Ny,2))
    m[:,0]=np.cos(p)
    m[:,1]=np.sin(p)
    E=0
    return E

p0=2*np.pi*np.random.rand(Nx*Ny)
bounds=[(0,2*np.pi)]*Nx*Ny
#res=scipy.optimize.minimize(energy,p0,method='Nelder-Mead')
#res=scipy.optimize.basinhopping(energy,p0)
#res=scipy.optimize.differential_evolution(energy,bounds)
#res=scipy.optimize.shgo(energy,bounds)
#res=scipy.optimize.dual_annealing(energy,bounds)

p=p0
#p=res.x
#p=pars.p4x4

print(energy(p))

plt.xlim(-1,Nx)
plt.ylim(-1,Ny)
plt.plot(R[:,0],R[:,1],'ro')
plt.quiver(R[:,0],R[:,1],np.cos(p),np.sin(p))
plt.show()
