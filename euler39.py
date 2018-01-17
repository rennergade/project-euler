def hyp(a,b):
    return ((a**2)+(b**2))**0.5

sol = {}
for p in range(1001):
    for a in range (1,p-2):
        for b in range(1, p-2):
            c = hyp(a,b)
            if a + b + c == p:
                try:
                    sol[p] +=1
                except KeyError:
                    sol[p] = 1
print sol
