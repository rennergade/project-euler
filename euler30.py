sumnum = 0
for i in range(2,1000000):
    total = 0
    digits = str(i)
    for digit in digits:
        total += (int(digit))**5
    if total == i:
        sumnum += i
print sumnum
