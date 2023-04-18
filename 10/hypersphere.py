import numpy as np
import scipy.special
import matplotlib.pyplot as plt

Dmax=16
N=100000
x=2*np.random.rand(Dmax,N)-1

for D in range(1,Dmax+1):
    V=2**D
    f=( np.sum(x[0:D,:]**2,axis=0) <=1 ).astype(float)    
    avg=np.sum(f)/N
    err=0
    
    print('%2d %10.6f %10.6f' % (D,V*avg,err))
    plt.errorbar(D,V*avg,err,fmt='r.')

D=np.linspace(1,Dmax,1000)
plt.plot(D, 2*np.pi**(D/2)/(D*scipy.special.gamma(D/2)), 'b-')
plt.show()