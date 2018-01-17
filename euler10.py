#!/usr/bin/python
import time
start = time.time()

def prime(n):
  if n == 2:
    return True
  else:
    for i in xrange(3,n,2):
      if n % i == 0:
        return False
    return True

total = 2
for i in xrange(3,2000000,2):
  if prime(i)==True:
    total += i
    print(total)

elapsed = (time.time() - start)
print(elapsed)
