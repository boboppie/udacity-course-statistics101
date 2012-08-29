# Regression: Compute a and b given x and y

from math import sqrt

def mean(l):
    return float(sum(l))/len(l)

x = [6,2,1,-1]
y = [7,3,2,0]

def compute_b(x,y):
    x_mean = mean(x)
    y_mean = mean(y)
    num = 0.0
    denum = 0.0
    for i in range(len(x)):
        num = num + (x[i]- x_mean)*(y[i] - y_mean)
        denum = denum + (x[i]- x_mean)**2        
    return num/denum

def compute_a(x,y):
    return mean(y) - (compute_b(x,y) * mean(x))

print "x:", x
print "y:", y
print "b = %f"% compute_b(x,y)
print "a = %f"% compute_a(x,y)
