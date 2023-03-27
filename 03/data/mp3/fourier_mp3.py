import numpy as np
import scipy.io.wavfile
from scipy.fft import fft,ifft

N=524288
Nsamp=1024
Nkept=Nsamp//20

rate,data = scipy.io.wavfile.read('sample1.wav')

data=data/np.max(data)

data_compr = np.zeros(N)

for i in range(N//Nsamp):
    samp=data[i*Nsamp:(i+1)*Nsamp]
    c=fft(samp)

    cred=np.zeros(Nsamp,np.complex128)
    
    for j in range(Nkept):
        k=np.argmax(np.absolute(c[1:Nsamp//4]))+1
        cred[k]=c[k]
        c[k]=0
        
    cred[Nsamp//2+1:Nsamp]=np.conj(cred[Nsamp//2-1:0:-1])

    samp=ifft(cred)
    data_compr[i*Nsamp:(i+1)*Nsamp]=samp

data_compr=(32768*data_compr).astype(np.int16)
scipy.io.wavfile.write("sample1_compr.wav",rate,data_compr)
