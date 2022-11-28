# Chinmayee Mishra Nov 28, 2022

# Gambler's ruin problem has been simulated with boundary conditions. It is pretty easy. Basically party A has 'x' amount of money and B has 'y'. In total the monetary value 'x+y' between the two parties is conserved. The parties play a game (can be as easy as tossing a coin) and the winner takes 1 unit of money from the the loser. The game is repeated until one of the parties win all the money from the other. 

import numpy as np
import matplotlib.pyplot as plt

# probability of party A winning is pa and B winning is pb
pa = 0.4
pb = 1 - pa

# initial asset with A and B assuming the total asset is 100
xa = 95
xb = 100 - xa

# maximum number of games to be played
steps = 1000

# multiple instances are necessary to see the distribution of ending times.
instances = 1000

# define a game with arguments 'a' and 'b' denoting current assets of party A and B
def game(a, b):
    flip = np.random.rand()
    if flip <= pa:
        a += 1
        b -= 1
    else:
        a -= 1
        b += 1
    return a, b

# initial asset values
asset_a = np.zeros((steps, instances))
asset_b = np.zeros((steps, instances))
asset_a[0] = xa
asset_b[0] = xb
ruin_time = np.zeros(instances)
did_A_win = 0
did_B_win = 0

# dynamic evolution with boundaries for a single instance
for j in np.arange(instances):
    for i in np.arange(1, steps):
        asset_a[i, j], asset_b[i, j] = game(asset_a[i-1, j], asset_b[i-1, j])
        if asset_a[i, j] == 100:
            asset_a[i+1:steps, j] += 100
            ruin_time[j] = i
            did_A_win += 1
            break
        elif asset_b[i, j] == 100:
            asset_b[i+1:steps, j] += 100
            ruin_time[j] = i
            did_B_win += 1
            break

# probability of winning
print("Probability of A winning is", did_A_win / instances, " and B winning is,", did_B_win / instances)
# plot the distribution of when one of them in ruined
plt.hist(ruin_time)
plt.show()
# plt.plot(np.arange(steps), asset_a)
# plt.plot(np.arange(steps), asset_b)
# plt.show()

# Seems like it is an poisson distribution (when xa = xb)! 
# The moment the game is even slightly biased, the party with favourable odds almost always wins if the initial asset prices are the same.
# If xa >> xb, seems like an exponential distribution (when pa = pb)!
# When xa >> xb but pa < pb, still party B has a much higher chance of winning.