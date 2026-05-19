import re

num = input("Enter mobile number: ")

if re.fullmatch(r"\d{10}", num):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")