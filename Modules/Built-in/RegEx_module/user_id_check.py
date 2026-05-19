import re

user_id = input("Enter User ID: ")

if re.fullmatch(r"[a-zA-Z][@#$%^&*][a-zA-Z0-9_]{4,14}", user_id):
    print("Valid User ID")
else:
    print("Invalid User ID ")