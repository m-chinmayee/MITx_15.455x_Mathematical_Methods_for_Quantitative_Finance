# Chinmayee Mishra Nov 29, 2022

# Monte Carlo simulation for price paths. It is a code following the second recitation video of the course. So, we will use a lognormal process but it is actually a discrete binomial model. When the time step of a discrete binomial model is tending to zero then we get back the true geometric brownian motion or the lognormal distribution. Right now let's just do the simpler binomial model case. 

import numpy as np
import matplotlib.pyplot as plt

# An easy way to remember the lognormal process (for me since I have struggled with it name) is 'log IS normal' i.e., if a random variable Y is lognormal then its log is normal. In other words, X = ln(Y) is normal. When we map this to actual stock prices, a crucial thing needs to be remembered which necessitates that we use lognormal process to model them. The crucial fact is that the returns are actually continuous compound returns. Let's understand it better below. 

# S(1) = S(0)*(1 + r)
# S(2) = S(0)*(1 + r)^2 This is compound return, not just return on the intial value S(0). 
# S(t) = S(0)*(1 + r)^t
# Now if r->0 and t is very large then, S(t) = S(0) exp(r)
# => r(t) = ln [S(t) / S(t-1)]
# Whenever we consider continuous compounding, it becomes natural to use lognormal processes. r(t) is normally distributed, so S(t) must be a lognormal process. While r(t) can take values from positive to negative the price of a stock can only vary from zero to infinity. Cool right, how everything falls into place automatically! Why did I not learn it this way before? Let's code now.

instances = 20
timesteps = 250
dt = 1 / timesteps
p = 0.5
q = 1 - p
u = 1.1
d = 1 / u

int = np.random.rand(timesteps, instances)
int = np.where(int < p, u, d)

S = np.zeros((timesteps, instances)) + 100
for i in np.arange(1, timesteps):
    S[i] = S[i-1] * int[i]

plt.plot(np.arange(timesteps), S)
plt.show()