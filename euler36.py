def pal(n):
    n = str(n)
    return n == n[::-1]

binary = lambda n: '' if n==0 else binary(n/2) + str(n%2)

total = 0

for i in range(1000001):
    if pal(i) and pal(binary(i)):
        total += i

print total
