#!/usr/bin/python

# find the number of ways to reach a total with the given number of combinations

pence = 200
denominations = [200, 100, 50, 20, 10, 5, 2, 1]
names = {1: "1p", 2: "2p", 5 : "5p", 10 : "10p", 20 : "20p", 50 : "50p", 100 : "1lb", 200 : "2lb"}

def count_combs(left, i, comb, add):
    if add: comb.append(add)
    if left == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and left > 0:
            comb.append( (left, denominations[i]) )
            i += 1
        while i < len(denominations):
            comb.append( (0, denominations[i]) )
            i += 1
        print " ".join("%d %s" % (n,names[c]) for (n,c) in comb)
        return 1
    cur = denominations[i]
    return sum(count_combs(left-x*cur, i+1, comb[:], (x,cur)) for x in range(0, int(left/cur)+1))

print count_combs(pence, 0, [], None)
