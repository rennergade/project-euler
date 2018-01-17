def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

faclist = []
n = 0
while len(faclist) < 4:
    n +=1
    if len(list(set(primes(n)))) == 4:
        faclist.append(n)
    else:
        faclist = []

for i in faclist:
    print i, primes(i)
