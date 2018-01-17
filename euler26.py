from prime import primes

maxn = 1000
primelist = primes(maxn)[::-1]

for d in primelist:
    period = 1
    while pow(10, period, d) != 1:
        period += 1
    if d-1 == period: break

print d
