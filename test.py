import numpy as np
from scipy import stats

dataset = [14000,12500,13000,10000,11000,11000,9750]

#mean value
mean= np.mean(dataset)

#median value
median = np.median(dataset)

#mode value
mode= stats.mode(dataset)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
