import numpy as np
import matplotlib.pyplot as plt

# before NumPy 1.17 ------------------------

r=np.random.random()

#r=np.random.rand()
#r=np.random.randn()

#x=np.random.rand(10)
#x=np.random.rand(1000,2)

#plt.plot(x[:,0],x[:,1],'b.')



# since NumPy 1.17 -------------------------
#rng = np.random.default_rng()

#r=rng.random()

#r=rng.standard_normal()

#x=rng.random(10)
#x=rng.random((1000,2))

#x=rng.standard_normal((1000,2))

#plt.plot(x[:,0],x[:,1],'b.')