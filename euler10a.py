#!/usr/bin/python
import time
start = time.time()

marked = [0] * 1000000
value = 3 
s = 2 
while value < 1000000: 
  if marked[value] == 0: 
    s += value 
    i = value 
    while i < 1000000: 
      marked[i] = 1 
      i += value
  value += 2 
print s

elapsed = (time.time() - start)
print(elapsed)
