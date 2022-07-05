def is_leap(year):
    leap = False
    if (year % 100 != 0 or year % 400 == 0) and year % 4 == 0:
        #print(year % 100, year % 400, year % 4)
        leap = True
    return leap


year = int(input())
print(is_leap(year))