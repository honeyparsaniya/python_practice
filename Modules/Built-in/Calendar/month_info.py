import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

start_day, total_days = calendar.monthrange(year, month)

print("Start Day Number:", start_day)
print("Total Days:", total_days)