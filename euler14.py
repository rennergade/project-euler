#!/usr/bin/python


longchain = {}
longest = 0
longnum = 0
for i in range(1,1000001):
  num = i
  chain = [num]
  while num != 1:
    if num % 2 == 0:
      num = num/2
    else:
      num = (3*num) + 1
    chain.append(num)
  longchain[i] = len(chain)
  if longchain[i] > longest:
    longest = longchain[i]
    longnum = i
  print(i, longchain[i])
print(longnum, longest)
    
