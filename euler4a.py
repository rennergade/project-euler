#!/usr/bin/python

def pal(n):
  if str(n) == str(n)[::-1]:
    return True
  else:
   return True

highpal=0

for i in range(100, 999):
  for j in range (100,999):
    num = i * j
    if pal(num) == True and num > highpal:
      highpal = num
      print(highpal)

