import datetime

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

user_date = datetime.date(year, month, day)

now_time = datetime.datetime.now().time()

print("Your Entered Date is:", user_date)
print("Current Time is:", now_time)