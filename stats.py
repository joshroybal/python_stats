from math import sqrt, atan, exp, cos, sin, log
from random import random, randint

def mean(x):
    return sum(x) / float(len(x))

def dev(x, m):
    return list(map(lambda y: y - m, x))

def adev(x, m):
    return list(map(lambda y: abs(y - m), x))

def popvar(ls):
    n = len(ls)
    mu = mean(ls)
    xdev = dev(ls, mu)
    return sum(map(lambda x: x**2, xdev)) / n

def samvar(ls):
    n = len(ls)
    mu = mean(ls)
    xdev = dev(ls, mu)
    return sum(map(lambda x: x**2, xdev)) / (n - 1)

def popstd(x):
    return sqrt(popvar(x))

def samstd(x):
    return sqrt(samvar(x))

def quickselect(x, k):
    n = len(x)
    if n is 0 or k < 1 or k > n: return None
    k -= 1
    left = 0
    right = n - 1
    idx = []
    for i in range(0, n): idx.append(i)
    while left < right:
        pivot = x[idx[k]]
        i = left
        j = right
        while True:
            while x[idx[i]] < pivot: i += 1
            while pivot < x[idx[j]]: j -= 1
            if i <= j:
                tmp = idx[i]
                idx[i] = idx[j]
                idx[j] = tmp
                i += 1
                j -= 1
            if i > j: break
        if j < k: left = i
        if k < i: right = j
    return x[idx[k]]

def median(x):
    n = len(x)
    if n is 0: return None
    if n%2 is not 0: return quickselect(x, n/2+1)
    else: return (quickselect(x,n/2)+quickselect(x,n/2+1))/2.

def median_deviation(x):
    return median(adev(x, median(x)))

def mean_deviation(x):
    return mean(adev(x, mean(x)))

def popskw(x):
    n = len(x)
    m = (sum(map(lambda(y): y**3, dev(x, mean(x))))) / n
    return m / (popstd(x))**3

def samskw(x):
    return ((sum(map(lambda(y):y**3,dev(x,mean(x)))))/len(x))/((samstd(x))**3)

def nonparametric_skew(x):
    return (mean(x) - median (x)) / popstd(x)

def covariance(x, y):
    xdev = dev(x, mean(x))
    ydev = dev(y, mean(y))
    n = min(len(xdev), len(ydev))
    return sum([xdev[i] * ydev[i] for i in range(n)]) / float(n)

def correlation_coefficient(x, y):
    return covariance(x, y) / (popstd(x) * popstd(y))

def normal_distribution(n):
    pi = 4.*atan(1.)
    mu = n/2.
    sd = n/6.018
    normal = []
    for x in xrange(1, n+1):
        y = (1./(sd*sqrt(2.*pi)))*exp(-.5*((x-mu)/sd)**2)
        normal.append(sd*y)
    return normal

def random_uniform(n):
    ls = []
    for x in xrange(0, n): ls.append(random())
    return ls

def random_normal(n):
    pi = 4.*atan(1.)
    ls = []
    for x in xrange(0, n/2):
        ls.append(sqrt(-2.0*log(random()))*cos(2.0*pi*random()))
        ls.append(sqrt(-2.0*log(random()))*sin(2.0*pi*random()))
    return ls

def randnorm(n):
    ls = random_normal(n)
    a = min(ls)
    b = max(ls)
    c = max(-a, b)
    r = 2*c
    d = (r-(b-a))/2
    return map(lambda x: (x-a+d)/r, ls)
