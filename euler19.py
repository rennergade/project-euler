weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

months = ['January', 'February','March','April','May','June','July','August','September','October','November','December']

monthday = {
'January': 31,
'February': 28,
'March': 31,
'April': 30,
'May': 31,
'June': 30,
'July': 31,
'August': 31,
'September': 30,
'October': 31,
'November': 30,
'December': 31
}

daycount = 0
day = (daycount)
currentday = weekday[daycount%7]
suncount = 0


for n in range(1900,2001):
    print n
    for i in months:
        if n % 4 == 0 and n != 1900:
            monthday['February'] = 29
        else:
            monthday['February'] = 28
        print i
        for j in range(1, monthday[i]+1):
            day = (daycount%7)
            print j, weekday[day]
            if weekday[day] == 'Sunday' and j == 1 and n != 1900:
                suncount += 1
            daycount += 1

print suncount
