from euler import primes

digtry = 1000
maxprimes = []

while len(maxprimes) < 8:

    primelist = primes(digtry)
    for n in range(1,10):
        for i in range(digtry/10,digtry):
            i = str(i)
            strloop = len(i)
            primecheck = []
            for j in range(0,strloop):
                p = int(i[:j] + str(n) + i[j+1:])
                if p in primelist: primecheck.append(p)
            if len(primecheck) > len(maxprimes): maxprimes = primecheck

    print maxprimes

    digtry *= 10
