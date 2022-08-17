'''
Calculating probability of getting 50 heads in a 100 coin toss experiment.
And plotting the probability distribution curve.
'''

import numpy as np
import matplotlib.pyplot as plt

def toss_100_times():
    return np.random.choice(['H', 'T'], 100)

n = 1000000
distribution = np.zeros(n)
for i in range(n):
    result = toss_100_times()
    distribution[i] = np.count_nonzero(result == 'H')

plt.figure(figsize=(10,8))
plt.hist(distribution, bins = 50)
plt.title('Probability Distribution of toss.')
plt.xlabel('Number of Heads in 100 coin toss.')
plt.ylabel('Occurrences')
plt.show()

print(f'Probability of getting 50 heads in 100 toss: {np.count_nonzero(distribution == 50)/n}')
