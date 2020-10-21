#!/usr/bin/env python

import stats

def dump(x, y, filename):
    outfile = open(filename, 'wb')
    for r, s in zip(x, y): print >> outfile, r, s
    outfile.close()

def retrieve(x, y, filename):
    x[:] = []
    y[:] = []
    infile = open(filename, 'rb')
    for record in infile:
        x.append(float(record.split()[0]))
        y.append(float(record.split()[1]))
    infile.close()

# report function
def report(x):
    print 'n =', len(x)
    print 'minimum =', min(x)
    print 'maximum =', max(x)
    print 'mean =', stats.mean(x)
    print 'median =', stats.median(x)
    print 'population variance =', stats.popvar(x)
    print 'sample variance =', stats.samvar(x)
    print 'population standard deviation =', stats.popstd(x)
    print 'sample standard deviation =', stats.samstd(x)
    print 'median deviation =', stats.median_deviation(x)
    print 'mean deviation =', stats.mean_deviation(x)
    print 'population skewness =', stats.popskw(x)
    print 'sample skewness =', stats.samskw(x)
    print 'nonparametric skew =', stats.nonparametric_skew(x)

# main program
n = 1000
# initialize and dump data
x = stats.random_uniform(n)
y = stats.random_uniform(n)
dump(x, y, 'uniform.dat')
x = stats.randnorm(n)
y = stats.randnorm(n)
x.sort()
y.sort()
dump(x, y, 'normal.dat')
# retrieve data
retrieve(x, y, 'uniform.dat')
print 'random uniform distributions'
print 'x'
report(x)
print 'y'
report (y)
print 'x y'
print 'covariance =', stats.covariance(x, y)
print 'correlation coefficient =', stats.correlation_coefficient(x, y)
retrieve(x, y, 'normal.dat')
print 'random normal distributions'
print 'x'
report(x)
print 'y'
report (y)
print 'x y'
print 'covariance =', stats.covariance(x, y)
print 'correlation coefficient =', stats.correlation_coefficient(x, y)
