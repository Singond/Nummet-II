import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2,ifft2,fftshift
import imageio

thrs=0.002

data = imageio.imread('chaloupka.png',as_gray=True)

c=fftshift(fft2(data))

data=ifft2(c)

plt.imshow(np.absolute(data),cmap='gray')
plt.figure()
plt.imshow(np.absolute(c),vmax=1e5)
plt.show()

imageio.imsave('chaloupka2.png',np.absolute(data))
