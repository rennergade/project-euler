def d(n):
    sumd = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            sumd += i
            sumd += n/i
    sumd -= n
    return sumd



maxn = 28123

abund = []
nabund = []
nabundt = 0

for i in range(maxn):
    nab = True
    for j in abund:
        if (i -j) < 0: continue
        if (i - j) in abund:
            nab = False
            break
    if nab == True: nabundt += i
    if d(i) > i:
        abund.append(i)
print nabundt
