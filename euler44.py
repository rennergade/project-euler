from timeit import default_timer as timer

i = 1
pents = []
done = False

start = timer()

while done == False:
    s = int(i*(3*i-1)/2)
    pents.append(s)
    for p in pents:
        if s-p in pents and (s-2*p) in pents:
            ans = (s - 2*p)
            done = True
    i += 1

elapsed_time = (timer() - start) * 1000 # s --> ms

print("Found %d in %r ms." % (ans, elapsed_time))
