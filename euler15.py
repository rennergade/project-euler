#!/usr/bin/python

def fac(n):
    return 1 if (n < 1) else n * fac(n-1)

n = 20

paths = fac(2*n)/(fac(n)*fac(n))
print paths
