#!/usr/bin/python

num = 100

def sumofsquare(n):
  total = 0
  for i in range(1,n+1):
    total += i**2
  return total

def squareofsum(n):
  total = 0
  ts = 0
  for i in range(1,n+1):
    total += i
  ts = total**2
  return ts

print(squareofsum(num)-sumofsquare(num))
