letterval = {'A': 1, 'B': 2, 'C': 3, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}


with open('names') as f:
    namelist = f.read().split(',')
for i in range(len(namelist)):
    namelist[i] = namelist[i].strip('"')
namelist.sort()

total = 0

for i in range(len(namelist)):
    namesum = 0
    for j in range(len(namelist[i])):
        namesum += letterval[namelist[i][j]]
    namesum *= (i+1)
    total += namesum

print total
