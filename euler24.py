from itertools import permutations

perms = []
for i in permutations(range(10)):
    perms.append(i)
pstr = ''

for i in perms[999999]:
    pstr += str(i)

print int(pstr)
