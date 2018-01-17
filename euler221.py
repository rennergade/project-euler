#!/usr/bin/python

alexlist = []

while len(alexlist) < 150001:
    for i in range(1,150000):
        for j in range(1,150000):
            for k in range(1,150000):
                if 1/(i*j*k) == (1/i)+ (1/j) + (1/k):
                    alexlist.append(i*j*k)
                if 1/(i*-j*k) == (1/i)+ (-1/j) + (1/k):
                    alexlist.append(i*-j*k)
                if 1/(i*j*-k) == (1/i)+ (1/j) + (-1/k):
                    alexlist.append(i*j*-k)
                if 1/(i*-j*-k) == (1/i)+ (-1/j) + (-1/k):
                    alexlist.append(i*-j*-k)
                if 1/(-i*j*k) == (-1/i)+ (1/j) + (1/k):
                    alexlist.append(i*j*k)
                if 1/(-i*-j*k) == (-1/i)+ (-1/j) + (1/k):
                    alexlist.append(-i*-j*k)
                if 1/(-i*-j*k) == (-1/i)+ (-1/j) + (1/k):
                    alexlist.append(-i*-j*k)
                if 1/(-i*j*-k) == (-1/i)+ (1/j) + (-1/k):
                    alexlist.append(-i*j*-k)
                if 1/(-i*-j*-k) == (-1/i)+ (-1/j) + (-1/k):
                    alexlist.append(-i*-j*-k)

print alexlist[150000]
