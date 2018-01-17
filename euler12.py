#!/usr/bin/python


trinum = 0
count = 1
fac = []
while len(fac) <= 500:
  trinum += count
  fac = [1,trinum]
  for i in range(2,trinum/2):
    if trinum % i == 0:
      fac.append(i)
  print count, trinum, len(fac)
  count +=1
