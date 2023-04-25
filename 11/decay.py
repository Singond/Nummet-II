import numpy as np
import matplotlib.pyplot as plt

dt=0.05
tau=100

t=np.arange(0,1000,dt)
N=np.zeros(t.size,dtype=int)

N[0]=1000

for j in range(t.size-1):
    Ndec=0
    for i in range(N[j]):
        if np.random.random() < dt/tau : Ndec=Ndec+1
    N[j+1]=N[j]-Ndec

plt.yscale('log')
plt.plot(t,N,'b-',t,N[0]*np.exp(-t/tau),'r-')
plt.show()