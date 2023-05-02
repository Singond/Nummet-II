import numpy as np
import matplotlib.pyplot as plt
import time
import numba as nb

@nb.jit(nb.types.UniTuple(nb.int64,2)(nb.float64, nb.int64, nb.int64[:,:]))
def sweep(beta,L,s):
    
    probs=np.array([0.5,np.exp(-4*beta),np.exp(-8*beta)])
    
    dMtot=0
    dEtot=0

    for i in range(L):
        for j in range(L):
            
            dE=2*s[i,j]*(s[i-1,j]+s[(i+1)%L,j]+s[i,j-1]+s[i,(j+1)%L])

            if dE>=0 and probs[dE//4]<np.random.random(): continue
            
            s[i,j]=-s[i,j]
            dMtot+=2*s[i,j]
            dEtot+=dE

    return dMtot,dEtot


def runMC(L,NT,T,Navg):

    s=np.ones((L,L),dtype=int)
    M=L**2
    E=-2*L**2
    
    Msamp=np.zeros((NT,Navg))
    Esamp=np.zeros((NT,Navg))

    for i in range(NT):
        print(i)
        beta=1/T[i]
    
        for j in range(Navg):
            dM,dE=sweep(beta,L,s)
            M+=dM
            E+=dE
            
        for j in range(Navg):
            dM,dE=sweep(beta,L,s)
            M+=dM
            E+=dE
            Msamp[i,j]=M/L**2
            Esamp[i,j]=E/L**2

    Mavg=np.average(Msamp,axis=1)
    Eavg=np.average(Esamp,axis=1)
    
    M2avg=np.average(Msamp**2,axis=1)
    E2avg=np.average(Esamp**2,axis=1)

    return Mavg,Eavg,M2avg,E2avg


L=32
NT=100
T=np.linspace(0.04,4,NT)
Navg=50

t1=time.perf_counter()
Mavg,Eavg,M2avg,E2avg = runMC(L,NT,T,Navg)
t2=time.perf_counter()
print(t2-t1,"s")

suscept=(M2avg-Mavg**2)/T
heatcap=(E2avg-Eavg**2)/T**2


plt.subplot(2,2,1)
plt.plot(T,Mavg)
plt.subplot(2,2,2)
plt.plot(T,Eavg)
plt.subplot(2,2,3)
plt.plot(T,suscept)
plt.subplot(2,2,4)
plt.plot(T,heatcap)
plt.show()
