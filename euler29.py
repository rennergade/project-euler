dispow = []
for a in range(2,101):
    for b in range(2,101):
        num = a**b
        if num not in dispow:
            dispow.append(num)
print len(dispow)
