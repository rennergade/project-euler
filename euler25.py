fiba = 1
fibb = 1
index = 2
while len(str(fibb)) < 1000:
    fibb, fiba = fibb + fiba, fibb
    index += 1

print index
