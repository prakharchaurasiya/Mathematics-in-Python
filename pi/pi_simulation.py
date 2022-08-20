'''
In this we calculate the value of pi using simulation.
Idea : We take one 2 by 2 square and draw a circle such that it's radius is 1 and throw darts on it.
Calculation : Value of pi is equal to the number of darts fall on circle divided by total number of darts.
'''

import numpy as np
import matplotlib.pyplot as plt

def pi(N=10_000, plot=True):
	a, b = 0, 2 # origin of squre is 0, 0
	x = np.random.uniform(a, b, N)
	y = np.random.uniform(a, b, N)
	Nc_points = np.sqrt((x-1)**2 + (y-1)**2) < 1 # number of points inside circle
	Nc = Nc_points.sum()
	print(f'The value of pi as calculated from simulation: {4*Nc/N}')
	
	if plot:
		plt.figure(figsize=(10, 10))
		plt.scatter(x, y, color='Red')
		plt.scatter(x[Nc_points], y[Nc_points], color='Blue')
		plt.show()
        
pi()
