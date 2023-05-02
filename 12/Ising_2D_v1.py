import numpy as np
import matplotlib.pyplot as plt
import time

def sweep():
    global beta,L,s,M,E
    
    probs=np.array([0.5,np.exp(-4*beta),np.exp(-8*beta)])
            
    for i in range(L):
        for j in range(L):
            
            dE=2*s[i,j]*(s[i-1,j]+s[(i+1)%L,j]+s[i,j-1]+s[i,(j+1)%L])

            if dE>=0 and probs[dE//4]<rng.random(): continue
            
            s[i,j]=-s[i,j]
            M=M+2*s[i,j]
            E=E+dE


rng = np.random.default_rng()

L=32

s=np.ones((L,L),dtype=int)
M=L**2
E=-2*L**2

NT=100
T=np.linspace(0.04,4,NT)

Navg=50

Msamp=np.zeros((NT,Navg))
Esamp=np.zeros((NT,Navg))

t1=time.perf_counter()

for i in range(NT):
    print(i)
    beta=1/T[i]

    for j in range(Navg):
        sweep()
        
    for j in range(Navg):
        sweep()
        Msamp[i,j]=M/L**2
        Esamp[i,j]=E/L**2

t2=time.perf_counter()
print(t2-t1,"s")

Mavg=np.average(Msamp,axis=1)
Eavg=np.average(Esamp,axis=1)

M2avg=np.average(Msamp**2,axis=1)
E2avg=np.average(Esamp**2,axis=1)

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
