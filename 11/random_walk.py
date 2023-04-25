import numpy as np
import matplotlib.pyplot as plt

Nwalk=1000
Nstep=1000

xpt=np.zeros((Nstep+1,Nwalk))
ypt=np.zeros((Nstep+1,Nwalk))

xpt[0,:]=0
ypt[0,:]=0

for i in range(Nwalk):
    for j in range(Nstep):
        phi=2*np.pi*np.random.random()
        xpt[j+1,i]=xpt[j,i]+np.cos(phi)
        ypt[j+1,i]=ypt[j,i]+np.sin(phi)

for i in range(Nwalk):
    plt.plot(xpt[:,i],ypt[:,i],'-')
plt.plot(xpt[Nstep,:],ypt[Nstep,:],'k.')

plt.figure()

plt.hist(np.sqrt(xpt[Nstep,:]**2+ypt[Nstep,:]**2),bins=20)
    
plt.show()