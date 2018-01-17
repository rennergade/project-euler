def fac(n):
    return 1 if (n < 1) else n * fac(n-1)

factors = str(fac(215))
total = 0

for i in range(len(factors)):
    total += int(factors[i])

print total
