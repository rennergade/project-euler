#!/usr/bin/python

def checkdiv(n):
  for i in range(1,20):
    if n % i != 0:
      return False
  else: return True

x=420

print checkdiv(x)

while checkdiv(x) == False:
  x+=420
  print(x)
