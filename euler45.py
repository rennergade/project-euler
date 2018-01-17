maxnum = 100000
answer = []

trilist = [int(x*(x+1)/2) for x in range(maxnum)]
pentlist = [int(x*(3*x-1)/2) for x in range(maxnum)]
hexlist = [int(x*(2*x-1)) for x in range(maxnum)]

for i in trilist:
    if i in pentlist and i in hexlist:
        print i
