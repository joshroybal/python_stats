#!/usr/bin/python

import sys
import random
import math

# subprogram definitions
def minimum(a):
    n = len(a)
    if n is 0: return None
    else: return min(a)

def maximum(a):
    n = len(a)
    if n is 0: return None
    else: return max(a)

def median(a):
    n = len(a)
    if n is 0: return None
    if n%2 is not 0: return quick_select(n/2+1, a)
    else: return (quick_select(n/2,a)+quick_select(n/2+1,a))/2.

def mean(a):
    n = len(a)
    if n is 0: return None
    s = 0.
    for i in range(0, n): s += a[i]
    return s / n
    
def population_variance(a):
    n = len(a)
    if n is 0: return None
    m = mean(a)
    s = 0.
    for x in a:
            s += (x-m)**2
    return s / n

def sample_variance(a):
    n = len(a)
    if n is 0: return None
    m = mean(a)
    s = 0.
    for x in a:
            s += (x-m)**2
    return s / (n - 1)
    
def population_standard_deviation(a):
    return math.sqrt(population_variance(a))

def sample_standard_deviation(a):
    return math.sqrt(sample_variance(a))

# C. A. R. Hoare 1961
def quick_select(k, a):
    n = len(a)
    if n is 0 or k < 1 or k > n: return None
    k -= 1
    left = 0
    right = n - 1
    idx = []
    for i in range(0, n): idx.append(i)
    while left < right:
        pivot = a[idx[k]]
        i = left
        j = right
        while True:
            while a[idx[i]] < pivot: i += 1
            while pivot < a[idx[j]]: j -= 1
            if i <= j:
                tmp = idx[i]
                idx[i] = idx[j]
                idx[j] = tmp
                i += 1
                j -= 1
            if i > j: break
        if j < k: left = i
        if k < i: right = j
    return a[idx[k]]

def absolute_deviations(a):
    n = len(a)
    if n is 0: return None
    m = median(a)
    dev = []
    for x in a: dev.append(abs(x-m))
    return dev
    
def median_deviation(a):
    n = len(a)
    if n is 0: return None
    else: return median(absolute_deviations(a))

# initialization block
data_set = []
n = 0
# input block
filename = sys.argv[1]
infile = open(filename, 'r')
for record in infile: 
    data_set.append(float(record))
    n += 1
infile.close()
# processing block
stat_list = []
stat_list.append('minimum = ' + str(minimum(data_set)))
stat_list.append('maximim = ' + str(maximum(data_set)))
stat_list.append('mean = ' + str(mean(data_set)))
stat_list.append('population variance = ' + str(population_variance(data_set)))
stat_list.append('population standard deviation = ' + str(population_standard_deviation(data_set)))
stat_list.append('sample variance = ' + str(sample_variance(data_set)))
stat_list.append('sample standard deviation = ' + str(sample_standard_deviation(data_set)))
stat_list.append('median = ' + str(median(data_set)))
stat_list.append('median deviation = ' + str(median_deviation(data_set)))
# output block
if len(data_set) <= 50: print data_set
print 'n = ', n
for stat in stat_list:
    print stat
if len(data_set) <= 50: print data_set
