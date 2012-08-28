#Complete the test function to perform a hypothesis test 
#on list l under the null hypothesis that the mean is h

from math import sqrt

def mean(l):
    return float(sum(l))/len(l)

def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)

def factor(l):
    return 1.96


def conf(l):
    # confidence interval
    return factor(l) * sqrt(var(l) / len(l))


def test(l, h):
    m = mean(l)
    c = conf(l)
    return abs(h-m) <= c

l = [199, 200, 201, 202, 203, 204]
h = 200

print "Mean:", mean(l)
print conf(l)
print "CI: [", mean(l) - conf(l), ",", mean(l) + conf(l), "]"
print "Is hypothesis in CI:", test(l,h)     
