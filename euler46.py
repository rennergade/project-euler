def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def isprime(n):
    r = primes(n+1)
    if n in r:
        return True
    else:
        return False

maxnum = 10000

allnum = range(3,maxnum,2)
primenum = primes(maxnum)


comp = list(set(allnum) - set(primenum))
comp.sort()

for i in comp:
    conj = False
    top = int(i**0.5)+1
    for j in range(1,top):
        if i < 2*(j**2):
            continue
        if isprime(i - 2*(j**2)) == True:
            conj = True
    if conj == False:
        print i
        break
