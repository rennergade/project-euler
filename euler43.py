from itertools import permutations
from euler import primes
from timeit import default_timer as timer

divisors = primes(18)

def follows_property(n):
    for k in range(7):
        if int(n[k+1:(k+4)]) % divisors[k] != 0:
            return False
    return True

sum = 0
start = timer()

for combo in permutations([str(x) for x in range(10)]):
    num = ''.join(combo)
    if follows_property(num):
        sum += int(num)

elapsed_time = (timer() - start) * 1000 # s --> ms

print("Found %d in %r ms." % (sum, elapsed_time))
