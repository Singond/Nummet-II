import numpy as np
import matplotlib.pyplot as plt
import scipy.fft

def FFT(N,f):
    if N==2:
        return np.array([f[0]+f[1],f[0]-f[1]])
    else:
        cA=FFT(N//2,f[0::2])
        cB=FFT(N//2,f[1::2])
        exp=np.exp(-2j*np.pi/N*np.arange(0,N))
    return np.concatenate( ( cA+exp[0:N//2]*cB, cA+exp[N//2:N]*cB ) )

N=64

f=np.zeros(N,dtype=complex)
f[0:N//2]=+1
f[N//2:N]=-1

c=FFT(N,f)
#c=scipy.fft.fft(f)

plt.subplot(2,1,1)
plt.stem(f.real,linefmt='k-',markerfmt='k.',basefmt=' ')
plt.subplot(2,1,2)
plt.stem(c.real,linefmt='b-',markerfmt='bs')
plt.stem(c.imag,linefmt='r-',markerfmt='ro')
plt.show()