import re

email = input("Enter email: ")

if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}", email):
    print("Valid Email")
else:
    print("Invalid Email")