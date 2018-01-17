def fac(n):
    return 1 if (n < 1) else n * fac(n-1)

digfac = []

for i in range(3,3000000):
    numsum = 0
    istr = str(i)

    for j in istr:
        numsum += fac(int(j))

    if numsum == i:
        digfac.append(i)

print digfac
