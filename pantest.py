def pan(n):
    n = str(n)
    r = range(1,len(n)+1)
    return True if sorted(map(int, n.lstrip('0')))==r else False

print pan(12384)
