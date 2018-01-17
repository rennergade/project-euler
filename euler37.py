from prime import primes
from re import search

def frontback(n):
    value = str(n)
    list = []
    while value:
        list.append(int(value))
        value = value[:-1]
    value = str(n)
    value = value[::-1]
    value = value[:-1]
    while value:
        list.append(int(value[::-1]))
        value = value[:-1]
    return list

primelist = primes(1000000)
truncprime = []



for i in primelist:
    if (search('[245680]', str(i))) and i > 100:
        continue
    if (set(frontback(i)) < set(primelist)) and i not in [2,3,5,7]:
        truncprime.append(i)

total = 0
for n in truncprime:
    total += n
print total


'''



n = 3137
print frontback(n)

if (set(frontback(n)) < set(primelist)) and n not in [2,3,5,7]:
    print "yes"
'''
