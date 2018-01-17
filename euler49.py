import itertools as it
from prime import primes

numbers = list(set(primes(10000)) - set(primes(1000)))
#numbers = [1487, 4817, 8147]
answer = []

for n in numbers:

    perms = it.permutations(str(n))
    permlist = []

    for perm in perms:
        itnum = ""
        for digit in perm:
            itnum += digit
        itnum = int(itnum)
        if itnum in numbers:
            permlist.append(itnum)
    for i in permlist:
        for j in permlist:
            k = i-j
            if k > 0 and i + k in permlist:
                if [i-k, i, i+k] not in answer:
                    answer.append([i-k, i, i+k])

for ans in answer:
    long = ''
    for n in ans:
        long += str(n)
    print int(long)
