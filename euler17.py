
numlet = {
'0' : 0,
'1' : 3,
'2' : 3,
'3' : 5,
'4' : 4,
'5' : 4,
'6' : 3,
'7' : 5,
'8' : 5,
'9' : 4,
'10': 3,
'11' : 6,
'12' : 6,
'13' : 8,
'14' : 8,
'15' : 7,
'16' : 7,
'17' : 9,
'18' : 8,
'19' : 8,
'20': 6,
'30': 6,
'40': 5,
'50': 5,
'60': 5,
'70': 7,
'80': 6,
'90': 6
}

count = 0

'nine hundred and ninety nine'

for i in range(0,10):
    num = 0
    for j in range(0,100):
        print (i*100)+j
        if j < 20:
            num = numlet[str(j)]
        else:
            dig2 = str(j-j%10)
            dig1 = str(j%10)
            num = numlet[dig2] + numlet[dig1]

        stri = str(i)
        if i > 0:
            stri = str(i)

            if j == 0:
                num += numlet[stri] + 7
            else:
                num += numlet[stri] + 10
        print num
        count += num


count += 11

print count
