import calendar
a = input()
s=a.split(' ')
a = calendar.weekday(int(s[2]),int(s[0]),int(s[1]))
print(calendar.day_name[a].upper())