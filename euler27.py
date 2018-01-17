from prime import primes


primelist = primes(10000)
print len(primelist)

length, ag, bg = 0, 0, 0


for a in range(1000):
    for b in range(1001):
        pplist, nplist, pnlist, nnlist = [],[],[],[]
        n = 0
        while 1:
            ppprime = (n**2) + (a*n) + b
            if ppprime not in primelist:
                break
            pplist.append(ppprime)
            n += 1
        n = 0
        while 1:
            npprime = (n**2) + (-a*n) + b
            if npprime not in primelist:
                break
            nplist.append(npprime)
            n += 1
        n = 0
        while 1:
            pnprime = (n**2) + (a*n) - b
            if pnprime not in primelist:
                break
            pnlist.append(pnprime)
            n += 1
        n = 0
        while 1:
            nnprime = (n**2) + (-a*n) - b
            if nnprime not in primelist:
                break
            nnlist.append(nnprime)
            n += 1
        if len(pplist) > length:
            length = len(pplist)
            ag = a
            bg = b
        if len(nplist) > length:
            length = len(nplist)
            ag = -a
            bg = b
        if len(pnlist) > length:
            length = len(pnlist)
            ag = a
            bg = -b
        if len(nnlist) > length:
            length = len(nnlist)
            ag = -a
            bg = -b
    print a

print "Length of list is %i, a = %i, and b = %i" %(length, ag, bg)
product = ag*bg
print "Product is %i" %(product)
