import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
import imageio

data = imageio.imread('stm-graphene.png',as_gray=True)

c=scipy.fft.fft2(data)

plt.imshow(data)
plt.figure()
plt.imshow(np.absolute(c),vmax=1e5)
plt.show()
