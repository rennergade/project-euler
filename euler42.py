
with open('words') as f:
    wordlist = f.read().split(',')

maxword = 0
for i in range(len(wordlist)):
    wordlist[i] = wordlist[i].strip('"')
    if len(wordlist[i]) > maxword: maxword = len(wordlist[i])

maxtri = maxword * 26
trilist = [int(0.5*x*(x+1)) for x in range(maxtri)]
total = 0

for word in wordlist:
    wscore = 0
    for l in word:
        wscore += (ord(l)-64)
    if wscore in trilist:
        total += 1
        
print total
