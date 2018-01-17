from euler import pan

def numcheck(n):
    i = 1
    nstr = str(n)
    while len(nstr) < 9:
        i += 1
        nadd = n * i
        nstr += str(nadd)
        if len(nstr) == 9 and pan(nstr):
            return nstr
    return 0

high = 0
for i in range(1000000):
    check = int(numcheck(i))
    if check > high:
        high = check

print high
