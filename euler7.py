#!/usr/bin/python

def prime(n):
  if n == 2:
    return True
  else:
    for i in range(2,n):
      if n % i == 0:
        return False
    return True
p=0
x=2
num=10001
while 1:
  if prime(x)==True:
    p+=1
  if p==num:
    break
  x+=1

print(x)
  
