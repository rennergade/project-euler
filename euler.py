def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def pan(a):
	count = 10*[0]
	while a != 0:
		if count[a%10] == 1: return False
		count[a%10] += 1
		a /= 10
	return True
