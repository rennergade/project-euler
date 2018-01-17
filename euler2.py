#!/usr/bin/python

def fib(n):
 if n==1 or n==2:
  return 1
 return fib(n-1)+fib(n-2)

x=1
fibtotal = 0
while fib(x) <= 4000000:
    if fib(x) % 2 == 0:
	fibtotal = fibtotal + fib(x)
    x += 1
print fibtotal
