import calendar

year=int(input("enter year="))

if calendar.isleap(year):
    print("year is leap year!")
else:
    print("year is not leap year")