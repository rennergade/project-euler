from euler import primes, pan

maxnum = 999999999
minnum = 0

primelist = primes(maxnum)


for i in primelist:
    if pan(i) == True:
        print i
