#Write a function sample that simulates N sets of coin flips and
#returns a list of the proportion of heads in each set of N flips
#It may help to use the flip and mean functions that you wrote before

import random
from math import sqrt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))
    

def flip(N):
    return [random.random()>0.5 for x in range(N)]
    
def sample(N):
    #Insert your code here
    return [mean(flip(N)) for x in range(N)]

N=1000
outcomes=sample(N)

mu, sigma = mean(outcomes), stddev(outcomes)

print 'Mean: ', mu
print 'Standard deviation: ', sigma

# the histogram of the data
n, bins, patches = plt.hist(outcomes, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.grid(True)
plt.show()

