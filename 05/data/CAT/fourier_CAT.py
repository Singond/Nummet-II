import numpy as np
import matplotlib.pyplot as plt
import scipy.fft

phi=np.loadtxt('projections_phi.txt')
proj=np.loadtxt('projections_pxp.txt')

Nx,Nphi=proj.shape


proj_mod=np.zeros([Nx,Nphi])
for i in range(Nphi):
    c=scipy.fft.fft(proj[:,i])
    proj_mod[:,i]=scipy.fft.ifft(c)


N=40

img=np.zeros([N,N])

for i in range(N):
    for j in range(N):
        x=2*(i-1)/(N-1)-1
        y=2*(j-1)/(N-1)-1
        for k in range(Nphi):
            xrot=x*np.cos(phi[k])+y*np.sin(phi[k])
            if np.abs(xrot)<1:
                img[j,i]=img[j,i]+proj_mod[int(Nx*(xrot+1)/2),k]


plt.imshow(proj,extent=[1,179,-1,+1], \
 cmap='jet',aspect='auto',origin='lower',interpolation='none')

plt.figure()

plt.imshow(img,extent=[-1,+1,-1,+1], \
 cmap='gray',aspect='auto',origin='lower',interpolation='none')
 
plt.show()
