import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
from scipy.fft import fft,ifft,fftfreq

# nacteni zvukoveho souboru
rate,data = scipy.io.wavfile.read('sample1.wav')

# velikost vzorku
N=data.shape[0]

# normovani do intervalu [-1,+1]
data=data/np.amax(np.fabs(data))

# casova osa
t=np.linspace(0.0,N/rate,N,endpoint=False)

plt.subplot(2,1,1)
plt.plot(t,data)

# vypocet frekvencniho spektra
dt=1/rate
f=np.linspace(0.0,1/dt,N,endpoint=False)
#f=fftfreq(N,1/rate)

spec=fft(data)

plt.subplot(2,1,2)
plt.plot(f,np.absolute(spec))

#data2=ifft(spec)
#scipy.io.wavfile.write("test.wav",rate,data2.real)
#plt.plot(t,data2)

plt.show()