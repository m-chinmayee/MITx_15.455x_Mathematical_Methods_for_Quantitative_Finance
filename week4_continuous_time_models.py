# Chinmayee Mishra Dec 6, 2022

import numpy as np
import matplotlib.pyplot as plt

timesteps = 1000
instances = 20
dt = 1
time = np.arange(timesteps)

zt = np.random.normal(0, 1, size = (timesteps, instances))
Bt = np.cumsum(zt, axis = 0)

plt.plot(time, Bt)
plt.xlabel("Time")
plt.ylabel("Normal Random Walk")
plt.xlim([0,1000])
plt.show()