from euler import pan

prodlist = []
total = 0
for a in range(10000):
    for b in range(100):
        prod = a*b
        num = str(a) + str(b) + str(prod)
        if pan(num) and len(num)==9:
            if prod not in prodlist:
                print a,b, prod
                prodlist.append(prod)
                total += int(prod)
print total
print sum(prodlist)
