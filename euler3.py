#!/usr/bin/python
import math

def prime(n):
  if n == 2:
    return True
  else:
    for i in range(2,n):
      if n % i == 0:
        return False
    return True

num = 600851475143
lim =  int(math.sqrt(num))


fac = 0

for x in range(2, lim):
  if prime(x) == True and num % x == 0 and x > fac:
    fac = x
    print(fac)
  x += 1

print(fac)

