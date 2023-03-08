import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft,fftfreq
import scipy.io.wavfile

rate,data = scipy.io.wavfile.read('sample4.wav')
data=data/np.max(data)
N=data.shape[0]

f=fftfreq(N,1/rate)

# original spectrum
spec=fft(data)

plt.subplot(2,1,1)
plt.plot(f,np.absolute(spec))

# multiplicative spectral filter
filt=np.ones(N)

# filtered spectrum
spec=spec*filt

plt.subplot(2,1,2)
plt.plot(f,np.absolute(spec))
plt.show()

# filtered data
data2=ifft(spec)

scipy.io.wavfile.write("sample4_filt.wav",rate,data2.real)
