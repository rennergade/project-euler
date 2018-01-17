from collections import deque
from prime import primes
from rotations import rotations

maxn = 1000000
total = 0
checked = []
circ = []

primelist = primes(maxn)


for m in primelist:
    if m in checked:
        continue
    rots = rotations(m)
    if set(rots) < set(primelist):
        circ += list(set(rots) - set(circ))
    checked.extend(rots)

print circ
print len(circ)
