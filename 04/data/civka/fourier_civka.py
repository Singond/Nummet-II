import numpy as np
import matplotlib.pyplot as plt
import scipy.fft

data=np.loadtxt('civka.dat')
N=data.shape[0]

t=data[:,0]
U=data[:,1]

Uavg=np.full(N,np.sum(U)/N)

#UFT=scipy.fft.fft(U)
#gFT=scipy.fft.fft(g)
#Uavg=scipy.fft.ifft(UFT*gFT)

plt.plot(t,U,'r.',t,Uavg,'b-')
plt.show()
