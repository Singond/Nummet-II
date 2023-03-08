import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile,scipy.fft

rate,data = scipy.io.wavfile.read('sample1.wav')
N=data.shape[0]

Nwin=256

# rectangular window
w=np.ones(Nwin) 

# Hamming window
#w=0.54-0.46*np.cos(2*np.pi*np.arange(Nwin)/Nwin)

# Blackman window
#w=0.42-0.5*np.cos(2*np.pi*np.arange(Nwin)/Nwin)+0.08*np.cos(4*np.pi*np.arange(Nwin)/Nwin)

Nt=500

t=np.zeros(Nt)
spect=np.zeros([N,Nt])

for j in range(Nt):

    j1=int(j*(N-Nwin)/(Nt-1))
    j2=j1+Nwin
    
    t[j]=(j1+j2)/(2*rate)

    aux=np.zeros(N)
    aux[j1:j2]=w*data[j1:j2]

    spect[:,j]=np.absolute(scipy.fft.fft(aux))

plt.ylim([0,5500])
plt.imshow(np.log10(spect),extent=[t[0],t[Nt-1],0.0,rate], \
  cmap='jet',aspect='auto',origin='lower',interpolation='none')
plt.colorbar()
plt.show()
